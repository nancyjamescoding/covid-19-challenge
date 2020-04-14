import uuid

from django.db import models


class LogsModel(models.Model):

    class Meta:
        db_table = 'logs'

    id = models.CharField(
        max_length=50, db_index=True, default=uuid.uuid4, primary_key=True)
    method = models.CharField(
        max_length=200, null=True)
    endpoint = models.CharField(
        max_length=200, null=True)
    status = models.CharField(
        max_length=200, null=True)
    response_time = models.CharField(
        max_length=100, null=True)
