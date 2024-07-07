from pydoc import pager

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', TemplateView.as_view(template_name='home.html'), name='home'),
                  path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
                  path('accounts/', include('allauth.urls')),
                  path('products/', include('products.urls')),
                  path('cart/', include('cart.urls')),
                  path('order/', include('orders.urls')),
                  path('payment/', include('payment.urls')),

                  # Rosetta
                  path('rosetta/', include('rosetta.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
