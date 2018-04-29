from django.conf.urls import url

from . import views

app_name = 'office'

urlpatterns = [

    url(r'^officeOfDeanStudents/$', views.officeOfDeanStudents, name='officeOfDeanStudents'),
    url(r'^officeOfPurchaseOfficer/', views.officeOfPurchaseOfficr, name='officeOfPurchaseOfficer'),
    url(r'^officeOfRegistrar/', views.officeOfRegistrar, name='officeOfRegistrar'),
    url(r'^officeOfDeanRSPC/', views.officeOfDeanRSPC, name='officeOfDeanRSPC'),
    url(r'^officeOfDeanPnD/', views.officeOfDeanPnD, name='officeOfDeanPnD'),
    url(r'^officeOfDeanAcademics/$', views.officeOfDeanAcademics, name='officeOfDeanAcademics'),
    url(r'^genericModule/', views.genericModule, name='genericModule'),
    url(r'^officeOfDeanStudents/holding_meeting', views.holdingMeeting, name='holdingMeetings'),
    url(r'^officeOfDeanStudents/meeting_Minutes', views.meetingMinutes, name='meetingMinutes'),
    url(r'^officeOfDeanStudents/hostelRoomAllotment', views.hostelRoomAllotment),
    url(r'^officeOfDeanStudents/budget_approval', views.budgetApproval),
    url(r'^officeOfDeanStudents/budget_rejection', views.budgetRejection),
    url(r'^officeOfDeanAcademics/assistantship', views.assistantship, name='assistantship'),
    url(r'^officeOfDeanAcademics/formsubmit', views.formsubmit, name='formsubmit'),
    url(r'^officeOfDeanAcademics/init_assistantship', views.init_assistantship, name='init_assistantship'),
    url(r'^officeOfDeanAcademics/scholarshipform', views.scholarshipform),
    url(r'^officeOfDeanAcademics/applications', views.applications, name='applications'),
    url(r'^officeOfDeanAcademics/courses', views.courses, name='courses'),
    url(r'^officeOfDeanAcademics/scholarship', views.scholarship, name='scholarship'),
    url(r'^officeOfDeanAcademics/semresults', views.semresults, name='semresults'),
    url(r'^officeOfDeanAcademics/thesis', views.thesis, name='thesis'),

]
