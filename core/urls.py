from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('finances/', include('apps.finances.urls')),
    path('stocks/', include('apps.stocks.urls')),
]
