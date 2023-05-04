from django.contrib import admin
from .models import Apartment, Expense, Invoice, InvoiceItem, Payment, CashFlow, InvoiceGenerationLog, Person, Account


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'description', 'value', 'category', 'account', 'due_date', 'expense_type', 'apartment', 'invoiced', 'paid')
    list_editable = ['description', 'value', 'category', 'account', 'due_date', 'expense_type', 'apartment', 'invoiced', 'paid']
    actions = ['duplicate_account']

    def duplicate_account(self, request, queryset):
        for obj in queryset:
            obj.pk = None
            obj.id = None
            obj.invoiced = False
            obj.paid = False
            obj.save()

        self.message_user(request, f"{queryset.count()} accounts duplicated successfully.")

    duplicate_account.short_description = "Duplicate selected accounts"


class InvoiceItemAdmin(admin.StackedInline):
    model = InvoiceItem
    extra = 0


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemAdmin, ]
    list_display = ('month_reference', 'apartment', 'total_value', 'paid')
    list_editable = ['paid']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'account', 'payment_date', 'paid_value')


class CashFlowAdmin(admin.ModelAdmin):
    list_display = ('description', 'value', 'date', 'type')


class InvoiceGenerationLogAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance')


admin.site.register(Account, AccountAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(InvoiceGenerationLog, InvoiceGenerationLogAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(CashFlow, CashFlowAdmin)
