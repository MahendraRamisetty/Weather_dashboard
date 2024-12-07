from django.db import models
from django.contrib.auth.models import User

class FavoriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Correctly named `user`
    city_name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name
