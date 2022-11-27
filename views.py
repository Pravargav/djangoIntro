
from django.template import loader
from .models import Student_registration,School
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    latest_student = Student_registration.objects.order_by('-student_date_of_registration')[:2]
    # output = '&'.join([x.student_name for x in latest_student])
    # return HttpResponse(output)

    # template = loader.get_template('register/index.html')
    # context = {'latest_student': latest_student,}
    # return HttpResponse(template.render(context, request))

    context = {'latest_student': latest_student}
    return render(request, 'register/index.html', context)

def detail(request, student_id):
    # return HttpResponse("You're looking at student %s." % student_id)
    x = Student_registration.objects.get(pk=student_id)
    return render(request, 'register/detail.html', {'x': x})

# def results(request, student_id):
#     response = "You're looking at the results of student %s."
#     return HttpResponse(response % student_id)

def results(request, student_id):
    x = Student_registration.objects.get(pk=student_id)
    return render(request, 'register/results.html', {'x': x})

# def vote(request, student_id):
#     return HttpResponse("You're voting on student %s." % student_id)
def vote(request, student_id):
    x= get_object_or_404(Student_registration, pk=student_id)
    try:
        selected = x.school_set.get(pk=request.POST['z'])
    except (KeyError, School.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'register/detail.html', {
            'x': x,
            'error_message': "You didnot select a choice!!",
        })
    else:
        selected.choices += 1
        selected.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('register:results', args=(x.id,)))
