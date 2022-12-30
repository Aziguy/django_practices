from django import forms

from blog.models import BlogPost

JOBS = (
    ('Développeur Python', 'Développeur Python'),
    ('Développeur Js', 'Développeur Js'),
    ('Développeur C#', 'Développeur C#'),
)


class SignUpForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=True, strip=True)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6)
    job = forms.ChoiceField(widget=forms.SelectMultiple(), choices=JOBS)
    cgp_accept = forms.BooleanField(initial=True)

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        not_contains_value = ['*', '$', '#', '!']
        for value in not_contains_value:
            if value in pseudo:
                raise forms.ValidationError(f"Pseudo can't contain {value} sign!")


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            # 'category',
            'title',
            'date',
            'description',
        ]

        labels = {
            'title': 'Titre',
        }
        widgets ={
            'date':forms.SelectDateWidget(years=range(1990, 2081))
        }
