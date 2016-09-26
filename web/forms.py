#coding:utf-8



from django import forms
import os



class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255,min_length=5)
    summary = forms.CharField(max_length=255,min_length=5)
    categroy_id = forms.IntegerField()
    head_img = forms.ImageField()
    content = forms.CharField(min_length=10)



def handle_uploaded_file(request,f):

    base_img_upload_path = 'static/img'
    user_path = "%s/%s" % (base_img_upload_path,request.user.userprofile.id)  #上传该图片的客户id
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    with open("%s/%s"%(user_path,f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return '/static/img/%s/%s'% (request.user.userprofile.id,f.name)