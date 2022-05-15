from django.shortcuts import render
import pyqrcode
import png
from pyqrcode import QRCode
from django.http import HttpResponse
from django.shortcuts import render
from . models import epassqr
def index(request) :
    qreq=epassqr()
    qgen=(request.POST.get('qgen','default'))
    epss = QRCode(qgen) 
    epss.png("qr/qgen.png")
    epss_str = epss.png_as_base64_str(scale=5)
    
    qreq.qr_id=qgen
    qreq.qr_img="qr/qgen.png"
    qreq.qr_bit64=epss_str
    qreq.save()
    print(qgen)
    print(epss_str)
    return render (request,'index.html')
# Create your views here.
