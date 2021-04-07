import os
import zipfile
from builtins import print
from io import StringIO

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render

from sbs.Forms.AbirimForm import AbirimForm
from sbs.Forms.AbirimSearchForm import AbirimSearchForm
from sbs.Forms.AbirimparametreFrom import AbirimparametreForm
from sbs.Forms.AcategoriForm import AcategoriForm
from sbs.Forms.AdosyaForm import AdosyaForm
from sbs.Forms.AdosyaFormSearch import AdosyaFormSearch
from sbs.Forms.AevrakForm import AevrakForm
from sbs.Forms.AklasorForm import AklasorForm
from sbs.Forms.AklasorSearchForm import AklasorSearchForm
from sbs.models.Abirim import Abirim
from sbs.models.AbirimParametre import AbirimParametre
from sbs.models.Adosya import Adosya
from sbs.models.AdosyaParametre import AdosyaParametre
from sbs.models.Aevrak import Aevrak
from sbs.models.Aklasor import Aklasor
from sbs.models.CategoryItem import CategoryItem
from sbs.services import general_methods


@login_required
def return_arsiv(request):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    return render(request, 'arsiv/arsiv.html')


@login_required
def arsiv_location_add(request):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST':
        category_item_form = AcategoriForm(request.POST)
        if category_item_form.is_valid():
            categori = category_item_form.save(commit=False)
            categori.forWhichClazz = "location"
            categori.save()
    category_item_form = AcategoriForm()
    categoryitem = CategoryItem.objects.filter(forWhichClazz='location')
    return render(request, 'arsiv/location.html',
                  {'category_item_form': category_item_form, 'categoryitem': categoryitem})


@login_required
def arsiv_location_update(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    categori = CategoryItem.objects.get(pk=pk)
    category_item_form = AcategoriForm(request.POST or None, instance=categori)
    if request.method == 'POST':
        if category_item_form.is_valid():
            category_item_form.save()
            return redirect('sbs:arsiv-konumEkle')
    categoryitem = CategoryItem.objects.filter(forWhichClazz='location')

    return render(request, 'arsiv/locationUpdate.html',
                  {'category_item_form': category_item_form, 'categoryitem': categoryitem})


@login_required
def arsiv_birim_add(request):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST':
        category_item_form = AbirimForm(request.POST)
        if category_item_form.is_valid():
            category_item_form.save()

    category_item_form = AbirimForm()
    categoryitem = Abirim.objects.all()
    return render(request, 'arsiv/birimAdd.html',
                  {'category_item_form': category_item_form, 'categoryitem': categoryitem})


@login_required
def categoryItemDelete(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Abirim.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except CategoryItem.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def arsiv_birim_update(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    birim = Abirim.objects.get(pk=pk)
    category_item_form = AbirimForm(request.POST or None, instance=birim)

    if request.method == 'POST':
        if category_item_form.is_valid():
            category_item_form.save()
    categoryitem = AbirimParametre.objects.filter(birim=birim)
    klasor=Aklasor.objects.filter(birim=birim)
    return render(request, 'arsiv/birimGuncelle.html', {'category_item_form': category_item_form,
                                                        'categoryitem': categoryitem,
                                                        'birim': birim,
                                                        'klasor':klasor})


@login_required
def arsiv_birimParametre(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    abirim = Abirim.objects.get(pk=pk)
    category_item_form = AbirimparametreForm(request.POST or None)
    if request.method == 'POST':
        if category_item_form.is_valid():
            test = AbirimParametre(title=category_item_form.cleaned_data['title'],
                                   birim=abirim,
                                   type=category_item_form.cleaned_data['type']
                                   )
            test.save()
            print()
            print(test.birim.name)
            print(test)

            return redirect('sbs:arsiv-birimUpdate', pk=abirim.pk)

    return render(request, 'arsiv/parametreEkle.html', {'parametre_form': category_item_form, })


@login_required
def arsiv_birimParametreUpdate(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    if AbirimParametre.objects.filter(pk=pk):
        parametre = AbirimParametre.objects.get(pk=pk)
        category_item_form = AbirimparametreForm(request.POST or None, instance=parametre)
    else:
        parametre = AbirimParametre.objects.none()
        category_item_form = AbirimparametreForm(request.POST or None)


    if request.method == 'POST':
        if category_item_form.is_valid():
            test = category_item_form.save()
            test.save()
            return redirect('sbs:arsiv-birimUpdate', parametre.birim.pk)
    return render(request, 'arsiv/parametreEkle.html', {'parametre_form': category_item_form, })


@login_required
def arsiv_birimListesi(request):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    birim_form=AbirimSearchForm()
    birimler=Abirim.objects.none()
    if request.method == 'POST':
        name=request.POST.get('name')
        if not (name):
            birimler=Abirim.objects.filter()

        else:
            query = Q()
            if name:
                query &= Q(name__icontains=name)
            birimler=Abirim.objects.filter(query)


    return render(request, 'arsiv/BirimList.html', {'birimler': birimler,
                                                    'birim_form':birim_form})


@login_required
def parametredelete(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = AbirimParametre.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except CategoryItem.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


def arsiv_klasorEkle(request):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')


    if request.GET.get('birim'):
        if Abirim.objects.filter(pk=request.GET.get('birim')):
            form=AklasorForm(initial = {'birim': Abirim.objects.get(pk=request.GET.get('birim'))})
    else:
        form = AklasorForm()


    if request.method == 'POST':
        form = AklasorForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

            return redirect('sbs:klasor-guncelle', form.pk)

    return render(request, 'arsiv/KlasorEkle.html', {'form': form})


def arsiv_klasorler(request):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    klasor = Aklasor.objects.none()
    klasor_form=AklasorSearchForm()
    if request.method == 'POST':
        name=request.POST.get('name')
        sirano = request.POST.get('sirano')
        location = request.POST.get('location')
        birim = request.POST.get('birim')
        if not (name or sirano or location or birim):
            klasor=Aklasor.objects.all()
        else:
            query = Q()
            if name:
                query &= Q(name__icontains=name)
            if sirano:
                query &= Q(sirano=sirano)
            if location:
                query &= Q(location__pk=int (location))
            if birim:
                query &= Q(birim__pk=int (birim))
            klasor=Aklasor.objects.filter(query)



    #
    # for item in klasor:
    #     parametre = Adosya.objects.filter(klasor=item)
    #     # print(parametre.values_list("title","title"))
    #     beka = {
    #         'pk': item.pk,
    #         'name': item.name,
    #         'parametre': parametre
    #     }
    #     birimler.append(beka)

    # arama alani yazılacak
    # if request.method == 'POST':
    #     if category_item_form.is_valid():
    #         category_item_form.save()
    #         return redirect('sbs:arsiv-birimEkle')

    return render(request, 'arsiv/KlasorListesi.html', {'klasor': klasor,
                                                        'klasor_form':klasor_form})
@login_required
def arsiv_klasorUpdate(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    klasor = Aklasor.objects.get(pk=pk)
    klasor_form = AklasorForm(request.POST or None, instance=klasor)
    dosya = Adosya.objects.filter(klasor=klasor)
    if request.method == 'POST':
        if klasor_form.is_valid():
            test = klasor_form.save()
            test.save()
    return render(request, 'arsiv/KlasorGuncelle.html', {'form': klasor_form, 'dosya': dosya, 'klasor': klasor})
def arsiv_dosyaEkle(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    klasor = Aklasor.objects.get(pk=pk)
    form = AdosyaForm(pk)
    if request.method == 'POST':

        form = AdosyaForm(pk,request.POST)
        if form.is_valid():
            pk=form.save(pk)
            return redirect('sbs:dosya-guncelle',pk)
    return render(request, 'arsiv/DosyaEkle.html', {'form': form})

@login_required
def arsiv_dosyaUpdate(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    dosya = Adosya.objects.get(pk=pk)
    form = AdosyaForm(dosya.klasor.pk,request.POST or None, instance=dosya)
    dosyaparametre=AdosyaParametre.objects.filter(dosya=dosya)
    for item in dosyaparametre:
        form.fields[item.parametre.title].initial = item.value

    files = Aevrak.objects.filter(adosya=dosya)
    evraklist=[]
    for item in files:
        # print(item.file.name)
        if item.file.name.split(".")[len(item.file.name.split("."))-1]== "pdf":
            evraklist.append(item)
    if request.method == 'POST':
        if request.FILES.get('file'):
            evrak = Aevrak(file=request.FILES.get('file'))
            evrak.save()
            dosya = Adosya.objects.get(pk=pk)
            dosya.evrak.add(evrak)
            dosya.save()

        dosya.sirano = request.POST.get('sirano')
        # Sonradan  parametre eklendigine  kontrol yazılmasi lazım
        if dosyaparametre:
            for item in dosyaparametre:

                if request.POST.get(item.parametre.title):
                    item.value = request.POST.get(item.parametre.title)
                    item.save()
        else:
            form.update(dosya.pk)
    return render(request, 'arsiv/DosyaGuncelle.html', {'form': form, 'dosya': dosya, 'files': files ,'evraklist':evraklist})


@login_required
def arsiv_evrakEkle(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    form = AevrakForm()
    if request.method == 'POST':
        form = AevrakForm(request.POST, request.FILES)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for file in files:
                evrak = Aevrak(file=file)
                evrak.save()
                dosya = Adosya.objects.get(pk=pk)
                dosya.evrak.add(evrak)
                dosya.save()
            return redirect('sbs:dosya-guncelle', dosya.pk)

    return render(request, 'arsiv/EvrakEkle.html',
                  {'form': form, }
                  )

@login_required
def arsiv_evrakDelete(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    evrak = Aevrak.objects.get(pk=pk)
    dosya = Adosya.objects.filter(evrak=evrak)[0]
    evrak.delete()
    return redirect('sbs:dosya-guncelle', dosya.pk)
@login_required
def arsiv_anasayfa(request):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    units=Abirim.objects.all()
    klasor=Aklasor.objects.all()
    dosyalar=Adosya.objects.all()
    return render(request, "arsiv/arsivAnasayfa.html",
                  {'units': units,
                   'klasor':klasor,
                   'files':dosyalar
                   }
                  )
@login_required
def parametre(request):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    if request.method == 'POST':
        if request.POST.get('cmd'):
            birim = Abirim.objects.get(pk=int(request.POST.get('cmd')))
            parametre = AbirimParametre.objects.filter(birim=birim)

            beka = []
            for item in parametre:
                data = {
                    'pk': item.pk,
                    'title': item.title,
                    'type': item.type,
                }
                beka.append(data)
            return JsonResponse(
                {
                    'data': beka,
                    'msg': 'Valid is  request'
                })
        else:
            return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


    try:

        print()


    except:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


def birimGeneralSearch(request):
    dosya = Adosya.objects.none()
    units = Abirim.objects.none()
    klasor = Aklasor.objects.none()

    if request.method == 'POST':
        if request.POST.get('search'):
            units |= Abirim.objects.filter(name__icontains=request.POST.get('search'))

            klasor |= Aklasor.objects.filter(name__icontains=request.POST.get('search'))
            try:
                dosya |= Adosya.objects.filter(sirano=request.POST.get('search'))
            except:
                print('Sayisal degil')
            if klasor:
                for item in klasor:
                    units |= Abirim.objects.filter(pk=item.birim.pk)
            if dosya:
                for item in dosya:
                    klasor |= Aklasor.objects.filter(pk=item.klasor.pk)
                    units |= Abirim.objects.filter(pk=item.klasor.birim.pk)
            dosyaparametre = AdosyaParametre.objects.filter(value__contains=request.POST.get('search'))
            if dosyaparametre:
                for item in dosyaparametre:
                    dosya |= Adosya.objects.filter(pk=int(item.dosya.pk))
                    klasor |= Aklasor.objects.filter(pk=item.dosya.klasor.pk)
                    units |= Abirim.objects.filter(pk=item.dosya.klasor.birim.pk)
    return render(request, "arsiv/GenelArama.html",
                  {
                      'units': units.distinct(),
                      'klasor': klasor.distinct(),
                      'files': dosya.distinct()
                  })



def birimsearch(request):
    birimler = []
    categori = Abirim.objects.all()

    for item in categori:
        parametre = AbirimParametre.objects.filter(birim=item)
        # print(parametre.values_list("title","title"))
        beka = {
            'pk': item.pk,
            'name': item.name,
            'parametre': parametre
        }
        birimler.append(beka)
    test=[]
    dosya=Adosya.objects.none()
    birimdizi=[]

    units=Abirim.objects.none()
    klasor=Aklasor.objects.none()

    if request.method == 'POST':
        if request.POST.get('birim_id'):
            birimparametre=AbirimParametre.objects.filter(birim__id=int(request.POST.get('birim_id')))
            for item in birimparametre:
                if request.POST.get(item.title):
                    print(request.POST.get(item.title))
                    dosyaParametre = AdosyaParametre.objects.filter(value__icontains=request.POST.get(item.title))
                    for item in dosyaParametre:
                        dosya |= Adosya.objects.filter(pk=int(item.dosya.pk))
                        klasor |=Aklasor.objects.filter(pk=item.dosya.klasor.pk)
                        units |= Abirim.objects.filter(pk=item.dosya.klasor.birim.pk)
    return render(request, "arsiv/BirimSearch.html",
                  {
                      'birimler':birimler,
                      'units': units.distinct(),
                      'klasor': klasor.distinct(),
                      'files': dosya.distinct()
                   })



def arsiv_dosyalar(request):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    dosya = Adosya.objects.none()
    dosya_form=AdosyaFormSearch()
    klasor_form=AklasorSearchForm()

    if request.method == 'POST':
        sirano = request.POST.get('sirano')
        location = request.POST.get('location')
        birim = request.POST.get('birim')
        klasor = request.POST.get('klasor')
        if not (klasor or sirano or location or birim):
            dosya=Adosya.objects.all()
        else:
            query = Q()
            if klasor:
                query &= Q(klasor__pk=klasor)
            if sirano:
                query &= Q(sirano=sirano)
            if location:
                query &= Q(klasor__location__pk=location)
            if birim:
                query &= Q(klasor__birim__pk=birim)
            dosya=Adosya.objects.filter(query)

    return render(request, 'arsiv/DosyaListesi.html', {'dosya': dosya,
                                      'klasor_form':klasor_form,
                                       'dosya_form': dosya_form
                                      })




def birimSearch(request):
    dosya = Adosya.objects.none()
    units = Abirim.objects.none()
    klasor = Aklasor.objects.none()
    klasor_form=AklasorSearchForm()

    if request.method == 'POST':
        name = request.POST.get('klasorname')
        sirano = request.POST.get('klasorsirano')
        location = request.POST.get('klasorlocation')
        birim = request.POST.get('klasorbirim')




        # genel arama alani
        if request.POST.get('search'):
            units |= Abirim.objects.filter(name__icontains=request.POST.get('search'))
            klasor |= Aklasor.objects.filter(name__icontains=request.POST.get('search'))
            try:
                dosya |= Adosya.objects.filter(sirano=request.POST.get('search'))
            except:
                print('Sayisal degil')
            if klasor:
                for item in klasor:
                    units |= Abirim.objects.filter(pk=item.birim.pk)
            if dosya:
                for item in dosya:
                    klasor |= Aklasor.objects.filter(pk=item.klasor.pk)
                    units |= Abirim.objects.filter(pk=item.klasor.birim.pk)
            dosyaparametre = AdosyaParametre.objects.filter(value__contains=request.POST.get('search'))
            if dosyaparametre:
                for item in dosyaparametre:
                    dosya |= Adosya.objects.filter(pk=int(item.dosya.pk))
                    klasor |= Aklasor.objects.filter(pk=item.dosya.klasor.pk)
                    units |= Abirim.objects.filter(pk=item.dosya.klasor.birim.pk)

        # dosya arama alani
        # if request.POST.get('searchdosya'):
        #     dosya |=Adosya.objects.filter(sirano=request.POST.get('searchdosya'))
        #     for item in dosya:
        #         klasor |= Aklasor.objects.filter(pk=item.klasor.pk)
        #         units |= Abirim.objects.filter(pk=item.klasor.birim.pk)
        # birim arama alani
        elif request.POST.get('searchbirim'):
            units |=Abirim.objects.filter(pk=request.POST.get('searchbirim'))
            birimparametre = AbirimParametre.objects.filter(birim__id=int(request.POST.get('searchbirim')))
            if birimparametre:
                for item in birimparametre:
                    if request.POST.get(item.title):
                        print(request.POST.get(item.title))
                        dosyaParametre = AdosyaParametre.objects.filter(value__icontains=request.POST.get(item.title))
                        for item in dosyaParametre:
                            dosya |= Adosya.objects.filter(pk=int(item.dosya.pk))
                            klasor |= Aklasor.objects.filter(pk=item.dosya.klasor.pk)
                            units |= Abirim.objects.filter(pk=item.dosya.klasor.birim.pk)




        # klasör arama alani

        elif (name or sirano or location or birim):
            query = Q()
            if name:
                query &= Q(name__icontains=name)
            if sirano:
                query &= Q(sirano=sirano)
            if location:
                query &= Q(location__pk=int(location))
            if birim:
                query &= Q(birim__pk=int(birim))
            klasor |= Aklasor.objects.filter(query)

            for item in klasor:
                units |= Abirim.objects.filter(pk=item.birim.pk)
        else:
            dosya = Adosya.objects.all()
            units = Abirim.objects.all()
            klasor = Aklasor.objects.all()



    dosyadizi=[]

    for item in dosya.distinct():
        if AdosyaParametre.objects.filter(dosya=item):
            test = AdosyaParametre.objects.filter(dosya=item)[0]
            print(test.parametre)
            beka = {
                'pk': item.pk,
                'sirano': item.sirano,
                'parametre': test.parametre.title,
                'klasor_id':item.klasor.pk
            }
            dosyadizi.append(beka)



    return render(request, "arsiv/Arama.html",
                  {
                      'units': units.distinct(),
                      'klasor': klasor.distinct(),
                      'files': dosyadizi,
                      'klasor_form':klasor_form
                  })

@login_required
def zipfile(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    dosya=Adosya.objects.get(pk=pk)
    files = Aevrak.objects.filter(adosya=dosya)
    evraklist = []

    for item in files:
        # print(item.file.name)
        if item.file.name.split(".")[len(item.file.name.split(".")) - 1] == "pdf":
            evraklist.append(item)

        # Files (local path) to put in the .zip
        # FIXME: Change this (get paths from DB etc)
    filenames =evraklist

    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = "somefiles"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = StringIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), mimetype="application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp

    # if request.method == 'POST' and request.is_ajax():
    #
    #
    #     try:
    #         obj = Abirim.objects.get(pk=pk)
    #         obj.delete()
    #         return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
    #     except CategoryItem.DoesNotExist:
    #         return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})
    #
    # else:
    #     return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})




@login_required
def arsiv_evrakDelete_ajax(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    if request.method == 'POST' and request.is_ajax():

        try:
            evrak = Aevrak.objects.get(pk=pk)
            dosya = Adosya.objects.filter(evrak=evrak)[0]
            evrak.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except CategoryItem.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def arsiv_klasor_delete(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    if request.method == 'POST' and request.is_ajax():
        klasor = Aklasor.objects.get(pk=pk)
        klasor.delete()

        try:


            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except CategoryItem.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})




@login_required
def arsiv_dosya_delete(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    if request.method == 'POST' and request.is_ajax():
        dosya = Adosya.objects.get(pk=pk)
        dosya.delete()

        try:


            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except CategoryItem.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})