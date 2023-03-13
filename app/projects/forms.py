from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        # model = Project  ## create a form based on this model can also make this a string "Project"
        model = Project
        fields = "__all__"  # include all fields in the form, or specify which fields to include
