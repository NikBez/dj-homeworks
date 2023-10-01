from django_filters.rest_framework import FilterSet, CharFilter

from logistic.models import Stock


class ProductFilter(FilterSet):
    product = CharFilter(field_name='products__title', lookup_expr='icontains', label='Поиск по названию товара')
    description = CharFilter(field_name='products__description', lookup_expr='icontains', label='Поиск по описанию товара')

    class Meta:
        model = Stock
        fields = ['products']