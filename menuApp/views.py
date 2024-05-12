from django.urls import reverse_lazy
from django.views import generic

from .models import Item, MEAL_TYPE
from .forms import CreateItemForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class MenuList(generic.ListView):
    queryset = Item.objects.order_by('-date_created')  # that provides access to the database to execute queries.
    template_name = 'menuApp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    model = Item  # Connect views class with class in model
    template_name = 'menuApp/item_detail.html'


@method_decorator(login_required, name='dispatch')
class CreateItem(generic.CreateView):
    model = Item
    template_name = 'menuApp/create_item.html'
    form_class = CreateItemForm
    success_url = reverse_lazy('home')


class UpdateItem(generic.UpdateView):
    model = Item
    form_class = CreateItemForm
    template_name = 'menuApp/update_item.html'
    success_url = reverse_lazy('home')


class DeleteItem(generic.DeleteView):
    model = Item
    success_url = reverse_lazy('home')
