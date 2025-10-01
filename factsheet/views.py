from django.shortcuts import render, redirect, get_object_or_404
from .forms import FactsheetForm
from .models import Factsheet
from django.shortcuts import render, redirect
from .forms import (
    FactsheetForm, AnnexureIIForm, AnnexureIIIForm,
    TransitCampForm, ApprovalForm, ConstructionStatusForm, StopWorkForm
)

def create_factsheet(request):
    if request.method == 'POST':
        factsheet_form = FactsheetForm(request.POST)
        annexureII_form = AnnexureIIForm(request.POST)
        annexureIII_form = AnnexureIIIForm(request.POST)
        transitcamp_form = TransitCampForm(request.POST)
        approval_form = ApprovalForm(request.POST)
        construction_form = ConstructionStatusForm(request.POST)
        stopwork_form = StopWorkForm(request.POST)

        if (factsheet_form.is_valid() and annexureII_form.is_valid() and
            annexureIII_form.is_valid() and transitcamp_form.is_valid() and
            approval_form.is_valid() and construction_form.is_valid() and
            stopwork_form.is_valid()):

            factsheet_form.save()
            annexureII_form.save()
            annexureIII_form.save()
            transitcamp_form.save()
            approval_form.save()
            construction_form.save()
            stopwork_form.save()

            return redirect('factsheet-list')  # Replace with your success page

    else:
        factsheet_form = FactsheetForm()
        annexureII_form = AnnexureIIForm()
        annexureIII_form = AnnexureIIIForm()
        transitcamp_form = TransitCampForm()
        approval_form = ApprovalForm()
        construction_form = ConstructionStatusForm()
        stopwork_form = StopWorkForm()

    context = {
        'factsheet_form': factsheet_form,
        'annexureII_form': annexureII_form,
        'annexureIII_form': annexureIII_form,
        'transitcamp_form': transitcamp_form,
        'approval_form': approval_form,
        'construction_form': construction_form,
        'stopwork_form': stopwork_form,
    }

    return render(request, 'factsheet/factsheet_form.html', context)

def factsheet_list(request):
    factsheets = Factsheet.objects.all().order_by('-created_at')
    return render(request, 'factsheet/factsheet_list.html', {'factsheets': factsheets})

# def factsheet_detail(request, pk):
#     factsheet = get_object_or_404(Factsheet, pk=pk)
#     return render(request, 'factsheet/factsheet_detail.html', {'factsheet': factsheet})
