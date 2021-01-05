from django.views.generic import TemplateView

from .models import MainPage
from products.models import Product


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self):
        context = super().get_context_data()

        main_page = MainPage.objects.first()
        if main_page:
            context['page_data'] = main_page
            context['paragraphs'] = main_page.paragraphs.all()
            context['images'] = main_page.images.all()
            context['products'] = Product.objects.all().order_by('-date_added')
        else:
            context['no_content'] = True

        return context
