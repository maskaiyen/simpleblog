from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        all_post = Post.objects.all()
        post_without_image = Post.objects.filter(header_image='') # filter without image
        post_with_image = Post.objects.exclude(header_image='')
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        if len(all_post) > 0:
            context['latest_post'] = all_post.order_by('-created_at')[0]
        context['post_with_image'] = post_with_image.order_by('-created_at')[:3]  # add object with image and limit the num # not support nagtive interge
        context['post_without_image'] = post_without_image.order_by('-created_at')[:3] # add object without image and limit the num
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'content')

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'content', 'file', 'location']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    # form_class = CategoryForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title', 'content')

def CategoryListView(request):
    category_list = Category.objects.all()
    return render(request, 'category_list.html', {'category_list': category_list,})

def CategoryView(request, cats):
    # templates |slugify???????????????'-', ??????views ?????? coding-tutorial,
    # templates |slugify???????????????'%', ??????views ?????? coding%tutorial, ????????????replace
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    cat_menu = Category.objects.all() # pass cat_menu to templates
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts, 'cat_menu': cat_menu})

    # class Meta:
    #     ordering = ['-created_at']
#
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user) # Post model # request ??????????????????
        liked = True
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))