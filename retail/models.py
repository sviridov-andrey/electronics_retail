from django.db import models


class BaseRetail(models.Model):
    name = models.CharField(max_length=350, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house_number = models.CharField(max_length=50, verbose_name='номер дома')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='задолженность')
    tame_created = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    class Meta:
        abstract = True


class Factory(BaseRetail):
    """завод"""

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class Network(BaseRetail):
    """розничная сеть"""

    supplier = models.ForeignKey(Factory, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'


class Entrepreneur(BaseRetail):
    """индивидуальный предприниматель"""

    supplier = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'индивидуальный предприниматель'
        verbose_name_plural = 'индивидуальные предприниматели'


class Product(models.Model):
    """продукт"""

    prod_name = models.CharField(max_length=100)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True, blank=True)
    network = models.ForeignKey(Network, on_delete=models.CASCADE, null=True, blank=True)
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f' {self.prod_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
