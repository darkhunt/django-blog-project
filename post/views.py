# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import post, comment
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


def post_list(request):
    posts = post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({ 'posts' :posts,'user':request.user}) 
   # html=''
    #for i in post_list:
       # html+='<p>'+ str(i ) +'</p>'+ '<br/>' +i.body +'<br/>'
    
    return HttpResponse(t.render(c))


class commentForm(ModelForm):
	class Meta:
	  model=comment
	  exclude=['post','name']

@csrf_exempt
def post_detail(request, id, showComments=False):
    post_det=post.objects.filter(pk=id)
    for h in post_det:
        wanted_post=h
    if request.method == 'POST':
	the_comment= comment(post=wanted_post)
	the_comment.name= request.user
	form=commentForm(request.POST,instance=the_comment)
        if form.is_valid ():
	   form.save()
	return HttpResponseRedirect(request.path)
    else:
	form=commentForm()

   
    comments = comment.objects.filter(post = id)
    t = loader.get_template('blog/post_detail.html')
    c = Context ({ 'post' :wanted_post, 'comments' : comments, 'form':form,'user':request.user})
    return HttpResponse(t.render(c))


    #html='<p> title: '+post_des.title +'</p>'+'<p>'+ 'body:'+ #post_des.body +'</p>'+'<p>'+ 'created:'+ str(post_des.created) +'</   #p>'+'<p>'+'updated:'+str(post_des.updated) +'</p>'

@csrf_exempt
def edit_comment(request, id ):
    edit_com=comment.objects.get(pk=id)
    
    if request.method == 'POST':
	form=commentForm(request.POST,instance=edit_com)
        if form.is_valid ():
	   form.save()

     
	return HttpResponseRedirect(edit_com.post.get_absolute_url())
    else:
	form=commentForm(instance=edit_com)

    t = loader.get_template('blog/edit_comment.html')
    c = Context ({ 'post' :edit_com, 'form':form})
    return HttpResponse(t.render(c))

   

    
    
def post_search(request, term):
    post_see=post.objects.filter(body__contains=term)
    
    return render_to_response('blog/post_search.html', {'posts' : post_see , 'term' : term} )

def home(request):
  return render_to_response('blog/base.html', {'user' :request.user} ) 
