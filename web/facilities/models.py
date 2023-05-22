from django.db import models
from accounts.models import *

# class UserInput(models.Model):
#     st_x = models.FloatField()
#     st_y = models.FloatField()
#     radius = models.FloatField()
#     checkbox = models.BooleanField(default=False)

class likes(models.Model):
    name = models.CharField(max_length=100)
    liked_users = models.ManyToManyField(User)
    like_num = models.IntegerField(null=True, default=0)

    # def toggle_like(self, user):
    #     if user in self.liked_users.all():
    #         self.liked_users.remove(user)
    #         return False
    #     else:
    #         self.liked_users.add(user)
    #         return True
        
    @property
    def like_count(self):
        return self.liked_users.count()