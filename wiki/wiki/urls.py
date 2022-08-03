from django.contrib import admin
from django.urls import path, include
from uche.views import user_login, user_logout, success


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uche.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    
    

    
]


