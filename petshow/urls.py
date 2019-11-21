from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('shows/', views.shows, name="shows"),
    path('article/', views.article, name="article"),
    path('about_us/', views.about_us, name="about_us"),
    path('cabinet', views.cabinet, name="cabinet"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', views.contactform, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
]