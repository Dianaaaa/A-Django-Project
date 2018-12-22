from django.db import models

# Create your models here.
class Artical(models.Model):
    title = models.CharField(max_length=100)  # CharField用于存储字符串，max_length设置最大长度
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add = True)   #自动增加时间
    content = models.TextField(blank=True, null=True)   #TextField用于长文本

    def __unicode__(self):  # 使用title字段来表示对象
        return self.title
    
    class Meta:
        ordering = ['-date_time']