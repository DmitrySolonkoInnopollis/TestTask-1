from django.contrib import admin
from django.urls import path, include

from mainapp.views import index, registration, catalogs, test
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('catalog/<int:pk>/', catalogs, name='catalog'),
    path('catalog/', catalogs, name='catalog'),
    path('catalog/test/<int:pk>/', test, name='test'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', registration, name='registration'),
]
