from django.db import models
 
# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question


class QuestionSet(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    mark = models.BooleanField(default=False)
    negative_mark = models.IntegerField(20)
    time = models.IntegerField(20)



# class Question(QuesModel):
#     id_question = models.ForeignKey(QuestionSet, related_name='questionset ', on_delete=models.CASCADE)
#     question_text = models.CharField(max_length=100)
#     question_image = models.ImageField(upload_to='templates/')
#     question_order = models.IntegerField(20)
#     question_marks = models.IntegerField(100)

# class QuestionOptions(QuesModel):
#     id_question = models.ForeignKey(Question, related_name="question", on_delete=models.CASCADE)
#     option_text = models.CharField(max_length=100)
#     option_image = models.ImageField()
#     option_order = models.IntegerField(default=1)
#     correct_answer = models.BooleanField(default=False)

