from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .forms import EmailEntryForm, EmailEntryUpdateForm
from .models import EmailEntry

# Create your views here.

@staff_member_required(login_url='/login')
def email_entry_get_view(request, id=None, *args, **kwargs):
    # get a single item stored in the database
    # obj = EmailEntry.objects.get(id=id)
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404


    return render(request, "emails/detail.html", {"object":obj, "email": "abc@gmail.com"})


def email_entry_create_view(request, *args, **kwargs):
    context = {}
    add = False
    if request.user.is_authenticated:
        context['some_cool_stuff'] = "Whatever"
    print(request.user.email, request.user.is_authenticated)

    form = EmailEntryForm(request.POST or None)
    # print(form)
    context['form'] = form
    if form.is_valid():
        '''
        obj = form.save(commit=False)
        obj.name = "Justin"
        obj.save()
        new_id = obj.id
        '''
        print('hola')
        form.save()
        form = EmailEntryForm()
        context['added'] = True
        context['form'] = form
        print(context)
    return render(request, "home.html", context)




@staff_member_required(login_url='/login')
def email_entry_update_view(request, id=None, *args, **kwargs):
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404

    form = EmailEntryUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        updated_obj = form.save()
        return redirect(f"/email/{updated_obj.id}")
    return render(request, "emails/update.html", {'object': obj, 'form': form})



@staff_member_required(login_url='/login')
def email_entry_destroy_view(request, id=None, *args, **kwargs):

    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404

    if request.method == "POST":
        obj.delete()
        return redirect("/")

    return render(request, "emails/destroy.html", {"object":obj})



@staff_member_required(login_url='/login')
def email_entry_list_view(request, id=None, *args, **kwargs):
    qs = EmailEntry.objects.all() # .filter(email__icontains='abc')
    return render(request, "emails/list.html", {"object_list": qs})