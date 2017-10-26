from rest_framework.serializers import (
	ModelSerializer,
)
from .models import SubCategory
from companies.models import Company
from categories.models import Category
from companies.serializers import CompanyDetailSerializer
from categories.serializers import CategoryDetailSerializer

class SubCategoryCreateSerializer(ModelSerializer):
	class Meta:
		model = SubCategory
		fields = [
			'id',
    		'name',
			'code',
            'category_id',
    		'company_id',
    		'updated',
            'timestamp',
		]

class SubCategoryListSerializer(ModelSerializer):
	# address = AddressDetailSerializer()
	class Meta:
		model = SubCategory
		fields = [
			'id',
    		'name',
			'code',
            'category_id',
    		'company_id',
    		'updated',
            'timestamp',
		]

class SubCategoryDetailSerializer(ModelSerializer):
    company_id = CompanyDetailSerializer()
    category_id = CategoryDetailSerializer()
    class Meta:
        model = SubCategory
        fields = [
			'id',
    		'name',
			'code',
            'category_id',
    		'company_id',
    		'updated',
            'timestamp',
		]
        read_only_fields=[
		    'updated',
		    'timestamp',
		]

class SubCategorySerializer(ModelSerializer):
	class Meta:
		model = SubCategory
		fields = [
			'id',
    		'name',
			'code',
            'category_id',
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
		instance.category_id = validated_data.get('category_id', instance.category_id)
		instance.company_id = validated_data.pop('company_id', instance.company_id)
		instance.save()
		return instance