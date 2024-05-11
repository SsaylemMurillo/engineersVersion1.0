from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="todos"),
    path("calculate/", views.calculate, name="calculate"),
    path("calculate/future_value/", views.future_value, name="calculate_future_value"),
    path("calculate/tax_value/", views.tax_value, name="e_tax_value"),
    path("calculate/capital_value/", views.capital_value, name="calculate_capital_value"),
    path("calculate/tax_rate_value/", views.tax_rate_value, name="calculate_tax_rate_value"),
    path("calculate/time_value/", views.time_value, name="calculate_time_value"),
    path('future_value/', views.calculate_future_value, name='future_value'),
    path('tax_value/', views.calculate_tax_value, name='tax_value'),
    path('capital_value/', views.calculate_capital_value, name='capital_value'),
    path('tax_rate_value/', views.calculate_tax_rate_value, name='tax_rate_value'),
    path('time_value/', views.calculate_time_value, name='time_value'),
    
    path("calculate2/", views.calculate2, name="calculate2"),
    path("calculate2/compound_amount/", views.compound_amount, name="calculate2_compound_amount"),
    path("calculate2/compound_capital/", views.compound_capital, name="calculate2_compound_capital"),
    path("calculate2/compound_tax_rate/", views.compound_tax_rate, name="calculate2_compound_tax_rate"),
    path("calculate2/compound_time/", views.compound_time, name="calculate2_compound_time"),
    path("compound_amount/", views.calculate_compound_amount, name="compound_amount"),
    path("compound_capital/", views.calculate_compound_capital, name="compound_capital"),
    path("compound_tax_rate/", views.calculate_compound_tax_rate, name="compound_tax_rate"),
    path("compound_time/", views.calculate_compound_time, name="compound_time"),
    
    path("calculate3/", views.calculate3, name="calculate3"),
    path("calculate3/amound_anuality/", views.amound_anuality, name="calculate3_amound_anuality"),
    path("calculate3/rent_anuality/", views.rent_anuality, name="calculate3_rent_anuality"),
    path("calculate3/capital_anuality/", views.capital_anuality, name="calculate3_capital_anuality"),
    path("amound_anuality/", views.calculate_amound_anuality, name="amound_anuality"),
    path("rent_anuality/", views.calculate_rent_anuality, name="rent_anuality"),
    path("capital_anuality/", views.calculate_capital_anuality, name="capital_anuality"),
]
