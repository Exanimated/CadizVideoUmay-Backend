from rest_framework import serializers

from .models import Property, Reservation

from useraccount.serializers import UserDetailSerializer



class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            'id',
            'tittle',    
            'price_per_night',
            'image_url'
            
        )

class PropertiesDetailsSerializer(serializers.ModelSerializer):
    landlord = UserDetailSerializer(read_only=True, many=False)

    class Meta:
        model = Property
        fields = (
            'id',
            'tittle',
            'description',
            'price_per_night',
            'image_url',
            'bedrooms',
            'bathrooms',
            'guests',
            'landlord'
           
            
        )

class ReservationsListSerializer(serializers.ModelSerializer):
    property = PropertiesListSerializer(read_only=True, many=False)

    class Meta:
        model = Reservation
        fields = (
            'id',
            'start_date',
            'property',
            'end_date',
            'number_of_nights',
            'total_price',
        )