from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

from main.models import Posts, UserProfile


# Permets de serializer les models et retourner les propriete desire pour le model
class PostSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ["id", "post_title", "post_description"]
