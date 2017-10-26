from rest_framework.serializers import (
	ModelSerializer,
)
from .models import Company
from addresses.models import Address
from addresses.serializers import AddressDetailSerializer

class CompanyCreateSerializer(ModelSerializer):
	class Meta:
		model = Company
		fields = [
			'id',
    		'info',
    		'name',
    		'corporate_type',
    		'phone_number',
    		'website',
            'email',
            'address_id',
            'emp_count',
            'updated',
            'timestamp',
		]

class CompanyListSerializer(ModelSerializer):
	# address = AddressDetailSerializer()
	class Meta:
		model = Company
		fields = [
			'id',
    		'info',
    		'name',
    		'corporate_type',
    		'phone_number',
    		'website',
            'email',
            'address_id',
            'emp_count',
            'updated',
            'timestamp',
		]

class CompanyDetailSerializer(ModelSerializer):
	address_id = AddressDetailSerializer()
	class Meta:
		model = Company
		fields = [
			'id',
    		'info',
    		'name',
    		'corporate_type',
    		'phone_number',
    		'website',
            'email',
            'address_id',
            'emp_count',
            'updated',
            'timestamp',
		]
		read_only_fields=[
		    'updated',
		    'timestamp',
		]

class CompanySerializer(ModelSerializer):
	class Meta:
		model = Company
		fields = [
			'id',
    		'info',
    		'name',
    		'corporate_type',
    		'phone_number',
    		'website',
            'email',
            'address_id',
            'emp_count',
            'updated',
            'timestamp',
		]
		read_only_fields=[
		    'updated',
		    'timestamp',
		]
	def update(self, instance, validated_data):
		instance.info = validated_data.get('info', instance.info)
		instance.name = validated_data.get('name', instance.name)
		instance.corporate_type = validated_data.get('corporate_type', instance.corporate_type)
		instance.phone_number = validated_data.pop('phone_number', instance.phone_number)
		instance.website = validated_data.get('website', instance.website)
		instance.email = validated_data.get('email', instance.email)
		instance.address_id = validated_data.get('address_id', instance.address_id)
		instance.emp_count = validated_data.pop('emp_count', instance.emp_count)
		instance.save()
		return instance