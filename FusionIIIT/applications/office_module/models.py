# imports
import datetime

from django.db import models
from django.utils.translation import gettext as _
from applications.globals.models import ExtraInfo

#assistantship tables,results
from applications.academic_information.models import Student, Instructor, Spi, Grades, Course
#scholarship
from applications.scholarships.models import *
from applications.academic_procedures.models import Thesis
from applications.file_tracking.models import *



class Constants:

    APPROVAL_TYPE = (
        ('APPROVED', 'Approved'),
        ('PENDING', 'Pending'),
    )

    HALL_NO = (
        ('HALL-1','hall-1'),
        ('HALL-3','hall-3'),
        ('HALL-4','hall-4'),
    )



class DeanS_approve_committes(models.Model):
    id = models.AutoField(primary_key=True)
    convener=models.ForeignKey(ExtraInfo, on_delete=models.CASCADE ,related_name='convener')
    faculty_incharge=models.ForeignKey(ExtraInfo, on_delete=models.CASCADE ,related_name='facultyincharge')
    date_approved=models.DateField(null=True, blank=True)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.convener + '-' + self.dateofapproval

class hostel_guestroom_approval(models.Model):
    id = models.AutoField(primary_key=True)
    intender=models.ForeignKey(ExtraInfo, on_delete=models.CASCADE)
    hall_no=models.CharField(max_length=5, choices=Constants.HALL_NO ,default='')
    arrival_date=models.DateField(_("Date"), default=datetime.date.today)
    departure_date=models.DateField(null=True, blank=True)
    status=models.CharField(max_length=20, choices=Constants.APPROVAL_TYPE ,default='Pending')

    def __str__(self):
        return self.hall_no + '-' + self.status


class hostel_allotment(models.Model):
    id = models.AutoField(primary_key=True)
    hall_no=models.CharField(max_length=5, choices=Constants.HALL_NO ,default='')
    allotment_file=models.FileField(upload_to='uploads/')
    description=models.CharField(max_length=200)
    
    def __str__(self):
        return '{} - {}'.format(self.hall_no, self.allotment_file)


class Assistantship(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/',blank=True,null=True)
    action = models.IntegerField(default=0)
    comments = models.CharField(null=True,blank=True,max_length=150);
    class Meta:
        db_table = 'Assistantship'
        unique_together = ('student_id','instructor_id')
    def __str__(self):
        return '{} - {}'.format(self.student_id, self.instructor_id)


class Dean_acad_application(models.Model):
    application_id = models.AutoField(primary_key=True)
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)
