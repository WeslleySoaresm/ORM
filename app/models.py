from django.db import models

class EcommerceUser(models.Model):

    id_user = models.AutoField(primary_key=True, db_column='id_user')
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.IntegerField(
        choices=[(1, "Admin"), (2, "User"), (3, "Guest")], default=2
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = '"ecommerce"."USER"'
        verbose_name_plural = "Users"


class Category(models.Model):
    id_category = models.AutoField(primary_key=True, db_column='id_category')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'