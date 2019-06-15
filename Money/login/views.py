# login/views.py
from django.core import serializers
from django.shortcuts import render, redirect
from . import models
from .forms import UserForm
from .forms import RegisterForm
from .forms import ModifyInfoForm
from .forms import UpTransForm
from .forms import FindTransForm
from .models import Transaction
from django.db.models import Q


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['password'] = user.password
                    request.session['email'] = user.email
                    request.session['sex'] = user.sex
                    request.session['point'] = user.point
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')


def transaction(request):
    pass
    return render(request, "login/transaction.html")

#########################################################################undo1
def up_trans(request):
    if request.method == 'POST':
        up_trans_form = UpTransForm(request.POST)
        if up_trans_form.is_valid():
            trans_type = request.POST.get('type')
            if trans_type == None:
                message = "请选择任务类型"
                return render(request, 'login/up_trans.html', locals())
            bonus = up_trans_form.cleaned_data['bonus']
            phone = up_trans_form.cleaned_data['phone']
            detail = up_trans_form.cleaned_data['detail']
            d_time = up_trans_form.cleaned_data['d_time']
            # ok
            new_trans = models.Transaction.objects.create()
            new_trans.type = trans_type
            new_trans.bonus = bonus
            new_trans.uploader = request.session.get('user_name')
            new_trans.phone = phone
            new_trans.detail = detail
            new_trans.d_time = d_time
            new_trans.save()
            user = models.User.objects.get(name=request.session.get('user_name'))
            user.point -= bonus
            request.session['point'] = user.point
            user.save()

        up_trans_form = UpTransForm(request.POST)
        message = "发布成功！"
        return render(request, 'login/index.html', {'message': message})

    up_trans_form = UpTransForm()
    return render(request, 'login/up_trans.html', locals())

#########################################################################

#########################################################################undo2
def find_trans(request):
    if request.method == "GET":
        trans_info = []
        '''
        trans_info['trans_num'] = []
        trans_info['type'] = []
        trans_info['bonus'] = []
        trans_info['uploader'] = []
        trans_info['phone'] = []
        trans_info['detail'] = []
        trans_info['d_time'] = []
        trans_info['is_accept'] = []
        trans_info['acceptor'] = []
        trans_info['is_finish'] = []
        '''
        lista = Transaction.objects.values_list('trans_num', flat=True)
        listb = Transaction.objects.values_list('type', flat=True)
        listc = Transaction.objects.values_list('bonus', flat=True)
        listd = Transaction.objects.values_list('uploader', flat=True)
        liste = Transaction.objects.values_list('phone', flat=True)
        listf = Transaction.objects.values_list('detail', flat=True)
        listg = Transaction.objects.values_list('d_time',  flat=True)
        listh = Transaction.objects.values_list('is_accept', flat=True)
        listi = Transaction.objects.values_list('acceptor', flat=True)
        listj = Transaction.objects.values_list('is_finish', flat=True)
        for i in range(len(lista)):
            dict = {
                '任务编号': lista[i],
                '任务类型': get_type(listb[i]),
                '积分奖励': listc[i],
                '发布者': listd[i],
                '联系电话': liste[i],
                '任务内容': listf[i],
                '截止日期': listg[i],
                '接受状态': listh[i],
                '执行人': listi[i],
                '完成状态': listj[i]
            }
            trans_info.append(
               dict
            )
            '''
            trans_info['trans_num'].append(lista[i])
            trans_info['type'].append(listb[i])
            trans_info['bonus'].append(listc[i])
            trans_info['uploader'].append(listd[i])
            trans_info['phone'].append(liste[i])
            trans_info['detail'].append(listf[i])
            trans_info['d_time'].append(listg[i])
            trans_info['is_accept'].append(listh[i])
            trans_info['acceptor'].append(listi[i])
            trans_info['is_finish'].append(listj[i])
            '''
        '''
        trans_num = Transaction.objects.values_list('trans_num', flat=True)
        type = Transaction.objects.values_list('type', flat=True)
        bonus = Transaction.objects.values_list('bonus', flat=True)
        uploader = Transaction.objects.values_list('uploader', flat=True)
        phone = Transaction.objects.values_list('phone', flat=True)
        detail = Transaction.objects.values_list('detail', flat=True)
        d_time = Transaction.objects.values_list('d_time',  flat=True)
        is_accept = Transaction.objects.values_list('is_accept', flat=True)
        acceptor = Transaction.objects.values_list('acceptor', flat=True)
        is_finish = Transaction.objects.values_list('is_finish', flat=True)
        '''
        temp = {
            'key': trans_info
        }
        return render(request, "login/find_trans.html", temp)
    elif request.method == "POST":
        temp_trans_num = request.POST.get('accept')
        trans = models.Transaction.objects.get(trans_num=temp_trans_num)
        request.session['trans_num'] = trans.trans_num
        request.session['trans_type'] = get_type(trans.type)
        request.session['trans_bonus'] = trans.bonus
        request.session['trans_uploader'] = trans.uploader
        request.session['trans_phone'] = trans.phone
        request.session['trans_detail'] = trans.detail
        return redirect('/accept_trans/')
    find_trans_form = FindTransForm()
    return render(request, 'login/find_trans.html', locals())

def get_type(var):
    if var == 'survey':
        return '填写问卷'
    elif var == 'morning':
        return '叫早服务'
    elif var == 'takeout':
        return '带饭服务'
    elif var == 'express':
        return '代领快递'
    elif var == 'drug':
        return '代买药品'
    else:
        return '测试样例'
#########################################################################


def membership(request):
    #print(request.session['point'])
    return render(request, "login/membership.html", locals())


def modify_info(request):
    # if request.session.get('is_login', None):
    if request.method == "POST":
        modify_info_form = ModifyInfoForm(request.POST)
        if modify_info_form.is_valid():  # 获取数据
            password1 = modify_info_form.cleaned_data['password1']
            password2 = modify_info_form.cleaned_data['password2']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/modify_info.html', locals())
            else:
                user = models.User.objects.get(name=request.session.get('user_name'))
                user.password = password1
                user.save()
                request.session.flush()
                message = "修改成功！"
                return render(request, 'login/index.html', {'message': message})
    modify_info_form = ModifyInfoForm()
    return render(request, 'login/modify_info.html', locals())


def my_transaction(request):
    pass
    return render(request, 'login/my_transaction.html')


def msg_center(request):
    pass
    return render(request, 'login/msg_center.html')


def accept_trans(request):
    dict = {
        '任务编号': request.session['trans_num'],
        '任务类型': request.session['trans_type'],
        '积分奖励': request.session['trans_bonus'],
        '发布者': request.session['trans_uploader'],
        '联系电话': request.session['trans_phone'],
        '任务内容': request.session['trans_detail'],
        # '截止日期': request.session['trans_d_time'],
    }
    # print(dict)
    temp_trans = models.Transaction.objects.get(trans_num=request.session['trans_num'])
    temp_trans.acceptor = request.session['user_name']
    temp_trans.is_accept = True
    temp_trans.save()
    return render(request, 'login/accept_trans.html', dict)


def my_doing(request):
    if request.method == "GET":
        my_doing = models.Transaction.objects.filter(Q(acceptor=request.session.get('user_name')) & Q(is_finish=False)).values_list()
        my_doing_trans = []
        for i in range(len(my_doing)):
            dict = {
                '任务编号': my_doing[i][0],
                '任务类型': get_type(my_doing[i][1]),
                '积分奖励': my_doing[i][2],
                '发布者': my_doing[i][3],
                '联系电话': my_doing[i][4],
                '任务内容': my_doing[i][5],
                '截止日期': my_doing[i][6],
                '接受状态': my_doing[i][8],
                '执行人': my_doing[i][9],
                '完成状态': my_doing[i][10]
            }
            my_doing_trans.append(
                dict
            )
        return render(request, 'login/my_doing.html', {'key': my_doing_trans})
    elif request.method == "POST":
        temp_trans = models.Transaction.objects.get(trans_num=request.POST.get('cancel'))
        temp_trans.acceptor = 'None'
        temp_trans.is_accept = False
        temp_trans.save()
        message = "取消成功"
        return render(request, 'login/my_transaction.html', {'message': message})
    return render(request, 'login/my_doing.html')


def my_finish(request):
    if request.method == "GET":
        my_finish = models.Transaction.objects.filter(Q(acceptor=request.session.get('user_name')) & Q(is_finish=True)).values_list()
        my_finish_trans = []
        for i in range(len(my_finish)):
            dict = {
                '任务编号': my_finish[i][0],
                '任务类型': get_type(my_finish[i][1]),
                '积分奖励': my_finish[i][2],
                '发布者': my_finish[i][3],
                '联系电话': my_finish[i][4],
                '任务内容': my_finish[i][5],
                '截止日期': my_finish[i][6],
                '接受状态': my_finish[i][8],
                '执行人': my_finish[i][9],
                '完成状态': my_finish[i][10]
            }
            my_finish_trans.append(
                dict
            )
        return render(request, 'login/my_finish.html', {'key': my_finish_trans})
    return render(request, 'login/my_finish.html')


def my_upload(request):
    if request.method == "GET":
        my_upload = models.Transaction.objects.filter(uploader=request.session.get('user_name')).values_list()
        my_upload_trans = []
        for i in range(len(my_upload)):
            dict = {
                '任务编号': my_upload[i][0],
                '任务类型': get_type(my_upload[i][1]),
                '积分奖励': my_upload[i][2],
                '发布者': my_upload[i][3],
                '联系电话': my_upload[i][4],
                '任务内容': my_upload[i][5],
                '截止日期': my_upload[i][6],
                '接受状态': my_upload[i][8],
                '执行人': my_upload[i][9],
                '完成状态': my_upload[i][10]
            }
            my_upload_trans.append(
                dict
            )
        return render(request, 'login/my_upload.html', {'key': my_upload_trans})
    elif request.method == "POST":
        temp_trans = models.Transaction.objects.get(trans_num=request.POST.get('delete'))
        temp_trans.is_finish = True
        temp_trans.save()
        temp_user = models.User.objects.get(name=temp_trans.acceptor)
        temp_user.point += temp_trans.bonus
        temp_user.save()
        request.session['point'] = temp_user.point
        message = "操作成功！"
        return render(request, 'login/my_transaction.html', {'message': message})
    return render(request, 'login/my_upload.html')


def delete_trans(request):
    if request.method == "GET":
        my_upload = models.Transaction.objects.filter(uploader=request.session.get('user_name')).values_list()
        my_upload_trans = []
        for i in range(len(my_upload)):
            dict = {
                '任务编号': my_upload[i][0],
                '任务类型': get_type(my_upload[i][1]),
                '积分奖励': my_upload[i][2],
                '发布者': my_upload[i][3],
                '联系电话': my_upload[i][4],
                '任务内容': my_upload[i][5],
                '截止日期': my_upload[i][6],
                '接受状态': my_upload[i][8],
                '执行人': my_upload[i][9],
                '完成状态': my_upload[i][10]
            }
            my_upload_trans.append(
                dict
            )
        return render(request, 'login/delete_trans.html', {'key': my_upload_trans})
    elif request.method == "POST":
        temp_trans = models.Transaction.objects.get(trans_num=request.POST.get('delete')).delete()
        message = "删除成功！"
        return render(request, 'login/my_transaction.html', {'message': message})
    return render(request, 'login/delete_trans.html')
