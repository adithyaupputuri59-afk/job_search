
from rest_framework import serializers
from .models import Job, Application


class JobSerializer(serializers.ModelSerializer):

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Job title cannot be empty."
            )
        return value

    def validate_company(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Company name cannot be empty."
            )
        return value

    def validate_salary(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Salary cannot be negative."
            )
        return value

    class Meta:
        model = Job
        fields = "__all__"
