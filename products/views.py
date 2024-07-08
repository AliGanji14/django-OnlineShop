from django.shortcuts import get_object_or_404, render, HttpResponse
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _
from orders.models import Order

from .forms import CommentForm
from .models import Product, Comment


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(status=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 2


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, pk=product_id)
        obj.product = product

        messages.success(self.request, _('Comment successfully created'))

        return super().form_valid(form)


def search_product_view(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Product.objects.filter(title__icontains=search)
        if len(products) == 0:
            return HttpResponse(_('Your product was not found'))
    return render(request, 'products/product_list.html', {'products': products})


def profile_account_view(request):
    orders = Order.objects.filter(user=request.user.id)
    return render(request, 'profile_account.html', {'orders': orders})
