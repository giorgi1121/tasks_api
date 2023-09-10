from django.urls import path, include
from rest_framework import routers
from .views import TasksView

router = routers.DefaultRouter()
router.register(r"", TasksView, "tasks")

urlpatterns = [
    path("", include(router.urls))
]