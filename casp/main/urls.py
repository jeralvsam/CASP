# main/urls.py
from django.urls import path
# pyrefly: ignore [missing-import]
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('admissions/', views.admissions, name='admissions'),
    path('departmens/', views.departments, name='departments'),
    path('placement/', views.placement, name='placement'),
    path('gallery/', views.gallery, name='gallery'),
    path('students-corner/', views.students_corner, name='students_corner'),
    path('iqac/', views.iqac, name='iqac'),
    path('contact/', views.contact, name='contact'),
]
