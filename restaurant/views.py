from restaurant.models import Cook, Dish, DishType

from django.urls import reverse_lazy

from django.shortcuts import render

from django.views import generic


def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "restaurant/dish_type_list.html"
    paginate_by = 5
    queryset = DishType.objects.all()


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    context_object_name = "dish_type_list"
    template_name = "restaurant/dish_type_create.html"
    paginate_by = 5
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    paginate_by = 5
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.all().select_related("DishType")


class DishCreateView(generic.CreateView):
    model = Dish
    success_url = reverse_lazy("restaurant:dish-list")
    fields = "__all__"


class DishDetailView(generic.DetailView):
    model = Dish


class DishUpdateView(generic.UpdateView):
    model = Dish
    success_url = reverse_lazy("restaurant:dish-list")
    fields = "__all__"


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dish-list")
