from django.db import models
from django.contrib.auth import get_user_model


class Lista(models.Model):

    STATUS = (
        ('Comprar', 'Comprar'),
        ('Comprado', 'Comprado'),
    )

    produto = models.CharField(max_length=50)
    quantidade = models.BigIntegerField(blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    done = models.CharField(
        max_length=10,
        choices=STATUS,
    )
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    class Meta:
        db_table = 'lista'

    def __str__(self):
        return self.produto

    def get_data_criacao(self):
        return self.created_at.strftime('%d/%m')