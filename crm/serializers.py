from rest_framework import serializers
from .models import Customer, Feedback, Task, Bill
from hrm.serializers import MemberSerializer

class CustomerSerializer(serializers.ModelSerializer):
    employee = MemberSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)

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

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        depth = 1

class BillSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Bill
        fields = '__all__'
        depth = 1