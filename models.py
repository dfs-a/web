from django.db import models

# Create your models here.

class Blog(models.Model):
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.IntegerField(default=0,verbose_name='密码')
    post_box = models.EmailField(max_length=30,verbose_name='邮箱')
    phone_number = models.CharField(max_length=11,unique='True',verbose_name='电话号码')

    class Meta:
        db_table = 'mydfs'
        verbose_name = '个人博客'
        verbose_name_plural = verbose_name
        # ordering = ['id']

    def __str__(self):
        return 'id=%s,USER=%s,password=%s,post_box=%s,phone_number=%s' %(self.id,self.username,self.password,self.post_box,self.phone_number)

