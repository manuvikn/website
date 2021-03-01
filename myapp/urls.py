from django.urls import path
from myapp.views import *
from django.conf.urls import url

urlpatterns = [
    path('', homePage),
    path("profile/<pk>/", UserDetailView.as_view(), name="profile_detail"),
    url(r'^profile/(?P<pk>\d+)/update$', UsuarioUpdate.as_view(), name='profile_update'),
    path("apariencia/", Apariencia, name="apariencia"),
    path("apariencia/uno", AparienciaUno, name="apariencia_uno"),
    path("apariencia/dos", AparienciaDos, name="apariencia_dos"),
]

