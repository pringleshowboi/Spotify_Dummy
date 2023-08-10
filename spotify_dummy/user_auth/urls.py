from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.login_register_view, name='login_register_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
