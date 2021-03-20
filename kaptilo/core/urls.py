from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.login, name="login"),
    path('auth/', views.register, name='auth'),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('create/', views.create_link, name="create_link"),
    path('<int:pk>/', views.follow_link, name='follow_link')
]
