from django.shortcuts import render

# Create your views here.

def product_list(request):
    return render(request, 'shop-list.html')



def product_detail(request):
    return render(request, 'single-product.html')



def wishlists(request):
    return render(request, 'wishlist.html')


# def sale(request):
#     return render(request, 'single-product-sale.html')