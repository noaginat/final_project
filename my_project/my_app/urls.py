from django.urls import path, include
from . import views
from rest_framework import routers
app_name = "employees"


router = routers.DefaultRouter()
router.register('employees', views.EmployeeView)
# router.register('job_type', views.TypeView)
# router.register('kind', views.KindView)
# router.register('specified', views.SpecifiedView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('employees/', views.employees_list, name='data'),
    path('<slug:slug>', views.employee_details, name='details')

]