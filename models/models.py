from django.db import models
from django.contrib.auth.models import AbstractUser


ADMIN_QUESTION_STATUS = (
    ("draft", "draft"),
    ("inprogress", "inprogress"),
    ("published", "published")
)

USER_QUESTION_STATUS = (
    ("solved", "solved"),
    ("unsolved", "unsolved"),
    ("inprogress", "inprogress")
)

DIFFICULTY_LEVEL = (
    ("one", "one"), # easy
    ("two", "two"),
    ("three", "three"),
    ("four", "four"),
    ("five", "five"), # hard
)


class User(AbstractUser):
    """
    This model is added so that I can add more fields/attributes here
    if need be later on.
    I used UserAdmin to show it nicely in the admin panel. But new fields won't show up
    check stackoverflow.
    """
    pass


class Category(models.Model):
    """
    This will say if the quetion is of type python/sql/rust/whatever
    """
    category_name = models.CharField(max_length=50)
    category_description = models.TextField(default="")

    def __str__(self):
        return self.category_name


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, default="")
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=ADMIN_QUESTION_STATUS,
        default="draft"
    )
    difficulty_level = models.CharField(
        max_length=20,
        choices=DIFFICULTY_LEVEL,
        default="one"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str___(self):
        return self.title

class UserQuestion(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    question = models.ForeignKey(Question, models.SET_NULL, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=USER_QUESTION_STATUS,
        default="unsolved"
    )

    def __str__(self):
        return f"{self.user.username} - {self.question.title}"
