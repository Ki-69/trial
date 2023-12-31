from django.db import models
from datetime import date
from django.contrib import admin
# Create your models here.
Vacancy_posts=[('principal','Principal'),('PGT (Physics)','PGT (Physics)'),('PGT (Chemistry)','PGT (Chemistry)'),('PGT (Maths)','PGT (Maths)'),
               ('PGT (Biology)','PGT (Biology)'),('PGT (Computer)','PGT (Computer)'),('PGT (Economics)','PGT (Economics)'), 
               ('PGT (Commerce)','PGT (Commerce)'),('PGT (English)','PGT (English)'),('PGT (Hindi)','PGT (Hindi)'),('TGT (Science)','TGT (Science)'),
               ('TGT (Maths)','TGT (Maths)'),('TGT (Sanskrit)','TGT (Sanskrit)'),('TGT (Social Science)','TGT (Social Science)'),
               ('TGT (English)','TGT (English)'),('TGT (Hindi)','TGT (Hindi)'),('PRT','PRT'),('SSA','SSA'),('Lab Attendant','Lab Attendant'),
               ('Sub Staff','Sub Staff'),('JR. Secratariat Assistant','JR. Secratariat Assistant')]
from django.db import models

class Class(models.Model):
    class_name=models.CharField(max_length=16)
    def __str__(self) :
        return f"{self.class_name}"
    class Meta:
        verbose_name = "Add Class in TC"
        verbose_name_plural = "Add Class in TC"
class principals_message(models.Model):
    message=models.TextField()
    image=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    def __str__(self):
        return "Principals Message"
    class Meta:
        verbose_name = "Add  Principals message"
        verbose_name_plural = "Add Principals message"
class Alumni(models.Model):
    name=models.CharField(max_length=64)
    description_of_acheivement=models.TextField(max_length=128)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Add Alumni"
        verbose_name_plural = "Add Alumni"
class News_letter(models.Model):
    title=models.CharField(max_length=32)
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    def __str__(self) :
        return f"{self.title}"
    class Meta:
        verbose_name = "Make News Letter Entry"
        verbose_name_plural = "Make News Letter Entry"
class TC(models.Model):
    serial_number=models.BigIntegerField(primary_key=True,unique=True)
    name=models.CharField(max_length=32,blank=False,null=False)
    parents_name=models.CharField(max_length=32,blank=False,null=False)
    date_of_birth=models.DateField(blank=False,null=False)
    Admission_number=models.BigIntegerField(blank=False,null=False)
    Class_left=models.ForeignKey(Class,related_name='TCs_issued_by_class',blank=False,null=False,on_delete=models.CASCADE)
    TC_no=models.BigIntegerField(unique=True,blank=False,null=False,)
    issue_date=models.DateField(blank=False,null=False,)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Add TC"
        verbose_name_plural = "Add TC"
class vmc_member(models.Model):
    name=models.CharField(max_length=128)
    post=models.TextField()
    address=models.CharField(max_length=128)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Add VMC member"
        verbose_name_plural = "Add VMC member"
class member_list(models.Model):
    name=models.CharField(max_length=32)
    designation=models.CharField(choices=Vacancy_posts,max_length=32)
    origin=models.CharField(choices=[("Local","Local"),("Indian","Indian")],null=False,blank=False,max_length=6)
    image=models.ImageField(upload_to='website/images/' ,blank=True ,null=True)
    def __str__(self):
        return f"{self.name},{self.designation}"
    class Meta:
        verbose_name = "Add Staff"
        verbose_name_plural = "Add Staff"
class Vacancy(models.Model):
    number=models.IntegerField()
    vacant_designation=models.CharField(choices=Vacancy_posts,max_length=32)
    def __str__(self):
        return f"{self.vacant_designation}"
    class Meta:
        verbose_name = "Add Vacancy"
        verbose_name_plural = "Add Vacancy"
class Notice(models.Model):
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    title=models.TextField(blank=False)
    description=models.TextField(blank=False)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Add Notice"
        verbose_name_plural = "Add Notice"
class News_and_Events(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True,blank=False,null=False)
    title=models.TextField(blank=False)
    description=models.TextField(blank=False)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Add Event Item"
        verbose_name_plural = "Add Event Item"
class Fee_structure(models.Model):
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    def __str__(self):
        return f"Fee structure for the year {date.today().year}"
    class Meta:
        verbose_name = "Add Fee Structure"
        verbose_name_plural = "Add Fee Structure"
class Holiday(models.Model):
    name=models.TextField(max_length=32,blank=False,null=False)
    start_date=models.DateField(blank=False,null=False)
    end_date=models.DateField(default=None)
    category=models.CharField(choices=
                              (('holiday','Holiday'),('summer_vacation','Summer Vacation'),('winter_vacation','Winter Vacation'),('autum_vacation','Autum Vacation')),
                              max_length=32)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Add Holiday"
        verbose_name_plural = "Add Holiday"
class Carousel_image(models.Model):
    image_1=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    image_2=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    image_3=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    image_4=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    class Meta:
        verbose_name = "Add Image to Caurosel"
        verbose_name_plural = "Add Image to Carousel"
class News_and_Events_GalleryAdmin(admin.ModelAdmin):
    exclude= ('id',)
class quote(models.Model):
    quote=models.TextField()
    last_updated=models.DateField()
    author=models.TextField()
class Images(models.Model):
    event=models.ForeignKey(News_and_Events,on_delete=models.CASCADE,related_name='images',blank=True,null=True)
    image=models.ImageField(upload_to='website/images/' ,blank=False ,null=False)
    def __str__(self):
        if self.event:
            return f"{self.event}"
        else:
            return f"{self.gallery}"
    class Meta:
        verbose_name = "Add Image for event"
        verbose_name_plural = "Add Image for event"
class Committies(models.Model):
    Committee_name=models.TextField(choices=(('Admissions','Admissions'),('Academic advisory','Academic_Advisory'),('Examination','Examination'),('Transpotation','Transpotation')))
    members=models.ManyToManyField(member_list,related_name='committees')
    class Meta:
        verbose_name = "Update Committee Member"
        verbose_name_plural = "Update Committee Member"
class Admissions(models.Model):
    grade=models.ManyToManyField(Class,related_name="vacancy_class",blank=False)
    vacancy=models.IntegerField(blank=False,null=False)
    file=models.FileField(upload_to='website/files',default=None)
    class Meta:
        verbose_name='Vacancy for Other Classes'
        verbose_name_plural = 'Vacancy for Other Classes'
    def __str__(self):
        return f"Vacancy for class {self.grade.get()}"
class class1(models.Model):
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    def __str__(self):
        return f"Fee structure for the year {date.today().year}"
    class Meta:
        verbose_name = "Add class 1 vacancy file"
        verbose_name_plural = "Add class 1 vacancy file"
class class11(models.Model):
    file=models.FileField(upload_to='website/files',blank=False,null=False)
    def __str__(self):
        return f"Fee structure for the year {date.today().year}"
    class Meta:
        verbose_name = "Add class 11 vacancy file"
        verbose_name_plural = "Add class 11 vacancy file"
class achievement(models.Model):
    description=models.TextField(blank=False,null=False)
    image=models.ImageField(upload_to='website/images')
    class Meta:
        verbose_name = "Add Achievement"
        verbose_name_plural = "Add Achievement"