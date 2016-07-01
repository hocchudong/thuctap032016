from django import template
from django.shortcuts import render
import paramiko
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.template.context_processors import csrf

from app.models import User, Directory, Path


def login(request):
    return render(request, 'HomePage.html')


def getatrr(request):
    c = {}
    c.update(csrf(request))
    username = request.POST.get('username')
    domain = request.POST.get('domain')
    password = request.POST.get('password')
    for i in User.objects.all():
        if (i.domain, i.username, i.password) == (
                domain, username, password) or domain == None or username == None or password == None:
            i.delete()
    User.objects.create(domain=domain, username=username, password=password)
    return render(request, 'HomePage.html')


def connect():
    user = User.objects.last()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=user.domain, username=user.username, password=user.password)
    return client


def execute(request):
    c = {}
    c.update(csrf(request))
    cmd = request.POST.get('command')
    client = connect()
    stdin, stdout, stderr = client.exec_command(cmd)
    return render(request, 'HomePage.html', {
        'stdout': stdout,
    })


def getpath(request):
    c = {}
    c.update(csrf(request))
    path = request.POST.get('path')
    client = connect()
    # cmd = 'tree -if --noreport ' + path
    cmd = 'find ' + path + '  -type f'
    str(cmd)
    stdin, stdout, stderr = client.exec_command(cmd)
    out = []
    for i in stdout:
        out.append(i)
    for i in out:
        for j in Directory.objects.all():
            if j.path == i:
                j.delete()
        Directory.objects.create(path=i)
    # cmd1 = 'tree -ifd --noreport ' + path
    # stdin1, stdout1, stderr1 = client.exec_command(cmd1)
    # out1 = []
    # for i in stdout1:
    #     out1.append(i)
    # for i in out1:
    #     for j in Directory.objects.all():
    #         if j.path == i:
    #             j.delete()
    return render(request, 'HomePage.html', {
        'dir': Directory.objects.all(),
    })


def getfile(request):
    c = {}
    c.update(csrf(request))
    path = request.POST.get('select')
    Path.objects.create(path=path)
    str(path)
    file = open('local', 'w')
    file.write(path)
    file.close()
    client = connect()
    sftp = client.open_sftp()
    sftp.get(path, 'temp.txt')
    file = open('temp.txt')
    output = file.read()
    return render(request, 'HomePage.html', {
        'output': output,
    })


def changefile(request):
    c = {}
    c.update(csrf(request))
    content = request.POST.get('textarea')
    # path = Path.objects.last()
    f = open('local', 'r')
    path = f.read()
    f.close()
    str(path)
    client = connect()
    sftp = client.open_sftp()
    file = open('temp.txt', 'w')
    file.write(content)
    file.close()
    sftp.put('temp.txt', path)
    Path.objects.all().delete()
    return render(request, 'HomePage.html')


def shortfile(request):
    c = {}
    c.update(csrf(request))
    client = connect()
    replace = request.POST.get('replace')
    wth = request.POST.get('with')
    path1 = request.POST.get('select')
    if (path1 != None):
        Path.objects.create(path=path1)
    path = Path.objects.last()
    # f = open('local', 'r')
    # path = f.read()
    cmd = "sed -i 's/%s/%s/g' %s" % (replace, wth, path)
    str(cmd)
    print cmd
    stdin, stdout, stderr = client.exec_command(cmd)
    for i in stdout:
        print i
    return render(request, 'HomePage.html')
