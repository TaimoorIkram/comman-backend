from django.shortcuts import render
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer

# Create your views here.
# app views
def home(request):
    members = Member.objects.all()

    return render(request, 'html/dash_team.html', context={'members' : members})

# api views
class MembersView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer