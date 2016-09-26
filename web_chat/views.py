#coding:utf-8

from django.shortcuts import render,HttpResponse
from web_chat import models
import json,Queue,time

# Create your views here.


GLOBAL_MQ = {}


def dashboard(request):
    # print 'i first'
    return render(request,'web_chat/dashboard.html')

def contacts(request):

    contact_dic = {}
    contacts = request.user.userprofile.friends.select_related().values('id','name')
    contact_dic['contact_list'] = list(contacts)

    #qqgroup对userprofile表有关联，但userprofile对qqgruop没关联，所有通过userprofile查询需反向,使用qqgroup_set

    groups = request.user.userprofile.qqgroup_set.select_related().values('id','name','max_member_num')
    contact_dic['gruop_list'] = list(groups)
    # print contact_dic
    # print contacts
    return HttpResponse(json.dumps(contact_dic))

def new_msg(request):
    if request.method == 'POST':
        print request.POST

        data = json.loads(request.POST.get('data'))
        send_to = data['to']
        if send_to not in GLOBAL_MQ:
            GLOBAL_MQ[send_to]= Queue.Queue()
        data['timestamp'] = time.time()
        GLOBAL_MQ[send_to].put(data)

        return HttpResponse(GLOBAL_MQ[send_to].qsize())
    else:
        request_user = str(request.user.userprofile.id) #因为数据库取过来是int，而前端是str

        # print type(request_user),request_user
        # print '-->',GLOBAL_MQ
        msg_lists = []
        if request_user in GLOBAL_MQ:
            print 'haha'
            stored_msg_nums = GLOBAL_MQ[request_user].qsize()
            if stored_msg_nums == 0:
                try:
                    print "\033[41;1mNo new msg,wait for ....\033[0m"
                    msg_lists.append(GLOBAL_MQ[request_user].get(timeout=5))
                except Exception as e:
                    print 'error: ',e
                    print "\033[41;1mtime out \033[0m"
            for i in range(stored_msg_nums):
                msg_lists.append(GLOBAL_MQ[request_user].get())
        else:
            GLOBAL_MQ[str(request.user.userprofile.id)] = Queue.Queue()

        return HttpResponse(json.dumps(msg_lists))




