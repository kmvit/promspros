import json
from django.contrib.auth import logout
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Order, Sentence, OrderImage, SentenceImage, CompanyImage

def delete_files(request):
    if request.user.is_authenticated() and request.is_ajax() and request.POST:
        object_id = request.POST.get('id', None)
        object_model_name =  request.POST.get('type', None)
        object_model_name = object_model_name.title()
        
        if object_model_name == 'Order':
            b = get_object_or_404(OrderImage, id=object_id)
            b.delete()
            data = {'message': 'delete'.format(b)}
            return HttpResponse(json.dumps(data), content_type='application/json')
        elif object_model_name == 'Company':
            b = get_object_or_404(CompanyImage, id=object_id)
            b.delete()
            data = {'message': 'delete'.format(b)}
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            b = get_object_or_404(SentenceImage, id=object_id)
            b.delete()
            data = {'message': 'delete'.format(b)}
            return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return JsonResponse({'error': 'Only authenticated users'}, status=404)
        
def companydeleteitem(request):
    if request.user.is_authenticated() and request.is_ajax() and request.POST:
        object_id = request.POST.get('id', None)
        b = get_object_or_404(CompanyImage, id=object_id)
        b.delete()
        data = {'message': 'delete'.format(b)}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return JsonResponse({'error': 'Only authenticated users'}, status=404)
        


def add_todo(request):
    if request.is_ajax() and request.POST:
        data = {'message': "%s added" % request.POST.get('item')}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404


def delfrfavorites(request):
    if request.user.is_authenticated() and request.is_ajax() and request.POST:
        object_id = request.POST.get('id', None)
        object_model_name = request.POST.get('type', None)

        if object_id and object_model_name:
            object_id = object_id.title()
            object_model_name = object_model_name.title()
        else:
            return JsonResponse({'error': 'Object id or type not exist in request data'},
                                status=404)

        try:
            model = apps.get_model('orders', model_name=object_model_name)
        except LookupError:
            return JsonResponse({'error': 'Model "{0}" not exist'.format(object_model_name)},
                                status=404)

        try:
            obj = model.objects.get(id=object_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Object with id={0} not exist in database'.format(object_id)},
                                status=404)
        else:
            if object_model_name == 'Order':
                favors = request.user.userprofile.liked_order
            elif object_model_name == 'Sentence':
                favors = request.user.userprofile.liked_sentence
            elif object_model_name == 'Company':
                favors = request.user.userprofile.liked_company
            else:
                return JsonResponse({'error': 'Model "{0}" not exist'.format(object_model_name)},
                                    status=404)

            if obj in favors.all():
                favors.remove(obj)
                data = {'message': '{0} removed'.format(obj)}
            return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only authenticated users'}, status=404)
    


def add2favorites(request):
    if request.user.is_authenticated() and request.is_ajax() and request.POST:
        object_id = request.POST.get('id', None)
        object_model_name = request.POST.get('type', None)

        if object_id and object_model_name:
            object_id = object_id.title()
            object_model_name = object_model_name.title()
        else:
            return JsonResponse({'error': 'Object id or type not exist in request data'},
                                status=404)

        try:
            model = apps.get_model('orders', model_name=object_model_name)
        except LookupError:
            return JsonResponse({'error': 'Model "{0}" not exist'.format(object_model_name)},
                                status=404)

        try:
            obj = model.objects.get(id=object_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Object with id={0} not exist in database'.format(object_id)},
                                status=404)
        else:
            if object_model_name == 'Order':
                favors = request.user.userprofile.liked_order
            elif object_model_name == 'Sentence':
                favors = request.user.userprofile.liked_sentence
            elif object_model_name == 'Company':
                favors = request.user.userprofile.liked_company
            else:
                return JsonResponse({'error': 'Model "{0}" not exist'.format(object_model_name)},
                                    status=404)

            if obj in favors.all():
                favors.remove(obj)
                data = {'message': '{0} removed'.format(obj)}
            else:
                favors.add(obj)
                data = {'message': '{0} added'.format(obj)}
            return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only authenticated users'}, status=404)


def move2(request):
    if request.user.is_authenticated() and request.is_ajax() and request.POST:
        object_id = request.POST.get('id', None)
        object_model_name = request.POST.get('type', None)
        status = request.POST.get('status', '1')

        if object_id and object_model_name:
            object_id = object_id.title()
            object_model_name = object_model_name.title()
        else:
            return JsonResponse({'error': 'Object id or type not exist in request data'},
                                status=404)

        try:
            model = apps.get_model('orders', model_name=object_model_name)
        except LookupError:
            return JsonResponse({'error': 'Model "{0}" not exist'.format(object_model_name)},
                                status=404)
        else:
            if object_model_name not in ['Order', 'Sentence']:
                return JsonResponse({'error': 'Model "{0}" not exist'.format(object_model_name)},
                                    status=404)
        try:
            obj = model.objects.get(id=object_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Object with id={0} not exist in database'.format(object_id)},
                                status=404)
        else:
            obj.status = status
            obj.save()
            data = {'message': 'Status {0} changed to {1}'.format(obj, status)}
            return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Only authenticated users'}, status=404)


def logout_ajax(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect('/accounts/login/')