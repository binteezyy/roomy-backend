from django.shortcuts                               import render
from django.core.paginator                          import Paginator
from django.db.models                               import Q
from apps.core.roomy_core.models import *
context = {
    "TITLE": "Explore",
    "viewtype": "explore"
}

def index(request):
    search = request.GET.get('search')

    if search is None:
        search=""
    rooms = Room.objects.filter(
            Q(property_id__name__icontains=search)|
            Q(property_id__property_address__icontains=search)
        )#.order_by('product_name')
    # if len(products) == 0 :
    #     message='No results for "' + search + '"'
    message = 'Results for "' + search + '"'

    paginator = Paginator(rooms, 12)#pagination
    page = request.GET.get('page')
    rooms = paginator.get_page(page)#pagintation end
    for room in rooms:
        for img in room.image_2d.all():
            print(img)
    print("SEARCH:",search)
    print("PAGE:",page)
    print("ROOM:",rooms)
    context.update({
        "message": message,
        "search": search,
        "rooms": rooms,
    })
    return render(request,"components/landing/explore/base.html",context)

def room_view(request,pk):
    room = Room.objects.get(pk=pk)
    print(room)
    return render(request,"components/property/room.html", context)
