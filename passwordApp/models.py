from django.db import models

class Password(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    pseudonym = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.url} {self.pseudonym} {self.password}"