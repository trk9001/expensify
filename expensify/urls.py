from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='login', template_name='registration/logged_out.html'),
        name='logout'
    ),
    path('', include('core.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += (
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
