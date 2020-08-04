from django.db import models
from django.conf import settings
import random


class Expense(models.Model):
    expense_date = models.DateField('Date of expense')
    description = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt = models.ImageField(upload_to="images/",null=True,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE, 
                            null=False,
                            blank=False)

    def __str__(self):
        return str(self.expense_date) + " " + str(self.amount)

    def get_absolute_url(self):
        return reverse('expense_detail', kwargs={'pk': self.pk})

class RecurringExpense(models.Model):
    day = models.IntegerField('Day of expense')
    description = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE, 
                            null=False,
                            blank=False)


class Income(models.Model):
    date = models.DateField('Income date')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paycheck = models.ImageField(upload_to="images/",null=True,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=False,blank=False)

    def __str__(self):
        return str(self.amount)

# List to keep track of all RGB combos for this user 
# to make sure all categories have unique colors
colors = []

class Category(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=False,blank=False)

    def __str__(self):
        return self.name

    # # List to keep track of all RGB combos for this user 
    # # to make sure all categories have unique colors
    # colors = []
    # @classmethod
    # def generateRandomRGB():
    #     red = random.randint(0,256)
    #     green = random.randint(0,256)
    #     blue = random.randint(0,256)

    #     return [red, green, blue]

    # RBG_colors = []
    # while RBG_colors in colors:
    #     RBG_colors = generateRandomRGB()

    # colors.append(RBG_colors)
    # red = models.DecimalField(max_digits=3, decimal_places=0)
    # red = RBG_colors[0]
    # red = 


# Make sure no other category has same red, green, blue?

# let randomColors = generateRandomRGB();
# let color = 'rgba(' + randomColors[0] + ', ' + randomColors[1] + ', ' + randomColors[2] + ', ' + .2 + ')';
# backgroundColors.push(color);
# let darkerColor = 'rgba(' + randomColors[0] + ', ' + randomColors[1] + ', ' + randomColors[2] + ', ' + 1 + ')';
# borderColors.push(darkerColor);