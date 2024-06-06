from django.contrib.auth.models import User
from django.db import models


# Create your models here.


# Kategoriya uchun
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='category_photos/')

    def __str__(self):
        return self.name


# PC uchun
class GamingBuilds(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='PC Nomi')
    cpu = models.CharField(max_length=200, verbose_name='Protsessor')
    cooler = models.CharField(max_length=100, verbose_name='Sovutgich')
    ram = models.IntegerField()
    ssd = models.IntegerField(verbose_name='Qattiq holat diski')
    hdd = models.IntegerField(verbose_name='qattiq disk')
    gpu = models.CharField(max_length=150, verbose_name='Video Karta')
    psu = models.CharField(max_length=100, verbose_name='Quvvatlantirish Manbai')
    case = models.CharField(max_length=100, verbose_name='Keys')
    quantity = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='pc_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narx')

    def __str__(self):
        return self.name


# Noutbuk uchun
class LapTop(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Noutbuk Nomi')
    cpu = models.CharField(max_length=150, verbose_name='Protsessor')
    ram = models.IntegerField()
    ssd = models.IntegerField()
    gpu = models.CharField(max_length=150, verbose_name='Video Karta')
    display = models.CharField(max_length=255, verbose_name='Ekran')
    quantity = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='laptop_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narx')

    def __str__(self):
        return self.name


# Kreslo Uchun
class Armchair(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Kreslo Nomi')
    chairtype = models.CharField(max_length=150, verbose_name='Stul Turi')
    upholsterymaterial = models.CharField(max_length=150, verbose_name='Material')
    upholsterycolor = models.CharField(max_length=100, verbose_name='Rang')
    reclining = models.CharField(max_length=100, verbose_name='Yotgan holda')
    permissibleload = models.IntegerField(verbose_name='Ruxsat etilgan yuk')
    quantity = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='armchair_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narx')

    def __str__(self):
        return self.name


# Sichqoncha Uchun
class Mice(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Sichqoncha Nomi')
    sensortype = models.CharField(max_length=150, verbose_name='Sensor turi')
    maximumdpicpiresolution = models.IntegerField(verbose_name='Maksimal DPI/CPI ruxsati')
    numberofbuttons = models.IntegerField(verbose_name='Tugmalar soni')
    pullingrate = models.CharField(max_length=100, verbose_name='Saylov darajasi')
    operatingmode = models.CharField(max_length=50, verbose_name='Ishlash rejimi')
    quantity = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='mice_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narx')

    def __str__(self):
        return self.name


# Klaviatura uchun
class Keyboard(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Klaviatura Nomi')
    keyboardtype = models.CharField(max_length=50, verbose_name='Klaviatura turi')
    switchtype = models.CharField(max_length=50, verbose_name='Kalit turi')
    interface = models.CharField(max_length=30, verbose_name='Interfeys')
    backlight = models.CharField(max_length=30, verbose_name='Orqa yorug\'lik')
    numberofkeys = models.IntegerField(verbose_name='Tugmalar soni')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Naxr')
    photo = models.ImageField(upload_to='keyboard_photos/', verbose_name='Rasm')

    def __str__(self):
        return self.name


# Monitorlar uchun
class Monitor(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Monitor Nomi')
    diagonal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ekran Diagonali')
    screentype = models.CharField(max_length=30, verbose_name='Ekran turi')
    matrixtype = models.CharField(max_length=50, verbose_name='Matritsa Turi')
    permission = models.CharField(max_length=100, verbose_name='Ruxsat')
    framerate = models.CharField(max_length=50, verbose_name='Kadr tezligi')
    interface = models.CharField(max_length=100, verbose_name='Interfeys')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narx')
    photo = models.ImageField(upload_to='monitor_photos/', verbose_name='Rasm')

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50, null=True, default='')
    last_name = models.CharField(max_length=50, null=True, default='')


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_activ = models.BooleanField(default=True)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    gaming = models.ForeignKey(GamingBuilds, on_delete=models.SET_NULL, null=True)
    laptop = models.ForeignKey(LapTop, on_delete=models.SET_NULL, null=True)
    armchair = models.ForeignKey(Armchair, on_delete=models.SET_NULL, null=True)
    mcie = models.ForeignKey(Mice, on_delete=models.SET_NULL, null=True)
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True)
    keyboard = models.ForeignKey(Keyboard, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
