"""URLs project module"""


from django.contrib import admin
from django.urls import path
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # users
    path('login/', users_views.login_view, name='login'),
]
