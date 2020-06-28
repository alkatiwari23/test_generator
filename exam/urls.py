from django.urls import path
from . import views

urlpatterns=[
    path('', views.ExamTemplateView.as_view(), name='first'),
    path('search/', views.search,name='search'),
    path('questions/list/',views.ExamListView.as_view(),name='home'),
    path('questions/<int:pk>/', views.ExamDetailView.as_view(), name='post_detail'),
    path('questions/new/', views.ExamCreateView.as_view(), name='post_new'),
]