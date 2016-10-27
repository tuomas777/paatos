from rest_framework import viewsets
from decisions.models import Category
from .base import DataModelSerializer


class CaseCategorySerializer(DataModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CaseCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CaseCategorySerializer
