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
    # path('', views.IndexView.as_view(), name='index'),

    path('', views.login_view, name='index'),

    path('logout/', views.logout_view, name='logout'),

    path('expenses/', views.expense_list, name='expense_list'),

    path('expenses/recurring', views.expense_list_recurring, name='expense_list_recurring'),
    # path('expenses/<str:key>', views.expense_list, name='expense_list'),

    # path('expenses/filter/', views.expense_list_filter, name='expense_list_filter'),

    path('expenses/expense-form-page/', views.expense_form_page, name='expense_form_page'),

    # path('expenses/<int:pk>/', views.ExpenseDetailView.as_view(), name='expense_detail'),

    path('expenses/<int:pk>/', views.expense_detail, name='expense_detail'),

    path('expenses/recurring/<int:pk>/', views.recurring_edit, name='recurring_edit'),
    # path('expenses/recurring/<int:pk>/', views.expense_detail_recurring, name='expense_detail_recurring'),

    path('expenses/<int:pk>/edit/', views.expense_edit, name='expense_edit'),

    path('income/<int:pk>/', views.IncomeDetailView.as_view(), name='income_detail'),

    # /budget/categories
    path('categories/', views.categories, name="categories"),

    # /budget/categories/3
    path('categories/<int:category_id>/', views.category_detail, name="category_detail")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

