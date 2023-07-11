from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class KitKat(models.Model):
	description = models.CharField(max_length=200) # short description to why the kitkat was sent to the other person
	sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name='sender')
	receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name='receiver')
	date = models.DateTimeField(auto_now_add=True)
	seen = models.BooleanField(default=False)
	amount = models.IntegerField(default=0)
	def __str__(self):
		return self.description
