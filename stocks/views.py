from rest_framework import viewsets, generics
from stocks.models import Stock, RealEstateInvestmentTrust, Broker
from stocks.serializer import StockSerializer, REITSerializer, BrokerSerializer, ListBrokerSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StocksViewSet(viewsets.ModelViewSet):
    """
    Show all stocks
    """
   
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class REITViewSet(viewsets.ModelViewSet):
    """
    Show all Real Estate Invement Trust
    """

    queryset = RealEstateInvestmentTrust.objects.all()
    serializer_class = REITSerializer

class BrokerViewSet(viewsets.ModelViewSet):
    """
    Show all brokers
    """

    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer

class ListBroker(generics.ListAPIView):
    """ 
    List all elements
    """

    def get_queryset(self):
        queryset = Broker.objects.filter(stock_id = self.kwargs['pk'])
        return queryset

    serializer_class = ListBrokerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]