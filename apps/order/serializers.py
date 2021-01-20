from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.order.models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    delivery_address = serializers.CharField(required=True)
    order_products = OrderProductSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = (
            'delivery_address', 'order_products',
        )

    def create(self, validated_data):
        order_products = validated_data.pop('order_products')
        order = Order.objects.create(**validated_data)
        for item in order_products:
            product = item['product']
            OrderProduct.objects.create(
                order=order, product=product, price=product.price,
                quantity=item['quantity']
            )
        return order

    def to_representation(self, instance):
        representation = super(OrderSerializer, self).to_representation(instance)
        representation['order_products'] = OrderProductSerializer(
            instance=instance.products.all(), many=True, context=self.context).data
        return representation
