from snippets.models import Snippet, PFRtoGuidModel, GameModel
from snippets.serializers import SnippetSerializer, PFRGuidSerializer, GameSerializer
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
    
    # def retrieve(self, request, pk=None):
    #     queryset = PFRtoGuidModel.objects.all()
    #     pfr_name = request.query_params.get('pro_football_ref_name', None)
    #     if pfr_name is not None:
    #         queryset = queryset.filter(pro_football_ref_name=pfr_name) 
    #     return Response(queryset)

    ''' Fetches name, pfr_name and guid '''
    def retrieve(self, request, pk=None):
        queryset = PFRtoGuidModel.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        serializer = PFRGuidSerializer(player)
        return Response(serializer.data)

    @detail_route(url_path='guid')
    def retrieve_guid_only(self, request, *args, **kwargs):
        # queryset = PFRtoGuidModel.objects.all()
        player = self.get_object()
        # serializer = PFRGuidSerializer(player)
        return Response({"pguid": player.pguid})

class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = GameModel.objects.all()

    def perform_create(self, serializer):
        serializer.save()
    # owner=self.request.user)
# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)

# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#     def perform_create(self, serializer):
#     	serializer.save(owner=self.request.user)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly,)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer