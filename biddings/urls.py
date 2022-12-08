from django.urls import path
from biddings import views

urlpatterns = [
    path('biddings/', views.BiddingList.as_view()),
    path('biddings/<int:pk>/', views.BiddingDetail.as_view())
]