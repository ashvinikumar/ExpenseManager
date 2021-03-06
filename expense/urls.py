from django.conf.urls import patterns, url
from expense import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^all_transactions/$', views.transactions, name='all transactions'),
        url(r'^add_transaction/$', views.add_transaction, name='add_transaction'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^add_monthly_budget/$', views.add_monthly_budget, name='add_monthly_budget'),
        url(r'^display_monthly_budget/$', views.display_monthly_budget, name='display_monthly_budget'),
        url(r'^remaining_budget_balance/$', views.remaining_budget_balance, name='remaining_budget_balance'),
        url(r'^transactions_per_category/$', views.transactions_per_category, name='transactions_per_category'),)
        # url(r'^month_year_transactions/$', views.month_year_transactions, name='month_year_transactions'),)
