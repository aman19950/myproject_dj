from django.db import models

# Create your models here.


class Course_Category(models.Model):
    course_name = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    slug = models.CharField(max_length=50, null=False, unique=True)
    desc = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(auto_now=True)
    resource = models.FileField(upload_to='files/resource')
    image = models.ImageField(upload_to='static/image')

    def __str__(self):
        return self.course_name


class Course_Information(models.Model):
    title = models.CharField(max_length=100, null=True)
    course = models.ForeignKey(
        Course_Category, on_delete=models.CASCADE, null=True)
    course_cat_id = models.CharField(max_length=100, null=True)
    course_content = models.TextField(
        blank=True, max_length=10000, null=True, default="")

    s_no = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class testing(models.Model):
    tes_id = models.ForeignKey(Course_Information, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.tes_id.title
