from rest_framework import serializers

from estimator.models import LogsModel


class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogsModel
        fields = ('id', 'method', 'endpoint', 'status', 'response_time')
