# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, UserManager
import datetime
from orders.models import Order, Sentence, Company
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save


class UserProfile(User):
    name = models.CharField(max_length='200', verbose_name='ФИО', default='ФИО')
    phone = models.CharField(max_length='12', verbose_name='Телефон', default='+7123456789')
    avatar = models.ImageField(upload_to='images/avatar',blank=True, verbose_name='Аватар')
    liked_order = models.ManyToManyField(Order, verbose_name='Избранные заказы', blank=True)
    liked_sentence = models.ManyToManyField(Sentence, verbose_name='Избранные предложения', blank=True)
    liked_company = models.ManyToManyField(Company, verbose_name='Избранные компании', blank=True)
    objects = UserManager()

    class Meta:
        verbose_name = u'Профиль'
        verbose_name_plural = u'Профили'

        
    def get_absolute_url(self):
        return "/profile/%i/" % self.id
    
    def create_custom_user(sender, instance, created, **kwargs):
        if created:
            values = {}
            for field in sender._meta.local_fields:
                values[field.attname] = getattr(instance, field.attname)
            user = UserProfile(**values)
            user.save()
    post_save.connect(create_custom_user, User)

    
