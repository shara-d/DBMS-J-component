import django_filters
from django_filters import DateFilter

from .models import *


class UniversityFilter(django_filters.FilterSet):
    class Meta:
        model = University
        fields = '__all__'
        exclude = ['university_id', 'Website']
