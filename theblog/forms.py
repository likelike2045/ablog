from django import forms
from .models import Category, Post, Category_2

#coding,coding, sports, sports
cats = Category_2.objects.all().values_list('name','name')
cat_list=[]

for item in cats:
	cat_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		category_2 = 'category'
		fields = ['category_2','title','author','body']

		widgets = {
			# 'category':forms.Select(attrs={'class':'form-control'}),
			'category_2':forms.Select(choices = cat_list, attrs={'class':'form-control'}),
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'author':forms.Select(attrs={'class':'form-control'}),
			'body':forms.Textarea(attrs={'class':'form-control'}),
		}



# class UpdateForm(forms.ModelForm):
# 	class Meta:
# 		model = Post
# 		fields = ['category','title','body']

# 		widgets = {
# 			'category':forms.Select(attrs={'class':'form-control'}),
# 			'title':forms.TextInput(attrs={'class':'form-control'}),
# 			'body':forms.Textarea(attrs={'class':'form-control'}),
# 		}