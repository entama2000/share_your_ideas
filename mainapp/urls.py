from django.urls import path
from mainapp import views

urlpatterns = [
    path('ideas/', views.idea_list),
    path('ideas/<int:pk>/', views.idea_detail),
]