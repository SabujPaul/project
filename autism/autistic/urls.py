from django.urls import path
from . import views

app_name = "autistic"

urlpatterns = [
    path('', views.home, name='home_page'),
    path('contact/', views.contact, name='contact'),
    path('predictor/', views.predict, name='prediction_page'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results'),
    path('questions/', views.question, name='questions'),
    
]