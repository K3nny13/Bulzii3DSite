from django.shortcuts import render

# Create your views here.
def artwork_list(request):
    content = {"section": "artwork"}
    return render(request, 'artwork/artwork.html', content)