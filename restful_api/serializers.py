# rest framework 사용 시 필수 파일, 직접 생성해야함

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('_id', 'password', 'name')
        # fields = '__all__'