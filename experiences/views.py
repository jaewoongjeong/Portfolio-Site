from django.views.generic import DetailView, ListView

from experiences.models import PostModel


# Create your views here.
class PostDV(DetailView):
    model = PostModel
    template_name = 'post.html'


class TaggedObjectLV(ListView):
    model = PostModel
    context_object_name = 'post_list'
    template_name = 'taggit/taggit_list.html'

    # Passed onto the template via 'object_list'
    def get_queryset(self):
        return PostModel.objects.filter(tags__name=self.kwargs.get('tag'))

    # Passed onto the template via 'tagname'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context