from rest_framework.serializers import (
	ModelSerializer,
)
from .models import t_Group
from companies.models import Company
from companies.serializers import CompanyDetailSerializer

class GroupCreateSerializer(ModelSerializer):
	class Meta:
		model = t_Group
		fields = [
			'id',
    		'name',
			'code',
    		'company_id',
    		'updated',
            'timestamp',
		]

class GroupListSerializer(ModelSerializer):
	class Meta:
		model = t_Group
		fields = [
			'id',
    		'name',
			'code',
    		'company_id',
    		'updated',
            'timestamp',
		]

class GroupDetailSerializer(ModelSerializer):
    company_id = CompanyDetailSerializer()
    class Meta:
        model = t_Group
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

class GroupSerializer(ModelSerializer):
	class Meta:
		model = t_Group
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