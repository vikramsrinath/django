from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from school.models import Student
from django.http import HttpResponse, HttpResponseForbidden
from django.template import RequestContext

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']

def student_list(request, template_name='school/student_list.html'):
    students = Student.objects.all()
    data = {}
    data['object_list'] = students
    return render(request, template_name, data)

def student_create(request, template_name='school/student_form.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, template_name, {'form':form})

def student_update(request, pk, template_name='school/student_form.html'):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, template_name, {'form':form})

def student_delete(request, pk, template_name='school/student_confirm_delete.html'):
    student = get_object_or_404(Student, pk=pk)    
    if request.method=='POST':
        student.delete()
        return redirect('student_list')
    return render(request, template_name, {'object':student})

def student_show_more(request):
    response_data = {}
    response_data['result'] = 'Load successful!'
    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json",
            context_instance=RequestContext(request)
        )
