from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import Output
# Create your views here.
def index(request):

    return render(request,'Add/index.html')

def add(request):


    if request.method == "POST":
        form = Output(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            input1 = cd['input1']
            input2 = cd['input2']
            output = input1 + input2
            # return render_to_response('Add/output.html', {'form': form, 'input1': input1, 'input2': input2, 'output': output},  RequestContext(request))
            return render(request,'Add/output.html',{'form': form, 'input1': input1, 'input2': input2, 'output': output})
    else:
        form = Output()
        # return render(request1,'Add/add.html')
        # return render_to_response('Add/add.html', {'form': form},RequestContext(request))
        return render(request,'Add/add.html',{'form': form})
        # return render(request, 'Add/add.html', {'form': {form}})



# def index(request):
#     # return HttpResponse('Hello from posts')
#
#     posts = Posts.objects.all()[:10]
#
#     context = {
#         'title': 'Latest Posts1',
#         'posts': posts
#     }
#
#     return render(request, 'posts/index.html', context)