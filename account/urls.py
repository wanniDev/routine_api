from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignupView.as_view()),
    path('token/', views.EmailTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]