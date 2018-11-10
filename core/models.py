from django.db import models

class Author(models.Model):
    name = models.CharField('Nome do autor', max_length=100)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, max_length=100, on_delete=models.CASCADE)
    title = models.CharField('Título da publicação', max_length=150)
    text = models.TextField('Conteúdo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # data é atualizada sempre que o método save é chamado

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.title