from django.shortcuts                   import render
from django.core.paginator              import Paginator
from django.db.models                   import Q
from django.shortcuts                   import render, get_object_or_404, redirect, reverse
from django.http                        import HttpResponseRedirect
from django.contrib.auth.decorators     import login_required
from datetime                           import datetime
from apps.core.roomy_core.models        import *
context = {
    "TITLE": "",
    "viewtype": "transaction"
}


@login_required
def booking_modal(request,pk):
    catalog = RoomCatalog.objects.get(pk=pk)
    property = Property.objects.get(pk=catalog.property_id.pk)
    addons = Fee.objects.filter(
                Q(property_id=property) & Q(fee_type=1))


    if request.method == "POST":
        request.session['form_error'] = False
        try:
            start_date = None
            try:
                start_date = datetime.strptime( request.POST.get('start-date'), '%B %d,%Y').strftime('%Y-%m-%d')
            except Exception as e:
                request.session['form_error'] = True
                request.session['form_error_msg'] = "Date format error"
                return redirect(reverse('room',args=(catalog.pk,)))

            book = Booking.objects.create(
                user_id=request.user,
                catalog_id = catalog,
                start_date = start_date
            )

            addons = request.POST.getlist('addons[]')

            book.save()
        except Exception as e:
            request.session['form_error'] = True
            request.session['form_error_msg'] = str(e)
        return redirect('bookings')
        # return redirect(request.META.get('HTTP_REFERER', 'index'))

    context.update({
        "catalog": catalog,
        "addons": addons,
    })
    if request.user_agent.device.family == "Roomy Native":
        return render(request,"mobile-native/components/property/modal/booking.html",context)
    else:
        return render(request,"web/components/property/modal/booking.html",context)
