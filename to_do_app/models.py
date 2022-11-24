from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

STATUS_CHOICES=(
    ('open','OPEN'),
    ('working','WORKING'),
    ('done','DONE'),
    ('overdue','OVERDUE'),
)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    dueDate= models.DateField(blank=True)
    tag = models.ManyToManyField(Tag)
    status = models.CharField(choices=STATUS_CHOICES, max_length=8, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def number_of_tags(self):
        return self.tag.all()

