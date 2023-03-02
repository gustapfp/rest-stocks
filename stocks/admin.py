from django.contrib import admin
from .models import Stock, RealEstateInvestmentTrust, Broker

# Register your models here.



class ListStocks(admin.ModelAdmin):
    list_display = ('id', 'name', 'ticket')
    list_display_links = ("id","name")
    search_fields = ("name",)
    list_filter = ("sector", )

admin.site.register(Stock, ListStocks)

class ListREIT(admin.ModelAdmin):
    list_display = ('id', 'name', 'ticket')
    list_display_links = ("id","name")
    search_fields = ("name",)
    list_filter = ("sector", )

admin.site.register(RealEstateInvestmentTrust, ListREIT)

class ListBroker(admin.ModelAdmin):
    list_display = ('stock', 'reit', 'listed')
    list_display_links = ("stock" , "reit" )
    list_editable = ("listed",)

admin.site.register(Broker, ListBroker)