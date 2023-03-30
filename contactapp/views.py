from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from contactapp.forms import AddContact
from django.views.generic.base import View

from .models import Person


def filter_person(request):
    filter_value = request.POST.get("filter_field", None)
    filter_field = request.POST.get("field", "name")
    if not filter_value:
        person = Person.objects.all()
    else:
        filter_data = {
            f"{filter_field}__istartswith": filter_value
        }
        person = Person.objects.filter(**filter_data)
    context = {
        "person": person,
    }

    return render(request, "contactapp/index.html", context)


def delete_person(request):
    if request.method == "POST":
        person = Person.objects.all()
        checked_list = request.POST.getlist('person_to_delete')
        context = {'person': person, 'checked_list': checked_list}

        for person_id in checked_list:
            person = Person.objects.filter(id=person_id)
            person.delete()
            return HttpResponseRedirect("/")

        return render(request, "contactapp/index.html", context)


def index(request):
    if request.method == "GET":
        person = Person.objects.all()
        return render(request, "contactapp/index.html", {"person": person})


def add(request):
    if request.method == "POST":
        form = AddContact(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            number = form.cleaned_data["number"]
            email = form.cleaned_data["email"]
            relation = form.cleaned_data["relation"]
            
            isDouble = Person.objects.filter(email=email)
            if isDouble.exists():
                context = {
                    "form": form,
                    "error": "CONTACT WITH GIVEN EMAIL ALREADY EXISTS!!"
                }
                return render(request, "contactapp/add.html", context)

            p = Person(name=name, number=number, email=email, relation=relation)
            p.save()
            
            return HttpResponseRedirect("/") 
    else:
        form = AddContact()

    context = {
       "form": form,
    }

    return render(request, "contactapp/add.html", context)

