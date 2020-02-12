from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('shows/', views.shows, name="shows"),
    path('shows/dogshow', views.dogshow, name="dogshow"),
    path('shows/catshow', views.catshow, name="catshow"),
    path('shows/mypets', views.mypets, name="mypets"),
    path('article/', views.articles, name="article"),
    path('article/<int:article_id>/', views.detail, name ='detail'),
    path('article/<int:article_id>/leave_comment/', views.leave_comment, name ='leave_comment'),
    path('about_us/', views.about_us, name="about_us"),
    path('cabinet', views.cabinet, name="cabinet"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', views.contactform, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
]