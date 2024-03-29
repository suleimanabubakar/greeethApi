"""greeeth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import SimpleRouter
from projects.views import *



from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Greeeth API",
      default_version='v1',
      description="Greeeth ApiEndpoints",
      terms_of_service="",
      contact=openapi.Contact(email="info@greeeth.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = SimpleRouter()
router.register('projectdetails',viewset=ProjectDetails,basename="project_details")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('authentication.urls')),
    path('trees/',include('trees.urls')),
    path('maintainance/',include('maintainance.urls')),
    path('projects/',include('projects.urls')),
    path('treeshare/',include('treeshare.urls')),
    path('wallet/',include('wallet.urls')),
    path('',include(router.urls)),
    path('awards/',include('awarding.urls')),
    path('carbonfootprint/',include('carbonfootprint.urls')),
    path('account/',include('accounts.urls')),
    path('orgs/',include('organisations.urls')),
    path('coupon/',include('coupon.urls')),

    path('currencies/',include('points.urls')),
    path('waste/',include('wastes.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
