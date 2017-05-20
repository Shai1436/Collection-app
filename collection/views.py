from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
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

@login_required
def edit_profile(request, slug):
    if thing.user != request.user:
        raise Http404
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


def create_profile(request):
    form_class = ProfileForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            thing = form.save(commit=False)

            # set the additional details
            thing.user = request.user
            thing.slug = slugify(thing.name)

            # save the object
            thing.save()

            # redirect to our newly created thing
            return redirect('profile_detail', slug=thing.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'profiles/create_profile.html', {
        'form': form,
    })


