from django.shortcuts import render, redirect
from apps.bill_tracker.models import Bill

def index(request):
    if ('user_id' in request.session):
        context = {}
        context['bills'] = Bill.objects.filter(user_id=request.session['user_id'])
        return render(request, 'bill_tracker/index.html', context)
    return redirect('travel_app:login')

def add_bill(request):
    if ('user_id' in request.session and len(request.POST['desc']) > 0 and len(request.POST['amount']) > 0):
        try:
            bill = Bill.objects.create(desc=request.POST['desc'], amount=request.POST['amount'], user_id=request.session['user_id'])
        except:
            pass
    return redirect('bill_tracker:index')

def edit_bill(request, bill_id):
    if ('user_id' in request.session):
        context = {}
        context['bill'] = Bill.objects.get(id=bill_id)
        return render(request, 'bill_tracker/edit.html', context)
    return redirect('bill_tracker:index')

def update_bill(request):
    if ('user_id' in request.session):
        try:
            bill = Bill.objects.get(id=request.POST['bill_id'])
            bill.desc = request.POST['desc']
            bill.amount = request.POST['amount']
            bill.save()
        except:
            pass
    return redirect('bill_tracker:index')

def del_bill(request, bill_id):
    if ('user_id' in request.session):
        bill = Bill.objects.get(id=bill_id)
        bill.delete()
    return redirect('bill_tracker:index')
