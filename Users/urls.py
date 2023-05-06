from django.urls import path

from . import views

urlpatterns = [

    path('register/Employer/', views.EmployerRegistrationView.as_view(), name="register"),
    path('register/Laborer/', views.LaborerRegistrationView.as_view(), name="register"),
    path('register/Contractor/', views.ContractorRegistrationView.as_view(), name="register"),

    path('login/', views.CustomAuthToken.as_view()),
    path('logout/', views.LogoutView.as_view()),

    path('Employer/Dashboard', views.EmployerOnlyView.as_view(), name='is_employer'),
    path('Laborer/Dashboard', views.LaborerOnlyView.as_view(), name='is_laborer'),
    path('Contractor/Dashboard', views.ContractorOnlyView.as_view(), name='is_contractor'),

    ]