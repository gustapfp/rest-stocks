from rest_framework import serializers
from stocks.models import Stock, RealEstateInvestmentTrust, Broker

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class REITSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateInvestmentTrust
        fields = '__all__'

class BrokerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Broker
        fields = '__all__'

class ListBrokerSerializer(serializers.ModelSerializer): 
    stock = serializers.ReadOnlyField(source='stock.ticket')
    reit = serializers.ReadOnlyField(source='reit.ticket')
    class Meta:
        model = Broker
        exclude = ['listed']
