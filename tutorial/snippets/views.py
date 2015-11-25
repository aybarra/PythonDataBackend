from snippets.models import Snippet, PFRtoGuidModel, GameModel, SeasonModel, CareerModel, SeasonAverageModel
from snippets.serializers import SnippetSerializer, GameSerializer, SeasonSerializer, CareerSerializer, SeasonAverageSerializer
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

# class PFRtoGuidViewSet(viewsets.ModelViewSet):
#     serializer_class = PFRGuidSerializer
#     queryset = PFRtoGuidModel.objects.all()

#     def perform_create(self, serializer):
#         serializer.save()
    
#     ''' Fetches name, pfr_name and guid '''
#     def retrieve(self, request, pk=None):
#         queryset = PFRtoGuidModel.objects.all()
#         player = get_object_or_404(queryset, pk=pk)
#         serializer = PFRGuidSerializer(player)
#         return Response(serializer.data)

#     @detail_route(url_path='guid')
#     def retrieve_guid_only(self, request, *args, **kwargs):
#         player = self.get_object()
#         return Response({'pguid': player.pguid})

class CareerFilter(django_filters.FilterSet):
    start_year = django_filters.NumberFilter(name="start_year", lookup_type='gte')
    start_year_end = django_filters.NumberFilter(name="start_year", lookup_type='lt')
    min_pts = django_filters.NumberFilter(name="ff_pts", lookup_type='gte')
    max_pts = django_filters.NumberFilter(name="ff_pts", lookup_type='lt')
    active = django_filters.BooleanFilter(name="active")

    choices = (('qb', 'QB'), ('wr', 'WR'), ('rb', 'RB'), ('te', 'TE'),)
    pos = django_filters.MultipleChoiceFilter(name="pos_type", choices=choices)
    class Meta:
        model = CareerModel
        fields = ['start_year', 'start_year_end', 'min_pts', 'max_pts', 'active', 'pos']

class CareerViewSet(viewsets.ModelViewSet):
    serializer_class = CareerSerializer
    queryset = CareerModel.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CareerFilter

    def perform_create(self, request):
        # if CareerModel.objects.filter(pguid=request.POST['pguid']).exists():
        #     content = {'error_creating_career': 'career with specified pguid already exists'}
        #     return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # else:
        request.save()

    # def partial_update(self, request, pk=None)

class SeasonFilter(django_filters.FilterSet):
    starts_with = django_filters.CharFilter(name='season_guid', lookup_type='icontains')
    
    class Meta:
        model = SeasonModel
        fields = ['starts_with']

class SeasonViewSet(viewsets.ModelViewSet):
    serializer_class = SeasonSerializer
    queryset = SeasonModel.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = SeasonFilter

    def perform_create(self, serializer):
        # if SeasonModel.objects.filter(pguid=serializer.POST['pguid'], year=int(serializer.POST['year'])).exists():
        #     content = {'error_creating_season': 'season with pguid and year already exists'}
        #     return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # else:
        serializer.save()

class GameFilter(django_filters.FilterSet):
    starts_with = django_filters.CharFilter(name='game_guid', lookup_type='icontains')
    
    class Meta:
        model = GameModel
        fields = ['starts_with']

class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = GameModel.objects.all() 
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class=GameFilter

    def perform_create(self, serializer):
        # if GameModel.objects.filter(pguid=serializer.POST['pguid'], date=serializer.POST['date']).exists():
        #     content = {'error_creating_game': 'game with pguid and date already exists'}
        #     return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # else:
        serializer.save()

class SeasonAverageViewSet(viewsets.ModelViewSet):
    serializer_class = SeasonAverageSerializer
    queryset = SeasonAverageModel.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer