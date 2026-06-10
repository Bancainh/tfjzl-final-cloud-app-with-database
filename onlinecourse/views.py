from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        score = 0
        selected_choices = []
        
        # Quét qua Bài học rồi mới kiểm tra Đáp án của Câu hỏi
        for lesson in course.lesson_set.all():
            for question in lesson.question_set.all():
                selected_choice_id = request.POST.get(f'question_{question.id}')
                if selected_choice_id:
                    choice = Choice.objects.get(pk=selected_choice_id)
                    selected_choices.append(choice)
                    if choice.is_correct:
                        score += question.grade
                    
        submission = Submission.objects.create(score=score)
        submission.choices.set(selected_choices)
        
        return redirect('show_exam_result', course_id=course.id, submission_id=submission.id)
        
    return render(request, 'onlinecourse/exam.html', {'course': course})

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    context = {
        'course': course,
        'submission': submission,
        'score': submission.score,
        'passed': submission.score >= 70 
    }
    return render(request, 'onlinecourse/exam_result.html', context)