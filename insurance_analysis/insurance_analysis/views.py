import simplejson as simplejson
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pandas.io import json

from .import processcsv

def index(request):
    params = {'name':'praveen','place':'mangal'}
    return render(request,'index.html',params)

def companylogin(request):
    return render(request, 'companylogin.html')

def companydataview(request):
    username = request.GET.get('uname', '')
    password = request.GET.get('pass', '')
    data = processcsv.compcountofall(username)
    max = processcsv.comppolicymax(username)
    policydata = processcsv.compallpolicy(username)
    policyyear = processcsv.comppolicyyear(username)
    empdetails = processcsv.compempdata(username)
    params = {'name': username, 'total': data, 'maximum': max, 'policy': policydata, 'year': policyyear,'empdetails':empdetails}
    if username == '' and password == '':
        return HttpResponse('username and password cannot be empty')
    else:
        return render(request, 'companydataview.html', params)

def companydataprocess(request):
    username = request.GET.get('name', '')
    alldata = processcsv.compempdata(username)
    params = {'name': username, 'alldata': alldata}
    return render(request, 'companyalldataview.html', params)

def agentlogin(request):
    return render(request,'agentlogin.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='csv')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        merge = processcsv.merge2csv(uploaded_file_url)
        params = {'uploadstat':merge,'uploaded_file_url': uploaded_file_url}
        return render(request, 'agentupload.html', params)
    return render(request, 'agentupload.html')

def agentdataview(request):
    username = request.GET.get('uname', '')
    password = request.GET.get('pass', '')
    data = processcsv.countofall(username)
    max = processcsv.policymax(username)
    policydata=processcsv.allpolicy(username)
    policyyear=processcsv.policyyear(username)
    params = {'name':username,'total': data,'maximum':max,'policy':policydata,'year':policyyear}
    if username == '' and password == '':
        return HttpResponse('username and password cannot be empty')
    else:
        return render(request, 'agentdataview.html',params)

def agentdataprocess(request):
    username = request.GET.get('agentname', '')
    startdate = request.GET.get('startdate', '')
    enddate = request.GET.get('enddate', '')
    if startdate == '' and enddate == '':
        alldata = processcsv.alldata(username)
        params = {'name': username, 'alldata': alldata}
    else:
        data = processcsv.datawithdate(username,startdate,enddate)
        params = {'name': username, 'total': data}

    return render(request,'agentalldataview.html',params)

def agentprofile(request):
    username = request.GET['username']
    params = {'name': username}
    return render(request,'agentprofile.html',params)

def administratorlogin(request):
    return render(request, 'administratorlogin.html')

def administratorviewdata(request):
    username = request.GET.get('uname', '')
    password = request.GET.get('pass', '')
    if username == '' and password == '':
        return HttpResponse('username and password cannot be empty')
    else:
        return render(request, 'administratorviewdata.html')