from rest_framework import serializers
from .models import (
    User,
    Brand,
    ModelType,
    Year,
    Car,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'UserId',
            'Name',
            'Email',
            'Phone',
            'Cpf,'
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'BrandId',
            'Name',
        )


class ModelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelType
        fields = (
            'ModelId',
            'Name',
        )


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = (
            'YearId',
            'Name',
        )


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'CarId',
            'Name',
            'Brand',
            'Model',
            'Year',
            'Location',
            'Transmission',
            'Price',
            'DiscountPrice',
            'Mileage',
            'Color',
            'Seat',
            'Fuel',
            'CreatedDate',
            'User',
            'ImageFile,'
        )

