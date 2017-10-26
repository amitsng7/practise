"""thanos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    # url(r'^silk/', include('silk.urls', namespace='silk')),
    url(r'^admin/', admin.site.urls),
    url(r'^zipcodes/', include("zipcodes.urls", namespace='zipcode-api')),
    url(r'^address/', include("addresses.urls", namespace='address-api')),
    url(r'^company/', include("companies.urls", namespace='company-api')),
    url(r'^category/', include("categories.urls", namespace='category-api')),
    url(r'^subcategory/', include("subcategories.urls", namespace='subcategory-api')),
    url(r'^department/', include("t_departments.urls", namespace='department-api')),
    url(r'^group/', include("t_groups.urls", namespace='group-api')),
    # url(r'^locations/', include("t_locations.urls", namespace='location-api')),
    # url(r'^customs/', include("t_customs.urls", namespace='custom-api')),
]
