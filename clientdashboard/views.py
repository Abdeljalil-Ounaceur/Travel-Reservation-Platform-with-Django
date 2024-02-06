from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from pages.models import Reservation
from pages.decorators import  require_client
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

@require_client
def accuile_page(request) :
    reservations = Reservation.objects.filter(utilisateur=request.user).reverse()
    for reservation in reservations :
        reservation.status = reservation.offre.date_debut > reservation.date

    return render(request,'clientdashboard/client.html',{'reservations':reservations})

@require_client
def settings_page(request) :
    return render(request,'clientdashboard/settings.html')

@require_client
def contactus_page(request) :
    return render(request,'clientdashboard/contactus.html')


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None




#Opens up page as PDF
def ViewPDF(request):
        data = {
            "company": "Dennnis Ivanov Company",
            "address": "123 Street name",
            "city": "Vancouver",
            "state": "WA",
            "zipcode": "98663",


            "phone": "555-555-2345",
            "email": "youremail@dennisivy.com",
            "website": "dennisivy.com",
            }
        pdf = render_to_pdf('pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
