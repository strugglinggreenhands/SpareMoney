from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')


class ModifyInfoForm(forms.Form):
    password1 = forms.CharField(label="新密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UpTransForm(forms.Form):

    TRANSTYPE=(
        ('survey', '填写问卷'),
        ('morning', '叫早服务'),
        ('takeout', '带饭服务'),
        ('express', '代领快递'),
        ('drug', '代买药品'),
    )
    # type = forms.ChoiceField(label=u'类型', widget=forms.ChoiceField())
    bonus = forms.IntegerField(label="分数", widget=forms.TextInput(attrs={'class': 'form-control'}))
    # uploader = forms.CharField(label="发布者", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="联系电话", max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    detail = forms.CharField(label="任务详情", max_length=512, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'resize:none'}))
    # c_time = forms.DateTimeField(label="发布日期", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    d_time = forms.DateTimeField(label="截止日期", widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_accept = forms.BooleanField(label="接受情况", max_length=128, widget=forms.BInput(attrs={'class': 'form-control'}))
    # is_finish = forms.BooleanField(label="完成情况", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))


class FindTransForm(forms.Form):
    accept_trans = forms.IntegerField(label="任务Id", widget=forms.TextInput(attrs={'class': 'form-control'}))

