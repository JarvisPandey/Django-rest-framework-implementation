from rest_framework import serializers
from . models import query


class queryserializer(serializers.ModelSerializer):

	class Meta:
		model=query
		fields='__all__'