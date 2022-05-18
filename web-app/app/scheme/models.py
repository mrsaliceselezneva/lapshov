from django.db import models


class Therm(models.Model):
    title = models.CharField('Термин', max_length=100)
    body = models.TextField('Определение')
    image = models.ImageField('Рисунок', null=True, upload_to='scheme/')
    mark = models.CharField('Обозначение', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Термин'
        verbose_name_plural = 'Термины'


class Connection(models.Model):
    title = models.CharField('Связь', max_length=100)
    body = models.TextField('Определение')
    image = models.ImageField('Рисунок', upload_to='scheme/connection')
    mark = models.CharField('Обозначение', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'


class XmlFile(models.Model):
    title = models.CharField('Имя файла', max_length=100)
    file = models.FileField('Файл', upload_to='scheme/xml')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xml файл'
        verbose_name_plural = 'Xml файлы'


class RelationshipsTerms(models.Model):
    title = models.CharField('Связь терминов', max_length=100)
    therm_id1 = models.IntegerField('id первого термина')
    therm_id2 = models.IntegerField('id второго термина')
    connection_id = models.IntegerField('id связи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Связь терминов'
        verbose_name_plural = 'Связи терминов'
