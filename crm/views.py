from django.shortcuts import render
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class CustomersView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_permissions(self):
        permission_classes = []

        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
class CustomerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
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