from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from .models import Product


class ProductView(DetailView):
    template_name = 'products/product.html'
    query_pk_and_slug = 'slug'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['lists'] = {}
        # context['lists'][] = context['product'].lists.all()

        context['lists'] = list()
        for lst in context['product'].lists.all():
            context['lists'].append({
                'head': lst.head,
                'items': lst.items.all(),
            })

        return context
