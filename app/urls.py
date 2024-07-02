from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Главный корневой settings, даже главнее чем наш.
from django.conf.urls.static import static
from app.settings import DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('main.urls')),
    path('', include('goods.urls')),
    path('crud/', include('crud_app.urls')),
    path('user/', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

