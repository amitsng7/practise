from rest_framework.serializers import (
	ModelSerializer,
)
from .models import t_Department
from companies.models import Company
from companies.serializers import CompanyDetailSerializer

class DepartmentCreateSerializer(ModelSerializer):
	class Meta:
		model = t_Department
		fields = [
			'id',
    		'name',
			'code',
    		'company_id',
    		'updated',
            'timestamp',
		]

class DepartmentListSerializer(ModelSerializer):
	class Meta:
		model = t_Department
		fields = [
			'id',
    		'name',
			'code',
    		'company_id',
    		'updated',
            'timestamp',
		]

class DepartmentDetailSerializer(ModelSerializer):
    company_id = CompanyDetailSerializer()
    class Meta:
        model = t_Department
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

class DepartmentSerializer(ModelSerializer):
	class Meta:
		model = t_Department
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