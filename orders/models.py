# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
import os
from tinymce.models import HTMLField
from django.core.validators import RegexValidator
from unidecode import unidecode

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'Название')
    slug = models.SlugField(unique=True, verbose_name=u'URL')
    keywords = models.TextField(default="Test")
    description = models.TextField()
    body = HTMLField(verbose_name=u'Содержание')
    class Meta:
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'

    def __unicode__(self):
        return  u'%s' % self.title
        
        
class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name=u'Категории')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = HTMLField(verbose_name='Описание', blank=True)
    icon = models.ImageField(upload_to='images/icons', blank=True, verbose_name='Иконки')
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')
    class Meta:
        verbose_name = u'Категории'
        verbose_name_plural = u'Категория'
        ordering = ('my_order',)
        
    def order_count(self):
        sentence_list = Sentence.objects.filter(category__parent__parent_slug = self.slug, status=1) 
        order_list = Order.objects.filter(category__parent__parent_slug = self.slug, status=1) 
        return sentence_list.count() + order_list.count()

    def __unicode__(self):
        return u'%s' % self.title


    def __unicode__(self):
        return u'%s' % self.title
        
class Subcategory(models.Model):
    title = models.CharField(max_length=300, verbose_name=u'Подкатегории')
    description = HTMLField(verbose_name='Описание', blank=True)
    icon = models.ImageField(upload_to='images/icons', blank=True, verbose_name='Иконки')
    parent = models.ForeignKey(Category, verbose_name=u'Родитель')
    class Meta:
        verbose_name = u'Подкатегории'
        verbose_name_plural = u'Подкатегория'
        ordering = ['title']
    
    def order_count(self):
        sentence_list = Sentence.objects.filter(category__parent_id = self.id, status=1) 
        order_list = Order.objects.filter(category__parent_id = self.id, status=1) 
        return sentence_list.count() + order_list.count()

    def __unicode__(self):
        return u'%s' % self.title
        
    
            

class Subsubcategory(models.Model):
    title = models.CharField(max_length=300, verbose_name=u'Название')
    slug = models.SlugField(unique=True, verbose_name='URL', max_length=300)
    description = HTMLField(verbose_name='Описание', blank=True)
    icon = models.ImageField(upload_to='images/icons', blank=True, verbose_name='Иконки')
    parent = models.ForeignKey(Subcategory, verbose_name=u'Родитель')
    class Meta:
        verbose_name = u'Подподкатегории'
        verbose_name_plural = u'Подподкатегория'
        ordering = ['title']
    
    def order_count(self):
        sentence_list = Sentence.objects.filter(category__slug = self.slug, status=1) 
        order_list = Order.objects.filter(category__slug = self.slug, status=1) 
        return sentence_list.count() + order_list.count()

    def __unicode__(self):
        return u'%s' % self.title

class Sentence(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'Название')
    slug = models.SlugField(unique=True, verbose_name='URL', max_length=300)
    category = models.ForeignKey(Subsubcategory, verbose_name='Категория', default=1)
    born = models.DateField(verbose_name="День создания", default=timezone.now)
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    email = models.EmailField(verbose_name=u'Почта')
    name = models.CharField(max_length='200', verbose_name=u'Имя представителя')
    phone = models.CharField(max_length='18', verbose_name=u'Телефон')
    city = models.CharField(max_length='100', verbose_name=u'Город')
    body = models.TextField(verbose_name=u'Описание проекта')
    price = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True, verbose_name=u'Стоимость')
    change = (
        ('1', 'активные'),
        ('2', 'неактивные'),
        ('3', 'черновики'),
    )
    status = models.CharField(max_length=50, choices=change, default='1', verbose_name=u'Статус')

    
    class Meta:
        ordering = ['-born']
        verbose_name = u'Предложение'
        verbose_name_plural = u'Предложения'

    def __unicode__(self):
        return u'%s' % self.title

    
    def get_next(self):
        next = Sentence.objects.filter(id__gt=self.id)
        if next:
            return next.first()
        return False

    def get_prev(self):
        prev = Sentence.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first()
        return False
        
    def get_absolute_url(self):
        return reverse('sentence_detail', kwargs={'category_slug': self.category.parent.parent.slug, 'subcategory_pk': self.category.parent.id, 'subsubcategory_slug': self.category.slug, 'slug': self.slug})
        
class SentenceImage(models.Model):
    file = models.FileField(upload_to='images/sentence',blank=True, null=True,verbose_name=u'Фотографии')
    sentence = models.ForeignKey(Sentence, verbose_name=u'Фото предложения')
    class Meta:
        verbose_name = u'Фото предложения'
        verbose_name_plural = u'Фото'

    def __unicode__(self):
        return  u'%s' % self.id  
        
    def css_class(self):
        file, extension = os.path.splitext(self.file.name)
        if extension == '.jpg':
            return 'jpg'
        if extension == '.png':
            return 'jpg'
        if extension == '.doc':
            return 'word'
        if extension == '.txt':
            return 'word'
        return 'other'
        
    def filename(self):
        return os.path.basename(self.file.name)


class Order(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'Название')
    slug = models.SlugField(unique=True, verbose_name='URL', max_length=300)
    category = models.ForeignKey(Subsubcategory, verbose_name='Категория', default=1)
    born = models.DateField(verbose_name="День создания", default=timezone.now)
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    email = models.EmailField(verbose_name=u'Почта')
    name = models.CharField(max_length='200', verbose_name='Имя представителя')
    phone = models.CharField(max_length='18', verbose_name=u'Телефон')
    city = models.CharField(max_length='100', verbose_name=u'Город')
    body = models.TextField(verbose_name=u'Описание проекта')
    change = (
        ('1', 'активные'),
        ('2', 'неактивные'),
        ('3', 'черновики'),)
    status = models.CharField(max_length=50, choices=change, default='1', verbose_name=u'Статус')

    class Meta:
        ordering = ['-born']
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

    def __unicode__(self):
        return u'%s' % self.title
        
    def get_next(self):
        next = Order.objects.filter(id__gt=self.id)
        if next:
            return next.first()
        return False

    def get_prev(self):
        prev = Order.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first()
        return False
        
    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'category_slug': self.category.parent.parent.slug, 'subcategory_pk': self.category.parent.id, 'subsubcategory_slug': self.category.slug, 'slug': self.slug})
    
    

class OrderImage(models.Model):
    file = models.FileField(upload_to='images/order',blank=True, null=True,verbose_name=u'Добавить файлы')
    order = models.ForeignKey(Order, verbose_name=u'Файлы заказа')
    class Meta:
        verbose_name = u'Фото заказа'
        verbose_name_plural = u'Фото'

    def __unicode__(self):
        return  u'%s' % self.id
    
    def filename(self):
        return os.path.basename(self.file.name)
    
    def css_class(self):
        file, extension = os.path.splitext(self.file.name)
        if extension == '.jpg':
            return 'jpg'
        if extension == '.png':
            return 'jpg'
        if extension == '.doc':
            return 'word'
        if extension == '.txt':
            return 'word'
        return 'other'
        
        
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(instance.id), ext)
    return os.path.join('uploads','avatar', filename)

class Company(models.Model):
    logo = models.ImageField(upload_to=get_file_path,blank=True, verbose_name='Лого')
    alphanumeric = RegexValidator(r'^[0-9]*$', u'Только цифры!')
    user = models.ForeignKey(User, verbose_name=u'Пользователь', default='1')
    info = models.TextField(max_length=1900, verbose_name=u'Информация о компании', blank=True)
    title = models.CharField(max_length=100, verbose_name=u'Название компании')
    url = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'Ссылка на сайт')
    city = models.CharField(max_length=140, verbose_name=u'Город')
    ur_adress = models.CharField(max_length=300, verbose_name=u'Юридиеский адрес')
    pochta_adress = models.CharField(max_length=300, verbose_name=u'Почтовый адрес')


    class Meta:
        verbose_name = u'Копания'
        verbose_name_plural = u'Компании'

    def __unicode__(self):
        return u'%s' % self.title
        
    

        
        
class CompanyImage(models.Model):
    file_up = models.ImageField(upload_to='images/company',blank=True, verbose_name=u'Фотографии')
    order = models.ForeignKey(Company, verbose_name=u'Фото компании')
    class Meta:
        verbose_name = u'Фото компании'
        verbose_name_plural = u'Фото'

    def __unicode__(self):
        return  u'%s' % self.id
        
    def filename(self):
        return os.path.basename(self.file_up.name)
    
    def css_class(self):
        file_up, extension = os.path.splitext(self.file_up.name)
        if extension == '.jpg':
            return 'jpg'
        if extension == '.png':
            return 'jpg'
        if extension == '.doc':
            return 'word'
        if extension == '.txt':
            return 'word'
        return 'other'
        
 
class City(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название населенного пункта')
    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'

    def __unicode__(self):
        return  u'%s' % self.title
        
        
class BlockInfo(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    body = HTMLField(verbose_name='Содержание')
    class Meta:
        verbose_name = 'Блок Информации'
    
    def __unicode__(self):
        return self.title
        
        
class BlockonPage(models.Model):
    title = models.CharField(max_length=300)
    block_one = HTMLField(blank=True)
    block_two = HTMLField(blank=True)
    block_three = HTMLField(blank=True)
    class Meta:
        verbose_name = 'Блок на странице'
        verbose_name_plural = u'Блоки на странице'
    
    def __unicode__(self):
        return self.title