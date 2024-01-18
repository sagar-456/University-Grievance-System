
# views.py'
from django.shortcuts import render, redirect 
from grievance.models import Contact, UserData, Complaint, UserNotice, UserResponse
from django.contrib.auth import authenticate, login , logout 
from django.contrib import messages
from grievance.forms import RegisterUserForm, ComplaintForm, ResponseForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone 
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
    return render(request,"home.html")
    


from django.shortcuts import render, get_object_or_404

def usernotice(request):
    return render(request,'usernotice.html')

def about(request):
    return render(request,"about.html")
# @login_required
# def profile(request):
#     return render(request,'authenticate/userdashboard.html')

@login_required
def notice(request):
    try:
        user_data = UserData.objects.get(user=request.user)
    except UserData.DoesNotExist:
        user_data = None

    user_complaints = Complaint.objects.filter(user=request.user)
    user_notice = UserNotice.objects.filter(user=request.user)
    user_responses = UserResponse.objects.filter(user=request.user)
    print(user_responses)

    if request.method == 'POST':
        response_form = ResponseForm(request.POST)
        if response_form.is_valid():
            notice_id = response_form.cleaned_data['notice_id']
            notice = get_object_or_404(UserNotice, id=notice_id)
            # Create and save the response with the associated complaint
            response = response_form.save(commit=False)
            response.user = request.user
            response.notice = notice  
            response.save()
    else:
        response_form = ResponseForm()

    context = {
        'user_data': user_data,
        'response_form': response_form,
        'user_complaints': user_complaints,
        'user_notice': user_notice,
        'user_responses': user_responses,
    }

    return render(request, 'notice.html', context)





@login_required
def guidelines(request):
    return render(request,'guidelines.html')

@login_required
def profile(request):
    
    try:
        user_data = UserData.objects.get(user=request.user)
    except UserData.DoesNotExist:
        # Handle the case where UserData does not exist for the user
        user_data = None
    # Handle ComplaintForm submission
    if request.method == 'POST':
        complaint_form = ComplaintForm(request.POST)
        if complaint_form.is_valid():
            complaint = complaint_form.save(commit=False)
            complaint.user = request.user
            complaint.created_at = timezone.now()
            complaint.save()
    else:
        complaint_form = ComplaintForm()
    user_complaints = Complaint.objects.filter(user=request.user)
    

    context = {
        'user_data': user_data,
        'complaint_form': complaint_form,
        'user_complaints': user_complaints,
    }

    return render(request, 'authenticate/userdashboard.html', context)



# def login_user(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('profile')
            
#         else:
#             messages.success(request,("There was an error Logging in!! Try Again..."))
#             return redirect('login')

#     else:
#         return render(request,'authenticate/login.html',{})
    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.success(request, "There was an error Logging in!! Try Again...")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})




def logout_user(request):
    logout(request)
    messages.success(request,("You were logged out!!!"))
    return redirect ('home')

    

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            gender = form.cleaned_data.get('gender')
            user_type = form.cleaned_data.get('user_type')
            phone_number = form.cleaned_data.get('phone_number')
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            user_data = UserData.objects.create(user=user, phone_number=phone_number, gender=gender, user_type=user_type)
            user_data.save()
            
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Registration Successful!")
                return redirect('home')

    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/signup.html', {'form': form})



def contact(request):
    if request.method == 'POST':
         email = request.POST['Email']
         name = request.POST['Name']
         subject = request.POST['subject']
         condata=Contact(email=email,name=name,subject=subject)
         condata.save()
         return render(request,'success.html')
    else:
        return render(request,'contact.html')


