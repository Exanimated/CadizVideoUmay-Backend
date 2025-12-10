from rest_framework import serializers

from .models import User



class UserDetailSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'avatar_url',
        )
    
    def get_avatar_url(self, obj):
        if obj.avatar:
            return f'http://localhost:8000{obj.avatar.url}'
        return ''