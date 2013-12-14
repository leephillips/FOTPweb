import settings
def media(request):
    return {'MEDIA_URL': settings.MEDIA_URL}
def securemedia(request):
    return {'SECURE_MEDIA_URL': settings.SECURE_MEDIA_URL}

