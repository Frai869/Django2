from django.contrib import admin

from main.models import Car, Sale, Client


admin.site.register(Car)
admin.site.register(Sale)
admin.site.register(Client)

# зарегистрируйте необходимые модели
