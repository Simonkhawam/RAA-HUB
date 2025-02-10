from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):  #LoginRequiredMixin,
    template_name = 'home/homepage.html'


