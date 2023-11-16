from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class MainJob(models.Model):

    job = models.CharField(verbose_name="جایگاه",
                                  max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = "-position"
        verbose_name = "دسته بندی جایگاه"
        verbose_name_plural = "دسته بندی جایگاه ها"

    def __str__(self):
        return self.position
    


class Skill(models.Model):
    skill = models.CharField(verbose_name="مهارت")
    mastery_persent = models.IntegerField(verbose_name="درصد تسلط",
                                          validators=[MinValueValidator(0), MaxValueValidator(100)])
    

    class Meta:
        ordering = "skill"
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت ها"

    def __str__(self):
        return self.skill





class Employe(models.Model):

    class Position(models.TextChoices):
        SENIOR =  'SN', 'Senior'
        JUNIOR = 'JN', 'Junior'


    full_name = models.CharField(verbose_name="نام", max_length=200)
    job = models.ForeignKey( MainJob,
                                    on_delete=models.CASCADE,
                                    related_name="employe_position", verbose_name="شغل")
    position = models.CharField(max_length=2,
                                verbose_name="جایگاه", 
                                choices=Position.choices)

    image = models.ImageField(verbose_name="تصویر",
                               upload_to="aboutus/employees/image/")
    resume_summery = models.TextField(verbose_name="خلاصه ی رزومه")

    skills = models.ManyToManyField(Skill,
                                    verbose_name="مهارت ها", blank=True, null=True)
    
    
    


    class Meta:
        ordering = "full_name"
        verbose_name = "کارمند"
        verbose_name_plural = "کارمندان"



    
    def __str__(self):
        return self.full_name


