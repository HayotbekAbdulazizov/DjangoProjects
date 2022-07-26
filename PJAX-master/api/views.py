from rest_framework.response import Response
from main.models import GitProfile, Repository
from .serializers import GitProfileSerializer, RepositorySerializer

# generic view
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin


class GitProfileAPIView(GenericAPIView, CreateModelMixin):
     serializer_class = GitProfileSerializer
     queryset = GitProfile.objects.all()

     def get(self, request):
        gitprofiles = GitProfile.objects.filter(status=True)
        serializer = GitProfileSerializer(gitprofiles, many=True)
        return Response(serializer.data)

     def post(self,request):
         return self.create(request)









class RepositoryAPIView(GenericAPIView, CreateModelMixin):
     serializer_class = RepositorySerializer
     queryset = Repository.objects.all()

     def get(self, request):
        repository = Repository.objects.all()
        serializer = RepositorySerializer(repository, many=True)
        return Response(serializer.data)

     def post(self,request):
         return self.create(request)