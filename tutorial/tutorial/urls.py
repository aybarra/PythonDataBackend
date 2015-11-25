"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'pfrguids', views.PFRtoGuidViewSet)
router.register(r'careers', views.CareerViewSet)
router.register(r'seasons', views.SeasonViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'season-ffpt-averages', views.SeasonAverageViewSet)
router.register(r'games_subset', views.GameViewSetSubset)
router.register(r'seasons_subset', views.SeasonViewSetSubset)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


# from django.conf.urls import include, url
# from django.contrib import admin
# from django.conf.urls import include

# urlpatterns = [
#     url(r'^', include('snippets.urls')),
# ]

# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]




# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
# ]
