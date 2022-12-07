from rest_framework import serializers
from apiapp.models import *

#Create serializers here
class Companyserializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

class Employeeserializer(serializers.HyperlinkedModelSerializer):
    emp_id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"