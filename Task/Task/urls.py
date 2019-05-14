from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView  # new


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'signup', include('users.urls', namespace='users')),
    url(r'order/', include('order.urls', namespace='order')),
    url('', TemplateView.as_view(template_name='home.html'), name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
