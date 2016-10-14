from rest_framework import serializers, viewsets
from decisions.models import Category


class CaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CaseCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CaseCategorySerializer
