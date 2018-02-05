from django.db import models
from django.template.defaultfilters import mark_safe

def user_directory_path(instance,filename):
	return 'documents/post_no_{0}/{1}'.format(instance.pk,filename)

class M_Post(models.Model):
	post_no = models.AutoField(primary_key=True)
	post_contents = models.TextField()
	post_interests = models.PositiveIntegerField()

class M_File(models.Model):
	file_no = models.AutoField(primary_key=True)
	file_title = models.TextField(default='')
	file_path = models.FileField(upload_to=user_directory_path,null=True,max_length=500,blank=True)
	def save(self, *args, **kwargs):
		if self.pk is None:
			file_path = self.file_path
			self.file_path = None
			super().save(*args, **kwargs)
			self.file_path = file_path
		super().save(*args, **kwargs)

class M_Post_File(models.Model):
	post = models.ForeignKey(M_Post,on_delete=models.CASCADE)
	file = models.ForeignKey(M_File,on_delete=models.CASCADE,null=True)