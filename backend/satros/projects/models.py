from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ['-name']
        indexes = [
            models.Index(fields=['-name']),
        ]

    def __str__(self):
        return self.name
    


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Project.Status.COMPELETED)




class Project(models.Model):


    class Status(models.TextChoices):
        NOTCOMPELETED = 'NC', 'NotCompeleted'
        COMPELETED = 'C', 'Compeleted'


    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    main_image = models.ImageField(upload_to="projects/image/main_image")
    small_description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.NOTCOMPELETED)
    started = models.DateField()
    ended = models.DateField()

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]


    def __str__(self):
        return self.title
