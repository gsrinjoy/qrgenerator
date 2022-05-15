from django.shortcuts import render
from itsdangerous import base64_decode
import pyqrcode
import png
from datetime import datetime 
from pyqrcode import QRCode
from django.http import HttpResponse  , JsonResponse  
from django.shortcuts import render
from  gen.models import epassqr
import base64
API_KEY = "2T7LAffHqWgZNx6BcRaNMkEq827eK9xr"
def index(request) :
    qreq=epassqr()
    qgen=(request.POST.get('qgen','default'))
    img_path=""
    mydict={}
    if(qgen != "default"):
        epss = QRCode(qgen) 
        epss.png("1.png")
        epss_str = epss.png_as_base64_str(scale=5)
        img_path = "media/gen/qr_data/QR" + str(datetime.now().strftime("%Y%m%d%H%M%S")) + ".png"
        fh = open(img_path, "wb")
        fh.write(base64.b64decode(epss_str)) #epss_str.decode('base64')
        qreq.qr_img=img_path
        qreq.qr_id=qgen
        qreq.qr_bit64=epss_str
        fh.close()
        qreq.save()
        print(qgen)
        print(epss_str)
        
        mydict['img_path']=img_path
        return render (request,'qr.html',mydict)
    return render (request,'index.html')

def display(request):
    reqd=list(epassqr.objects.values('qr_id','qr_bit64'))
    params={'qr':reqd}
    return  JsonResponse(params)
# Create your views here.
