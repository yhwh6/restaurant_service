from django.urls import path

from restaurant.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishListView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishCreateView,
    DishDetailView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookCreateView,
    CookDetailView,
    CookUpdateView,
    CookDeleteView,
    manage_cook,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish_types/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dish_types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish_types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish_types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path(
        "dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"
    ),
    path(
        "dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"
    ),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path(
        "cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"
    ),
    path(
        "cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"
    ),
    path(
        "cooks/<int:pk>/manage_cook/",
        manage_cook,
        name="manage-cook"
    ),
]

app_name = "restaurant"
