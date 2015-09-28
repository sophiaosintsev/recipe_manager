from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

from .forms import UserForm


def register(request):

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()
            return HttpResponseRedirect(reverse('recipes'))

    else:
        form = UserForm()

    return render(
        request,
        'register.html',
        context={
            'form': form,
        }
    )

@csrf_protect
def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('recipes'))
            else:
                return HttpResponse('Your account is disabled')
        else:
            return HttpResponse('Invalid login details')

    else:
        return render_to_response('registration/login.html', context)


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('recipes'))

# def reset_confirm(request, uidb64=None, token=None):
#     # Wrap the built-in reset confirmation view and pass to it all the captured parameters like uidb64, token
#     # and template name, url to redirect after password reset is confirmed.
#     return password_reset_confirm(request, template_name='password_reset_confirm.html',
#         uidb64=uidb64, token=token, post_reset_redirect=reverse('password_reset_complete'))