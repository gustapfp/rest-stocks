from django.contrib import admin
from .models import Stock, RealEstateInvestmentTrust

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