import django_filters
from .models import *

 class regionFilter(django_filters.FilterSet):
 	class Meta:
 		model = Dealer
 		