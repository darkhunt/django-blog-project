# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import post, comment 


def post_list(request):
    post_list = post.objects.all() 
    html=''
    for i in post_list:
        html+='<p>'+ str(i ) +'</p>'+ '<br/>' +i.body +'<br/>'
    
    return HttpResponse(html)

def post_detail(request, id, showComments=True):
    post_des=post.objects.get(pk=id)
    k=post_des.title
    html='<p> title: '+post_des.title +'</p>'+'<p>'+ 'body:'+ post_des.body +'</p>'+'<p>'+ 'created:'+ str(post_des.created) +'</   p>'+'<p>'+'updated:'+str(post_des.updated) +'</p>'

    return HttpResponse(html)

    
    
def post_search(request, term):
    post_see=post.objects.filter(body__contains=term)
    
    return HttpResponse(post_see)

def home(request):
    print 'it works'
    return HttpResponse('hello fellow forex, today is non-farm payroll!') 
