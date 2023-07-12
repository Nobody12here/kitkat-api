from django.contrib.auth.models import User
from .models import KitKat
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username','email']
class KitKatSerializer(serializers.ModelSerializer):
	sender = UserSerializer()
	receiver = UserSerializer()
	class Meta:
		model = KitKat
		fields = ['id','description','amount','sender','receiver','date','seen']
		