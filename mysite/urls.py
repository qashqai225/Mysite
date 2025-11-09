
from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', userViews.register, name='register'),
    path('profile/', userViews.profile, name='profile'),
    path('user/', authViews.LoginView.as_view(template_name='users/users.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(
    template_name='users/exit.html',
    next_page=None  # Отключаем редирект, чтобы показать шаблон
), name='exit'),
    path('', include('blog.urls'))
]
