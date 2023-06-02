from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('EN_To_BN.urls')),
    path('admin/', admin.site.urls),
]
