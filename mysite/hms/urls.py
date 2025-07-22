from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # Role selection page
    path('', views.select_role, name='select_role'),

    # Logins
    path('login/', LoginView.as_view(template_name='hms/doctor_login.html'), name='login'),  # Doctor login
    path('patient-login/', views.patient_login, name='patient_login'),

    # Dashboards
    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('my-records/', views.my_records, name='my_records'),

    # Patient detail (for doctor)
    path('patient/<int:patient_id>/', views.patient_detail, name='patient_detail'),

    # Logout
    path('logout/', views.logout_and_redirect, name='logout'),

    # About & Feedbacks
    path('about/', views.about, name='about'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
]
