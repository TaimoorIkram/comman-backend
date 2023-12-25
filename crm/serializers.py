from rest_framework import serializers
from .models import Customer, Feedback, CustomerTask, Bill
from hrm.serializers import OrganizationSerializer, TaskSerializer

class CustomerSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    organization_id = OrganizationSerializer(write_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'rating': {
                'min_value': 1,
                'max_value': 5,
            }
        }

class CustomerTaskSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.IntegerField(write_only=True)

    task = TaskSerializer(read_only=True)
    task_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CustomerTask
        fields = '__all__'
        depth = 1

class BillSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Bill
        fields = '__all__'
        depth = 1