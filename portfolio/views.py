from django.views.generic import ListView, TemplateView
from django.db.models.aggregates import Count

from experiences.models import PostModel
from taggit.models import Tag


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return PostModel.objects.all().order_by('-start_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = Tag.objects.all().annotate(num_times=Count('taggit_taggeditem_items'))
        mydict = {}
        for tag in queryset:
            mydict[tag.name] = tag.num_times
        mydict = {k: v for k, v in sorted(mydict.items(), key=lambda x: x[1], reverse=True)}

        context['tags'] = Tag.objects.all()
        context['tag_names'] = list(mydict.keys())[:15]
        context['tag_values'] = list(mydict.values())[:15]
        context['tag_sum'] = sum(list(mydict.values()))

        return context


class TestView(TemplateView):
    template_name = 'test.html'

