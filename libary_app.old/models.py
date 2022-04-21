from django.db import models

# Create your models here.
#جدول التصنيفات
class category(models.Model):
    category = models.CharField(max_length=200, help_text="Enter a book category (Historical, Islamic, cultural, scientific...")
    def __str__(self):
        return self.category


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=1000, help_text="Enter a brief description of the book")
    author = models.CharField(max_length=1000, help_text="Enter a brief description of the book")
    category = models.ForeignKey(category, on_delete=models.CASCADE ,help_text="Select a category for this book")
    
    CHOICES = (
        ('EN', 'EN'),
        ('عربي', 'عربي'),
        
    )
    language = models.CharField(max_length=100, choices=CHOICES, default='EN')
    pic_book=models.ImageField(blank=True, null=True, upload_to='book_image')
    pdf_File = models.FileField(upload_to='pdf')
    add_date = models.DateField(auto_now=True)

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
