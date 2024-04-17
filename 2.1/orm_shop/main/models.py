from django.db import models

GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('CVT', 'Вариатор'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)

DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(blank=True)
    phone_number = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=128)
    year = models.IntegerField(max_length=4)
    color = models.CharField(max_length=32)
    mileage = models.IntegerField(max_length=16)
    volume = models.DecimalField(max_digits=2, decimal_places=1)
    body_type = models.CharField(choices=BODY_TYPE_CHOICES, max_length=32)
    drive_unit = models.CharField(choices=DRIVE_UNIT_CHOICES, max_length=32)
    gearbox = models.CharField(choices=GEARBOX_CHOICES, max_length=32)
    fuel_type = models.CharField(choices=FUEL_TYPE_CHOICES, max_length=32)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return f'{self.model}'


class Sale(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sales')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='sales')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.created_at} {self.car} {self.client}'
