from django.db import models
# 用户表
class userinfo(models.Model):
    user_name =models.CharField(max_length=32,primary_key=True)
    user_pwd=models.CharField(max_length=32)
    def __str__(self):
        return self.user_name
#上传文件表
class files(models.Model):
    files_id=models.AutoField(primary_key=True)
    files_name=models.FileField(upload_to='media')
    files_user=models.ForeignKey(userinfo,on_delete=models.CASCADE)


# Create your models here.
