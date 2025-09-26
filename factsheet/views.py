from django.shortcuts import render, redirect, get_object_or_404
from .forms import FactsheetForm
from .models import Factsheet

def create_factsheet(request):
    if request.method == 'POST':
        form = FactsheetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('factsheet-list')
    else:
        form = FactsheetForm()
    return render(request, 'factsheet/factsheet_form.html', {'form': form})

def factsheet_list(request):
    factsheets = Factsheet.objects.all().order_by('-created_at')
    return render(request, 'factsheet/factsheet_list.html', {'factsheets': factsheets})

# def factsheet_detail(request, pk):
#     factsheet = get_object_or_404(Factsheet, pk=pk)
#     return render(request, 'factsheet/factsheet_detail.html', {'factsheet': factsheet})
