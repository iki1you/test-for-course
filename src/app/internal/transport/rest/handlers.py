from rest_framework.generics import RetrieveAPIView, CreateAPIView

from rest_framework import serializers

from ....models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone', 'username', 'first_name', 'last_name']


class GetData(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class AddData(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer