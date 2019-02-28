from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import newCarForm
from .models import newCarModel

# function used to test server
def index(request):
    return HttpResponse("made it")

# If data is clean print new entry
def newCar(request):
    if(request.method == "post"):
        form = newCarForm(request.POST)
        if(form.is_valid()):
            newCarModel.objects.create(make=request.POST["make"], model=request.POST["model"],year=request.POST["year"],
                                       mpg=request.POST["mpg"],)

        else:
            context = {
                "errors": form.errors,
                "form": form,
                "allEntries": newCarModel.objects.all(),
            }
            return render(request, "validationcwApp/Congrats.html", context)

        context = {
            "allEntries": newCarModel.objects.all(),
            "form": newCarForm(),
        }

        return render(request, "validationcwApp/Congrats.html", context)