from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .forms import PersonaForm , JournalForm

from .models import Profile, Persona, Journal

# Create your views here.

def home(request):
    people = Persona.objects.all()
    profile = request.user.profile
    return render(request, 'index.html', {'people':people, 'profile':profile})

def form(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        persona = form.save()
        persona.save()
        return redirect('home')
    else:
        form = PersonaForm()
    return render(request, 'form.html', {'form':form})



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to profile after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'registerform': form})

def my_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username  = form.cleaned_data.get('username')
            password  = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'loginform':form})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('home')  # Redirect to login if user is not authenticated
    return render(request, 'profile.html', {'profile': request.user.profile})

##---------------------------JOURNAL----------------------------------##

def journal(request):
    journals = Journal.objects.all()
    profile = request.user.profile
    
    context = {
        'journals':journals,
        'profile':profile
    }
    return render(request, 'journal/home.html', context=context)

def new_journal(request):
    if request.method == "POST":
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)  # Create an instance but don't save it yet
            journal.user = request.user.profile  # Set the user field
            journal.save()  # Now save the journal instance
            return redirect('journal')  # Redirect after saving
    else:
        form = JournalForm()
    return render(request, 'journal/new.html', {'journalform': form})        

def journal_detail(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    context = {
        'journal': journal
    }
    return render(request, 'journal/detail.html', context)

def update_journal(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    if journal.user == request.user.profile:
        if request.method == "POST":
            form = JournalForm(data=request.POST, instance=journal)  # Correctly pass the instance
            if form.is_valid():
                form.save()  # Save the form
                return redirect('journal')  # Redirect after saving
        else:
            form = JournalForm(instance=journal)  # Initialize with the existing journal instance
    else:
        return redirect('journal')  # Redirect if the user is not the author

    context = {
        'journal': journal,
        'updatejournalform': form
    }
    return render(request, 'journal/update.html', context=context)

def del_journal(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    if journal.user == request.user.profile:
        if request.method == 'POST':
            journal.delete()
            return redirect('journal')
    
    return render(request, 'journal/delete.html', {'journal':journal})