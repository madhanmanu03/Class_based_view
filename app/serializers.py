from rest_framework import serializers
from app.models import *
from app.views import *


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'



