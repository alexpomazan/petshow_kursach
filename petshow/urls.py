from django.urls import include, path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/login/', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('cabinet', views.cabinet, name="cabinet"),
    path('cabinet', TemplateView.as_view(template_name="cabinet.html"), name="settings"),
    path('accounts/', include('django.contrib.auth.urls'))
]