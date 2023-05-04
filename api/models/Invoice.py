import math
from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, F
from django.db.models.functions import Cast
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.forms import FloatField
from django.utils import timezone
from api.models import Apartment, Expense, CashFlow, Account


class Invoice(models.Model):
    month_reference = models.CharField(max_length=7)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    total_value = models.FloatField(default=0.00)
    paid = models.BooleanField(default=False)
    cashflow = models.ForeignKey(CashFlow, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Invoice {self.pk} - {self.apartment}"


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return f"InvoiceItem {self.pk} - {self.expense} ({self.value})"


class InvoiceGenerationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    generated_on = models.DateTimeField(default=timezone.now)
    reference_month = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Invoice Generation Log - {self.reference_month.strftime('%m-%Y')}"


@receiver(post_save, sender=InvoiceGenerationLog)
def post_save_generation_invoices(sender, instance, created, **kwargs):
    if created:
        generate_invoices(instance.reference_month)


@receiver(pre_save, sender=Invoice)
def pre_save_payment_invoices(sender, instance, **kwargs):
    old_instance = sender.objects.get(pk=instance.pk)
    if old_instance.paid != instance.paid:
        add_cashflow(description=f"Pagamento condomínio - {instance.month_reference} - Apartamento - {instance.apartment.number}" ,
                     value=instance.total_value,
                     date=timezone.now(),
                     account=instance.account,
                     invoice=instance,
                     cashflow_type=CashFlow.Type.INFLOW)


def add_cashflow(description, value, date, account, invoice, cashflow_type):
    inflow = CashFlow.objects.create(
        description=description,
        value=value,
        date=date,
        account=account,
        type=cashflow_type,
        invoice=invoice,
        balance=0.00,
    )



def generate_invoices(reference_date):
    apartments = Apartment.objects.all()
    expenses = Expense.objects.filter(invoiced=False,
                                      due_date__month=reference_date.month,
                                      due_date__year=reference_date.year)

    for apartment in apartments:
        invoice = Invoice.objects.create(month_reference=reference_date.strftime('%m-%Y'), apartment=apartment)
        for expense in expenses:
            if expense.expense_type == expense.Type.EXCLUSIVE and expense.apartment == apartment:
                item = InvoiceItem.objects.create(invoice=invoice,
                                                  expense=expense,
                                                  value=round(expense.value, 2))
                item_value = item.value
            elif expense.expense_type == expense.Type.SHARED:
                item = InvoiceItem.objects.create(invoice=invoice,
                                                  expense=expense,
                                                  value=round(expense.value / apartments.count(), 2))
                item_value = item.value
            else:
                item_value = 0

            invoice.total_value = invoice.total_value + item_value
            # expense.paid = True
            expense.invoiced = True
            expense.save()
        invoice.total_value = math.ceil(invoice.total_value)
        invoice.save()
