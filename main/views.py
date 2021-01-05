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
            # разбить текст на абзацы
            paragraphs = [p.strip() for p in main_page.text.split('\n')]
            # отфильтровать пустые абзацы
            context['paragraphs'] = filter(lambda p: bool(p), paragraphs)
            context['images'] = main_page.images.all()
            context['products'] = Product.objects.all().order_by('-date_added')
        else:
            context['no_content'] = True

        return context
