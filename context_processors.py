import settings
def media(request):
    return {'MEDIA_URL': settings.MEDIA_URL}
