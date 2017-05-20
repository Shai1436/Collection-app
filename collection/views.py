
from django.shortcuts import render

from collection.models import Profile

# the rewritten view!
def index(request):
    profiles = Profile.objects.all()

    return render(request, 'index.html', {
        'things': profiles,
    })

def profile_detail(request, slug):
    # grab the object...
    profile = Profile.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'profiles/profile_detail.html', {
        'thing': profile,
    })
