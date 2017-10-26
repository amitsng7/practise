from rest_framework.serializers import (
	ModelSerializer,
)
from .models import Team
from companies.models import Company
from companies.serializers import CompanyDetailSerializer

class TeamCreateSerializer(ModelSerializer):
	class Meta:
		model = Team
		fields = [
			'id',
    		'name',
			'code',
			'detail_type',
    		'company_id',
    		'updated',
            'timestamp',
		]

class TeamListSerializer(ModelSerializer):
	class Meta:
		model = Team
		fields = [
			'id',
    		'name',
			'code',
			'detail_type',
    		'company_id',
    		'updated',
            'timestamp',
		]

class TeamDetailSerializer(ModelSerializer):
    company_id = CompanyDetailSerializer()
    class Meta:
        model = Team
        fields = [
			'id',
    		'name',
			'code',
			'detail_type',
    		'company_id',
    		'updated',
            'timestamp',
		]
        read_only_fields=[
		    'updated',
		    'timestamp',
		]

class TeamSerializer(ModelSerializer):
	class Meta:
		model = Team
		fields = [
			'id',
    		'name',
			'code',
			'detail_type',
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
		instance.detail_type = validated_data.get('detail_type', instance.detail_type)
		instance.company_id = validated_data.pop('company_id', instance.company_id)
		instance.save()
		return instance