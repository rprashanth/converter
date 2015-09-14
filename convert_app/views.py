from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#function to res mass line 7-53
#functions to res energy line 56-104

w=0




def conv(n4):
    x=n4 * 1000
    return x

def convgtokg(n4):
    x=n4/1000
    return x

def convkgtop(y):
    x=2.2046226218*y
    return x

def convkgtomg(n4):
    x=n4*1000000
    return x

def convkgtomt(n4):
    x=n4*0.001
    return x

def convkgtooun(n4):
    x=n4*35.273961949
    return x

def convkgtost(n4):
    x=n4*0.1574730444
    return x

def convptokg(n4):
    x=n4/2.2046226218
    return x

def convmttokg(n4):
    x=n4/0.001
    return x

def convotokg(n4):
    x=n4/35.273961949
    return x

def convstokg(n4):
    x=n4/0.1574730444
    return x

def convmtokg(n4):
    x=n4/1000000
    return x
#---------------------------------------------------------------------------
    #######to convert energy

def convjtocal(n4):
    x=n4 * 0.2388458966
    return x

def convjtokcal(n4):
    x=n4 * 0.0002388458966
    return x

def convjtokj(y):
    x=n4 *0.001
    return x

def convjtohp(n4):
    x=n4*0.0000003725
    return x

def convjtokwh(n4):
    x=n4*0.0000002777
    return x

def convctojou(n4):
    y=n4*4.1868
    return y

def convkctojou(n4):
    y=n4*4186.8
    return y

def convevtojou(n4):
    y=n4/((6.25)*(10**18))
    return y

def convkjtoj(n4):
    y=n4*1000
    return y

def convhptojou(n4):
    y=n4*2684519.5392
    return y

def convkwhtojou(n4):
    y=n4*3600000
    return y

def convjtoev(n4):
    x=n4*((6.25)*(10**18))
    return x
#----------------------------------------------------------------

#### convert areas

def convsqcmtom(n4):
    x=n4*0.0001
    return x

def convsqcmtoin(n4):
    x=n4*0.15500031
    return x

def convsqcmtoft(n4):
    x=n4*0.001076391
    return x

def convsqcmtoy(n4):
    x=n4*0.000119599
    return x

def convsqcmtomm(n4):
    x=n4*100
    return x

def convsqcmtokm(n4):
    x=n4*0.0000000001
    return x

def convsqcmtoacre(n4):
    x=n4*0.0000000247
    return x

def convsqcmtohectare(n4):
    x=n4*0.00000001
    return x

def convsqmtocm(n4):
    x=n4/0.0001
    return x

def convsqintocm(n4):
    x=n4/0.15500031
    return x

def convsqmmtocm(n4):
    x=n4/100
    return x

def convsqkmtocm(n4):
    x=n4/0.0000000001
    return x

def convsqfttocm(n4):
    x=n4/0.001076391
    return x

def convsqactocm(n4):
    x=n4/0.0000000247
    return x

def convsqhectocm(n4):
    x=n4/0.00000001
    return x

#-----------------------------------------------------------------------
#to convert length
def convmtomm(n4):
    x=n4 * 1000
    return x

def convmmtom(n4):
    x=n4 *0.001
    return x

def convcmtom(n4):
    x=n4 *0.01
    return x

def convkmtom(n4):
    x=n4 *1000
    return x

def convintom(n4):
    x=n4 *0.0254
    return x

def convmtocm(n4):
    x=n4 * 100
    return x

def convmtokm(n4):
    x=n4 *0.001
    return x

def convmtoin(n4):
    x=n4*39.37007874
    return x

def convfetom(n4):
    x=n4*0.3048
    return x

def convmtofe(n4):
    x=n4*3.280839895
    return x

def convyatom(n4):
    x=n4*0.9144
    return x

def convmitom(n4):
    x=n4*1609.344
    return x

def convnmitom(n4):
    x=n4*1852
    return x

def convmtoya(n4):
    x=n4*1.0936132983
    return x

def convmtomi(n4):
    x=n4*0.0006213711
    return x

def convmtonmi(n4):
    x=n4*0.0005399568
    return x

#----------------------------------------------------------------------
#to convert pressure
def convatmtobar(n4):
    x=n4*1.01325
    return x

def convatmtopas(n4):
    x=n4*101325
    return x

def convatmtommhg(n4):
    x=n4*760
    return x

def convbartoatm(n4):
    x=n4/1.01325
    return x

def convpastoatm(n4):
    x=n4/101325
    return x

def conmmhgtoatm(n4):
    x=n4/760
    return x
#----------------------------------------------------------------------
#to convert temperature
def convceltofah(n4):
    x=((n4*(9/5))+32)
    return x

def convceltokel(n4):
    x=n4+273.15
    return x

def convfahtocel(n4):
    x=((n4-32)*(9/5))
    return x

def convkeltocel(n4):
    x=n4-273.15
    return x
#----------------------------------------------------------------------
###to convert volume
def convcumtolit(n4):
    x=n4*1000
    return x

def convcumtocumm(n4):
    x=n4*1000000000
    return x

def convcumtocuf(n4):
    x=n4*35.314724827
    return x

def convcumtogals(n4):
    x=n4*264.17205235
    return x

def convcumtogalk(n4):
    x=n4*219.96915733
    return x

def convcumtopin(n4):
    x=n4*1759.7539863
    return x

def convcumtodry(n4):
    x=n4*1816.1675232
    return x

def convcumtoliq(n4):
    x=n4*2113.3606661
    return x

def convcumtoliqo(n4):
    x=n4*33818.058843
    return x

def convcumtoflu(n4):
    x=n4*35198.873636
    return x

def convcumtobarrel(n4):
    x=n4*6.2898109653
    return x


def convlittocum(n4):
    x=n4/1000
    return x

def convcummtocum(n4):
    x=n4/1000000000
    return x

def convcuftocum(n4):
    x=n4/35.314724827
    return x

def convgalktocum(n4):
    x=n4/219.96915733
    return x
def convgalstocum(n4):
    x=n4/264.17205235
    return x

def convpintocum(n4):
    x=n4/1759.7539863
    return x

def convdrytocum(n4):
    x=n4/1816.1675232
    return x

def convliqtocum(n4):
    x=n4/2113.3606661
    return x

def convliqotocum(n4):
    x=n4/33818.058843
    return x

def convflutocum(n4):
    x=n4/35198.873636
    return x

def convbarreltocum(n4):
    x=n4/6.2898109653
    return x

#----------------------------------------------------------------------
##function to convert time
def convsectomin(n4):
    x=n4*(1/60)
    return x

def convmintosec(n4):
    x=n4*60
    return x

def conmintohr(n4):
    x=n4*(1/60)
    return x

def convmintody(n4):
    x=n4*(1/(24*60))
    return x

def convmintowk(n4):
    x=n4*0.0000992063
    return x

def convhrtomin(n4):
    x=n4*60
    return x
def convdytomin(n4):
    x=n4*1440
    return x

def convwktomin(n4):
    x=n4*10080
    return x
#----------------------------------------------------------------------
def start(request):
    return render(request,'pr3/convert1.html')

def convert1(request):
    global w
    w=request.POST['n1']
    if w=='length':
        w1=1
        return render(request,'pr3/res.html',{'w1':w1})
    if w=='area':
        w2=1
        return render(request,'pr3/res.html',{'w2':w2})
    if w=='weight':
        w3=1
        return render(request,'pr3/res.html',{'w3':w3})
    if w=='pressure':
        w4=1
        return render(request,'pr3/res.html',{'w4':w4})
    if w=='temperature':
        w5=1
        return render(request,'pr3/res.html',{'w5':w5})
    if w=='power':
        w6=1
        return render(request,'pr3/res.html',{'w6':w6})
    if w=='time':
        w7=1
        return render(request,'pr3/res.html',{'w7':w7})
    if w=='volume':
        w8=1
        return render(request,'pr3/res.html',{'w8':w8})

def convert(request):
    global w
    n2=request.POST['n2']
    n3=request.POST['n3']
    n4=request.POST['n4']
    if w =='weight':
        if n2 == n3:
            x=conv(float(n4))
            return render(request,'pr3/res.html',{'x3':n4})
        if n2 =='kilogram' and n3 == 'gram' :
            x=conv(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 =='gram'  and n3 == 'kilogram':
            x=convgtokg(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 =='gram' and n3 == 'pound':
            y=convgtokg(float(n4))
            x=convkgtop(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'kilogram' and n3 == 'pound':
            x=convkgtop(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'kilogram' and n3 == 'milligram':
            x=convkgtomg(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'kilogram' and n3 == 'metrictons':
            x=convkgtomt(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'kilogram' and n3 == 'ounce':
            x=convkgtooun(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'kilogram' and n3 == 'stones':
            x=convkgtost(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'gram' and n3 == 'metrictons':
            y=convgtokg(float(n4))
            x=convkgtomt(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'gram' and n3 == 'pound':
            y=convgtokg(float(n4))
            x=convkgtop(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'gram' and n3 == 'ounce':
            y=convgtokg(float(n4))
            x=convkgtooun(y)
            return render(request,'pr3/res.html',{'x3':x})

        if n2 == 'gram' and n3 == 'milligram':
            y=convgtokg(float(n4))
            x=convkgtomg(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'pound' and n3 == 'metrictons':
            y=convptokg(float(n4))
            x=convkgtomt(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'pound' and n3 == 'kilogram':
            x=convptokg(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'pound' and n3 == 'ounce':
            y=convptokg(float(n4))
            x=convkgtooun(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'pound' and n3 == 'stones':
            y=convptokg(float(n4))
            x=convkgtost(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'pound' and n3 == 'gram':
            y=convptokg(float(n4))
            x=convkgtog(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'pound' and n3 == 'milligram':
            y=convptokg(float(n4))
            x=convkgtomg(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'metrictons' and n3 == 'gram':
            y=convmttokg(float(n4))
            x=conv(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'metrictons' and n3 == 'kilogram':
            x=convmttokg(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'metrictons' and n3 == 'ounce':
            y=convmttokg(float(n4))
            x=convkgtooun(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'metrictons' and n3 == 'stones':
            y=convmttokg(float(n4))
            x=convkgtost(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'metrictones' and n3 == 'pound':
            y=convmttokg(float(n4))
            x=convkgtog(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'metrictons' and n3 == 'milligram':
            y=convmttokg(float(n4))
            x=convkgtomg(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'ounce' and n3 == 'gram':
            y=convotokg(float(n4))
            x=conv(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'ounce' and n3 == 'kilogram':
            x=convotokg(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'ounce' and n3 == 'pound':
            y=convotokg(float(n4))
            x=convkgtop(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'ounce' and n3 == 'stones':
            y=convotokg(float(n4))
            x=convkgtost(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'ounce' and n3 == 'metrictons':
            y=convotokg(float(n4))
            x=convkgtomt(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'ounce' and n3 == 'milligram':
            y=convotokg(float(n4))
            x=convkgtomg(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'stones' and n3 == 'gram':
            y=convsokg(float(n4))
            x=conv(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'stones' and n3 == 'kilogram':
            x=convstokg(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'stones' and n3 == 'pound':
            y=convstokg(float(n4))
            x=convkgtop(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'stones' and n3 == 'ounce':
            y=convstokg(float(n4))
            x=convkgtost(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'stones' and n3 == 'metrictons':
            y=convstokg(float(n4))
            x=convkgtomt(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'stones' and n3 == 'milligram':
            y=convstokg(float(n4))
            x=convkgtomg(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'milligram' and n3 == 'gram':
            y=convmsokg(float(n4))
            x=conv(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'milligram' and n3 == 'kilogram':
            x=convmtokg(float(n4))
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'milligram' and n3 == 'pound':
            y=convmtokg(float(n4))
            x=convkgtop(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'milligram' and n3 == 'ounce':
            y=convmtokg(float(n4))
            x=convkgtost(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'milligram' and n3 == 'metrictons':
            y=convmtokg(float(n4))
            x=convkgtomt(y)
            return render(request,'pr3/res.html',{'x3':x})
        if n2 == 'milligram' and n3 == 'stones':
            y=convmtokg(float(n4))
            x=convkgtomg(y)
            return render(request,'pr3/res.html',{'x3':x})
        #----------------------------------------------------------
     # to convert energy
    if w=='power':
        if n2 == n3:
            x=conv(float(n4))
            return render(request,'pr3/res.html',{'x4':n4})
        if n2 =='joules' and n3 == 'calories' :
            x=convjtocal(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 =='joules'  and n3 == 'kilo calories':
            x=convjtokcal(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 =='joules' and n3 == 'kilo joules':
            x=convjtokj(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'joules' and n3 == 'horse power':
            x=convjtohp(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'joules' and n3 == 'kilo watt hour':
            x=convjtokwh(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'joules' and n3 == 'electron volt':
            x=convjtoev(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'calories' and n3 == 'kilo calories':
            y=convctojou(float(n4))
            x=convjtokcal(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'calories' and n3 == 'joules':
            x=convctojou(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'calories' and n3 == 'kilo joules':
            y=convctoj(float(n4))
            x=convjtokj(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'calories' and n3 == 'horse power':
            y=convctoj(float(n4))
            x=convjtohp(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'calories' and n3 == 'kilo watt hour':
            y=convctoj(float(n4))
            x=convjtokwh(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'calories' and n3 == 'electron volt':
            y=convctoj(float(n4))
            x=convjtoev(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo calories' and n3 == 'calories':
            y=convkctojou(float(n4))
            x=convjtocal(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo calories' and n3 == 'joules':
            x=convkctojou(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo calories' and n3 == 'kilo joules':
            y=convkctojou(float(n4))
            x=convjtokj(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo calories' and n3 == 'horse power':
            y=convkctojou(float(n4))
            x=convjtohp(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo calories' and n3 == 'kilo watt hour':
            y=convkctojou(float(n4))
            x=convjtokwh(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo calories' and n3 == 'electron volt':
            y=convkctojou(float(n4))
            x=convjtoev(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo joules' and n3 == 'calories':
            y=convkjtoj(float(n4))
            x=convjtocal(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo joules' and n3 == 'joules':
            x=convkjtoj(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo joules' and n3 == 'kilo calories':
            y=convkjtoj(float(n4))
            x=convjtokcal(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo joules' and n3 == 'horse power':
            y=convkjtoj(float(n4))
            x=convjtohp(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo joules' and n3 == 'kilo watt hour':
            y=convkjtoj(float(n4))
            x=convjtokwh(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo joules' and n3 == 'electron volt':
            y=convkjtoj(float(n4))
            x=convjtoev(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'horse power' and n3 == 'calories':
            y=convhptojou(float(n4))
            x=convjtocal(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'horse power' and n3 == 'joules':
            x=convhptojou(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'horse power' and n3 == 'kilo joules':
            y=convhptojou(float(n4))
            x=convjtokj(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'horse power' and n3 == 'kilo calories':
            y=convhptojou(float(n4))
            x=convjtokcal(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'horse power' and n3 == 'kilo watt hour':
            y=convhptojou(float(n4))
            x=convjtokwh(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'horse power' and n3 == 'electron volt':
            y=convhptojou(float(n4))
            x=convjtoev(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo watt hour' and n3 == 'calories':
            y=convkwhtojou(float(n4))
            x=convjtocal(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo watt hour' and n3 == 'joules':
            x=convkwhtojou(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo watt hour' and n3 == 'kilo joules':
            y=convkwhtojou(float(n4))
            x=convjtokj(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo watt hour' and n3 == 'kilo calories':
            y=convkwhtojou(float(n4))
            x=convjtokcal(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo watt hour' and n3 == 'horse power':
            y=convkwhtojou(float(n4))
            x=convjtohp(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'kilo watt hour' and n3 == 'electron volt':
            y=convkwhtojou(float(n4))
            x=convjtoev(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'electron volt' and n3 == 'calories':
            y=convevtojou(float(n4))
            x=convjtocal(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'electron volt' and n3 == 'joules':
            x=convevtojou(float(n4))
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'electron volt' and n3 == 'kilo joules':
            y=convevtojou(float(n4))
            x=convjtokj(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'electron volt' and n3 == 'kilo calories':
            y=convevtojou(float(n4))
            x=convjtokcal(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'electron volt' and n3 == 'horse power':
            y=convevtojou(float(n4))
            x=convjtohp(y)
            return render(request,'pr3/res.html',{'x4':x})
        if n2 == 'electron volt' and n3 == 'kilo watt hour':
            y=convevtojou(float(n4))
            x=convjtokwh(y)
            return render(request,'pr3/res.html',{'x4':x})
        #-------------------------------------------------------------------
        ##to convert areas
    if w=='area':
        if n2 == n3:
            x=conv(float(n4))
            return render(request,'pr3/res.html',{'x1':n4})
        if n2 =='square cm' and n3 == 'square m':
            x=convsqcmtom(float(n4))
            return render(request,'pr3/res.html',{'x1':x})
        if n2 =='square cm' and n3 == 'square inch':
            x=convsqcmtoin(float(n4))
            return render(request,'pr3/res.html',{'x1':x})
        if n2 =='square cm' and n3 == 'square feet':
            x=convsqcmtoft(float(n4))
            return render(request,'pr3/res.html',{'x1':x})
        if n2 =='square cm' and n3 == 'square yard':
            x=convsqcmtoy(float(n4))
            return render(request,'pr3/res.html',{'x1':x})
        if n2 =='square cm' and n3 == 'square mm':
            x=convsqcmtommm(float(n4))
            return render(request,'pr3/res.html',{'x1':x})
        if n2 =='square cm' and n3 == 'square km':
            x=convsqcmtokm(float(n4))
            return render(request,'pr3/res.html',{'x1':x})
        if n2 =='square cm' and n3 == 'acre':
            x=convsqcmtoacre(float(n4))
            return render(request,'pr3/res.html',{'x1':x})
        if n2 =='square cm' and n3 == 'hectare':
            x=convsqcmtohectare(float(n4))
            return render(request,'pr3/res.html',{'x1':x})
        if n2 =='square m' and n3 == 'square cm':
            x=convsqmtocm(float(n4))
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square m' and n3 == 'square inch':
            y=convsqmtocm(float(n4))
            x=convsqcmtoin(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square m' and n3 == 'square feet':
            y=convsqmtocm(float(n4))
            x=convsqcmtoft(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square m' and n3 == 'square yard':
            y=convsqmtocm(float(n4))
            x=convsqcmtoy(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square m' and n3 == 'square mm':
            y=convsqmtocm(float(n4))
            x=convsqcmtomm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square m' and n3 == 'square km':
            y=convsqmtocm(float(n4))
            x=convsqcmtokm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square m' and n3 == 'acre':
            y=convsqmtocm(float(n4))
            x=convsqcmtoacre(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square m' and n3 == 'hectare':
            y=convsqmtocm(float(n4))
            x=convsqcmtohectare(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})

        if n2 =='square inch' and n3 == 'square cm':
            x=convsqintocm(float(n4))
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square inch' and n3 == 'square mm':
            y=convsqintocm(float(n4))
            x=convsqcmtomm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square inch' and n3 == 'square yard':
            y=convsqintocm(float(n4))
            x=convsqcmtoy(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square inch' and n3 == 'square km':
            y=convsqintocm(float(n4))
            x=convsqcmtokm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square inch' and n3 == 'square feet':
            y=convsqintocm(float(n4))
            x=convsqcmtoft(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square inch' and n3 == 'acre':
            y=convsqintocm(float(n4))
            x=convsqcmtoacre(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square inch' and n3 == 'hectare':
            y=convsqintocm(float(n4))
            x=convsqcmtohectare(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square inch' and n3 == 'square m':
            y=convsqintocm(float(n4))
            x=convsqcmtom(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})

        if n2 =='square mm' and n3 == 'square cm':
            x=convsqmmtocm(float(n4))
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square mm' and n3 == 'square m':
            y=convsqmmtocm(float(n4))
            x=convsqcmtom(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square mm' and n3 == 'square yard':
            y=convsqmmtocm(float(n4))
            x=convsqcmtoy(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square mm' and n3 == 'square feet':
            y=convsqmmtocm(float(n4))
            x=convsqcmtoft(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square mm' and n3 == 'square inch':
            y=convsqmmtocm(float(n4))
            x=convsqcmtoin(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square mm' and n3 == 'acre':
            y=convsqmmtocm(float(n4))
            x=convsqcmtoacre(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square mm' and n3 == 'hectare':
            y=convsqmmtocm(float(n4))
            x=convsqcmtohectare(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square mm' and n3 == 'square km':
            y=convsqmmtocm(float(n4))
            x=convsqcmtokm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        
        if n2 =='square km' and n3 == 'square cm':
            x=convsqkmtocm(float(n4))
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square km' and n3 == 'square m':
            y=convsqkmtocm(float(n4))
            x=convsqcmtom(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square km' and n3 == 'square yard':
            y=convsqkmtocm(float(n4))
            x=convsqcmtoy(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square km' and n3 == 'square feet':
            y=convsqkmtocm(float(n4))
            x=convsqcmtoft(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square km' and n3 == 'square inch':
            y=convsqkmtocm(float(n4))
            x=convsqcmtoin(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square km' and n3 == 'acre':
            y=convsqkmtocm(float(n4))
            x=convsqcmtoacre(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square km' and n3 == 'hectare':
            y=convsqkmtocm(float(n4))
            x=convsqcmtohectare(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square km' and n3 == 'square mm':
            y=convsqkmtocm(float(n4))
            x=convsqcmtomm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})

        if n2 =='square yard' and n3 == 'square cm':
            x=convsqytocm(float(n4))
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square yard' and n3 == 'square m':
            y=convsqytocm(float(n4))
            x=convsqcmtom(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square yard' and n3 == 'square mm':
            y=convsqytocm(float(n4))
            x=convsqcmtomm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square yard' and n3 == 'square feet':
            y=convsqytocm(float(n4))
            x=convsqcmtoft(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square yard' and n3 == 'square inch':
            y=convsqytocm(float(n4))
            x=convsqcmtoin(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square yard' and n3 == 'acre':
            y=convsqytocm(float(n4))
            x=convsqcmtoacre(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square yard' and n3 == 'hectare':
            y=convsqytocm(float(n4))
            x=convsqcmtohectare(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square yard' and n3 == 'square km':
            y=convsqytocm(float(n4))
            x=convsqcmtokm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})

        if n2 =='square feet' and n3 == 'square cm':
            x=convsqfttocm(float(n4))
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square feet' and n3 == 'square m':
            y=convsqfttocm(float(n4))
            x=convsqcmtom(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square feet' and n3 == 'square yard':
            y=convsqfttocm(float(n4))
            x=convsqcmtoy(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square feet' and n3 == 'square mm':
            y=convsqfttocm(float(n4))
            x=convsqcmtomm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square feet' and n3 == 'square inch':
            y=convsqfttocm(float(n4))
            x=convsqcmtoin(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square feet' and n3 == 'acre':
            y=convsqfttocm(float(n4))
            x=convsqcmtoacre(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square feet' and n3 == 'hectare':
            y=convsqfttocm(float(n4))
            x=convsqcmtohectare(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='square feet' and n3 == 'square km':
            y=convsqfttocm(float(n4))
            x=convsqcmtokm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})

        if n2 =='acre' and n3 == 'square cm':
            x=convsqactocm(float(n4))
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='acre' and n3 == 'square m':
            y=convsqactocm(float(n4))
            x=convsqcmtom(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='acre' and n3 == 'square yard':
            y=convsqactocm(float(n4))
            x=convsqcmtoy(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='acre' and n3 == 'square mm':
            y=convsqactocm(float(n4))
            x=convsqcmtomm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='acre' and n3 == 'square inch':
            y=convsqactocm(float(n4))
            x=convsqcmtoin(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='acre' and n3 == 'square feet':
            y=convsqactocm(float(n4))
            x=convsqcmtoft(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='acre' and n3 == 'hectare':
            y=convsqactocm(float(n4))
            x=convsqcmtohectare(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='acre' and n3 == 'square km':
            y=convsqactocm(float(n4))
            x=convsqcmtokm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})

        if n2 =='hectare' and n3 == 'square cm':
            x=convsqhectocm(float(n4))
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='hectare' and n3 == 'square m':
            y=convsqhectocm(float(n4))
            x=convsqcmtom(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='hectare' and n3 == 'square yard':
            y=convsqhectocm(float(n4))
            x=convsqcmtoy(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='hectare' and n3 == 'square mm':
            y=convsqhectocm(float(n4))
            x=convsqcmtomm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='hectare' and n3 == 'square inch':
            y=convsqhectocm(float(n4))
            x=convsqcmtoin(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='hectare' and n3 == 'square feet':
            y=convsqhectocm(float(n4))
            x=convsqcmtoft(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='hectare' and n3 == 'acre':
            y=convsqhectocm(float(n4))
            x=convsqcmtoacre(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
        if n2 =='hectare' and n3 == 'square km':
            y=convsqhectocm(float(n4))
            x=convsqcmtokm(y)
            return render(request,'pr3/res.html',{'x1':x,'w':w})
#----------------------------------------------------------------------
        ##to convert length
    if w=='length':
        if n2 == n3:
            return render(request,'pr3/res.html',{'x':n4})
        if n2 =='metres' and n3 == 'millimetres' :
            x=convmtomm(float(n4))
            return render(request,'pr3/res.html',{'x':x,'w':w})
        if n2 =='metres'  and n3 == 'centimetres':
            x=convmtocm(float(n4))
            return render(request,'pr3/res.html',{'x':x})
        if n2 =='metres' and n3 == 'kilometres':
            x=convmtokm(float(n4))
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'metres' and n3 == 'inches':
            x=convmtoin(float(n4))
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'metres' and n3 == 'feet':
            x=convmtofe(float(n4))
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'metres' and n3 == 'yards':
            x=convmtoya(float(n4))
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'metres' and n3 == 'miles':
            x=convmtomi(float(n4))
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'metres' and n3 == 'nautical miles':
            x=convmtonmi(float(n4))
            return render(request,'pr3/res.html',{'x':x})
      
        if n2 =='millimetres' and n3 == 'metres' :
            x=convmtomm(float(n4))
            return render(request,'pr3/res.html',{'x':x,'w':w})
        if n2 =='millimetres'  and n3 == 'centimetres':
            y=convmmtom(float(n4))
            x=convmtocm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 =='millimetres' and n3 == 'kilometres':
            y=convmmtom(float(n4))
            x=convmtokm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'millimetres' and n3 == 'inches':
            y=convmmtom(float(n4))
            x=convmtoin(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'millimetres' and n3 == 'feet':
            y=convmmtom(float(n4))
            x=convmtofe(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'millimetres' and n3 == 'yards':
            y=convmmtom(float(n4))
            x=convmtoya(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'millimetres' and n3 == 'miles':
            y=convmmtom(float(n4))
            x=convmtomi(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'millimetres' and n3 == 'nautical miles':
            y=convmmtom(float(n4))
            x=convmtonmi(y)
            return render(request,'pr3/res.html',{'x':x})

        if n2 =='centimetres' and n3 == 'metres' :
            x=convcmtom(float(n4))
            return render(request,'pr3/res.html',{'x':x,'w':w})
        if n2 =='centimetres'  and n3 == 'millimetres':
            y=convcmtom(float(n4))
            x=convmtomm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 =='centimetres' and n3 == 'kilometres':
            y=convcmtom(float(n4))
            x=convmtokm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'centimetres' and n3 == 'inches':
            y=convcmtom(float(n4))
            x=convmtoin(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'centimetres' and n3 == 'feet':
            y=convcmtom(float(n4))
            x=convmtofe(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'centimetres' and n3 == 'yards':
            y=convcmtom(float(n4))
            x=convmtoya(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'centimetres' and n3 == 'miles':
            y=convcmtom(float(n4))
            x=convmtomi(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'centimetres' and n3 == 'nautical miles':
            y=convcmtom(float(n4))
            x=convmtonmi(y)
            return render(request,'pr3/res.html',{'x':x})

        if n2 =='kilometres' and n3 == 'metres' :
            x=convkmtom(float(n4))
            return render(request,'pr3/res.html',{'x':x,'w':w})
        if n2 =='kilometres'  and n3 == 'millimetres':
            y=convkmtom(float(n4))
            x=convmtomm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 =='kilometres' and n3 == 'centimetres':
            y=convkmtom(float(n4))
            x=convmtocm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'kilometres' and n3 == 'inches':
            y=convkmtom(float(n4))
            x=convmtoin(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'kilometres' and n3 == 'feet':
            y=convkmtom(float(n4))
            x=convmtofe(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'kilometres' and n3 == 'yards':
            y=convkmtom(float(n4))
            x=convmtoya(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'kilometres' and n3 == 'miles':
            y=convkmtom(float(n4))
            x=convmtomi(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'kilometres' and n3 == 'nautical miles':
            y=convkmtom(float(n4))
            x=convmtonmi(y)
            return render(request,'pr3/res.html',{'x':x})

        if n2 =='inches' and n3 == 'metres' :
            x=convintom(float(n4))
            return render(request,'pr3/res.html',{'x':x,'w':w})
        if n2 =='inches'  and n3 == 'millimetres':
            y=convintom(float(n4))
            x=convmtomm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 =='inches' and n3 == 'centimetres':
            y=convintom(float(n4))
            x=convmtocm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'inches' and n3 == 'kilometres':
            y=convintom(float(n4))
            x=convmtokm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'inches' and n3 == 'feet':
            y=convintom(float(n4))
            x=convmtofe(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'inches' and n3 == 'yards':
            y=convintom(float(n4))
            x=convmtoya(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'inches' and n3 == 'miles':
            y=convintom(float(n4))
            x=convmtomi(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'inches' and n3 == 'nautical miles':
            y=convintom(float(n4))
            x=convmtonmi(y)
            return render(request,'pr3/res.html',{'x':x})

        if n2 =='feet' and n3 == 'metres' :
            x=convfetom(float(n4))
            return render(request,'pr3/res.html',{'x':x,'w':w})
        if n2 =='feet'  and n3 == 'millimetres':
            y=convfetom(float(n4))
            x=convmtomm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 =='feet' and n3 == 'centimetres':
            y=convfetom(float(n4))
            x=convmtocm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'feet' and n3 == 'kilometres':
            y=convfetom(float(n4))
            x=convmtokm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'feet' and n3 == 'inches':
            y=convfetom(float(n4))
            x=convmtoin(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'feet' and n3 == 'yards':
            y=convfetom(float(n4))
            x=convmtoya(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'feet' and n3 == 'miles':
            y=convfetom(float(n4))
            x=convmtomi(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'feet' and n3 == 'nautical miles':
            y=convfetom(float(n4))
            x=convmtonmi(y)
            return render(request,'pr3/res.html',{'x':x})

        if n2 =='yards' and n3 == 'metres' :
            x=convyatom(float(n4))
            return render(request,'pr3/res.html',{'x':x,'w':w})
        if n2 =='yards'  and n3 == 'millimetres':
            y=convyatom(float(n4))
            x=convmtomm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 =='yards' and n3 == 'centimetres':
            y=convyatom(float(n4))
            x=convmtocm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'yards' and n3 == 'kilometres':
            y=convyatom(float(n4))
            x=convmtokm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'yards' and n3 == 'inches':
            y=convyatom(float(n4))
            x=convmtoin(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'yards' and n3 == 'feet':
            y=convyatom(float(n4))
            x=convmtofe(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'yards' and n3 == 'miles':
            y=convyatom(float(n4))
            x=convmtomi(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'yards' and n3 == 'nautical miles':
            y=convyatom(float(n4))
            x=convmtonmi(y)
            return render(request,'pr3/res.html',{'x':x})

        if n2 =='miles' and n3 == 'metres' :
            x=convmitom(float(n4))
            return render(request,'pr3/res.html',{'x':x,'w':w})
        if n2 =='miles'  and n3 == 'millimetres':
            y=convmitom(float(n4))
            x=convmtomm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 =='miles' and n3 == 'centimetres':
            y=convmitom(float(n4))
            x=convmtocm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'miles' and n3 == 'kilometres':
            y=convmitom(float(n4))
            x=convmtokm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'miles' and n3 == 'inches':
            y=convmitom(float(n4))
            x=convmtoin(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'miles' and n3 == 'feet':
            y=convmitom(float(n4))
            x=convmtofe(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'miles' and n3 == 'yards':
            y=convmitom(float(n4))
            x=convmtoya(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'miles' and n3 == 'nautical miles':
            y=convmitom(float(n4))
            x=convmtonmi(y)
            return render(request,'pr3/res.html',{'x':x})

        if n2 =='nautical miles' and n3 == 'metres' :
            x=convnmitom(float(n4))
            return render(request,'pr3/res.html',{'x':x,'w':w})
        if n2 =='nautical miles'  and n3 == 'millimetres':
            y=convnmitom(float(n4))
            x=convmtomm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 =='nautical miles' and n3 == 'centimetres':
            y=convnmitom(float(n4))
            x=convmtocm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'nautical miles' and n3 == 'kilometres':
            y=convnmitom(float(n4))
            x=convmtokm(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'nautical miles' and n3 == 'inches':
            y=convnmitom(float(n4))
            x=convmtoin(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'nautical miles' and n3 == 'feet':
            y=convnmitom(float(n4))
            x=convmtofe(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'nautical miles' and n3 == 'yards':
            y=convnmitom(float(n4))
            x=convmtoya(y)
            return render(request,'pr3/res.html',{'x':x})
        if n2 == 'nautical miles' and n3 == 'miles':
            y=convnmitom(float(n4))
            x=convmtomi(y)
            return render(request,'pr3/res.html',{'x':x})
#--------------------------------------------------------------------------
        ##to convert presure
    if w == 'pressure':
        if n2 == n3:
            x=conv(float(n4))
            return render(request,'pr3/res.html',{'x5':n4})
        if n2 =='atmosphere' and n3 == 'bars' :
            x=convatmtobar(float(n4))
            return render(request,'pr3/res.html',{'x5':x})
        if n2 == 'atmosphere' and n3 == 'pascals':
            x=convatmtopas(float(n4))
            return render(request,'pr3/res.html',{'x5':x})
        if n2 == 'atmosphere' and n3 == 'mm hg':
            x=convatmtommhg(float(n4))
            return render(request,'pr3/res.html',{'x5':x})

        if n2 =='pascals' and n3 == 'atmosphere':
            x=convpastoatm(float(n4))
            return render(request,'pr3/res.html',{'x5':x}) 
        if n2 =='pascals' and n3 == 'mm hg':
            y=convpastoatm(float(n4))
            x=convatmtommhg(y)
            return render(request,'pr3/res.html',{'x5':x})
        if n2 =='pascals' and n3 == 'bars':
            y=convpastoatm(float(n4))
            x=convatmtobar(y)
            return render(request,'pr3/res.html',{'x5':x})

        if n2 =='bars' and n3 == 'atmosphere':
            x=convbartoatm(float(n4))
            return render(request,'pr3/res.html',{'x5':x}) 
        if n2 =='bars' and n3 == 'mm hg':
            y=convbartoatm(float(n4))
            x=convatmtommhg(y)
            return render(request,'pr3/res.html',{'x5':x})
        if n2 =='bars' and n3 == 'pascals':
            y=convbartoatm(float(n4))
            x=convatmtopas(y)
            return render(request,'pr3/res.html',{'x5':x})

        if n2 =='mm hg' and n3 == 'atmosphere':
            x=convmmhgtoatm(float(n4))
            return render(request,'pr3/res.html',{'x5':x}) 
        if n2 =='mm hg' and n3 == 'bars':
            y=convmmhgtoatm(float(n4))
            x=convatmtommhg(y)
            return render(request,'pr3/res.html',{'x5':x})
        if n2 =='mm hg' and n3 == 'pascals':
            y=convmmhgtoatm(float(n4))
            x=convatmtopas(y)
            return render(request,'pr3/res.html',{'x5':x})

 #---------------------------------------------------------------------------       

    if w=='temperature':
        if n2 =='celsius' and n3 == 'fahrenheit' :
            x=convceltofah(float(n4))
            return render(request,'pr3/res.html',{'x6':x,'w':w})
        if n2 =='celsius'  and n3 == 'kelvin':
            x=convceltokel(float(n4))
            return render(request,'pr3/res.html',{'x6':x})
                  
        if n2 =='fahrenheit' and n3 == 'celsius' :
            x=convfahtocel(float(n4))
            return render(request,'pr3/res.html',{'x6':x,'w':w})
        if n2 =='fahrenheit'  and n3 == 'kelvin':
            y=convfahtocel(float(n4))
            x=convceltokel(y)
            return render(request,'pr3/res.html',{'x6':x})
       
        if n2 =='kelvin' and n3 == 'celsius' :
            x=convkeltocel(float(n4))
            return render(request,'pr3/res.html',{'x6':x,'w':w})
        if n2 =='kelvin'  and n3 == 'fahrenheit':
            y=convkeltocel(float(n4))
            x=convceltofah(y)
            return render(request,'pr3/res.html',{'x6':x})
 #--------------------------------------------------------------------------
    if w=='volume':
        if n2 == n3:
            x=conv(float(n4))
            return render(request,'pr3/res.html',{'x7':n4})
        if n2 =='cubic meters' and n3 == 'litres' :
            x=convcumtolit(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 =='cubic meters'  and n3 == 'cubic mm':
            x=convcumtocumm(float(n4))
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='cubic meters' and n3 == 'cubic feet':
            x=convcumtocuf(float(n4))
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic meters' and n3 == 'gallons us':
            x=convcumtogals(float(n4))
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic meters' and n3 == 'gallons uk':
            x=convcumtogalk(float(n4))
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic meters' and n3 == 'pints uk':
            x=convcumtopin(float(n4))
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic meters' and n3 == 'dry pt us':
            x=convcumtodry(float(n4))
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic meters' and n3 == 'liquid pt us':
            x=convcumtoliq(float(n4))
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic meters' and n3 == 'liquid oz us':
            x=convcumtoliqo(float(n4))
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic meters' and n3 == 'fluid oz uk':
            x=convcumtoflu(float(n4))
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic meters' and n3 == 'barrels us':
            x=convcumtobarrel(float(n4))
            return render(request,'pr3/res.html',{'x7':x})

        if n2 =='litres' and n3 == 'cubic meters' :
            x=convlittocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 =='litres'  and n3 == 'cubic mm':
            y=convlittocum(float(n4))
            x=convcumtocumm(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='litres' and n3 == 'cubic feet':
            y=convlittocum(float(n4))
            x=convcumtocuf(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'litres' and n3 == 'gallons us':
            y=convlittocum(float(n4))
            x=convcumtogals(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'litres' and n3 == 'gallons uk':
            y=convlittocum(float(n4))
            x=convcumtogalk(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'litres' and n3 == 'pints uk':
            y=convlittocum(float(n4))
            x=convcumtopin(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'litres' and n3 == 'dry pt us':
            y=convlittocum(float(n4))
            x=convcumtodry(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'litres' and n3 == 'liquid pt us':
            y=convlittocum(float(n4))
            x=convcumtoliq(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'litres' and n3 == 'liquid oz us':
            y=convlittocum(float(n4))
            x=convcumtoliqo(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'litres' and n3 == 'fluid oz uk':
            y=convlittocum(float(n4))
            x=convcumtoflu(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'litres' and n3 == 'barrels us':
            y=convlittocum(float(n4))
            x=convcumtobarrel(y) 
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='cubic mm' and n3 == 'cubic meters' :
            x=convcummtocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 =='cubic mm'  and n3 == 'litres':
            y=convcummtocum(float(n4))
            x=convcumtolit(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='cubic mm' and n3 == 'cubic feet':
            y=convcummtocum(float(n4))
            x=convcumtocuf(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic mm' and n3 == 'gallons us':
            y=convcummtocum(float(n4))
            x=convcumtogals(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic mm' and n3 == 'gallons uk':
            y=convcummtocum(float(n4))
            x=convcumtogalk(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic mm' and n3 == 'pints uk':
            y=convcummtocum(float(n4))
            x=convcumtopin(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic mm' and n3 == 'dry pt us':
            y=convcummtocum(float(n4))
            x=convcumtodry(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic mm' and n3 == 'liquid pt us':
            y=convcummtocum(float(n4))
            x=convcumtoliq(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic mm' and n3 == 'liquid oz us':
            y=convcummtocum(float(n4))
            x=convcumtoliqo(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic mm' and n3 == 'fluid oz uk':
            y=convcummtocum(float(n4))
            x=convcumtoflu(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic mm ' and n3 == 'barrels us':
            y=cconvcummtocum(float(n4))
            x=convcumtobarrel(y) 
            return render(request,'pr3/res.html',{'x7':x})

        if n2 =='cubic feet' and n3 == 'cubic meters' :
            x=convcuftocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 =='cubic feet'  and n3 == 'litres':
            y=convcuftocum(float(n4))
            x=convcumtolit(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='cubic feet' and n3 == 'cubic mm':
            y=convcuftocum(float(n4))
            x=convcumtocumm(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic feet' and n3 == 'gallons us':
            y=convcuftocum(float(n4))
            x=convcumtogals(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic feet' and n3 == 'gallons uk':
            y=convcuftocum(float(n4))
            x=convcumtogalk(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic feet' and n3 == 'pints uk':
            y=convcuftocum(float(n4))
            x=convcumtopin(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic feet' and n3 == 'dry pt us':
            y=convcuftocum(float(n4))
            x=convcumtodry(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic feet' and n3 == 'liquid pt us':
            y=convcuftocum(float(n4))
            x=convcumtoliq(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic feet' and n3 == 'liquid oz us':
            y=convcuftocum(float(n4))
            x=convcumtoliqo(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic feet' and n3 == 'fluid oz uk':
            y=convcuftocum(float(n4))
            x=convcumtoflu(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'cubic feet' and n3 == 'barrels us':
            y=convcuftocum(float(n4))
            x=convcumtobarrel(y) 
            return render(request,'pr3/res.html',{'x7':x})

        if n2 =='gallons us' and n3 == 'cubic meters' :
            x=convgalstocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 =='gallons us'  and n3 == 'litres':
            y=convgalstocum(float(n4))
            x=convcumtolit(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='gallons us' and n3 == 'cubic mm':
            y=convgalstocum(float(n4))
            x=convcumtocumm(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons us' and n3 == 'cubic feet':
            y=convgalstocum(float(n4))
            x=convcumtocuf(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons us' and n3 == 'gallons uk':
            y=convgalstocum(float(n4))
            x=convcumtogalk(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons us' and n3 == 'pints uk':
            y=convgalstocum(float(n4))
            x=convcumtopin(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons us' and n3 == 'dry pt us':
            y=convgalstocum(float(n4))
            x=convcumtodry(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons us' and n3 == 'liquid pt us':
            y=convgalstocum(float(n4))
            x=convcumtoliq(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons us' and n3 == 'liquid oz us':
            y=convgalstocum(float(n4))
            x=convcumtoliqo(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons us' and n3 == 'fluid oz uk':
            y=convgalstocum(float(n4))
            x=convcumtoflu(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons us' and n3 == 'barrels us':
            y=convgalstocum(float(n4))
            x=convcumtobarrel(y) 
            return render(request,'pr3/res.html',{'x7':x})

        if n2 =='gallons uk' and n3 == 'cubic meters' :
            x=convgalktocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 =='gallons uk'  and n3 == 'litres':
            y=convgalktocum(float(n4))
            x=convcumtolit(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='gallons uk' and n3 == 'cubic mm':
            y=convgalktocum(float(n4))
            x=convcumtocumm(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons uk' and n3 == 'cubic feet':
            y=convgalktocum(float(n4))
            x=convcumtocuf(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons uk' and n3 == 'gallons us':
            y=convgalktocum(float(n4))
            x=convcumtogals(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons uk' and n3 == 'pints uk':
            y=convgalktocum(float(n4))
            x=convcumtopin(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons uk' and n3 == 'dry pt us':
            y=convgalktocum(float(n4))
            x=convcumtodry(float(n4))
            return render(request,'pr3/res.html',{'x7':x,})
        if n2 == 'gallons uk' and n3 == 'liquid pt us':
            y=convgalktocum(float(n4))
            x=convcumtoliq(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons uk' and n3 == 'liquid oz us':
            y=convgalktocum(float(n4))
            x=convcumtoliqo(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons uk' and n3 == 'fluid oz uk':
            y=convgalktocum(float(n4))
            x=convcumtoflu(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'gallons uk' and n3 == 'barrels us':
            y=convgalktocum(float(n4))
            x=convcumtobarrel(y) 
            return render(request,'pr3/res.html',{'x7':x})

        if n2 =='pints uk' and n3 == 'cubic meters' :
            x=convpintocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 == 'pints uk'  and n3 == 'litres':
            y=convgalstocum(float(n4))
            x=convcumtolit(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='pints uk' and n3 == 'cubic mm':
            y=convpintocum(float(n4))
            x=convcumtocumm(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'pints uk' and n3 == 'cubic feet':
            y=convpintocum(float(n4))
            x=convcumtocuf(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'pints uk' and n3 == 'gallons uk':
            y=convpintocum(float(n4))
            x=convcumtogalk(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'pints uk' and n3 == 'gallon us':
            y=convpintocum(float(n4))
            x=convcumtogals(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'pints uk' and n3 == 'dry pt us':
            y=convpintocum(float(n4))
            x=convcumtodry(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'pints uk' and n3 == 'liquid pt us':
            y=convpintocum(float(n4))
            x=convcumtoliq(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'pints uk' and n3 == 'liquid oz us':
            y=convpintocum(float(n4))
            x=convcumtoliqo(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'pints uk' and n3 == 'fluid oz uk':
            y=convpintocum(float(n4))
            x=convcumtoflu(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'pints uk' and n3 == 'barrels us':
            y=convpintocum(float(n4))
            x=convcumtobarrel(y) 
            return render(request,'pr3/res.html',{'x7':x})

        if n2 =='dry pt us' and n3 == 'cubic meters' :
            x=convdrytocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 == 'dry pt us'  and n3 == 'litres':
            y=convdrytocum(float(n4))
            x=convcumtolit(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='dry pt us' and n3 == 'cubic mm':
            y=convdrytocum(float(n4))
            x=convcumtocumm(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'dry pt us' and n3 == 'cubic feet':
            y=convdrytocum(float(n4))
            x=convcumtocuf(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'dry pt us' and n3 == 'gallons uk':
            y=convdrytocum(float(n4))
            x=convcumtogalk(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'dry pt us' and n3 == 'gallon us':
            y=convdrytocum(float(n4))
            x=convcumtogals(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'dry pt us' and n3 == 'pints uk':
            y=convdrytocum(float(n4))
            x=convcumtopin(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'dry pt us' and n3 == 'liquid pt us':
            y=convdrytocum(float(n4))
            x=convcumtoliq(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'dry pt us' and n3 == 'liquid oz us':
            y=convdrytocum(float(n4))
            x=convcumtoliqo(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'dry pt us' and n3 == 'fluid oz uk':
            y=convdrytocum(float(n4))
            x=convcumtoflu(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'dry pt us' and n3 == 'barrels us':
            y=convdrytocum(float(n4))
            x=convcumtobarrel(y) 
            return render(request,'pr3/res.html',{'x7':x})

        if n2 =='liquid pt us' and n3 == 'cubic meters' :
            x=convliqtocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 == 'liquid pt us'  and n3 == 'litres':
            y=convliqtocum(float(n4))
            x=convcumtolit(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='liquid pt us' and n3 == 'cubic mm':
            y=convliqtocum(float(n4))
            x=convcumtocumm(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid pt us' and n3 == 'cubic feet':
            y=convliqtocum(float(n4))
            x=convcumtocuf(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid pt us' and n3 == 'gallons uk':
            y=convliqtocum(float(n4))
            x=convcumtogalk(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid pt us' and n3 == 'gallon us':
            y=convliqtocum(float(n4))
            x=convcumtogals(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid pt us' and n3 == 'pints uk':
            y=convliqtocum(float(n4))
            x=convcumtopin(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid pt us' and n3 == 'dry pt us':
            y=convliqtocum(float(n4))
            x=convcumtodry(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid pt us' and n3 == 'liquid oz us':
            y=convliqtocum(float(n4))
            x=convcumtoliqo(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid pt us' and n3 == 'fluid oz uk':
            y=convliqtocum(float(n4))
            x=convcumtoflu(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid pt us' and n3 == 'barrels us':
            y=convliqtocum(float(n4))
            x=convcumtobarrel(y) 
            return render(request,'pr3/res.html',{'x7':x})

        if n2 =='liquid oz us' and n3 == 'cubic meters' :
            x=convliqotocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 == 'liquid oz us'  and n3 == 'litres':
            y=convliqotocum(float(n4))
            x=convcumtolit(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='liquid oz us' and n3 == 'cubic mm':
            y=convliqotocum(float(n4))
            x=convcumtocumm(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid oz us' and n3 == 'cubic feet':
            y=convliqotocum(float(n4))
            x=convcumtocuf(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid oz us' and n3 == 'gallons uk':
            y=convliqotocum(float(n4))
            x=convcumtogalk(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid oz us' and n3 == 'gallon us':
            y=convliqotocum(float(n4))
            x=convcumtogals(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid oz us' and n3 == 'pints uk':
            y=convliqotocum(float(n4))
            x=convcumtopin(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid oz us' and n3 == 'dry pt us':
            y=convliqotocum(float(n4))
            x=convcumtodry(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid oz us' and n3 == 'liquid pt us':
            y=convliqotocum(float(n4))
            x=convcumtoliq(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid oz us' and n3 == 'fluid oz uk':
            y=convliqotocum(float(n4))
            x=convcumtoflu(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'liquid oz us' and n3 == 'barrels us':
            y=convliqotocum(float(n4))
            x=convcumtobarrel(y) 
            return render(request,'pr3/res.html',{'x7':x})

        if n2 =='fluid oz us' and n3 == 'cubic meters' :
            x=convflutocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 == 'fluid oz us'  and n3 == 'litres':
            y=convflutocum(float(n4))
            x=convcumtolit(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='fluid oz us' and n3 == 'cubic mm':
            y=convflutocum(float(n4))
            x=convcumtocumm(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'fluid oz us' and n3 == 'cubic feet':
            y=convflutocum(float(n4))
            x=convcumtocuf(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'fluid oz us' and n3 == 'gallons uk':
            y=convflutocum(float(n4))
            x=convcumtogalk(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'fluid oz us' and n3 == 'gallon us':
            y=convflutocum(float(n4))
            x=convcumtogals(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'fluid oz us' and n3 == 'pints uk':
            y=convflutocum(float(n4))
            x=convcumtopin(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'fluid oz us' and n3 == 'dry pt us':
            y=convflutocum(float(n4))
            x=convcumtodry(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'fluid oz us' and n3 == 'liquid pt us':
            y=convflutocum(float(n4))
            x=convcumtoliq(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'fluid oz us' and n3 == 'liquid oz uk':
            y=convflutocum(float(n4))
            x=convcumtoliqo(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'fluid oz us' and n3 == 'barrels us':
            y=convflutocum(float(n4))
            x=convcumtobarrel(y) 
            return render(request,'pr3/res.html',{'x7':x})

        if n2 =='barrels us' and n3 == 'cubic meters' :
            x=convbarreltocum(float(n4))
            return render(request,'pr3/res.html',{'x7':x,'w':w})
        if n2 == 'barrels us'  and n3 == 'litres':
            y=convbarreltocum(float(n4))
            x=convcumtolit(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 =='barrels us' and n3 == 'cubic mm':
            y=convbarreltocum(float(n4))
            x=convcumtocumm(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'barrels us' and n3 == 'cubic feet':
            y=convbarreltocum(float(n4))
            x=convcumtocuf(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'barrels us' and n3 == 'gallons uk':
            y=convbarreltocum(float(n4))
            x=convcumtogalk(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'barrels us' and n3 == 'gallon us':
            y=convbarreltocum(float(n4))
            x=convcumtogals(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'barrels us' and n3 == 'pints uk':
            y=convbarreltocum(float(n4))
            x=convcumtopin(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'barrels us' and n3 == 'dry pt us':
            y=convbarreltocum(float(n4))
            x=convcumtodry(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'barrels us' and n3 == 'liquid pt us':
            y=convbarreltocum(float(n4))
            x=convcumtoliq(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'barrels us' and n3 == 'liquid oz uk':
            y=convbarreltocum(float(n4))
            x=convcumtoliqo(y)
            return render(request,'pr3/res.html',{'x7':x})
        if n2 == 'barrel us' and n3 == 'fluid oz us':
            y=convbarreltocum(float(n4))
            x=convcumtoflu(y) 
            return render(request,'pr3/res.html',{'x7':x})

#---------------------------------------------------------------------------
    if w=='time':
        if n2 == n3:
            x=conv(float(n4))
            return render(request,'pr3/res.html',{'x8':n4})
        if n2 =='minutes' and n3 == 'seconds' :
            x=convmintosec(float(n4))
            return render(request,'pr3/res.html',{'x8':x,'w':w})
        if n2 =='minutes'  and n3 == 'hours':
            x=conmintohr(float(n4))
            return render(request,'pr3/res.html',{'x8':x})
        if n2 =='minutes'  and n3 == 'days':
            x=convmintody(float(n4))
            return render(request,'pr3/res.html',{'x8':x})
        if n2 =='minutes'  and n3 == 'weeks':
            x=convmintowk(float(n4))
            return render(request,'pr3/res.html',{'x8':x})
                  
        if n2 =='seconds' and n3 == 'minutes' :
            x=convsectomin(float(n4))
            return render(request,'pr3/res.html',{'x8':x,'w':w})
        if n2 =='seconds'  and n3 == 'hours':
            y=convsectomin(float(n4))
            x=convmintohr(y)
            return render(request,'pr3/res.html',{'x8':x})
        if n2 =='seconds'  and n3 == 'days':
            y=convsectomin(float(n4))
            x=convmintody(y)
            return render(request,'pr3/res.html',{'x8':x})
        if n2 =='seconds'  and n3 == 'weeks':
            y=convsectomin(float(n4))
            x=convmintowk(y)
            return render(request,'pr3/res.html',{'x8':x})

        if n2 =='hours' and n3 == 'minutes' :
            x=convhrtomin(float(n4))
            return render(request,'pr3/res.html',{'x8':x,'w':w})
        if n2 =='hours'  and n3 == 'seconds':
            y=convhrtomin(float(n4))
            x=convmintosec(y)
            return render(request,'pr3/res.html',{'x8':x})
        if n2 =='hours'  and n3 == 'days':
            y=convhrtomin(float(n4))
            x=convmintody(y)
            return render(request,'pr3/res.html',{'x8':x})
        if n2 =='hours'  and n3 == 'weeks':
            y=convhrtomin(float(n4))
            x=convmintowk(y)
            return render(request,'pr3/res.html',{'x8':x})
      
        if n2 =='days' and n3 == 'minutes' :
            x=convdytomin(float(n4))
            return render(request,'pr3/res.html',{'x8':x,'w':w})
        if n2 =='days'  and n3 == 'seconds':
            y=convdytomin(float(n4))
            x=convmintosec(y)
            return render(request,'pr3/res.html',{'x8':x})
        if n2 =='days'  and n3 == 'hours':
            y=convdytomin(float(n4))
            x=convmintohr(y)
            return render(request,'pr3/res.html',{'x8':x})
        if n2 =='days'  and n3 == 'weeks':
            y=convdytomin(float(n4))
            x=convmintowk(y)
            return render(request,'pr3/res.html',{'x8':x})
       
        if n2 =='weeks' and n3 == 'minutes' :
            x=convwktomin(float(n4))
            return render(request,'pr3/res.html',{'x8':x,'w':w})
        if n2 =='weeks'  and n3 == 'seconds':
            y=convwktomin(float(n4))
            x=convmintosec(y)
            return render(request,'pr3/res.html',{'x8':x})
        if n2 =='weeks'  and n3 == 'hours':
            y=convwktomin(float(n4))
            x=convmintohr(y)
            return render(request,'pr3/res.html',{'x8':x})
        if n2 =='weeks'  and n3 == 'days':
            y=convwktomin(float(n4))
            x=convmintody(y)
            return render(request,'pr3/res.html',{'x8':x})

    return HttpResponse('prashanth')

            
        
