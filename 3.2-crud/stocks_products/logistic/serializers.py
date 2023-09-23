from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position_data in positions:
            StockProduct.objects.create(
                stock=stock,
                product=position_data.get('product'),
                quantity=position_data.get('quantity'),
                price=position_data.get('price')
            )
        return stock

    def update(self, instance, validated_data):

        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for position_data in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=position_data.get('product'),
                defaults={
                    'quantity': position_data.get('quantity'),
                    'price': position_data.get('price')
                }
            )
        return stock
