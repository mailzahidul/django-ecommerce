from django.shortcuts import render
from .forms import BlogCreteForm
from .models import BlogCrete, BlogCategories
# Create your views here.

def blog_page(request):
    return render(request, 'blog/blogs.html')

def blog_create(request):
    forms = BlogCreteForm()
    author = ""
    login_user= request.user.username
    categories = BlogCategories.objects.all()
    if request.method == 'POST':
        forms = BlogCreteForm(request.POST, request.FILES)
        if forms.is_valid():
            author=forms.cleaned_data['author']
            title = forms.cleaned_data['title']
            category = forms.cleaned_data['category']
            content = forms.cleaned_data['content']
            feature_img = forms.cleaned_data['feature_img']
            print(author, title, category,content, feature_img)
            BlogCrete.objects.create(
                author=author,title=title, content=content, feature_img=feature_img
            )
        else:
            print("empty")
    context={
        'forms':forms,
        'username':login_user,
        'categories':categories,
    }
    return render(request, 'blog/blog_create.html', context)