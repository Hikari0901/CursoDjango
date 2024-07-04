
from django.contrib import admin
from django.urls import path, include

from home.views import IndexView, PruebaListView, ModeloPruebaListView
urlpatterns = [
    #ruta principal admin
    path('admin/', admin.site.urls),
    
    #incluir rutas empleados
    path('', include('empleados.urls')),
]
