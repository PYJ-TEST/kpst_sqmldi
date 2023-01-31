from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=45)
    user_password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_job_users'