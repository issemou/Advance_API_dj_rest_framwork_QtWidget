from django.http import HttpResponse
from rest_framework import viewsets

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from main.models import Posts
from main.serializer import PostSerializers


# Creation des vues pour API

# Permet de faire sur une meme url (get, post, put, delete)
class PostViewSets(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


# Permet de definir une methode pour chaque action ( get, post, put, delete)
class PostViewSetsAlternate(viewsets.ViewSet):

    def list(self, request):
        posts = Posts.objects.all()
        serializer = PostSerializers(posts, many=True, context={'request': request})
        data = serializer.data
        return Response({"error": False, "message": "List of Post", "data": data})

    def create(self, request):
        serializer = PostSerializers(data=request.data, context={'request': request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "New Data Created"})

    def update(self, request, pk=None):
        queryset = Posts.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializers(post, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Data Update"})

    def retrieve(self, request, pk=None):
        queryset = Posts.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializers(post, context={"request": request})
        return Response({"error": False, "message": "Success", "data": serializer.data})

    def destroy(self, request, pk=None):
        queryset = Posts.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response({"error": False, "message": "Post Deleted"})


post_get_data = PostViewSetsAlternate.as_view({"get": "list"})
post_create_data = PostViewSetsAlternate.as_view({"post": "create"})
post_update_data = PostViewSetsAlternate.as_view({"put": "update"})
post_get_data_by_id = PostViewSetsAlternate.as_view({"get": "retrieve"})
post_destroy = PostViewSetsAlternate.as_view({"delete": "destroy"})
