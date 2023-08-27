from rest_framework.serializers import Serializer
from rest_framework import serializers
from .models import Link

jsonDict = {
    "link": "https://mobina.com",
    "description": "m♥bina is my l♥ve",
    "owner": "Amani",
    "shortedLink": "tadaa",
}


class LinkSerializerOld(Serializer):
    link = serializers.CharField(max_length=255)
    description = serializers.CharField(
        max_length=511, allow_blank=True, allow_null=True
    )
    owner = serializers.CharField(max_length=255)
    shortedLink = serializers.CharField(max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `Link` instance, given the validated data.
        """
        return Link.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Link` instance, given the validated data.
        """
        instance.link = validated_data.get("link", instance.link)
        instance.description = validated_data.get("description", instance.description)
        instance.owner = validated_data.get("owner", instance.owner)
        instance.shortedLink = validated_data.get("shortedLink", instance.shortedLink)
        instance.save()
        return instance


class LinkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Link
        fields = "__all__"


from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Link.objects.all()
    )

    class Meta:
        model = User
        fields = "__all__"
