from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Make name unique for login
    age = models.PositiveIntegerField()

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True)

    contact_number = models.CharField(max_length=15)
    address = models.TextField(blank=True)

    room_number = models.CharField(max_length=10, blank=True, null=True)
    floor_number = models.CharField(max_length=10, blank=True, null=True)
    bed_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def password(self):
        """
        Build password from floor + room + bed.
        Example: F2R101B5
        """
        return f"{self.floor_number}{self.room_number}{self.bed_number}"

    @property
    def patient_id(self):
        """
        Returns a unique patient ID based on room, floor, and bed.
        Example: R101-F2-B5
        """
        if self.room_number and self.floor_number and self.bed_number:
            return f"R{self.room_number}-F{self.floor_number}-B{self.bed_number}"
        return f"Patient-{self.pk}"


class VitalRecord(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='vitals'
    )
    date_recorded = models.DateTimeField(auto_now_add=True)

    systolic = models.IntegerField(default=120)
    diastolic = models.IntegerField(default=80)

    heart_rate = models.PositiveIntegerField(help_text="Beats per minute")
    temperature = models.DecimalField(max_digits=4, decimal_places=1, help_text="In Celsius")
    sugar_level = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Blood sugar level in mg/dL",
        null=True,
        blank=True,
    )

    @property
    def blood_pressure(self):
        return f"{self.systolic}/{self.diastolic}"

    def __str__(self):
        return f"Vitals of {self.patient.name} on {self.date_recorded.date()}"


class Feedback(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.patient.name} at {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
