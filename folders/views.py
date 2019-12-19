from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from core.permissions import IsCreatorOrReadOnly
from .models import Folder
from .serializers import FolderSerializer

class FolderViewSet(ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # if self.action == 'own':
        #     return Folder.objects.filter(user_id=self.request.user)
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