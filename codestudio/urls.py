from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main.views import IndexView
from products.views import ProductView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>', ProductView.as_view(), name='product'),
    path('', IndexView.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
