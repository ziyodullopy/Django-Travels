from django.urls import path
from .import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('place/<int:pk>/', views.PlaceDetailView.as_view(), name='place_detail'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("search/", views.search_view, name="search"),
    path('gallarey/<int:pk>/', views.GallareyView.as_view(), name='gallarey'),
    path('contact/', views.ContactUsView.as_view(), name='contact'),
    path('rate/', views.RateUsView.as_view(), name='rate'),
    
]

