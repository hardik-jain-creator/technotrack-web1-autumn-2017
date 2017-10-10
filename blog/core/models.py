# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    company_name = models.CharField(max_length=255)


class Category(models.Model):

    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Question(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255, verbose_name=u'Тайтл')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='questions')
    is_deleted = models.BooleanField(default=False)
    qtype = models.SmallIntegerField(choices=((1, 'urgent'), (2, 'etc')))

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = '-id',
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'


class Answer(models.Model):

    question = models.ForeignKey(Question, related_name='answers')
    text = models.TextField(default='')

    def __unicode__(self):
        return u'{} ({})'.format(self.id, self.question.text)