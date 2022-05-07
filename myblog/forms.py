from django import forms
from .models import Post, Category
from ckeditor.widgets import CKEditorWidget
#
# # choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]
choices = Category.objects.all().values_list('name', 'name') # maybe just use query set
choice_list = [item for item in choices]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'content', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'},),
            # 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}), # review add_post.html <script>
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            # 'header_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            # 'content': forms.Textarea(attrs={'class': CKEditorWidget}),

        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            # 'header_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }