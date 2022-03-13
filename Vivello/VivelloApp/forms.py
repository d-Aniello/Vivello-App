from django import forms
from VivelloApp.models import Farm, Field, Task


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 px-5 bg-[#FCFDFE] "
                                                    "text-base text-body-color placeholder-[#ACB6BE] outline-none "
                                                    "focus-visible:shadow-none focus:border-primary transition"}),
            'address': forms.TextInput(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 px-5 "
                                                       "bg-[#FCFDFE] text-base text-body-color placeholder-[#ACB6BE] "
                                                       "outline-none focus-visible:shadow-none focus:border-primary "
                                                       "transition"}),
            'employee': forms.CheckboxSelectMultiple(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 "
                                                                     "px-5 bg-[#FCFDFE] text-base text-body-color "
                                                                     "placeholder-[#ACB6BE] outline-none "
                                                                     "focus-visible:shadow-none focus:border-primary "
                                                                     "transition"}),
            'vehicle': forms.CheckboxSelectMultiple(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 "
                                                                    "px-5 bg-[#FCFDFE] text-base text-body-color "
                                                                    "placeholder-[#ACB6BE] outline-none "
                                                                    "focus-visible:shadow-none focus:border-primary "
                                                                    "transition"}),
            'machine': forms.CheckboxSelectMultiple(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 "
                                                                    "px-5 bg-[#FCFDFE] text-base text-body-color "
                                                                    "placeholder-[#ACB6BE] outline-none "
                                                                    "focus-visible:shadow-none focus:border-primary "
                                                                    "transition"}),
        }


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 px-5 bg-[#FCFDFE] "
                                                    "text-base text-body-color placeholder-[#ACB6BE] outline-none "
                                                    "focus-visible:shadow-none focus:border-primary transition"}),
            'area': forms.NumberInput(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 px-5 "
                                                      "bg-[#FCFDFE] text-base text-body-color placeholder-[#ACB6BE] "
                                                      "outline-none focus-visible:shadow-none focus:border-primary "
                                                      "transition"}),
            'location': forms.TextInput(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 px-5 "
                                                        "bg-[#FCFDFE] text-base text-body-color placeholder-[#ACB6BE] "
                                                        "outline-none focus-visible:shadow-none focus:border-primary "
                                                        "transition"}),
            'farm': forms.Select(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 "
                                                 "px-5 bg-[#FCFDFE] text-base text-body-color "
                                                 "placeholder-[#ACB6BE] outline-none "
                                                 "focus-visible:shadow-none focus:border-primary "
                                                 "transition"}),
            'crop': forms.CheckboxSelectMultiple(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 "
                                                                 "px-5 bg-[#FCFDFE] text-base text-body-color "
                                                                 "placeholder-[#ACB6BE] outline-none "
                                                                 "focus-visible:shadow-none focus:border-primary "
                                                                 "transition"}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 px-5 bg-[#FCFDFE] "
                                                    "text-base text-body-color placeholder-[#ACB6BE] outline-none "
                                                    "focus-visible:shadow-none focus:border-primary transition"}),
            'description': forms.Textarea(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 px-5 "
                                                          "bg-[#FCFDFE] text-base text-body-color placeholder-[#ACB6BE]"
                                                          "outline-none focus-visible:shadow-none focus:border-primary "
                                                          "transition"}),
            'date': forms.SelectDateWidget(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 px-5 bg-[#FCFDFE] "
                                                    "text-base text-body-color placeholder-[#ACB6BE] outline-none "
                                                    "focus-visible:shadow-none focus:border-primary transition"}),
            'user': forms.CheckboxSelectMultiple(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 "
                                                                 "px-5 bg-[#FCFDFE] text-base text-body-color "
                                                                 "placeholder-[#ACB6BE] outline-none "
                                                                 "focus-visible:shadow-none focus:border-primary "
                                                                 "transition"}),
            'vehicle': forms.CheckboxSelectMultiple(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 "
                                                                    "px-5 bg-[#FCFDFE] text-base text-body-color "
                                                                    "placeholder-[#ACB6BE] outline-none "
                                                                    "focus-visible:shadow-none focus:border-primary "
                                                                    "transition"}),
            'machine': forms.CheckboxSelectMultiple(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 "
                                                                    "px-5 bg-[#FCFDFE] text-base text-body-color "
                                                                    "placeholder-[#ACB6BE] outline-none "
                                                                    "focus-visible:shadow-none focus:border-primary "
                                                                    "transition"}),
            'field': forms.CheckboxSelectMultiple(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 "
                                                                  "px-5 bg-[#FCFDFE] text-base text-body-color "
                                                                  "placeholder-[#ACB6BE] outline-none "
                                                                  "focus-visible:shadow-none focus:border-primary "
                                                                  "transition"}),
            'crop': forms.CheckboxSelectMultiple(attrs={'class': "w-full rounded-md border bordder-[#E9EDF4] py-3 "
                                                                 "px-5 bg-[#FCFDFE] text-base text-body-color "
                                                                 "placeholder-[#ACB6BE] outline-none "
                                                                 "focus-visible:shadow-none focus:border-primary "
                                                                 "transition"}),
        }
