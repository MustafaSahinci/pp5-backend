from django.urls import path
from cars import views

urlpatterns = [
    path('cars/', views.CarList.as_view()),
    path('cars/<int:pk>/', views.CarDetail.as_view()),
]
