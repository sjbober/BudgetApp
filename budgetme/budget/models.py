from django.db import models

class Expense(models.Model):
    expense_date = models.DateField('Date of expense')
    # vendor = models.CharField(max_length=100,blank=True)
    description = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt = models.ImageField(upload_to="images/",null=True,blank=True)

    def __str__(self):
        return str(self.expense_date) + " " + self.vendor

    def get_absolute_url(self):
        return reverse('expense_detail', kwargs={'pk': self.pk})

class RecurringExpense(models.Model):
    day = models.IntegerField('Day of expense')
    description = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Income(models.Model):
    start_date = models.DateField()
    does_repeat = models.BooleanField('Repeats monthly?',blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.amount)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
