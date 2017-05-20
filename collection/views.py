
from django.shortcuts import render, redirect

from collection.forms import ProfileForm

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


def edit_profile(request, slug):
    # grab the object
    thing = Profile.objects.get(slug=slug)
    # set the form we're using
    form_class = ProfileForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('profile_detail', slug=thing.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=thing)

    # and render the template
    return render(request, 'profiles/edit_profile.html', {
        'thing': thing,
        'form': form,
    })
