from django.http import Http404, HttpResponse

from django.shortcuts import redirect, render

from django.views.generic import DetailView, ListView

from .forms import UserForm

from .models import User

# Create your views here.

class SnippetView(SnippetView):
    model = SnippetForm
    template_name = './form/templates/index.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)


class AddFormView(AddView):
    model = User
    template_name = 'users/detail.html'

def add(request):

    if request.method == 'POST':

        form = UserForm(request.POST)

        if form.is_valid():
            # Create and save directly.

            User(
             title=form.cleaned_data['title'],
             language=form.cleaned_data['language'],
             code=form.cleaned_data['code'],
             descript=form.cleaned_data['descript']).save()

            return redirect('users:index')

        else:

            return render(request, 'users/add.html', { 'form' : form })

        else:

        context = { 'header' : 'GET', 'form' : UserForm() }

        return render(request, 'users/add.html', context)
