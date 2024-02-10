from django.db import models
from utils import NULLABLE


class Course(models.Model):
    """
    Модель для создания курса
    """
    name_course = models.CharField(max_length=50, verbose_name='название курса')
    image = models.ImageField(upload_to='media/', verbose_name='картинка курса', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='описание курса')

    def __str__(self):
        return f'{self.name_course}'

    class Meta:
        verbose_name = 'курс'


class Lesson(models.Model):
    """
    Модель для создания урока
    """
    name_lesson = models.CharField(max_length=50, verbose_name='название урока')
    image = models.ImageField(upload_to='media/', verbose_name='картинка урока')
    description = models.TextField(verbose_name='описание урока')
    link = models.CharField(max_length=50, verbose_name='ссылка на видео')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return f'{self.name_lesson}'

    class Meta:
        verbose_name = 'урок'