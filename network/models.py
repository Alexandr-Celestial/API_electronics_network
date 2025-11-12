from django.db import models
from django.db.models import CASCADE


class NetworkLink(models.Model):
    """Модель Звено сети"""

    LEVELS = (
        (0, "завод"),
        (1, "розничная сеть"),
        (2, "индивидуальный предприниматель"),
    )

    name = models.CharField(max_length=250, verbose_name="название", null=True, blank=True)
    email = models.EmailField(unique=True, null=False, verbose_name="email", help_text="Введите адрес эл. почты")
    country = models.CharField(max_length=100, verbose_name="страна", null=True, blank=True)
    street = models.CharField(max_length=100, verbose_name="улица", null=True, blank=True)
    house_number = models.CharField(max_length=100, verbose_name="номер дома", null=True, blank=True)

    arrears = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="задолженность", null=True, blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVELS, verbose_name="уровень", editable=False)
    supplier = models.ForeignKey("self", verbose_name="поставщик", null=True, blank=True, on_delete=CASCADE,
                                 related_name="clients", help_text="поставщик узла сети")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="время создания")

    def __str__(self):
        return f"{self.name} уровень {self.level}"

    class Meta:
        verbose_name = "узел сети"
        verbose_name_plural = "узлы сети"

    @property
    def hierarchy_level(self):
        """Определение уровня иерархии"""
        if self.supplier is None:
            return 0
        return self.supplier.hierarchy_level + 1


class Product(models.Model):
    """Модель Продукта"""

    name = models.CharField(max_length=250, verbose_name="название", null=True, blank=True)
    model = models.CharField(max_length=250, verbose_name="модель", null=True, blank=True)
    release_date = models.DateField(verbose_name="дата выхода продукта на рынок")
    supplier = models.ForeignKey(NetworkLink, verbose_name="узел сети", related_name="products", on_delete=CASCADE)

    def __str__(self):
        return f"{self.name} {self.model}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

