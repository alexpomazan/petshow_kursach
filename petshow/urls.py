from django.urls import include, path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('cabinet', views.cabinet, name="cabinet"),
    path('accounts/', include('django.contrib.auth.urls'))
]