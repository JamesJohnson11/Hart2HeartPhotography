from django.conf import settings
from django.db import models
from django.utils import timezone

'''
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=5000, default="Add Text Here...")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="images/")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    CATEGORY = (
        ('1', 'Nature'),
        ('2', 'Maternity'),
        ('3', 'Baby'),
        ('4', 'Engagement'),
    )

    status = models.CharField(
        max_length=1,
        choices=CATEGORY,
        blank=True,
        default='1',
    )

    class Meta:
        verbose_name_plural = "Galleries"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        '''