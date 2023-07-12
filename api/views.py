from django.contrib.auth.models import User
from .models import KitKat
from rest_framework import viewsets,permissions
from .serializer import UserSerializer,KitKatSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]
class KitKatViewSet(viewsets.ModelViewSet):
	queryset = KitKat.objects.all()
	serializer_class = KitKatSerializer
	#permission_classes = [permissions.IsAuthenticated]
	def perform_create(self,serializer):
		serializer.save(sender=self.request.user)