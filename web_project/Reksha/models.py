from django.db import models


# Create your models here.
class authentication(models.Model):
    email = models.CharField(max_length=50,unique=True)

class RescueForce(models.Model):
    RESCUE_FORCES_CHOICES = [
        ('fire', 'Fire and Rescue Services'),
        ('police', 'Police'),
        ('coast_guard', 'Coast Guard'),
        ('ndrf', 'NDRF'),
        ('volunteer', 'Volunteer'),
        ('sdma','SDMA'),
        ('healthcare','HEALTHCARE & MEDICAL SERVICE'),
        ('trauma','TRAUMA CARE'),
    ]

    DISTRICT_CHOICES = [
        ('tvm', 'Thiruvananthapuram'),
        ('kollam', 'Kollam'),
        ('pta', 'Pathanamthitta'),
        ('alpy', 'Alappuzha'),
        ('kottayam', 'Kottayam'),
        ('ekm', 'Ernakulam'),
        ('tcr', 'Thrissur'),
        ('pkd', 'Palakkad'),
        ('mlp', 'Malappuram'),
        ('kkd', 'Kozhikode'),
        ('wnd', 'Wayanad'),
        ('knr', 'Kannur'),
        ('ksd', 'Kasaragod'),
    ]

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10, unique=True, help_text="Enter your 10-digit mobile number")
    rescue_forces = models.CharField(max_length=50, choices=RESCUE_FORCES_CHOICES, help_text="Select your rescue force")
    location = models.CharField(max_length=255, help_text="Enter your location")
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES, help_text="Select your district")
    pincode = models.CharField(max_length=6, help_text="Enter your 6-digit pincode")

    def _str_(self):
        return f"{self.username} - {self.rescue_forces}"
    

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    DISTRICT_CHOICES = [
        ('tvm', 'Thiruvananthapuram'),
        ('kollam', 'Kollam'),
        ('pta', 'Pathanamthitta'),
        ('alpy', 'Alappuzha'),
        ('kottayam', 'Kottayam'),
        ('ekm', 'Ernakulam'),
        ('tcr', 'Thrissur'),
        ('pkd', 'Palakkad'),
        ('mlp', 'Malappuram'),
        ('kkd', 'Kozhikode'),
        ('wnd', 'Wayanad'),
        ('knr', 'Kannur'),
        ('ksd', 'Kasaragod'),
    ]

    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    mobile_no = models.CharField(max_length=10, help_text="Enter your 10-digit mobile number")
    email = models.EmailField()
    address = models.TextField(help_text="Enter your address",null=True)
    dob = models.DateField(help_text="Enter your date of birth (YYYY-MM-DD)",null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES,null=True, help_text="Select your district")
    pincode = models.CharField(max_length=6,null=True, help_text="Enter your 6-digit pincode")
    relative_contact = models.CharField(max_length=10,null=True, help_text="Enter relative's 10-digit contact number")
    password = models.CharField(max_length=128, help_text="Enter your password",null=True)  

    def _str_(self):
        return self.username
    



class UserFeedback(models.Model):
    Username=models.CharField(max_length=50)
    name = models.CharField(max_length=100)  
    email = models.EmailField()          
    subject = models.CharField(max_length=200)  
    message = models.TextField()     
    created_at = models.DateTimeField(auto_now_add=True)       

    def _str_(self):
        return f"{self.name} - {self.subject}"
    

class Updateoprres(models.Model):
    workid = models.TextField()
    victimname = models.CharField(max_length=50,unique=True)                   
    username = models.CharField(max_length=50,unique=True)
    location = models.CharField(max_length=255)                   
    message = models.TextField()                
    created_at = models.DateTimeField(auto_now_add=True)  


class Reportres(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Add this field

    def _str_(self):
        return f"Subject: {self.subject} - Message: {self.message[:100]}"  

class Complaintres(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def _str_(self):
        return f"Message from {self.name} - {self.subject}"
    

class Notification(models.Model):
    mobile_number = models.CharField(max_length=15, verbose_name="Mobile Number")
    situation = models.CharField(max_length=255, verbose_name="Situation")
    message = models.TextField(verbose_name="Message")
    location = models.CharField(max_length=255, verbose_name="Location")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp")
    username=models.CharField(max_length=50)


    def _str_(self):
        return f"Notification to {self.mobile_number} - {self.situation[:20]}"

class Meta:
    verbose_name = "Notification"
    verbose_name_plural = "Notifications"


class Staff(models.Model):
    DISTRICT_CHOICES = [
        ('TVM', 'Thiruvananthapuram'),
        ('KLM', 'Kollam'),
        ('PTA', 'Pathanamthitta'),
        ('ALP', 'Alappuzha'),
        ('KTM', 'Kottayam'),
        ('IDK', 'Idukki'),
        ('EKM', 'Ernakulam'),
        ('TSR', 'Thrissur'),
        ('PKD', 'Palakkad'),
        ('MLP', 'Malappuram'),
        ('KKD', 'Kozhikode'),
        ('WYD', 'Wayanad'),
        ('KNR', 'Kannur'),
        ('KSG', 'Kasaragod'),
    ]

    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    district = models.CharField(max_length=25, choices=DISTRICT_CHOICES)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    email_id = models.EmailField()
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def _str_(self):
        return self.name


class assigntab(models.Model):
    """Model for storing complaint details."""
    victimuser = models.CharField(max_length=25)  # Victim username
    location = models.CharField(max_length=255)  # Incident location
    mobile_number = models.CharField(max_length=15)  # Complainant's contact number
    rescue_force = models.CharField(max_length=30)  # Related rescue force
    landmark = models.CharField(max_length=255)  # victim landmark
    pincode = models.CharField(max_length=6)
    message = models.TextField(verbose_name="Message")
    def _str_(self):
        return f"{self.location} - {self.mobile_number}"
    
class commonFeedback(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField()          
    subject = models.CharField(max_length=200)  
    message = models.TextField()     
    created_at = models.DateTimeField(auto_now_add=True)       

    def _str_(self):
        return f"{self.name} - {self.subject}"

    
class OTPVerification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    
class sendrepuser(models.Model):
    username = models.CharField(max_length=100)  
    subject = models.CharField(max_length=200)  
    message = models.TextField()     
    created_at = models.DateTimeField(auto_now_add=True)       

    def _str_(self):
        return f"{self.name} - {self.subject}"
    
class sendrepres(models.Model):
    username = models.CharField(max_length=100)  
    subject = models.CharField(max_length=200)  
    message = models.TextField()     
    created_at = models.DateTimeField(auto_now_add=True)       

    def _str_(self):
        return f"{self.name} - {self.subject}"