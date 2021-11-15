from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import PassportOfObject, CounterParty, SubJobs
from .forms import CounterPartyForm
from django.forms import modelformset_factory


class MainTemplateView(TemplateView):
    template_name = 'main/index.html'
    table = PassportOfObject

    def get_context_data(self, **kwargs):
        form = CounterPartyForm(self.request.GET or None)
        kwargs['Objects'] = PassportOfObject.objects.order_by('-id')
        kwargs['form'] = form
        return super().get_context_data(**kwargs)


def agents(request, subjob_id):
    subjob = SubJobs.objects.get(id=subjob_id)
    formset = modelformset_factory(CounterParty, form=CounterPartyForm, extra=0)
    if request.method == "POST":
        forms = formset(request.POST, queryset=CounterParty.objects.filter(Accreditation__id=subjob.id))
        if forms.is_valid():
            instances = forms.save(commit=False)
            for instance in instances:
                instance.subjob_id = subjob.id
                instance.save()
            return redirect('/')
    forms = formset(queryset=CounterParty.objects.filter(Accreditation__id=subjob.id))

    return render(request, 'main/agents.html', {'forms': forms})
# Create your views here.
