from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='library/login.html'), name='login'),
    path('', include('library.urls')),
]
