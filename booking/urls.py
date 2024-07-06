from django.urls import path
from django.views.generic import TemplateView
from .views import contact_view
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book_table, name='book_table'),
    path('menu/', views.menu, name='menu'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
]
