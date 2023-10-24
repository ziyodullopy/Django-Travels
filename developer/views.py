from typing import Any
from django import http
from django.shortcuts import redirect
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from travel.models import OrderPlaces,LogoutModel, ContactUs, LoginModel, RegisterModel
from django.contrib.auth.models import User
from django.db.models import Q
import datetime

class DeveloperHomePage(LoginRequiredMixin ,ListView):
    template_name = 'developer/developer_home.html'
    model = OrderPlaces

    def serach_table(self):
        search = self.request.GET.get('q')
        if search ==None:
            contact = ContactUs.objects.all().order_by('-date_created')[:3]
        else:
            contact = ContactUs.objects.filter(Q(Q(full_name__icontains=search) | Q(phone_number__icontains=search) | Q(email__icontains=search)))
        return contact


    def get_context_data(self,**kwargs): 
        context = super ().get_context_data(**kwargs)
        today = datetime.date.today()
        ##
        context['logout_month_1'] = LogoutModel.objects.filter(timelogout__month=8).count()
        context['logout_month_2'] = LogoutModel.objects.filter(timelogout__month=9).count()
        context['logout_month_3'] = LogoutModel.objects.filter(timelogout__month=10).count()   
        context['login_month_1'] = LoginModel.objects.filter(timelogin__month=8).count()
        context['login_month_2'] = LoginModel.objects.filter(timelogin__month=9).count()
        context['login_month_3'] = LoginModel.objects.filter(timelogin__month=10).count()
        context['reg_month_1'] = RegisterModel.objects.filter(timereg__month=8).count()
        context['reg_month_2'] = RegisterModel.objects.filter(timereg__month=9).count()
        context['reg_month_3'] = RegisterModel.objects.filter(timereg__month=10).count() 
        ## 
        context['order'] = OrderPlaces.objects.count()
        context["orders"] = OrderPlaces.objects.filter(date_ordered__date=today)
        context['users'] = User.objects.count()
        context['logout_user'] = LogoutModel.objects.filter(timelogout__date=today).count()
        context["search_table_context"] = self.serach_table()

        return context

developer_home_page = DeveloperHomePage.as_view()


