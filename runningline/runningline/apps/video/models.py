from django.db import models


class RequestLog(models.Model):
    text = models.TextField('текст бегущей строки')
    date = models.DateTimeField('дата запроса')

    def __str__(self):
        return f"{self.date}: {self.text}"

    def __repr__(self):
        return f"RequestLog({self.date}, {self.text})"
