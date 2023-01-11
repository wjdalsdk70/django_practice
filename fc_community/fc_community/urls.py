from django.contrib import admin
from django.urls import include, path
from fcuser.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('fcuser/', include('fcuser.urls')),
    path('', home),
]
