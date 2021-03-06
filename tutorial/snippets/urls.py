# from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

from snippets.views import SnippetViewSet, UserViewSet, api_root, PFRtoGuidViewSet, GameViewSet, GameViewSetSubset, SeasonViewSet, SeasonViewSetSubset, CareerViewSet, SeasonAverageViewSet
from rest_framework import renderers


games_list = GameViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

games_list_subset = GameViewSetSubset.as_view({
    'get': 'list'
})

games_detail = GameViewSet.as_view({
    'delete': 'destroy',
})

seasons_list = SeasonViewSet.as_view({
    'get':'list'
    'post': 'create'
})

seasons_list_subset = SeasonViewSetSubset.as_view({
    'get': 'list'
})

seasons_pupdate = SeasonViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update'
})

season_average = SeasonAverageViewSet.as_view({
    'get': 'list'
})

season_average_update = SeasonAverageViewSet.as_view({
    'put': 'update'
})

careers_list = CareerViewSet.as_view({
    'get':'list',
    'post': 'create'
})

careers_pupdate = CareerViewSet.as_view({
    'patch': 'partial_update',
    'get': 'retrieve'

})

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),

    # Guid routes
    # url(r'^pfrguids/$', pfrguids_list, name='pfrguids-list'),
    # # url(r'^pfrguids/(?P<pk>[0-9]+)/$', pfrguids_detail, name='pfrguids-detail')
    # url(r'^pfrguids/(?P<pk>[a-zA-z0-9_]+)/$', pfrguids_fetch_guid, name='pfrguids-fetch-guid'),
    # url(r'^pfrguids/(?P<pk>[a-zA-z0-9_]+)/guid/$', pfrguids_fetch_guid_only, name='pfrguids-fetch-guid-only'),

    # Game log route
    url(r'^games/$', games_list, name='games-list'),
    url(r'^games/(?P<pk>[a-zA-z0-9]+)/$', games_detail, name='games-detail'),
    
    # Game subset route
    url(r'^games_subset/$', games_list_subset, name='games-list-subset'),

    # Season route
    url(r'^seasons/$', seasons_list, name='seasons-list'),
    url(r'^seasons/(?P<pk>[a-zA-z0-9]+)/$', seasons_pupdate, name='seasons-pupdate'),

    # Season subset route
    url(r'^seasons_subset/$', seasons_list_subset, name='seasons-list-subset'),

    # Career route
    url(r'^careers/$', careers_list, name='careers-list'),
    url(r'^careers/(?P<pk>[a-zA-z0-9]+)/$', careers_pupdate, name='careers-pupdate'),
    # url(r'^careers/"([a-zA-Z]+[0-9]+|[a-zA-Z]+\.[0-9]+)"', careers_pupdate, name='careers-pupdate'),


    # Season ff_pt averages
    url(r'^season-ffpt-averages/$', season_average, name=season-average),
    url(r'^season-ffpt-averages/(?P<pk>[0-9]+)/$', season_average_update, name=season-average-update),
])