from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from app.form import ContactForm
from app.models import Mentors, Portfolio


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    from django.views import View
    from django.shortcuts import render

    class ContactView(View):

        def get(self, request):
            return render(request, "contact.html")

        def post(self, request):
            name = request.POST.get("name")
            course = request.POST.get("course")
            phone = request.POST.get("phone_number")

            print(name, course, phone)

            return render(request, "contact.html")

class CourseView(TemplateView):
    template_name = 'courses.html'


class MentorsView(TemplateView):
    template_name = 'mentors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mentors'] = Mentors.objects.all()
        return context


class PortfolioView(ListView):
    template_name = 'portfolio.html'
    context_object_name = 'portfolios'
    paginate_by = 3
    queryset = Portfolio.objects.all()


class TeamView(TemplateView):
    template_name = 'team.html'
