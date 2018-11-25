from django.conf.urls import url
from views import home, conexion, consultar


urlpatterns = [
    url(r'^home/', home, name="respositorio_home"),
    url(r'^connect/', conexion, name="repositorio_connect"),
    #url(r'consultar/(?P<comando>\w+)$', consultar, name="repositorio_consultar")
    url(r'consultar/', consultar, name="repositorio_consultar")

]
