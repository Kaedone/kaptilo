from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('create-link', views.create_link, name="create_link"),
    path('login/', views.login, name="login"),
    path('auth/', views.register, name='auth'),
    path('logout/', views.logout, name="logout"),
    path('<int:id>', views.show_link, name='show_link')
]