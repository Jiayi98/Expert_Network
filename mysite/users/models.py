from django.db import models
from django.conf import settings
# from django.contrib.auth.models import AbstractUser
# from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    class Meta:
        permissions = (
            ("view_details", "Can see details of experts' information"),
            ("add_expert_info", "Can add a new expert"),
            ("add_expert_comment", "Can add new expert comment"),
            ("add_expert_exp", "Can add new experience of a specified expert"),

            ("del_expert_info", "Can remove an existing expert"),
            ("del_expert_comment", "Can remove an existing expert comment"),
            ("del_expert_exp", "Can remove existing experience of a specified expert"),

            ("mod_expert_info", "Can modify an existing expert"),
            ("mod_expert_comment", "Can modify an existing expert comment"),
            ("mod_expert_exp", "Can modify existing experience of a specified expert"),
        )

    def __str__(self):
        return self.user.username
# # Create your models here.
#
# #每个model默认都有三个permission，即 add model, change model 和 delete model
# class Permission(models.Model):
#     class Meta:
#         #权限信息，这里定义的权限的名字，后面是描述信息，描述信息是在django admin中显示权限用的
#         permissions = (
#             ('views_slg_users_tem', '查看玩家管理'),
#         )


