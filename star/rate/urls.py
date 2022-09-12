from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'       

urlpatterns = [
    path('', home ,name='home'),
    path('rate-image/', rate_img ,name='rate_img'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
