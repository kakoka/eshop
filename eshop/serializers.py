from django.contrib.auth.models import User, Group, Permission
from eshop.models.products import Product, Image, Category, Suppliers
from rest_framework import serializers

class ProductListSerializer(serializers.ModelSerializer):
    image = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product_photo'
    )

    class Meta:
        model = Product
        fields = ('id', 'image', 'name', 'description')

        #  = models.ForeignKey('Category')
        #  = models.ForeignKey('Images', on_delete=models.CASCADE)
        #  = models.CharField(max_length=50)
        # product_description = models.TextField(blank=True, default='')
        # product_buy_price = models.DecimalField(max_digits=9, decimal_places=2)
        # product_sell_price = models.DecimalField(max_digits=9, decimal_places=2)
        # product_quantity = models.PositiveSmallIntegerField(default=0)
        # last_update = models.DateTimeField(

        # class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     permissions = serializers.ManySlugRelatedField(
#         slug_field='codename',
#         queryset=Permission.objects.all()
#     )
#
#     class Meta:
#         model = Group
#         fields = ('url', 'name', 'permissions')
