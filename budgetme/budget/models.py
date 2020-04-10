from django.db import models

# Create your models here.
class Expense(models.Model):
    expense_date = models.DateField('Date of expense')
    vendor = models.CharField(max_length=100,blank=True)
    description = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt = models.ImageField(upload_to="images/", blank=True)
    # receipt = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return str(self.expense_date) + " " + self.vendor

    def get_absolute_url(self):
        return reverse('expense_detail', kwargs={'pk': self.pk})


class Income(models.Model):
    start_date = models.DateField()
    does_repeat = models.BooleanField('Repeats monthly?',blank=True)
    # is_ongoing = models.BooleanField('Current?',blank=True)
    # end_date = models.DateField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.amount)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TempReceipt(models.Model):
    image = models.ImageField(upload_to="temp/", blank=True)