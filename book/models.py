from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='book_pictures/')
    video = models.FileField(upload_to='book_videos/')
    audio = models.FileField(upload_to='book_audios/')
    pdf = models.FileField(upload_to='book_pdfs/')
