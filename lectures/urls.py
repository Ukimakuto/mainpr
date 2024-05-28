from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', userlogin, name='home'),
    path('home', home, name='home'),
    path('login/', userlogin, name='login'),
    path('logout', userlogout, name='logout'), 
    path('prog1lec', lec_one, name='lecture1'), 
    path('prog2lec', lec_two, name='lecture2'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
