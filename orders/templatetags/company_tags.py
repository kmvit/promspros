from django import template
from orders.models import *
from profiles.models import *

register = template.Library()
@register.inclusion_tag('company_list_tags.html', takes_context=True)
def show_company(context):
    request = context['request']
    company_list = Company.objects.all().exclude(user__pk=request.user.pk)
    context_dict = {'company_list':company_list,}
    return context_dict

@register.inclusion_tag('favorite_tags.html', takes_context=True)
def all_favorite(context):
    request = context['request']
    all_favorites = Order.objects.all()
    context_dict = {'all_favorites':all_favorites,}
    return context_dict