from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import *

class VacancyListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        company = request.GET.get('company')

        if company:
            vacancies = vacancies.filter(company__icontains=company)

        programming_language = request.GET.get('programming_language')
        if programming_language:
            vacancies = vacancies.filter(programming_language__icontains=programming_language)

        status = request.GET.get('status')
        if status:
            vacancies = vacancies.filter(status=status)

        paginator = Paginator(vacancies, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'vacancies/vacancy_list.html', {'page_obj': page_obj})

class VacancyDetailView(View):
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        return render(request, 'vacancies/vacancy_detail.html', {'vacancy': vacancy})