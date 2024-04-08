from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from taxi.forms import CarCreateForm, DriverCreationForm, DriverLicenseUpdateForm

from .models import Driver, Car, Manufacturer


@login_required
def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    form_class = CarCreateForm
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    form_class = CarCreateForm
    success_url = reverse_lazy("taxi:car-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")


class DriverCreatelView(LoginRequiredMixin, generic.CreateView):
    model = Driver
    form_class = DriverCreationForm
    # template_name = "taxi/driver_form.html"
    # success_url = reverse_lazy("taxi:driver-list")


class DriverUpdatelView(LoginRequiredMixin, generic.UpdateView):
    model = Driver
    form_class = DriverCreationForm
    # template_name = "taxi/driver_form.html"
    # success_url = reverse_lazy("taxi:driver-detail")


class DriverDeletelView(LoginRequiredMixin, generic.DeleteView):
    model = Driver
    # form_class = DriverCreationForm
    # template_name = "taxi/driver_confirm_delete.html"
    success_url = reverse_lazy("taxi:driver-list")


class DriverLicenseUpdateView(LoginRequiredMixin, generic.UpdateView):
    # model = Driver
    model = get_user_model()
    form_class = DriverLicenseUpdateForm
    template_name = "taxi/license_form.html"


class AssignToCarView(LoginRequiredMixin, generic.View):
    model = Car

    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        car.drivers.add(request.user)
        return HttpResponseRedirect(reverse("taxi:car-detail", kwargs={"pk": pk}))

    # def get(self, request, pk):
    #     car = get_object_or_404(Car, pk=pk)
    #     return render(request, self.template_name, {'car': car})


class DeleteFromCarView(LoginRequiredMixin, generic.View):
    model = Car

    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        car.drivers.remove(request.user)
        return HttpResponseRedirect(reverse("taxi:car-detail", kwargs={"pk": pk}))

    # def get(self, request, pk):
    #     car = get_object_or_404(Car, pk=pk)
    #     return render(request, self.template_name, {'car': car})


# @login_required
# def assign_to_car(request: HttpRequest, pk: int) -> HttpResponse:
#     car = get_object_or_404(Car, pk=pk)
#     car.drivers.add(request.user)
#     return HttpResponseRedirect(reverse("taxi:car-detail", kwargs={"pk": pk}))


# @login_required
# def delete_from_car(request: HttpRequest, pk: int) -> HttpResponse:
#     car = get_object_or_404(Car, pk=pk)
#     car.drivers.remove(request.user)
#     return HttpResponseRedirect(reverse("taxi:car-list", kwargs={"pk": pk}))
