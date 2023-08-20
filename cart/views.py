from django.shortcuts import render

# Create your views here.

def shop_page(request):
    return render(request, 'shop-list.html')


# def cart_page(request):
#     return render(request, 'cart.html')


def shop_cart_page(request):
    return render(request, 'shopping-cart.html')



def checkout_page(request):
    return render(request, 'checkout.html')


def compare_page(request):
    return render(request, 'compare.html')



# def shop_left_sidebar_page(request):
#     return render(request, 'shop-left-sidebar.html')