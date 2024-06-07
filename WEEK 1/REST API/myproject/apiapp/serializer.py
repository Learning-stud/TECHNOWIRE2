from rest_framework import serializers
from .models import blogs

class blogserializing(serializers.ModelSerializer):
 class Meta:
  model = blogs
  fields = ['id','title','content','date_publish']