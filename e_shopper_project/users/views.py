
from django.shortcuts import render
from django.http import HttpResponse
from .form import CustomerUserForm

def register_view(request):
    if request.method == 'POST':
        form = CustomerUserForm(request.POST , request.FILES)
        if form.is_valid():
            user= form.save(commit=False)
            user.set_password(form.cleaned_data['password'])

            user.is_superuser = False
            user.is_staff = False

            user.save()

            return HttpResponse("Đăng ký thành công , đã gửi mail.")
    else :
        form=CustomerUserForm()

    return render(request, "register.html", {"form": form})
