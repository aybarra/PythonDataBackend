from snippets.models import Snippet, PFRtoGuidModel, GameModel, SeasonModel, CareerModel
from snippets.serializers import SnippetSerializer, PFRGuidSerializer, GameSerializer, SeasonSerializer, CareerSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

# Part V
from rest_framework.decorators import api_view
# from rest_framework.decorators import link
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

# Part VI
from rest_framework import viewsets
from rest_framework.decorators import detail_route

from django.shortcuts import get_object_or_404

# Filtering
import django_filters
from rest_framework import filters

# Serializing joined tables
from django.core import serializers

# import pdb

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'pfrguids': reverse('pfrguids-list', request=request, format=format),
        'games': reverse('games-list', request=request, format=format),
    })

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PFRtoGuidViewSet(viewsets.ModelViewSet):
    serializer_class = PFRGuidSerializer
    queryset = PFRtoGuidModel.objects.all()

    def perform_create(self, serializer):
        serializer.save()
    
    ''' Fetches name, pfr_name and guid '''
    def retrieve(self, request, pk=None):
        queryset = PFRtoGuidModel.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        serializer = PFRGuidSerializer(player)
        return Response(serializer.data)

    @detail_route(url_path='guid')
    def retrieve_guid_only(self, request, *args, **kwargs):
        player = self.get_object()
        return Response({'pguid': player.pguid})

class CareerFilter(django_filters.FilterSet):
    start_year = django_filters.NumberFilter(name="start_year", lookup_type='gte')
    ff_pts = django_filters.NumberFilter(name="ff_pts", lookup_type='gte')

    class Meta:
        model = CareerModel
        fields = ['start_year', 'ff_pts']

class CareerViewSet(viewsets.ModelViewSet):
    serializer_class = CareerSerializer
    queryset = CareerModel.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CareerFilter

    def perform_create(self, request):
        request.save()

class SeasonViewSet(viewsets.ModelViewSet):
    serializer_class = SeasonSerializer
    queryset = SeasonModel.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = GameModel.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer