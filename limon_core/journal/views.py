from django.views.generic import TemplateView
from journal.models import Publication, AboutMe


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = {
            'about_me': AboutMe.objects.first()
        }
        return context


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.filter(is_active = True)
        }
        return context
    #  all() = Вытаскивает все Записи!
    #  first() = Вытаскивает одну запись из всех!
    #  git() =



class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            'publication': Publication.objects.get(id=publication_pk)
        }
        return context
