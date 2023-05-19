from django.shortcuts import render

# Create your views here.


tax = 0.15  


def home(request):
    
    return render(request, 'home.html')




def tax_rate_view(request):
    
    return render(request, 'tax_rate.html', {'tax_rate': tax})


def calculate_total(request, number):
    
    total = float(number) * (1 + tax)
    return render(request, 'total.html', {'number': number, 'total': total})
