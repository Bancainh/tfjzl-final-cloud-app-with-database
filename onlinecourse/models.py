from django.db import models
from django.conf import settings

# Giả định mô hình Course và Lesson đã có (nếu chưa có, hệ thống sẽ báo lỗi và ta sẽ xử lý sau)
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class Submission(models.Model):
    choices = models.ManyToManyField(Choice)
    score = models.IntegerField(default=0)

class Instructor(models.Model):
    user = models.CharField(max_length=100, null=True)

class Learner(models.Model):
    user = models.CharField(max_length=100, null=True)