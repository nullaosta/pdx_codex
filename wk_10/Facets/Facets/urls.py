"""Facets URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from gallery.views import (create,
                           retrieve,
                           update,
                           delete,
                           display,
                           thanks)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^gallery/create/', create, name='create'),
    url(r'^gallery/retrieve/(?P<pk>\d+)/', retrieve, name='retrieve'),
    url(r'^gallery/update/(?P<pk>\d+)/', update, name='update'),
    url(r'^gallery/delete/(?P<pk>\d+)/', delete, name='delete'),

    url(r'^gallery/list/', display, name='list'),
    url(r'^gallery/thanks/', thanks, name='thanks')

]

