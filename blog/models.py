from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

# Create your models here.

class Post(models.Model):
    post_name = models.CharField(max_length=100, help_text="Enter the post name")
    post_message = models.TextField(max_length=3000, help_text="Enter the post details")
    post_author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    post_img = models.FileField()
    post_date = models.DateField(null=True, blank=True)
    post_highlight = models.TextField(null=True,  max_length=400,
                                      help_text="Highlight of your post e.g Trump, we have to stop rocket man"
                                      )

    def __str__(self):
        return self.post_name

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-post_date']


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    author_img = models.FileField()
    author_description = models.TextField(max_length=200, default="I am an author that live in Nigeria.")

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

    """
    To get the particular instance of an author
    """

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
