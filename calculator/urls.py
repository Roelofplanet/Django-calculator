from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('count/', views.count, name='count'),
    path('result/', views.result, name='result'),
    path('kwadraat/', views.kwadraat, name='kwadraat'),
    path('result_kwadraat/', views.result_kwadraat, name='result_kwadraat'),
    path('circel_omtrek/', views.circel_omtrek, name='circel_omtrek'),
    path('result_circel_omtrek/', views.result_circel_omtrek, name='result_circel_omtrek'),
    path('circel_oppervlakte/', views.circel_oppervlakte, name='circel_oppervlakte'),
    path('result_circel_oppervlakte/', views.result_circel_oppervlakte, name='result_circel_oppervlakte'),
    path('modulo/', views.modulo, name='modulo'),
    path('result_modulo/', views.result_modulo, name='result_modulo'),
    path('relativiteitstheorie/', views.relativiteitstheorie, name='relativiteitstheorie'),
    path('result_relativiteitstheorie/', views.result_relativiteitstheorie, name='result_relativiteitstheorie'),
]