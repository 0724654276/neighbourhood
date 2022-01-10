from django.shortcuts import render

# Create your views here.
class BusinessListView(ListView):
    model = Business
    template_name= 'estate/home.html'
    context_object_name = 'businesses'
    
class BusinessDetailView(DetailView):
    model=Business
class BusinessCreateView(LoginRequiredMixin,CreateView):
    model = Business
    fields=['name','email','business_image','location']
    
    def form_valid(self,form):
        form.instance.business_owner = self.request.user
        return super().form_valid(form)

class BusinessUpdateView(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
    model=Business
    fields = ['name','email','business_image','location']

    def form_valid(self):
        forms.instance.business_owner =self.request.user
        return super().form_valid()

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.business_owner:
            return True
        return False
    
class BusinessDeleteView(LoginRequiredMixin,DeleteView):
    model=Business
    success_url='/'
    
    def test_func(self):
        business=self.get_object()
        
        if self.request.user==business.business_owner:
            return True
        return False

class PostListView(ListView):
    model=Post
    template_name='engine/post_list.html'
    context_object_name='posts'
    ordering='-date_posted'

class PostCreateView(LoginRequiredMixin,CreateView,UserPassesTestMixin):
    model = Post
    fields = ['post']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
    model=Post
    success_url='/'
    
    def test_func(self):
        post = self.get_object()
        
        if self.request.user ==post.author:
            return True
        return False
    
class PostDetailView(DetailView):
    model=Post

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields = ['post']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

    def test_func(self):
        post = self.get_object
        if self.request.user == post.author:
            return True
        return False