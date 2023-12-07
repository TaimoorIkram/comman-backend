from rest_framework import serializers
from .models import Customer
from hrm.serializers import MemberSerializer

class CustomerSerializer(serializers.ModelSerializer):
    employee = MemberSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1