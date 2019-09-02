from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
from .routers import router

app_name = 'main'

urlpatterns = [
    path('api/', include(router.urls), name='api'),
]