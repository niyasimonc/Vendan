# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import CustomUser


def get_order_image_path(instance, filename):
    name = 'order/%s' % (
        filename)
    return name


class Order(models.Model):
    user = models.ForeignKey(CustomUser, default=None, blank=True, null=True)
    img = models.ImageField(
        upload_to=get_order_image_path,
        null=True, default=None, blank=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.address
