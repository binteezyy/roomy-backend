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
    rooms = RoomCatalog.objects.filter(
            Q(property_id__name__icontains=search)|
            Q(property_id__property_address__icontains=search)
        )#.order_by('product_name')
    # if len(products) == 0 :
    #     message='No results for "' + search + '"'
    message = 'Showing results for "' + search + '"'

    paginator = Paginator(rooms, 12)#pagination
    page = request.GET.get('page')
    rooms = paginator.get_page(page)#pagintation end
    for room in rooms:
        for img in room.img_2d.all():
            print(img)
    print("SEARCH:",search)
    print("PAGE:",page)
    print("ROOM:",rooms)
    context.update({
        "message": message,
        "search": search,
        "rooms": rooms,
    })
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/explore/base.html",context)
    else:
        return render(request,"web/components/explore/base.html",context)

def room_view(request,pk):
    room = RoomCatalog.objects.get(pk=pk)
    room_avail = Room.objects.filter(catalog_id=room).exclude(status=2)
    addons = Fee.objects.filter(Q(fee_type=1) & Q(property_id=room.property_id))
    # request.session['form_error'] = False
    try: booking = Booking.objects.get(catalog_id=room,user_id=request.user)
    except Exception as e:
        booking = None

    if request.method == 'POST' and request.user.is_authenticated and room_avail > 0: #BOOK ONCE
        book = Booking.objects.create(
            user_id=request.user,
            catalog_id = room,
        )
        book.save()
    else:
        pass
    context.update({
        "room":room,
        "booking":booking,
        "available": room_avail,
        "addons": addons
    })
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/property/room.html", context)
    else:
        return render(request,"web/components/property/room.html", context)
