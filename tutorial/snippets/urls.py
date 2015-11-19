# from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

from snippets.views import SnippetViewSet, UserViewSet, api_root, PFRtoGuidViewSet, GameViewSet, SeasonViewSet, CareerViewSet
from rest_framework import renderers

# pfrguids_list = PFRtoGuidViewSet.as_view({
# 	'get': 'list',
# 	'post': 'create'
# })

# pfrguids_fetch_guid = PFRtoGuidViewSet.as_view({
#     'get': 'retrieve'
# })

# pfrguids_fetch_guid_only = PFRtoGuidViewSet.as_view({
#     'get': 'retrieve_guid_only'
# })

games_list = GameViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

games_detail = GameViewSet.as_view({
    'delete': 'destroy'
})

seasons_list = SeasonViewSet.as_view({
    'get':'list'
    'post': 'create'
})

careers_list = CareerViewSet.as_view({
    'get':'list'
    'post': 'create'
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

    # Season route
    url(r'^seasons/$', seasons_list, name='seasons-list'),

    # Career route
    url(r'^careers/$', careers_list, name='careers-list'),
])

# # API endpoints
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^snippets/$',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     url(r'^users/$',
#         views.UserList.as_view(),
#         name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ])

# # Login and logout views for the browsable API
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]


# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)