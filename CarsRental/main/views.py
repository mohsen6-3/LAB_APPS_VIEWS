from django.shortcuts import render
import random
import string
# Create your views here.
def home_view(request):
    return render(request, 'main/home.html')

def about_view(request):
    return render(request, 'main/about.html')

def password_generate_view(request):
    password = [
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    ]
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password += [random.choice(chars) for i in range(9)]
    
    random.shuffle(password)
    password = ''.join(password)
    return render(request, 'main/password_generate.html', {'password': password})