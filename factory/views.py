from django.shortcuts import render
from .models import Workshop, Order, OrderStage


def dashboard(request):
    workshops = Workshop.objects.all()
    orders = Order.objects.order_by('-created_at')
    stages = OrderStage.objects.all()

    return render(
        request,
        'factory/dashboard.html',
        {
            'workshops': workshops,
            'orders': orders,
            'stages': stages
        }
    )
