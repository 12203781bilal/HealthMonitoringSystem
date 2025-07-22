# hms/context_processors.py
def patient_logged_in(request):
    return {'patient_logged_in': request.session.get('patient_id') is not None}
