from django.urls import path
from .views import *

urlpatterns = [
    path('vacancies/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail')
]