from rest_framework import serializers

from tickets.models import Organization

###
### Admin Serializers
###
class AdminOrganization(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "name", "address", "city", "state", "zip_code", "phone_number", "is_active", "is_paid", "users", "labels"]
        read_only_fields = ["id"]

###
### Non-Admin Serializers
###
class Organization(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "name", "address", "city", "state", "zip_code", "phone_number", "users", "labels"]
        read_only_fields = ["id", "name"]

