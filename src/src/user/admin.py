# 在yourapp/admin.py中
from django.contrib import admin
from user.models import User  # 替换为你的自定义用户模型

admin.site.register(User)