from rest_framework.serializers import (
	ModelSerializer,
)
from .models import Category
from companies.models import Company
from companies.serializers import CompanyDetailSerializer

class CategoryCreateSerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = [
			'id',
    		'name',
			'code',
    		'company_id',
    		'updated',
            'timestamp',
		]

class CategoryListSerializer(ModelSerializer):
	# address = AddressDetailSerializer()
	class Meta:
		model = Category
		fields = [
			'id',
    		'name',
			'code',
    		'company_id',
    		'updated',
            'timestamp',
		]

class CategoryDetailSerializer(ModelSerializer):
	company_id = CompanyDetailSerializer()
	class Meta:
		model = Category
		fields = [
			'id',
    		'name',
			'code',
    		'company_id',
    		'updated',
            'timestamp',
		]
		read_only_fields=[
		    'updated',
		    'timestamp',
		]

class CategorySerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = [
			'id',
    		'name',
			'code',
    		'company_id',
    		'updated',
            'timestamp',
		]
		read_only_fields=[
		    'updated',
		    'timestamp',
		]
	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.code = validated_data.get('code', instance.code)
		instance.company_id = validated_data.pop('company_id', instance.company_id)
		instance.save()
		return instance