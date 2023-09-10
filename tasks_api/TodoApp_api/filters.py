import django_filters
from .models import Tasks

class TaskFilter(django_filters.FilterSet):
  title = django_filters.CharFilter(lookup_expr="icontains")
  class Meta:
    model = Tasks
    fields = ["completed", "title"]