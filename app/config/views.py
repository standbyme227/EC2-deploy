import mimetypes
import os

from django.http import FileResponse
from django.shortcuts import render

from config import settings


def serve_media(request, path):
    media_path = os.path.join(settings.MEDIA_ROOT, path)
    content_type = mimetypes.guess_type(path)
    return FileResponse(
        open(media_path, 'rb'),
        content_type=content_type
    )






    # def index(request):
    #     return render(request, 'index.html')
    #
    # def song_edit(request, song_pk):
    #     song = get_object_or_404(Song, pk=song_pk)
    #     if request.method == 'POST':
    #         form = SongForm(request.POST, request.FILES, instance=song)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('song:song-list')
    #     else:
    #         form = SongForm(instance=song)
    #     context = {
    #         'song_form': form,
    #     }
    #     return render(request, 'song/song_edit.html', context)