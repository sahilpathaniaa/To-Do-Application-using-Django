
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('to_do_app.urls')),
    path('', include('to_do_app.urls_api')),
    path('admin/', admin.site.urls),
]
