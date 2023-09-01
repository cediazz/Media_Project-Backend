from django.urls import path, include
from .views import MyTokenObtainPairView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [

    path('login/',MyTokenObtainPairView.as_view()),
    path('refresh-token/',jwt_views.TokenRefreshView.as_view()),

]