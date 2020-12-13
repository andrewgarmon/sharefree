from django.contrib import admin
from .models import Portfolio, Stock, User, Share
# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'value')

class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'price')

class ShareAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'stock', 'shares')

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Share, ShareAdmin)