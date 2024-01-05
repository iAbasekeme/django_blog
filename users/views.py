from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUser, userUpdateForm, profileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):       
    if request.method == 'POST':        
        form = RegisterUser(request.POST)                
        if form.is_valid():      
            form.save()  
            username = form.cleaned_data.get('username')            
            messages.success(request, f"Account created for {username}!")
            return redirect('login')   
    else:
        form = RegisterUser()        
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    userInfo = request.user
    if request.method == 'POST':            
        u_form = userUpdateForm(request.POST, instance=userInfo)   
        # import pdb; pdb.set_trace()                
        p_form = profileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():             
            p_form.save()
            u_form.save()
            messages.success(request, f"Account Updated")
            return redirect('profile')           
    else:
        u_form = userUpdateForm(instance=userInfo)
        p_form = profileUpdateForm(instance=request.user.profile)        
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)