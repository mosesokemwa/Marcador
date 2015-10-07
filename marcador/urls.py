from django.conf.urls import url

<<<<<<< HEAD

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
        name='marcador_bookmark_user'),
    url(r'^create/$', 'marcador.views.bookmark_create',
        name='marcador_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'marcador.views.bookmark_edit',
        name='marcador_bookmark_edit'),
=======
#view of all private bookmarks
#view of all public bookmarks
urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
        name='marcador_bookmark_user'),
>>>>>>> b13cbb0db4ca8e0d6810ffcb15b01665d68d4abc
    url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list'),
]
