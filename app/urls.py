from django.conf.urls import url
from . import views

urlpatterns = [url(r'^index$', views.index, name='index'), 
	url(r'^form$', views.form, name='form'),
#    ('', (r'^static/*$', 'django.views.static.serve', {'document_root': order_online.settings.STATICFILES_DIRS, 'show_indexes': True})),
]

#urlpatterns = patterns('', (r'^static/*$', 'django.views.static.serve', {'document_root': order_online.settings.STATICFILES_DIRS, 'show_indexes': True}),
# )
