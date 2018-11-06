from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from orders.views import *
from profiles.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from endless_pagination.views import AjaxListView
from orders.ajax import *
from django.contrib.auth.decorators import login_required


from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
admin.autodiscover()

info_dict = {
    'queryset': Order.objects.all(),
    'date_field': 'born',
}
sentense_dict = {
    'queryset': Sentence.objects.all(),
    'date_field': 'born',}

urlpatterns = [
    url(r'^page/(?P<slug>\w+)/$', PageView.as_view(), name='page_detail'),
    url(r'^contact/$', contactView, name='contact_form'),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^delete-file/$', delete_files, name='delete_files'),
    url(r'^deletefromfavorites/$', delfrfavorites, name='delfrfavorites'),
    url(r'^companydeleteitem/$', companydeleteitem, name='companydeleteitem'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^add2favorites/$', add2favorites, name='add2favorites'),
    url(r'^move2/$', move2, name='move2'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^order/add/$', OrderCreate.as_view()),
    url(r'^download$', getfiles, name='zip'),
    url(r'^downloads$', getfiles_sentence, name='zip'),
    url(r'^company/add/$', login_required(CompanyCreate.as_view()), name='company_add'),
    url(r'^company/edit/(?P<pk>\d+)/$', CompanyUpdate.as_view(), name='company_edit'),
    url(r'^company/delete/(?P<pk>\d+)/$', CompanyDelete.as_view(), name='company_delete'),
    url(r'^companies/$', CompanyList.as_view(), name='company_list'),
    url(r'^companies/(?P<pk>\d+)/$', CompanyView.as_view(), name='company_detail'),
    url(r'^notcompanies/(?P<pk>\d+)/$', NotCompanyView.as_view(), name='notcompany_detail'),
    url(r'^profile/$', ProfileListView.as_view(), name='profile_list'),
    url(r'^profile/edit/(?P<pk>\d+)$', ProfileUpdate.as_view(), name='profile_edit'),
    url(r'^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name='profile_detail'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^search/$', SearchList.as_view()),
    url(r'^search-city/$', SearchCityList.as_view()),
    url(r'^logout/$', logout_ajax, name='logout_ajax'),
    url(r'^robots.txt$', robots, name='robots'),
    url(r'^sitemap\.xml$', sitemap,  {'sitemaps': {'order': GenericSitemap(info_dict, priority=0.6), 'sentence':GenericSitemap(sentense_dict, priority=0.6)}}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^order/edit/(?P<pk>[-\w]+)/$', OrderUpdate.as_view(), name='order_edit'),
    url(r'^order/delete/(?P<pk>[-\w]+)/$', OrderDelete.as_view(), name='order_delete'),
    url(r'^orders/$', OrderList.as_view(), name='order-list'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<subcategory_pk>\d+)/(?P<subsubcategory_slug>[\w-]+)/o/(?P<slug>[\w-]+)/$', OrderView.as_view(), name='order_detail'),
    url(r'^sentence/add/$', SentenceCreate.as_view()),
    url(r'^sentence/edit/(?P<pk>\d+)/$', SentenceUpdate.as_view(), name='sentence_edit'),
    url(r'^sentence/delete/(?P<pk>\d+)/$', SentenceDelete.as_view(), name='sentence_delete'),
    url(r'^sentences/$', SentenceList.as_view(), name='sentence_list'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<subcategory_pk>\d+)/(?P<subsubcategory_slug>[\w-]+)/s/(?P<slug>[\w-]+)/$', SentenceView.as_view(), name='sentence_detail'),

    url(r'^(?P<slug>[\w-]+)/$', CategoryView.as_view(), name='categorydetail'),
    url(r'^(?P<slug>[\w-]+)/(?P<subcategory_slug>[\w-]+)/$', SubcategoryDetail.as_view(), name='subcategorydetail'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<subcategory_slug>[\w-]+)/(?P<slug>[\w-]+)/$', SubsubcategoryDetail.as_view(), name='subsubcategorydetail'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
