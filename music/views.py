from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from form import UserForm, LoginForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlbumSerializer
import xmlrpclib
import sys


class indexView(generic.ListView):
   template_name = 'music/index.html'
   context_object_name = 'all_albums'
   def get_queryset(self):
    return Album.objects.all()

# song view
class SongView(generic.ListView):
    template_name = 'music/song.html'
    context_object_name = 'all_songs'
    def get_queryset(self):
        return Song.objects.all()
class SongCreate(CreateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', 'file']

class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:SongView')

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

# album view
class AlbumCreate(CreateView):
    model = Album
    fields = ['price', 'address', 'phone', 'room_picture', 'room_picture1', 'room_picture2']
        
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


# register form view
class UserFormView(View):
     form_class = UserForm
     template_name = 'music/registration_from.html'

#      display blank form
     def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

     # process form data
     def post(self, request):
         form = self.form_class(request.POST)
         context = {}
         if form.is_valid():
             user = form.save(commit=False)
             # clean (normalized) data
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             confirm_password = form.cleaned_data['confirm_password']
             if password != confirm_password:
                 context["error_message"] = "Password not matches!"
                 form = self.form_class(None)
                 return render(request, self.template_name, {'form': form})
             user.set_password(password)
             user.save()

             # return the user object if the credentials are correct
             user = authenticate(username = username, password = password)

             if user is not None:
                 if user.is_active:
                     login(request, user)
                     return redirect('music:index')

         return render(request, self.template_name, {'form': form})


# login form view
class LoginFormView(View):
     form_class = LoginForm
     template_name = 'music/login_form.html'

#      display blank form
     def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

     # process form data
     def post(self, request):
         form = self.form_class(request.POST)
         context = {}

         username = request.POST['username']
         password = request.POST['password']

         # return the user object if the credentials are correct
         user = authenticate(username = username, password = password)

         if user:
             login(request, user)
             return redirect('music:index')
         else:
             context["error_message"] = "Provide valid credentials!"
             form = self.form_class(None)
             return render(request, self.template_name, {'form':form})



class LogoutView(View):
    form_class = LoginForm
    template_name = 'music/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        logout(request)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        context = {}
        username = request.POST['username']
        password = request.POST['password']

        # return the user object if the credentials are correct
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('music:index')
        else:
            context["error_message"] = "Provide valid credentials!"
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

# API view
class AlbumList(APIView):

    def get(self,request):
        albums = Song.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self):
        pass

# request API

def RequestAPI(test):
    # info = xmlrpclib.ServerProxy('http://96.9.67.154:8070').start()
    # url, db, username, password = \
    #     info['host'], info['KIT'], info['admin'], info['admin123321']
    url = 'http://192.168.7.222:8069'
    db = 'KIT'
    username = 'admin'
    password = 'adminkit'
    common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
    a = common.version()

    uid = common.authenticate(db, username, password, {})
    print(uid, "hehehehehehehe")


    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    record1 = models.execute_kw(db, uid, password,
                      'res.partner', 'check_access_rights',
                      ['read'], {'raise_exception': False})
    #
    ids = models.execute_kw(db, uid, password,
                      'op.attendance.line', 'search',
                      [[['batch_id.name', '=', "Batch 3"],['attendance_id.name', '=', "Semester 3"],['subject_id.name', '=', "Internship - III"], ]])
    #
    b = models.execute_kw(db, uid, password,
                      'res.partner', 'read',
                      [ids], {'fields': ['student_id',]})
    print(record1)
    print(len(b))
    print(test,"================")