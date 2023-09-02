from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mainapp import views

urlpatterns = [
    path('ideas/', views.IdeaList.as_view()),
    path('ideas/<int:pk>/', views.IdeaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)