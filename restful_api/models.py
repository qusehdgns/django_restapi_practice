from django.db import models

class User(models.Model):
    # 사용자 id (pk)
    _id = models.CharField(max_length=50, primary_key=True)

    password = models.CharField(max_length=50)

    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'