from django.db import models

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fosterable = models.BooleanField(default=False)
    image_path = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.fosterable:
            self.price = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Dog(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    breed = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField()
    personality = models.TextField()
    up_to_date_on_vaccines = models.BooleanField(default=False)

    def __str__(self):
        return self.animal.name

class Cat(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    breed = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField()
    personality = models.TextField()
    up_to_date_on_vaccines = models.BooleanField(default=False)

    def __str__(self):
        return self.animal.name

class Lizard(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    temperature = models.IntegerField()

    def __str__(self):
        return self.animal.name

class Bird(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    wingspan = models.IntegerField()

    def __str__(self):
        return self.animal.name

class Fish(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    species = models.CharField(max_length=100)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    food = models.CharField(max_length=100)

    def __str__(self):
        return self.animal.name