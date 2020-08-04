from django.core.management.base import BaseCommand

# Import models
from budget.models import Expense
from budget.models import RecurringExpense

from datetime import date


class Command(BaseCommand):
    help = 'Auto generate spending activity from monthly bills'

    def handle(self, *args, **kwargs):
        today = date.today()
        monthly_expenses = RecurringExpense.objects.filter(day__iexact=today.day)

        for expense in monthly_expenses:
            one_time_expense = Expense(expense_date=date.today(),description=expense.description,category=expense.category,amount=expense.amount,user=expense.user)
            one_time_expense.save()