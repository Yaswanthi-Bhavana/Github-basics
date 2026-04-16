from django.shortcuts import render
from .forms import StudentForm

def enroll(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'crs/success.html')
    else:
        form = StudentForm()

    return render(request, 'crs/enroll.html', {'form': form})