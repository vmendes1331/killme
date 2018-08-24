from __future__ import unicode_literals

from django.db import models

import uuid

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission

class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'


class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True


class Jogada(models.Model):

    LETRA = (('A'),
            ('B'),
            ('C'))

    letra = models.CharField(Choice=LETRA)
    palavra = models.CharField(max_leght=30)
    usuario = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='usuario', verbose_name='UUIDUser')

    class Meta:
        verbose_name = 'Jogada'
        verbose_name_plural = 'Jogadas'