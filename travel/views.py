
from typing import Any
from .forms import OrderPlaceForm
from django.shortcuts import render, redirect
from django.template import RequestContext
from .models import Places, PlaceDetail, Gallarey, ContactUs, Rate, LogoutModel, LoginModel
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (  
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import (
    CreateView,
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.contrib.auth import logout

class UserLoginView(LoginView):

    template_name = 'login.html'
    success_url = '/rate/'

def logout_view(request):
    if request.user.is_authenticated:
        LogoutModel.objects.create(user=request.user)
    logout(request)
    return redirect("/")

class HomePageView(ListView):
    model = Places
    template_name = 'home.html'
    context_object_name = 'places'

class PlaceDetailView(DetailView):
    model = Places
    template_name ='place_detail.html'
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = PlaceDetail.objects.get(place=self.object)
        context["form"] = OrderPlaceForm()
        context['gallarey'] = Gallarey.objects.get(place=self.object)
        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = OrderPlaceForm(request.POST)
            if form.is_valid():
                place = Places.objects.get(id=self.kwargs['pk'])
                form.instance.place = place
                token = '6374683006:AAHrzFjO2LLu371rPXainL4qlFNDwNtEsjQ'
                text = f"New messege \nFull Name: {form.instance.full_name} \nPhone Number: {form.instance.phone_number} \nPlace: {form.instance.place}"
                url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id='
                requests.get(url + str(1845780630) + '&text=' + text)
                form.save()
                return redirect('/')
        else:
            form = OrderPlaceForm()


def search_view(request):
    if request.method == 'GET':
        search = request.GET.get("q")
        if search:
            places = Places.objects.filter(name__icontains=search)
            return render(request, 'search.html', {'places': places})
        else:
            return render(request, 'search.html')

def notfound(request, exception):
    return render(request, "404.html")

def error500(request, *args, **kwargs):
    response = render(request, "404.html")
    response.status_code = 500
    return response

class GallareyView(DetailView):
    model = Gallarey
    template_name = 'gallarey.html'
    context_object_name = 'gallarey'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gallarey = self.get_object()
        images = gallarey.travel_gallarey.all()
        context['images'] = images
        return context
        

class ContactUsView(CreateView):
    model = ContactUs
    fields = ['full_name', 'email', 'phone_number', 'message']
    template_name = "contact_us.html"
    context_object_name = "form"
    success_url = '/'

class RateUsView( LoginRequiredMixin ,CreateView):
    model = Rate
    fields = ['text', 'rate']
    template_name = "rate.html"
    context_object_name = "form"
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(). form_valid(form)
    

