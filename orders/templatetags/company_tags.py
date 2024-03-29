from django import template
from orders.models import *
from profiles.models import *

register = template.Library()
@register.inclusion_tag('company_list_tags.html', takes_context=True)
def show_company(context):
    request = context['request']
    company_list = Company.objects.all().exclude(user__pk=request.user.pk).order_by('-id')[:15]
    context_dict = {'company_list':company_list,}
    return context_dict

@register.inclusion_tag('favorite_tags.html', takes_context=True)
def all_favorite(context):
    request = context['request']
    all_favorites = Order.objects.all()
    context_dict = {'all_favorites':all_favorites,}
    return context_dict
    
@register.inclusion_tag('category_tags.html', takes_context=True)
def category_list(context):
    request = context['request']
    category_list = Category.objects.all()
    context_dict = {'category_list':category_list,}
    return context_dict

@register.inclusion_tag('block_info.html', takes_context=True)
def block_info(context):
    category = Category.objects.all()
    context = {'category':category}
    return context
    
@register.inclusion_tag('block_info_main.html', takes_context=True)
def block_info_main(context):
    block = BlockInfo.objects.first()
    context = {'block_info':block}
    return context
    
@register.filter
def add(a, b):
    return a+b