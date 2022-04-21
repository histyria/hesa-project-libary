from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#جدول الأقسام
class category(models.Model):
    category = models.CharField(max_length=200, verbose_name ="إسم القسم" , help_text="الرجاء كتابة التصنيفات التي سيتم إدراج الكتب تحتها ( إسلامي , تاريخي , مجلة علمية .... إلخ )")
    def __str__(self):
        return self.category
    def get_category_count(self):
        return Book.objects.filter(category=self).count()
class site_viwes(models.Model):
    views = models.CharField(max_length=200)



class site_viwes2(models.Model):
    views = models.CharField(max_length=200)



class Book(models.Model):
    title = models.CharField(max_length=200 ,verbose_name ="إسم الكتاب" )
    summary = models.CharField(max_length=1000, verbose_name ="نبذه مختصره عن الكتاب")
    author = models.CharField(max_length=1000, verbose_name ="إسم المؤلف")
    category = models.ForeignKey(category, on_delete=models.CASCADE  ,verbose_name ="إسم القسم")
    CHOICES = (
        ('EN', 'EN'),
        ('عربي', 'عربي'),

    )
    language = models.CharField(max_length=100, choices=CHOICES, default='EN' ,verbose_name ="لغة الكتاب ")
    pic_book=models.ImageField(blank=True, null=True, upload_to='book_image')
    pdf_File = models.FileField(blank=True, null=True, upload_to='book_pdf')
    created_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
class Reviews(models.Model):
    review=models.CharField(max_length=100,default="none")
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    CHOICES = (
        ('0', '0'),
        ('.5', '.5'),
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    )

    rating=models.CharField(max_length=3, choices=CHOICES, default='2')

class scoole_appoitment(models.Model):
    school_name = models.CharField(max_length=30 , verbose_name ="إسم المدرسة" ,help_text="  الرجاء تحديد إسم المدرسة مع المرحلة الدراسية")
    staff_name = models.CharField(max_length=30 , verbose_name ="إسم المشرفه" ,help_text=" إسم المشرفة المسؤولة عن طلب الزيارة ")
    student_count = models.IntegerField( verbose_name ="عدد الطالبات" ,help_text=" عدد الطالبات المتوقع حضورهم ")
    appoitment_dt = models.DateField(null=True ,help_text=" تاريخ الزياره ")
    created_dt = models.DateTimeField(auto_now_add=True)


class project_team(models.Model):
    name = models.CharField(max_length=30 , verbose_name ="الإسم" )
    school_level = models.CharField(max_length=30 , verbose_name ="المرحلة الدراسية" )
    information_me = models.CharField(max_length=30 , verbose_name =" نبذة شخصية" )
    def __str__(self):
        return self.name
