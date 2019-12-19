"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from core.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

from users.views import UserViewSet
from taggit.views import tagged_object_list
from users import views as users_views
from folders.views import FolderViewSet
from pages.views import PageViewSet


router = DefaultRouter(False)
router.register('users', UserViewSet)
router.register('pages', PageViewSet)
router.register('folders', FolderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('password/set/<str:uid>/<str:token>/', users_views.password),
    path('password/reset/<str:uid>/<str:token>/', users_views.repassword),
]
