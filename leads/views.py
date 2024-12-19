from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import lead, Agent
from .forms import LeadForm,LeadModelform

def lead_list(request):
    leads = lead.objects.all()
    context = {
        "leads":leads
    }
    
    return render(request, 'leads/lead_list.html', context)

def lead_detail(request, pk):
    leads = lead.objects.get(id=pk)
    context = {
        "leads":leads
    }
    return render(request, 'leads/lead_detail.html', {"lead":leads})

def lead_create(request):
    form = LeadModelform()
    if request.method == 'POST':
        form = LeadModelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context ={
        "form":form
    }
    return render(request, 'leads/lead_create.html',context)



def lead_update(request, pk):
    leads = lead.objects.get(id=pk)
    form = LeadModelform(instance=leads)
    if request.method == 'POST':
        form = LeadModelform(request.POST, instance=leads)
        if form.is_valid():
            
            form.save()
            return redirect('/leads')

    context = {
        "form" :form,   
        "leads":leads
    }
    return render(request, 'leads/lead_update.html',context)


# def lead_update(request, pk):
#     leads = lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             leads.first_name = first_name
#             leads.last_name = last_name
#             leads.age = age
#             leads.save()
#             return redirect('/leads')

#     context = {
#         "form" :form,   
#         "leads":leads
#     }
#     return render(request, 'leads/lead_update.html',context)

def lead_delete(request, pk):
    leads = lead.objects.get(id=pk)
    leads.delete()
    return redirect('/leads')
