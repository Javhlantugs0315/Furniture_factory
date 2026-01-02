from django.db import models


class Workshop(models.Model):
    name = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Worker(models.Model):
    full_name = models.CharField(max_length=100)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Order(models.Model):
    FURNITURE_TYPE_CHOICES = [
        ('корпусная', 'Корпусная мебель'),
        ('мягкая', 'Мягкая мебель'),
    ]

    customer = models.CharField(max_length=100)
    furniture_type = models.CharField(max_length=20, choices=FURNITURE_TYPE_CHOICES)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Заказ №{self.id} ({self.customer})"


class OrderStage(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50,
        choices=[
            ('ожидает', 'Ожидает'),
            ('в работе', 'В работе'),
            ('выполнено', 'Выполнено'),
        ]
    )

    def __str__(self):
        return f"{self.order} — {self.workshop}"
