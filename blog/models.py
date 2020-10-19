from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Post(models.Model):
    # PROTECT makes it so that if someone deletes a category, all the posts associated with the category remain
    # CASCADE will delete associated objects
    # options for default status of post when they're being written up
    # PostObjects model manager gets only posts from db that are in published status so frontend filtering not required

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (("draft", "Draft"), ("published", "Published"))

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=240)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=240, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    status = models.CharField(max_length=10, choices=options, default="published")
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ("-published",)  # return data in descending order by default

    def __str__(self):
        return self.title  # return title of post by default
