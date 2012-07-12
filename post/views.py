# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import post, comment 


def post_list(request):
    posts = post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({ 'posts' :posts}) 
   # html=''
    #for i in post_list:
       # html+='<p>'+ str(i ) +'</p>'+ '<br/>' +i.body +'<br/>'
    
    return HttpResponse(t.render(c))

def post_detail(request, id, showComments=False):
    post_det=post.objects.filter(pk=id)
    for h in post_det:
        wanted_post=h
    comments = comment.objects.filter(post = id)
    t = loader.get_template('blog/post_detail.html')
    c = Context ({ 'post' :wanted_post, 'comments' : comments })


    #html='<p> title: '+post_des.title +'</p>'+'<p>'+ 'body:'+ #post_des.body +'</p>'+'<p>'+ 'created:'+ str(post_des.created) +'</   #p>'+'<p>'+'updated:'+str(post_des.updated) +'</p>'

    return HttpResponse(t.render(c))

    
    
def post_search(request, term):
    post_see=post.objects.filter(body__contains=term)
    
    return render_to_response('blog/post_search.html', {'posts' : post_see , 'term' : term} )

def home(request):
  return render_to_response('blog/base.html', {} ) 
