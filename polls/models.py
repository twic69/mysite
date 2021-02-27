from django.db import models

# Обработка вопроса
class Question(models.Model):
    text = models.CharField(max_length=420)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.text

# Обработка варианта ответа на вопрос
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=420)
    voter = models.IntegerField(default=0)

    def __str__(self):
        return self.text