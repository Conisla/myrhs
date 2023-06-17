from rest_framework import serializers

from api.models import Salarie


class SalarieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salarie
        fields = '__all__'