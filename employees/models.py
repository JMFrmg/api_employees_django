from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    floor = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Employee(models.Model):
    hired = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField(default=30)
    city = models.CharField(max_length=200, default="paris")
    position = models.CharField(max_length=200, default="cadre")
    salary = models.SmallIntegerField(default=30000)
    current = models.BooleanField(default=True)
    department = models.ForeignKey(Department, related_name="employees", on_delete=models.RESTRICT)
    department_chief = models.ForeignKey("auth.User", related_name="employees", on_delete=models.CASCADE)

    def full_name(self):
        return '%s %s' % (self.first_name.capitalize(), self.last_name.capitalize())

    def __str__(self):
        return self.full_name()

    class Meta:
        ordering = ['hired']