from django.urls import re_path,include
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [re_path(r'^$', views.index, name='index'),
               re_path(r'^login/$', views.login, name='login'),
               re_path(r'^regi/$', views.regi, name='regi'),
               re_path(r'^signup/$', views.signup, name='signup'),
               re_path('Email_Verification/', views.Email_Verification.as_view(), name='Email_Verification'),
               re_path(r'^generateOTP/$', views.generateOTP, name='generateOTP'),
               re_path(r'^send_OTP/$', views.send_OTP, name='send_OTP'),
               re_path(r'^Verifyotp/$', views.Verifyotp, name='Verifyotp'),
               re_path(r'^complaint/$', views.complaint, name='complaint'),
               re_path(r'^feed/$', views.feed, name='feed'),
               re_path(r'^loginres/$', views.loginres, name='loginres'),
               re_path(r'^profile/$', views.profile, name='profile'),
               re_path(r'^regires/$', views.regires, name='regires'),
               re_path(r'^reportres/$', views.reportres, name='reportres'),
               re_path(r'^updateopr/(\d+)$', views.updateopr, name='updateopr'),
               re_path(r'^updateprof/$', views.updateprof, name='updateprof'),
               re_path(r'^index/$', views.index, name='index'),
               re_path(r'^addstaff/$', views.addstaff, name='addstaff'),
               re_path(r'^userhome/$', views.userhome, name='userhome'),
               re_path(r'^usernav/$', views.usernav, name='usernav'),
               re_path(r'^assignwrk/$', views.assignwrk, name='assignwrk'),
               re_path(r'^viewprofuser/$', views.viewprofuser, name='viewprofuser'),
               re_path(r'^userreg/$', views.userreg, name='userreg'),
               re_path(r'^userlog/$', views.userlog, name='userlog'),
               re_path(r'^logoutuser/$', views.logoutuser, name='logoutuser'),
               re_path(r'^registration/$', views.registration, name='registration'),
               re_path(r'^ViewProfile/$', views.ViewProfile, name='ViewProfile'),
               re_path(r'^UserProfileUpdate/$', views.UserProfileUpdate, name='UserProfileUpdate'),
               re_path(r'^EditProfile/$', views.EditProfile, name='EditProfile'),
               re_path(r'^feedtable/$', views.feedtable, name='feedtable'),
               re_path(r'^emergency/$', views.emergency, name='emergency'),
               re_path(r'^rescuenav/$', views.rescuenav, name='rescuenav'),
               re_path(r'^startopres/(\d+)$', views.startopres, name='startopres'),
               re_path(r'^reporttab/$', views.reporttab, name='reporttab'),
               re_path(r'^complaintres/$', views.complaintres, name='complaintres'),
               re_path(r'^adminlog/$', views.adminlog, name='adminlog'),
               re_path(r'^admin/$', views.admin, name='admin'),
               re_path(r'^adminnav/$', views.adminnav, name='adminnav'),
               re_path(r'^addstafftab/$', views.addstafftab, name='addstafftab'),
               re_path(r'^assigntable/$', views.assigntable, name='assigntable'),
               re_path(r'^rescuelog/$', views.rescuelog, name='rescuelog'),
               re_path(r'^Editopr/$', views.Editopr, name='Editopr'),
               re_path(r'^rescueUpdateopr/$', views.rescueUpdateopr, name='rescueUpdateopr'),
               re_path(r'^startopr/$', views.startopr, name='startopr'),
               re_path(r'^viewstaff/$', views.viewstaff, name='viewstaff'),
               re_path(r'^viewstf/$', views.viewstf, name='viewstf'),
               re_path(r'^deletestaff/(\d+)$', views.deletestaff, name='deletestaff'),
               re_path(r'^viewnotification/$', views.viewnotification, name='viewnotification'),
               re_path(r'^viewntf/$', views.viewntf, name='viewntf'),
               re_path(r'^viewreport/$', views.viewreport, name='viewreport'),
               re_path(r'^viewrep/$', views.viewrep, name='viewrep'),
               re_path(r'^viewcmuser/$', views.viewcmuser, name='viewcmuser'),
               re_path(r'^viewcmpuser/$', views.viewcmpuser, name='viewcmpuser'),
               re_path(r'^viewcmres/$', views.viewcmres, name='viewcmres'),
               re_path(r'^viewcmpres/$', views.viewcmpres, name='viewcmpres'),
               re_path(r'^viewnotif/(\d+)$', views.viewnotif, name='viewnotif'),
               re_path(r'^resworks/$', views.resworks, name='resworks'),
               re_path(r'^operations/$', views.operations, name='operations'),
               re_path(r'^resop/$', views.resop, name='resop'),
               re_path(r'^usertrack/$', views.usertrack, name='usertrack'),
               re_path(r'^trackuser/$', views.trackuser, name='trackuser'),
               re_path(r'^admintr/$', views.admintr, name='admintr'),
               re_path(r'^logoutres/$', views.logoutres, name='logoutres'),
               re_path(r'^logoutadmin/$', views.logoutadmin, name='logoutadmin'),
               re_path(r'^commonfeed/$', views.commonfeed, name='commonfeed'),
               re_path(r'^new/$', views.new, name='new'),
               re_path(r'^UserProfUpdate/$', views.UserProfUpdate, name='UserProfUpdate'),
               re_path(r'^fpass/$', views.fpass, name='fpass'),
               re_path(r'^verify_otp/$', views.verify_otp, name='verify_otp'),
               re_path(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
               re_path(r'^reset_password/$', views.reset_password, name='reset_password'),
               re_path(r'^sendreplyu/(\d+)$', views.sendreplyu, name='sendreplyu'),
               re_path(r'^replyusr/$', views.replyusr, name='replyusr'),
                re_path(r'^replyres/$', views.replyres, name='replyres'),
               re_path(r'^sidebar/$', views.sidebar, name='sidebar'),
               re_path(r'^resetp/$', views.resetp, name='resetp'),
                re_path(r'^sendreplyc/(\d+)$', views.sendreplyc, name='sendreplyc'),
               re_path(r'^userreplies/$', views.userreplies, name='userreplies'),
               re_path(r'^resreplies/$', views.resreplies, name='resreplies'),
               re_path(r'^rescue/$', views.rescue, name='rescue'),
               re_path(r'^user/$', views.user, name='user'),
               re_path(r'^download_pdf/$', views.download_pdf, name='download_pdf'),



               
















                
]
