from django.shortcuts import render,redirect

from complaint.models import Complaint

# Create your views here.

def complaint(request):
    if (request.user.is_authenticated):
        return render(request,'complaint/complaint.html')
    else:
        return render(request,'user/signin.html')

def add_complaint(request):
    if request.method == "POST":
        user = request.user
        violation_date=request.POST.get("vdate")
        place = request.POST.get("place")
        district=request.POST.get("district")
        state=request.POST.get("state")
        comment=request.POST.get("comment")
        uploaded_file = request.FILES.get('evidence')
        complaint = Complaint(
                    user=user,
                    violation_date=violation_date,
                    place=place,
                    district=district,
                    state=state,
                    comment=comment,
                    # Set other fields similarly
                    uploaded_file=uploaded_file,
                )

        # Save the model to the database
        complaint.save()

        content={
            "success":1
        }
        return render(request,'pages/index.html',content)

# views.py
# from django.shortcuts import render, redirect
# from .forms import ComplaintForm

# def create_complaint(request):
#     if request.method == 'POST':
#         form = ComplaintForm(request.POST, request.FILES)
#         if form.is_valid():
#             complaint = form.save(commit=False)

#             # Save file to the model instance
#             complaint.uploaded_file = form.cleaned_data['uploaded_file']

#             # Save the model to the database
#             complaint.save()

#             # Do any additional processing or redirect as needed
#             return redirect('success_page')
#     else:
#         form = ComplaintForm()

#     return render(request, 'complaint/complaint.html', {'form': form})

def complaints(request):
    complaints=Complaint.objects.filter(user=request.user).order_by('-id')
    # complaints=Complaint.objects.filter(id=request.user)
    # complaint=Complaint.objects.filter(id=cid)
    content={
        "complaints":complaints
    }
    return render(request,'complaint/complaints.html',content)

def cancel(request,id):
    Complaint.objects.filter(id=id).delete()
    content={
            "delete":1
        }
    return render(request,'pages/index.html',content)