from django.shortcuts import render

context = {
    "TITLE": "Roomy — Explore",
    "viewtype": "explore"
}

def index(request):
    search = request.GET.get('search')
    print(search)
    if search is None:
        search=""
    # products = Product.objects.filter(
    #     Q(product_name__icontains=search)|Q(brand__brand_name__icontains=search)|Q(category__category__icontains=search)).filter(brand__is_available=True).order_by('product_name')
    # if len(products) == 0 :
    #     message='No results for "' + search + '"'
    message = 'Results for "' + search + '"'

    context.update({
        "message": message,
        "search": search,
    })
    return render(request,"components/landing/explore/base.html",context)
