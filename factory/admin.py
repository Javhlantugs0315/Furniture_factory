from django.contrib import admin
from .models import Workshop, Worker, Order, OrderStage

admin.site.register(Workshop)
admin.site.register(Worker)
admin.site.register(Order)
admin.site.register(OrderStage)
