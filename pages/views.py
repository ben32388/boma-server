from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from core.permissions import IsCreatorOrReadOnly
from .models import Page
from taggit.models import Tag
from .serializers import PageSerializer

class PageViewSet(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    def get_queryset(self):
        # if self.action == 'own':

        #     return Page.objects.filter(user_id=self.request.user)

        if self.action == 'tag_pages':
            pk = self.kwargs.get('pk')
            tag = get_object_or_404(Tag, id=pk)
            
            return Page.objects.filter(tags=tag)

        if self.action == 'folder_pages':
            pk = self.kwargs.get('pk')
            
            return Page.objects.filter(folder=pk)

        return super().get_queryset().filter(user_id=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



    # @action(['DELETE'], False, permission_classes=[IsAuthenticated])
    # def my(self, request):
    #     planargraph = Folder.objects.filter(user_id = self.request.user)
    #     planargraph.delete()
    #     return Response({
    #         'success': True,
    #     })

    # @action(['GET'], False, permission_classes=[IsAuthenticated])
    # def own(self, request):

    #     return self.list(request)

    @action(['GET'], False, permission_classes=[IsAuthenticated])
    def own_tags(self, request):
        pages = Page.objects.filter(user_id=self.request.user)
        own_tags =[]
        tags =[]
        if pages:
            for page in pages:
                own_tags += page.tags.all()
            own_tags = list(set(own_tags))
            for mt in own_tags:
                tags.append({"id":mt.id,"name":mt.name})
                print(mt.id)
            
        return Response(tags)

    @action(['GET'], False, 'tag/(?P<pk>[^/.]+)', permission_classes=[IsAuthenticated])
    def tag_pages(self, request, pk):

        return self.list(request)

    @action(['GET'], False, 'folder_pages/(?P<pk>[^/.]+)', permission_classes=[IsAuthenticated])
    def folder_pages(self, request, pk):

        return self.list(request)