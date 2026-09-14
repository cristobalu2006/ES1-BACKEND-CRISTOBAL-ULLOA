from django.contrib import admin
from django.urls import path

from paginas_app.views import mostrar_home, mostrar_servicio

urlpatterns = [
    path('', mostrar_home),
    path('servicio/', mostrar_servicio),
    path('admin/', admin.site.urls)
]
