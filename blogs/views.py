from django.shortcuts import render

# Create your views here.

def blog_list(request):
    return render(request, 'blog-list.html')



def blog_detail_left(request):
    return render(request, 'blog-details-left-sidebar.html')


def blog_grid_view(request):
    return render(request, 'blog-right-sidebar.html')

