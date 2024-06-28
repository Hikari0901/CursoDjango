
from django.contrib import admin
from django.urls import path

from home.views import IndexView, PruebaListView, ModeloPruebaListView
urlpatterns = [
    path('home/', IndexView.as_view()),
    path('lista/', PruebaListView.as_view()),
    path('lista-prueba/', ModeloPruebaListView.as_view()),
    path('admin/', admin.site.urls),
]
