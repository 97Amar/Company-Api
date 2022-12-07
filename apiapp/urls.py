from django.urls import path,include
from apiapp.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers

#Create a defalut router
#Routers provide an easy way of automatically determining the URL confg.
router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet),
router.register(r'employees',EmployeeViewSet)
urlpatterns = [
    path('',include(router.urls))
]


#companies/{companyid}/employees