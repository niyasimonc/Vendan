from order.forms import OrderForm
from django.shortcuts import render
from users.models import CustomUser
from django.http import HttpResponseRedirect
from django.urls import reverse


def place_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.save(commit=False)
            custm_user = CustomUser.objects.filter(user=request.user).first()
            data.user = custm_user
            data.save()
            return HttpResponseRedirect(reverse
                                        ('home'))
    else:
        form = OrderForm()

    return render(request, "order/index.html", {'form': form})
