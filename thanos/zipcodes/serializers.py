from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
)
from .models import Zipcode

class ZipcodeCreateSerializer(ModelSerializer):
	class Meta:
		model = Zipcode
		fields = [
			'zipcode',
    		'state',
		    'country',
		]

class ZipcodeListSerializer(ModelSerializer):
	# url = HyperlinkedIdentityField(
	# 	view_name = "zipcodes-api:detail",
	# )
	class Meta:
		model = Zipcode
		fields = [
			# 'url',
			'zipcode',
    		'state',
		    'country',
		    'updated',
		    'timestamp',
		]

class ZipcodeDetailSerializer(ModelSerializer):
	class Meta:
		model = Zipcode
		fields = [
			'zipcode',
    		'state',
		    'country',
		    'updated',
		    'timestamp',
		]
		read_only_fields=[
		    'updated',
		    'timestamp',
		]
