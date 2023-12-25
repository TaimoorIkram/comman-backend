from django.shortcuts import render
from rest_framework import generics
from .models import Customer, Feedback, Task, Bill, CustomerTask
from .serializers import CustomerSerializer, FeedbackSerializer, CustomerTaskSerializer, BillSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class CustomersView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    ordering_fields = ['first_name', 'last_name']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
class CustomerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    ordering_fields = ['first_name', 'last_name']
    
    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]

class CustomerRelationshipsView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        """
        Return a list of assigned relationships

        ### Requires:   
            - id of the employee to get the relationships of.
        ### Returns:    
            - a json response that contains all customers associated to that employee id.
            - all unassigned customers returned if no id is sent in query.
        """
        
        id = request.GET.get('id')
        results = CustomerTask.objects.all()

        if id: results = CustomerTask.objects.filter(customer_id=id)
        else: results = CustomerTask.objects.filter(employee_id=None)
        serialized_results = CustomerTaskSerializer(results, many=True)
        return Response(serialized_results.data)    

class TasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = CustomerTaskSerializer
    ordering_fields = ['task__date_due']
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    search_fields = ['task__title', 'task__completion_status', 'task__date_due']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]    

class TaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = CustomerTaskSerializer
    ordering_fields = ['task__date_due']
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    search_fields = ['task__title', 'task__completion_status', 'task__date_due']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
class FeedbacksView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    ordering_fields = ['rating', 'heading']
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    search_fields = ['heading', 'comment', 'rating']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]    

class FeedbackView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    ordering_fields = ['rating', 'heading']
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    search_fields = ['heading', 'comment', 'rating']
    
    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]

class BillsView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    ordering_fields = ['payment_status', 'date_due', 'arrears']
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    search_fields = ['customer__first_name', 'customer__last_name', 'date_due']

    def create(self, request, *args, **kwargs):
        unpaid_bills = Bill.objects.filter(customer__id=request.data['customer_id'], payment_status=False)
        arrears = 0
        for bill in unpaid_bills: arrears += bill.amount
        request.data['arrears'] = arrears
        
        return super().create(request, *args, **kwargs)

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]    

class BillView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    ordering_fields = ['payment_status', 'date_due', 'arrears']
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    search_fields = ['customer__first_name', 'customer__last_name', 'date_due']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
