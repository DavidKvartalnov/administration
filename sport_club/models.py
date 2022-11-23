from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=16)
    age = models.IntegerField()
    person_sail = models.FloatField(default=.0)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=16)
    age = models.IntegerField()
    post = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class SectionKind(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=16)
    trainer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    customer = models.ManyToManyField(Customer)
    kind = models.ForeignKey(SectionKind, on_delete=models.SET_NULL, null=True)
    lessons_month_quantity = models.IntegerField()
    single_lesson_price = models.IntegerField()

    def __str__(self):
        return self.name

    def subscription(self, sale):
        return self.lessons_month_quantity * self.single_lesson_price * sale


class Box(models.Model):
    buyer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    purchase = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    activation_time = models.DateTimeField(auto_now=True)
