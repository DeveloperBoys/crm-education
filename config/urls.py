from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.authentication import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.loginPage, name='login'),
    path('doLogin/', auth_views.doLogin, name='doLogin'),
    path('logout_user/', auth_views.logout_user, name="logout_user"),
    path('', include('apps.accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)