from django.contrib import admin

# Register your models here.
from .models import Expense
admin.site.register(Expense)

from .models import Category
admin.site.register(Category)

from .models import Income
admin.site.register(Income)