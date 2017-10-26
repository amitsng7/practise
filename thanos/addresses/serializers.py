from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	HyperlinkedModelSerializer,
)
from .models import Address
from zipcodes.models import Zipcode
from zipcodes.serializers import ZipcodeDetailSerializer

class AddressCreateSerializer(ModelSerializer):
	class Meta:
		model = Address
		fields = [
			'id',
			'street',
    		'landmark',
    		'city',
    		'zipcode',
		]

class AddressListSerializer(ModelSerializer):
	zipcode = ZipcodeDetailSerializer()
	class Meta:
		model = Address
		fields = [
			'id',
			'street',
    		'landmark',
    		'city',
    		'zipcode',
    		'updated',
    		'timestamp',
		]

class AddressDetailSerializer(ModelSerializer):
	zipcode = ZipcodeDetailSerializer()
	class Meta:
		model = Address
		fields = [
			'id',
			'street',
    		'landmark',
    		'city',
    		'zipcode',
    		'updated',
    		'timestamp',
		]
		read_only_fields=[
		    'updated',
		    'timestamp',
		]

class AddressSerializer(ModelSerializer):
	# zipcode = ZipcodeDetailSerializer()
	class Meta:
		model = Address
		fields = [
			'id',
			'street',
    		'landmark',
    		'city',
    		'zipcode',
    		'updated',
    		'timestamp',
		]
		read_only_fields=[
		    'updated',
		    'timestamp',
		]
	def update(self, instance, validated_data):
		instance.street = validated_data.get('street', instance.street)
		instance.landmark = validated_data.get('landmark', instance.landmark)
		instance.city = validated_data.get('city', instance.city)
		instance.zipcode = validated_data.pop('zipcode', instance.zipcode)
		instance.save()
		return instance