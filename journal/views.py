from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import JournalEntryForm, RegisterForm
from .sentiment import analyse_sentiment
from .models import JournalEntry, Profile

@login_required
def create_entry(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user

            label, score = analyse_sentiment(entry.content)
            entry.sentiment_label = label
            entry.sentiment_score = score
            entry.save()
            return redirect('create_entry')
    else:
        form = JournalEntryForm()
    

    entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')


    return render(request, 'journal/create_entry.html',{
        'form':form,
        'entries':entries
        })

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,'journal/home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            
            user.profile.theme = form.cleaned_data['theme']
            user.profile.save()

            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    
    return render(request, 'journal/register.html', {'form':form})


@login_required
def dashboard(request):
    entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journal/dashboard.html', {'entries':entries})

@login_required
def settings (request):
    return render(request, 'journal/settings.html')