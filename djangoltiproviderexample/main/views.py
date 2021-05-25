from django.views.generic.base import TemplateView
from lti_provider.mixins import LTIAuthMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'main/index.html'


# class LTIAssignment1View(LTIAuthMixin, LoginRequiredMixin, TemplateView):
#
#     template_name = 'main/assignment.html'
#
#     def get_context_data(self, **kwargs):
#         return {
#             'is_student': self.lti.lis_result_sourcedid(self.request),
#             'course_title': self.lti.course_title(self.request),
#             'number': 1
#         }
#
#
class LTIAssignment2View(LTIAuthMixin, LoginRequiredMixin, TemplateView):

    template_name = 'main/assignment.html'

    def get_context_data(self, **kwargs):
        return {
            'is_student': self.lti.lis_result_sourcedid(self.request),
            'course_title': self.lti.course_title(self.request),
            'number': 2
        }


class LTIAssignment1View(TemplateView):

    template_name = 'main/assignment.html'


class LTIAssignmentx2View(LTIAuthMixin, TemplateView):

    template_name = 'main/assignment.html'



from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt


@method_decorator(xframe_options_exempt, name='dispatch')
class LTIFailAuthorizationX(TemplateView):
    template_name = 'main/index.html'


from django.views import generic
from django.shortcuts import render

class T1(generic.View):

    def get(self, request, *args, **kwargs):

        return render(request, 'main/index.html', {})

    def post(self, request, *args, **kwargs):
        return render(request, 'main/index.html', {})
