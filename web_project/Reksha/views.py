from django.shortcuts import render
from django.http import HttpResponse
import math
import random
from django.conf import settings
from django.views.generic import View
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.template import loader
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random
# Create your views here.
#def index(request):
    #return HttpResponse("Hello ..this is first Application")
def login(request):
    return render(request, "Reksha/login.html")
def regi(request):
    return render(request, "Reksha/registration.html")
def signup(request):
    return render(request, "Reksha/signupmail.html")
def feed(request):
    return render(request, "Reksha/feedback.html")
def loginres(request):
    return render(request, "Reksha/loginres.html")
def complaint(request):
    return render(request, "Reksha/complaint.html")
def regires(request):
    return render(request, "Reksha/registerres.html")
def reportres(request):
    return render(request, "Reksha/reportres.html")
def profile(request):
    return render(request, "Reksha/profile.html")

def updateprof(request):
    return render(request, "Reksha/updateprof.html")
def index(request):
    return render(request, "Reksha/index.html")
def addstaff(request):
    return render(request, "Reksha/addstaff.html")
def userhome(request):
    return render(request, "Reksha/userhome.html")
def usernav(request):
    return render(request, "Reksha/usernav.html")
def assignwrk(request):
    return render(request, "Reksha/assignwrk.html")
def viewprofuser(request):
    return render(request, "Reksha/viewprofuser.html")

def rescuenav(request):
    return render(request, "Reksha/rescuenav.html")
def new(request):
    return render(request, "Reksha/new.html")



def adminlog(request):
    return render(request, "Reksha/adminlog.html")
def adminnav(request):
    return render(request, "Reksha/adminnav.html")

def viewstaff(request):
    return render(request, "Reksha/viewstaff.html")
def viewnotification(request):
    return render(request, "Reksha/viewnotification.html")
def viewreport(request):
    return render(request, "Reksha/viewreport.html")
def viewcmuser(request):
    return render(request, "Reksha/viewcmuser.html")

def viewcmres(request):
    return render(request, "Reksha/viewcmres.html")
def operations(request):
    return render(request, "Reksha/operations.html")
def index(request):
    return render(request, "Reksha/index.html")

def fpass(request):
    return render(request, "Reksha/forgotpassword.html")

def resetp(request):
    return render(request, "Reksha/resetpass.html")


def user(request):
    return render(request, "Reksha/user.html")



from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.utils.crypto import get_random_string


password_reset_tokens = {}
def forgot_password(request):
     if request.method == "POST":
        email = request.POST.get('email')
        user = UserProfile.objects.filter(email=email).first()
        if user:
            otp = str(random.randint(100000, 999999))
            OTPVerification.objects.update_or_create(user=user, defaults={'otp': otp})

            # Send OTP via Email
            send_mail(
                'Password Reset OTP',
                f'Your OTP is: {otp}',
                'your-email@gmail.com',  # Replace with your email
                [email],
                fail_silently=False,
            )
            request.session['reset_email'] = email
            return redirect('verify_otp')
        return render(request, 'Reksha/forgotpassword.html')


def verify_otp(request):
    email = request.session.get('reset_email')
    if not email:
        return redirect('forgot_password')

    if request.method == "POST":
        otp = request.POST.get('otp')
        user = UserProfile.objects.filter(email=email).first()
        otp_record = OTPVerification.objects.filter(user=user, otp=otp).first()
        if otp_record:
            return redirect('reset_password')
    return render(request,'Reksha/verotp.html')

def reset_password(request):
    email = request.session.get('reset_email')
    if not email:
        return redirect('forgot_password')

    if request.method == "POST":
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            user = UserProfile.objects.filter(email=email).first()
            if user:
                user.password = new_password
                user.save()
                OTPVerification.objects.filter(user=user).delete()
                return redirect('login')
    return render(request,'Reksha/resetpass.html')






    
def generateOTP():
    # which stores all digits    #Declare a digits variable
    digits = "0123456789"
    global OTP
    OTP = ""
    # length of passwords can be changed
    # by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


class Email_Verification(View):
    def get(self,request,*args,**kwargs):
        return render(request,"Reksha/signupmail.html",)



def send_OTP(request):
    if request.method == 'POST':
        subject = "NC Registration OTP"
        message = generateOTP()
        recipient = request.POST.get('to')
        if subject and message:

            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient],fail_silently=False)
            verified_email = authentication(email=recipient)
            verified_email.save()
            otp = message
            print(subject, message, settings.EMAIL_HOST_USER, [recipient],otp)

            #return HttpResponse('Invalid header found.')
            return render(request,'Reksha/otp.html',{"recipient":recipient})
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
def Verifyotp(request):
    recipient = request.POST.get('otp')
    if OTP == recipient:
        return render(request,'Reksha/registration.html')
    else:
        message = "Invalid OTP"
        return render(request, "Reksha/otp.html", {"message": message})
def userreg(request):
    if request.method=="POST":
        name=request.POST["txtuser"]
        em=request.POST["txtemail"]
        pas=request.POST["txtpass"]
        user= UserProfile(username=name, email=em, password=pas)
        user.save()
    return render(request,"Reksha/login.html")


# def userlog(request):
#     template = loader.get_template('Reksha/new.html')
#     context = {}
#     if request.method == "POST":
#         try:
#             uname = request.POST.get('username')
#             psd = request.POST.get('password')
#             login_obj = UserProfile.objects.filter(username=uname).exists()
#             if login_obj:
#                 user_obj=UserProfile.objects.get(username=uname,password=psd)
#                 request.session['USERNAME'] = user_obj.username
#                 template = loader.get_template('Reksha/userhome.html')
                                               
#             else:
#                 context = {"error": "invalid user"}
#                 HttpResponse(template.render(context, request))
#         except Exception as e:
#             context = {"error": "invalid password"}
#             HttpResponse(template.render(context, request))
#     return HttpResponse(template.render(context, request))
from django.shortcuts import render, redirect
from django.contrib import messages
# from .models import UserProfile

def userlog(request):
    if request.method == "POST":
        uname = request.POST.get('username', '').strip()  # Strip whitespace
        psd = request.POST.get('password', '').strip()   # Strip whitespace

        # Check if fields are empty
        if not uname or not psd:
            messages.error(request, "Both username and password are required.")
            return render(request, 'Reksha/login.html')

        try:
            # Check for valid user
            user_obj = UserProfile.objects.get(username=uname, password=psd)
            request.session['USERNAME'] = user_obj.username
            return redirect('user')  # Replace with the correct URL name
        except UserProfile.DoesNotExist:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'Reksha/login.html')


def logoutuser(request):
    del request.session['USERNAME']
    return render(request, "Reksha/index.html")   



def registration(request):
    if request.method=="POST":
        name=request.POST["txtuser"]
        em=request.POST["txtemail"]
        pas=request.POST["txtpass"]
        user=UserProfile(username=name,email=em,password=pas)
        user.save()
    return render(request,"Reksha/login.html")


def ViewProfile(request):
    prof = UserProfile.objects.get(username=request.session['USERNAME'])
    context = {'userprof': prof}
    
    return render(request, "Reksha/viewprofuser.html",context)

def EditProfile(request):
    prof = UserProfile.objects.get(username=request.session['USERNAME'])
    context = {'userprof': prof}
    
    return render(request, "Reksha/updateprof.html",context)

def UserProfileUpdate(request):
    if request.method == 'POST':
       
        name= request.POST["txtname"]
        username= request.POST["txtuser"]
        mobilenumber= request.POST["txtmobile"]
        email= request.POST["txtemail"]
        address= request.POST["txtaddress"]
        dob= request.POST["txtdob"]
        district= request.POST["txtdis"]
        pin= request.POST["txtpin"]
        relative_contact= request.POST["txtrel"]
        passwd= request.POST["txtpass"]
        gender= request.POST["gender"]

    
        UserProfile.objects.filter(username=request.session['USERNAME']).update(
            name=name,
            username=username,
            mobile_no=mobilenumber,
            email=email,
            address=address,
            dob=dob,
            district=district,
            pincode=pin,
            relative_contact=relative_contact,
            password=passwd,
            gender=gender,
        )
    
        return redirect('user')
    else:
        return redirect('updateprof')


def UserProfUpdate(request):
    if request.method == 'POST':
        passwd= request.POST["txtpass"]
    
        UserProfile.objects.filter(username=request.session['USERNAME']).update(
            password=passwd,

        )
    
        return redirect('login')
    else:
        return redirect('resetpass')
    
def feedtable(request):
    if request.method=="POST":
        username= request.session['USERNAME']
        name=request.POST["txtname"]
        em=request.POST["txtemail"]
        subject=request.POST["txtsub"]
        message=request.POST["txtmes"]
        abc=UserFeedback(Username=username,name=name, email=em, subject=subject,message=message)
        abc.save()
    return render(request,"Reksha/user.html")

def emergency(request):
    if request.method=="POST":
        uname=request.session['USERNAME']
        mobile_no=request.POST["txtmob"]
        situation=request.POST["txtres"]
        message=request.POST["txtmes"]
        location=request.POST["txtloc"]
        abc=Notification(mobile_number=mobile_no, situation=situation, message=message,location=location,username= uname)
        abc.save()
    return render(request,"Reksha/user.html")


def reporttab(request):
    if request.method=="POST":
        subject=request.POST["subject"]
        message=request.POST["message"]
        msg= Reportres(subject=subject, message=message)
        msg.save()
    return redirect('resworks')

def complaintres(request):
    if request.method=="POST":
        name=request.POST["txtname"]
        email=request.POST["txtemail"]
        subject=request.POST["txtsub"]
        message=request.POST["txtmes"]
        msg= Complaintres(name=name, email=email,subject=subject,message=message)
        msg.save()
    return redirect('resworks')


def admin(request):
    template = loader.get_template('Reksha/adminlog.html')
    context = {}
    
    # Hardcoded admin credentials
    admin_username = "reksha"
    admin_password = "reksha@123"
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check hardcoded credentials
        if username == admin_username and password == admin_password:
            request.session['USERNAME'] = username  # Store session for logged-in admin
            template = loader.get_template('Reksha/sidebar.html')
            return HttpResponse(template.render({}, request))
        else:
            context = {"error": "Invalid username or password"}
    
    return HttpResponse(template.render(context, request))
def logoutadmin(request):
    del request.session['USERNAME']
    return render(request, "Reksha/index.html")   

def addstafftab(request):
    if request.method=="POST":
        name=request.POST["txtres"]
        address=request.POST["txtaddess"]
        contact=request.POST["txtnum"]
        district=request.POST["txtdis"]
        city=request.POST["txtcty"]
        pincode=request.POST["pincode"]
        email=request.POST["txtemail"]
        user=request.POST["txtuser"]
        passwd=request.POST["txtpass"]
        msg= Staff(name=name, address=address,contact_number=contact,district=district,email_id=email,username=user,password=passwd,city=city,pincode=pincode)
        msg.save()
    return render(request,"Reksha/sidebar.html")


def assigntable(request):
    if request.method=="POST":
        victimuser=request.POST["txtvic"]
        loc=request.POST["txtloc"]
        mobile=request.POST["txtmob"]
        rescue_team=request.POST["txtres"]
        landmark=request.POST["txtldmk"]
        message=request.POST["txtmes"]
        pincode=request.POST["txtpin"]
        msg= assigntab(location=loc, mobile_number=mobile,rescue_force=rescue_team,message=message,landmark=landmark,pincode=pincode,victimuser=victimuser)
        msg.save()
    return render(request,"Reksha/sidebar.html")


def rescuelog(request):
    template = loader.get_template('Reksha/loginres.html')
    context = {}
    if request.method == "POST":
        try:
            uname = request.POST.get('username')
            psd = request.POST.get('password')
            login_obj = Staff.objects.filter(username=uname).exists()
            if login_obj:
                user_obj=Staff.objects.get(username=uname,password=psd)
                request.session['USERNAME'] = user_obj.username


                # assigned_works = assigntab.objects.filter(
                #     pincode=user_obj.pincode, 
                #     rescue_force=user_obj.name
                # )

                # context = {'assigned_works': assigned_works}

                return redirect('resworks')
                                               
            else:
                context = {"error": "invalid user"}
                HttpResponse(template.render(context, request))
        except Exception as e:
            context = {"error": "invalid password"}
            HttpResponse(template.render(context, request))
    return HttpResponse(template.render(context, request))
def logoutres(request):
    del request.session['USERNAME']
    return render(request, "Reksha/index.html")


def resworks(request):
    if 'USERNAME' in request.session:
        username = request.session['USERNAME']
        user_obj = Staff.objects.get(username=username) 
        assigned_works = assigntab.objects.filter(pincode=user_obj.pincode, rescue_force=user_obj.name)
        context = {'assigned_works': assigned_works}
        return render(request, 'Reksha/rescue.html', context)
    else:
        return redirect('rescuelog') 
    

# def logout(request):
#     del request.session['USERNAME']
#     return render(request, "Reksha/loginres.html")   

def Editopr(request):
    prof = Staff.objects.get(username=request.session['USERNAME'])
    edit = Updateoprres.objects.filter(username=prof)
    context = {'userprof': prof}
    
    return render(request, "Reksha/updateoprres.html",context)

def rescueUpdateopr(request):
    if request.method == 'POST':
        work_id= request.POST["txtid"]       
        username= request.POST["txtnme"]
        location= request.POST["txtloc"]
        messages= request.POST["txtmsg"]
        
        Updateoprres.objects.filter(username=request.session['USERNAME']).update(
            workid=work_id,
            username=username,
            location=location,
            message=messages,
        )
    
        return redirect('resworks')
    else:
        return redirect('updateopr')


def startopres(request, sid):
    start =assigntab.objects.get(id=sid)
    return render(request, "Reksha/startopres.html", {'Works':start})

def updateopr(request,sid):
    upd =Updateoprres.objects.get(id=sid)
    return render(request, "Reksha/updateoprres.html", {'up':upd})



def startopr(request):
    if request.method=="POST":
        workid=request.POST["txtid"]  
        victimname=request.POST["txtvic"]     
        username=request.POST["txtnme"]
        location=request.POST["txtloc"]
        message=request.POST["txtmsg"]
        msg= Updateoprres(username=username,location=location,message=message,workid=workid,victimname=victimname)
        msg.save()
    return redirect('resworks')


def deletestaff(request,sid):
    dlt =Staff.objects.get(id=sid)
    dlt.delete()
    return redirect('viewstf')


def viewstf(request):
    alls=Staff.objects.all()
    return render(request,"Reksha/viewstaff.html",{'Staff':alls})

def viewntf(request):
    msg=Notification.objects.all()
    return render(request,"Reksha/viewnotification.html",{'Notification':msg})

def viewrep(request):
    msg=Reportres.objects.all()
    return render(request,"Reksha/viewreport.html",{'Reportres':msg})


def viewcmpuser(request):
    msg=UserFeedback.objects.all()
    return render(request,"Reksha/viewcmuser.html",{'UserFeedback':msg})


def viewcmpres(request):
    msg=Complaintres.objects.all()
    return render(request,"Reksha/viewcmres.html",{'Complaintres':msg})

def viewnotif(request,sid):
    prof = Notification.objects.get(id=sid)
    context = {'userprof': prof}
    
    return render(request, "Reksha/assignwrk.html",context)


def resop(request):
    if 'USERNAME' in request.session:
        username = request.session['USERNAME']
        user_obj = Staff.objects.get(username=username) 
        update_works = Updateoprres.objects.filter(username=user_obj.username)
        context = {'upwork': update_works}
        return render(request, 'Reksha/operations.html', context)
    else:
        return redirect('updateopr')



def usertrack(request):
    return render(request, "Reksha/usertrack.html")



def trackuser(request):
    if 'USERNAME' in request.session:
        username = request.session['USERNAME']
        user_obj =UserProfile.objects.get(username=username) 
        track = Updateoprres.objects.filter(victimname=user_obj.username)
        context = {'truser': track}
        return render(request, 'Reksha/usertrack.html', context)
    else:
        return redirect('userhome')

def admintr(request):
    msg=Updateoprres.objects.all()
    return render(request,"Reksha/admintrack.html",{'Updateoprres':msg})


def commonfeed(request):
    if request.method=="POST":
        name=request.POST["txtname"]
        em=request.POST["txtemail"]
        subject=request.POST["txtsub"]
        message=request.POST["txtmes"]
        abc=commonFeedback(name=name, email=em, subject=subject,message=message)
        abc.save()
    return render(request,"Reksha/index.html")

def sendreplyu(request,sid):
    rpl = UserFeedback.objects.get(id=sid)
    context = {'rpl': rpl}
    return render(request, "Reksha/sendreplyu.html",context)

def replyusr(request):
    if request.method=="POST":
        name=request.POST["username"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        abc=sendrepuser(username=name,subject=subject,message=message)
        abc.save()
    return render(request,"Reksha/sidebar.html")


def replyres(request):
    if request.method=="POST":
        name=request.POST["username"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        abc=sendrepres(username=name,subject=subject,message=message)
        abc.save()
    return render(request,"Reksha/sidebar.html")

def sendreplyc(request,sid):
    rpl = Complaintres.objects.get(id=sid)
    context = {'rpl': rpl}
    return render(request, "Reksha/sendrepc.html",context)

def sidebar(request):
    return render(request,"Reksha/sidebar.html")


def userreplies(request):
    if 'USERNAME' in request.session:
        username = request.session['USERNAME']
        reply =sendrepuser.objects.filter(username=username)
        context = {'reply': reply}
        return render(request, 'Reksha/viewrepuser.html', context)
    else:
        return redirect('userhome') 


def resreplies(request):
    if 'USERNAME' in request.session:
        username = request.session['USERNAME']
        reply =sendrepres.objects.filter(username=username)
        context = {'reply': reply}
        return render(request, 'Reksha/viewrepres.html', context)
    else:
        return redirect('resworks') 
    

def rescue(request):
    return render(request,"Reksha/rescue.html")

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from .models import Reportres

def download_pdf(request):
    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Create a PDF document
    pdf = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Define Styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title_style.fontSize = 18  # Increase title font size
    title_style.alignment = 1  # Center align title

    # Add Title
    title = Paragraph("Rescue Reports", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))  # Add space below the title

    # Table Header
    data = [["Subject", "Message", "Date & Time"]]  # Header row

    # Fetch data from the database
    reports = Reportres.objects.all()
    for report in reports:
        data.append([
            report.subject[:20],  # Truncate long subjects
            report.message[:50],  # Truncate long messages
            str(report.created_at)
        ])

    # Create Table with adjusted column widths
    table = Table(data, colWidths=[180, 250, 180])  # Increased Date & Time column width

    # Add Style to Table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header Background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header Text Color
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Alternate Row Color
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid lines
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Align text to the middle of each cell
        ('TOPPADDING', (0, 0), (-1, -1), 6),  # Add top padding
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),  # Add bottom padding
    ])

    table.setStyle(style)

    # Add table to the elements list
    elements.append(table)

    # Build the PDF
    pdf.build(elements)

    return response
