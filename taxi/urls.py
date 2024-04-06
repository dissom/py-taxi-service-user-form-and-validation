from django.urls import path

from .views import (
    assign_to_car,
    delete_from_car,
    index,
    license_update,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    DriverListView,
    DriverDetailView,
    DriverCreatelView,
    DriverDeletelView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "drivers/<int:driver_id>/license-update/",
        license_update,
        name="license-update"
    ),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    ),
    path(
        "cars/",
        CarListView.as_view(),
        name="car-list"
    ),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car-detail"
    ),
    path(
        "cars/create/",
        CarCreateView.as_view(),
        name="car-create"
    ),
    path(
        "cars/<int:pk>/update/",
        CarUpdateView.as_view(),
        name="car-update"
    ),
    path(
        "cars/<int:pk>/delete/",
        CarDeleteView.as_view(),
        name="car-delete"
    ),
    path(
        "drivers/",
        DriverListView.as_view(),
        name="driver-list"
    ),
    path(
        "drivers/create",
        DriverCreatelView.as_view(),
        name="driver-create"
    ),
    path(
        "drivers/<int:pk>/delete/",
        DriverDeletelView.as_view(),
        name="driver-delete"
    ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
    path("cars/<int:pk>/assign/", assign_to_car, name="assign-to-car"),
    path("cars/<int:pk>/delete/", delete_from_car, name="delete-from-car")
]

app_name = "taxi"
