from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Patient, Feedback
from .forms import VitalRecordForm, PatientLoginForm, FeedbackForm


# 🔷 Helper functions
def is_doctor(user):
    return user.is_superuser


# 🔷 Home redirect based on role
def home(request):
    if request.user.is_authenticated and is_doctor(request.user):
        return redirect('doctor_dashboard')
    elif request.session.get('patient_id'):
        return redirect('my_records')
    else:
        return redirect('select_role')

# 🔷 Doctor dashboard
@login_required
@user_passes_test(is_doctor)
def doctor_dashboard(request):
    patients = Patient.objects.all()
    return render(request, 'hms/doctor_dashboard.html', {
        'patients': patients
    })


# 🔷 Patient dashboard
def my_records(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('patient_login')

    patient = get_object_or_404(Patient, id=patient_id)
    vitals = patient.vitals.all()

    return render(request, 'hms/my_records.html', {
        'patient': patient,
        'vitals': vitals
    })


# 🔷 Doctor: view and add vitals for a patient
@login_required
@user_passes_test(is_doctor)
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    vitals = patient.vitals.all()

    if request.method == 'POST':
        form = VitalRecordForm(request.POST)
        if form.is_valid():
            vital = form.save(commit=False)
            vital.patient = patient
            vital.save()
            return redirect('patient_detail', patient_id=patient.id)
    else:
        form = VitalRecordForm()

    return render(request, 'hms/patient_detail.html', {
        'patient': patient,
        'vitals': vitals,
        'form': form,
    })


# 🔷 Unknown role fallback
def unknown_role(request):
    return render(request, 'hms/unknown_role.html')


# 🔷 Patient login view
def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                patient = Patient.objects.get(name=username)
                expected_password = f"{patient.floor_number}{patient.room_number}{patient.bed_number}"

                if password == expected_password:
                    request.session['patient_id'] = patient.id
                    messages.success(request, f"Welcome, {patient.name}!")
                    return redirect('my_records')
                else:
                    messages.error(request, "Invalid password.")
            except Patient.DoesNotExist:
                messages.error(request, "No patient found with that name.")
    else:
        form = PatientLoginForm()

    return render(request, 'hms/patient_login.html', {'form': form})


# 🔷 Logout
def logout_and_redirect(request):
    logout(request)  # doctor logout
    if 'patient_id' in request.session:
        del request.session['patient_id']  # also clear patient session
    return redirect('select_role')


# 🔷 Role selection
def select_role(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('doctor_dashboard')
    elif request.session.get('patient_id'):
        return redirect('my_records')

   # If neither doctor nor patient
    return render(request, 'hms/select_role.html', {
        'patient_logged_in': request.session.get('patient_id') is not None
    })


# 🔷 About & Feedback
def about(request):
    patient_id = request.session.get('patient_id')
    patient = None
    if patient_id:
        patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST' and patient:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.patient = patient
            feedback.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('about')
    else:
        form = FeedbackForm()

    return render(request, 'hms/about.html', {'form': form})


# 🔷 Doctor view of feedbacks
@login_required
@user_passes_test(is_doctor)
def feedbacks(request):
    all_feedbacks = Feedback.objects.order_by('-submitted_at')
    return render(request, 'hms/feedbacks.html', {'feedbacks': all_feedbacks})
