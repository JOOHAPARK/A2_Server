from rest_framework import serializers
from .models import *

# class UserInputSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserInput
#         fields = ['id','st_x','st_y','radius','checkbox']

class LikeSerializer(serializers.ModelSerializer):
    liked = serializers.SerializerMethodField()
    like_count = serializers.ReadOnlyField()


    class Meta:
        model = likes
        fields = '__all__'

    def get_liked(self, obj):
        user = self.context['request'].user
        return user in obj.liked_users.all()