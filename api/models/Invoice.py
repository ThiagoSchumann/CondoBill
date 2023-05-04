from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from api.models import Apartment, Expense


class Invoice(models.Model):
    month_reference = models.CharField(max_length=7)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    total_value = models.FloatField(default=0.00)
    paid = models.BooleanField(default=False)

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
def pre_save_generation_invoices(sender, instance, created, **kwargs):
    if created:
        generate_invoices(instance.reference_month)


def generate_invoices(reference_date):
    expenses = Expense.objects.filter(invoiced=False,
                                      due_date__month=reference_date.month,
                                      due_date__year=reference_date.year)
    apartments = Apartment.objects.filter(account__in=expenses).distinct()

    for apartment in apartments:
        invoice = Invoice.objects.create(month_reference=reference_date.strftime('%m-%Y'), apartment=apartment)
        for expense in expenses:
            if expense.expense_type == expense.Type.EXCLUSIVE and expense.apartment == apartment:
                item = InvoiceItem.objects.create(invoice=invoice, expense=expense, value=expense.value)
                invoice.total_value = round(invoice.total_value + expense.value, 0)
                # expense.paid = True
                expense.invoiced = True
                expense.save()
            elif expense.expense_type == expense.Type.SHARED:
                item = InvoiceItem.objects.create(invoice=invoice, expense=expense,
                                                  value=expense.value / apartments.count())
                invoice.total_value = round(invoice.total_value + (expense.value / apartments.count()), 0)
                # expense.paid = True
                expense.invoiced = True
                expense.save()
        invoice.save()
