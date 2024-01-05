from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
            Returns the absolute URL for a specific post.

            The URL is constructed using the 'post-detail' view and the post's primary key (pk).

            Returns:
            str: The absolute URL for the post.
        """
        return reverse("post-detail", kwargs={"pk": self.pk})
        # return reverse('blog-home')
