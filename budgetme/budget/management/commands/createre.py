from django.core.management.base import BaseCommand
# from polls.models import Question as Poll
from budget.models import Expense
from budget.models import RecurringExpense

from datetime import date
import schedule
import time


class Command(BaseCommand):
    help = 'Auto generate spending activity from monthly bills'

    def handle(self, *args, **kwargs):
        monthly_expenses = RecurringExpense.objects.all()

        for expense in monthly_expenses:
            one_time_expense = Expense(expense_date=date.today(),description=expense.description,category=expense.category,amount=expense.amount)

            one_time_expense.save()
    
# class Expense(models.Model):
#     expense_date = models.DateField('Date of expense')
#     description = models.CharField(max_length=200, blank=True)
#     category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True,blank=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     receipt = models.ImageField(upload_to="images/",null=True,blank=True)

# class RecurringExpense(models.Model):
#     day = models.IntegerField('Day of expense')
#     description = models.CharField(max_length=200, blank=True)
#     category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True,blank=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)