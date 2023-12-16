from django.shortcuts import render
from rest_framework import generics
from .models import Customer, Feedback, Task, Bill
from .serializers import CustomerSerializer, FeedbackSerializer, TaskSerializer, BillSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class CustomersView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication]
    ordering_fields = ['first_name', 'last_name', 'visit_date']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
class CustomerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [SessionAuthentication]
    ordering_fields = ['first_name', 'last_name', 'visit_date']
    
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
        results = Customer.objects.all()

        if id: results = Customer.objects.filter(employee_id=id)
        else: results = Customer.objects.filter(employee_id=None)
        serialized_results = CustomerSerializer(results, many=True)
        return Response(serialized_results.data)
    

class TasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    ordering_fields = ['due_date']
    authentication_classes = [SessionAuthentication]
    search_fields = ['title', 'member__first_name', 'due_date']

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    

class TaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    ordering_fields = ['due_date']
    authentication_classes = [SessionAuthentication]
    search_fields = ['title', 'member__first_name', 'due_date']
    
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
    ordering_fields = ['payment_status', 'due_date', 'arrears']
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    search_fields = ['customer__first_name', 'customer__last_name', 'due_date']

    def create(self, request, *args, **kwargs):
        unpaid_bills = Bill.objects.filter(customer__id=request.data['customer_id'], payment_status=False)
        arrears = 0
        for bill in unpaid_bills: arrears += bill.due_amount
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
    ordering_fields = ['payment_status', 'due_date', 'arrears']
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    search_fields = ['customer__first_name', 'customer__last_name', 'due_date']
    
    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
