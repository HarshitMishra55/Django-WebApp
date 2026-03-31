from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import loader
from .models import Member, MyTable
from django.db import IntegrityError
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return HttpResponse("Hello Django")


def mypage(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())


def members(request):
    mymembers = Member.objects.all()
    return render(request, "all_members.html", {"mymembers": mymembers})


def table_members(request):
    mymembers = MyTable.objects.all()
    return render(request, "table.html", {"mymembers": mymembers})


def values(request):
    mymembers = Member.objects.all()

    template = loader.get_template("all_members.html")

    context = {
        "mymembers": mymembers,
    }

    return HttpResponse(template.render(context, request))


def insert_data(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        email = request.POST.get("email")

        try:
            MyTable.objects.create(name=name, subject=subject, email=email)
            messages.success(request, "Data inserted successfully")
        except IntegrityError:
            messages.error(request, "Email already exists")
            return render(request, "form.html", {"error": "Email already exists"})
        return redirect("insert")

    return render(request, "form.html")


def show_data(request):
    data_list = MyTable.objects.all().order_by("-id")

    paginator = Paginator(data_list, 5)  # 5 rows per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "show.html", {"page_obj": page_obj})


def delete_data(request, id):
    try:
        obj = MyTable.objects.get(id=id)
        obj.delete()
        messages.success(request, "Data deleted successfully")
    except:
        messages.error(request, "Data not found")

    return redirect("show")


def number_view(request):
    numbers = [1, 2, 3, 4, 5]
    return render(request, "numbers.html", {"numbers": numbers})
