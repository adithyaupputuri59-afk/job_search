
from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):

    applicant_name = serializers.CharField(
        source="applicant.username",
        read_only=True
    )

    job_title = serializers.CharField(
        source="job.title",
        read_only=True
    )

    class Meta:
        model = Application
        fields = [
            "id",
            "applicant",
            "applicant_name",
            "job",
            "job_title",
            "applied_at",
            "status",
        ]

        read_only_fields = [
            "id",
            "applicant",
            "applied_at",
            "status",
        ]
