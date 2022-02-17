from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import  Pray_tb,Comment
from django.views.generic import DetailView,ListView,UpdateView,CreateView,DeleteView
from django.views.generic.base import TemplateView

# Create your views here.
# def prayer(request):
    
#     get_pray = Pray_tb.objects.all()
#     return render(request,'prayer.html', {'get_pray': get_pray})
class indexview(ListView):
    template_name="prayer.html"
    context_object_name = "pray"
    model = Pray_tb
    # context_object_name = "pray"
class indexdetailview(DetailView):
    template_name="detail/single.html"
    context_object_name = "pray"
    model = Pray_tb

class CommentEntry(CreateView):
    model = Comment
    # the fields mentioned below become the entry rows in the generated form
    fields = ['name', 'email', 'comment']
    # context_object_name = "pray"
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['pray_tb'] = Pray_tb.objects.all()
    #     return context
# def details(request,id):
#     get_more = More_tb.objects.all()
    # return render(request,'prayer.html', {'get_pray': get_pray})
# class Details(TemplateView):
#     # model = Pray_tb
#     template_name = 'single.html'
#     # context_object_name = 'details'
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['book'] = Pray_tb.objects.all()
#         return context


