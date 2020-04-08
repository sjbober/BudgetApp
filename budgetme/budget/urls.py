from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

# from . import views, settings
# from django.contrib.staticfiles.urls import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'budget'
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    # generic views!
    # new index url
    path('', views.IndexView.as_view(), name='index'),

    # path('expenses/', views.ExpenseListView.as_view(), name='expense_list'),

    path('expenses/', views.expense_list, name='expense_list'),

    path('expenses/expense-form-page/', views.expense_form_page, name='expense_form_page'),

    # path('expenses/<int:pk>/', views.ExpenseDetailView.as_view(), name='expense_detail'),

    path('expenses/<int:pk>/', views.expense_detail, name='expense_detail'),

    path('expenses/<int:pk>/edit', views.expense_edit, name='expense_edit'),

    path('income/<int:pk>/', views.IncomeDetailView.as_view(), name='income_detail'),

    # /budget/categories
    path('categories/', views.categories, name="categories"),

    # /budget/categories/3
    path('categories/<int:category_id>/', views.category_detail, name="category_detail")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

