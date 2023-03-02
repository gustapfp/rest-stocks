from rest_framework import serializers
from stocks.models import Stock, RealEstateInvestmentTrust

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name', 'ticket', 'sector']

class REITSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateInvestmentTrust
        fields = '__all__'