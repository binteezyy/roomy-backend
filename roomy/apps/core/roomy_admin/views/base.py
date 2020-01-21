from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse  # get_object_or_404

from apps.core.roomy_admin.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.core.roomy_core.models import *

context = {
    "title": "Roomy",
}


def index(request):
    next = request.GET.get('next')

    if request.user.is_authenticated:
        return render(request, "components/billing.html")
    else:
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return HttpResponseRedirect(reverse('home'))

        context = {
            'form': form,
            'title': 'Login',
        }
        return render(request, 'components/admin_login/login.html', context)


def admin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('admin-index'))


def demo(request, place):
    if place == "luneta":
        context['place'] = "luneta.jpg"
    elif place == "vigan":
        context['place'] = "vigan.jpg"
    elif place == "siargao":
        context['place'] = "siargao.jpg"
    else:
        context['place'] = "alma.jpg"
    return render(request, "demo.html", context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def property_upload(request, pk):

    property_object = Property.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'property': property_object,
        }
        return render(request, "components/upload_template/property-upload.html", context)

    elif request.method == 'POST' and request.FILES['myfile'] and request.POST.get('filetitle'):
        upload_image = ImageFile(title=request.POST.get(
            'filetitle'), img_path=request.FILES['myfile'])
        upload_image.save()

        property_object.property_image.add(upload_image)
        return HttpResponse("ok")
    else:
        return HttpResponse("not ok")

@login_required
@user_passes_test(lambda u: u.is_staff)
def room_upload2d(request, pk):

    room_object = Room.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'room': room_object,
            '2d': True,
        }
        return render(request, "components/upload_template/room-upload.html", context)

    elif request.method == 'POST' and request.FILES['myfile'] and request.POST.get('filetitle'):
        upload_image = ImageFile(title=request.POST.get(
            'filetitle'), img_path=request.FILES['myfile'])
        upload_image.save()

        room_object.image_2d.add(upload_image)
        return HttpResponse("ok")
    else:
        return HttpResponse("not ok")

@login_required
@user_passes_test(lambda u: u.is_staff)
def room_upload3d(request, pk):

    room_object = Room.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'room': room_object,
            '2d': False,
        }
        return render(request, "components/upload_template/room-upload.html", context)

    elif request.method == 'POST' and request.FILES['myfile'] and request.POST.get('filetitle'):
        upload_image = ImageFile(title=request.POST.get(
            'filetitle'), img_path=request.FILES['myfile'])
        upload_image.save()

        room_object.image_3d.add(upload_image)
        return HttpResponse("ok")
    else:
        return HttpResponse("not ok")
