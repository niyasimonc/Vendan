# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


def get_user_image_path(instance, filename):
    """
    Function to return the image path for user images.

    Input Params:
        instance (obj): instance object
        filename (str): Original file name of the file
    Output Params:
        path (str): path name for the file
    """
    name = 'profilepic/%s/%s/%s' % (
        instance.type,
        instance.user.first_name, filename)
    return name


class CustomUser(models.Model):
    """
    Root User model.

    Atribs:
        user (obj): Django user model.
        type (int): field define the type of the user
        access_token (char): Hex value representing the token of the
            user.
        image (img): user image.
        address(char): address of the user.
        active_devices (int): no of active devices of user.
        blocked(bool): field which shows the active status of user.
        phone (char): phone number of the user
    """

    user = models.OneToOneField(User)
    address = models.CharField(
        default='', max_length=2000, blank=True)
    phone = models.CharField(
        default='', max_length=200, blank=True)
    image = models.ImageField(
        upload_to=get_user_image_path,
        null=True, default=None, blank=True)
    blocked = models.BooleanField(default=False)

    @property
    def name(self):
        """Get user name."""
        return self.user.username

    @property
    def image_url(self):
        """Get file url name."""
        try:
            return self.image.url
        except:
            None

    def __unicode__(self):
        """Object name in django admin."""
        return '%s : %s' % (self.name, self.id)
