# serializers are classes that take a model and serialize its objects into json data
# work like a model form
from rest_framework.serializers import ModelSerializer
from base.models import Room 


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


