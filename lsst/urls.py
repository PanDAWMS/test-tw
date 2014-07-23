from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

#import lsst.settings
from django.conf import settings

#from lsst import views as lsstmon_views
#import lsst.views as lsstmon_views
#import core.pandajob.views_support as core_lsstmon_support_views
#import core.pandajob.views as core_lsstmon_views

urlpatterns = patterns('',
 #   url(r'^$', lsstmon_views.mainPage, name='mainPage'),
    url(r'^', include('core.lsst.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#urlpatterns += common_patterns
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
