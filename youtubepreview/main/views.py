from pytube import YouTube
from django.shortcuts import render
from .models import Video

# Create your views here.

def index(request):
	user_link = request.POST.get('link')

	if user_link:
		yt = YouTube('https://youtu.be/GZPpvXcdtoQ')
		print(yt.title)
		print(yt.thumbnail_url)
		video_not = yt.streams.get_lowest_resolution.download()
		video = Video.objects.create(title=yt.title, video=video_not)
		context = {
			'video':video
		}
		return render(request, 'index.html', context)

	else:
		print('#'*10)
	return render(request, 'index.html',)

	# request.POST.get('link')\










# yt = YouTube('https://youtu.be/s94t0DVh4mo')
# print(yt.title)
# stream = yt.streams.first()
# stream.download()

