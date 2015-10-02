from django.shortcuts import get_obbject_or_404, redirect, render

from .models import Bookmark

#creating path from urls in marcador

def bookmark_list(request):
	bookmarks = Bookmark.public.all()
	context = {'bookmarks': bookmarks}
	return render(request, 'marcador/bookmark_list.html', context)
