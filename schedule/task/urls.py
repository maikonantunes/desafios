from django.urls import path,include
from rest_framework import routers

from task.views import TaskViewSet

app_name = 'task'
router = routers.DefaultRouter()
router.register('', TaskViewSet, basename="")

urlpatterns = [
    path('', include(router.urls)),
]
