from django.shortcuts import render
from .models import *
from apiapp.serializers import Companyserializer,Employeeserializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

#A ViewSet class is simply a type of class-based View,
# that does not provide any method handlers such as .get() or .post(), 
# and instead provides actions such as .list() and .create().

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=Companyserializer
    
    # companies/{companyId}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            # print("get employees of ", pk, "company")

            company=Company.objects.get(pk=pk)
            emp=Employee.objects.filter(company=company)
            emp_serializer=Employeeserializer(emp,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'company might not exist!! Error'})
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer