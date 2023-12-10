from django import forms
from django.contrib.auth.models import User
import re
from customer.models import CustomerModel


class RegisterForm(forms.Form):
    # username = forms.CharField(label="Tài khoản", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Mật khẩu", required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Xác nhận mật khẩu", required=True, widget=forms.PasswordInput)
    full_name = forms.CharField(label="Họ và tên")
    phone_number = forms.CharField(label="Số điện thoại")
    address = forms.CharField(label="Địa chỉ")

    def clean_password2(self):
        if "password1" in self.cleaned_data:
            password1 = self.cleaned_data["password1"]
            password2 = self.cleaned_data["password2"]
            if password1 and password1 == password2:
                return password2

        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data["email"]
        # if not re.search(r'^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$', username):
        #     raise forms.ValidationError("Email không hợp lệ")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError("Email đã tồn tại trong hệ thống")

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data["email"],
            password=self.cleaned_data["password1"],
            # email=self.cleaned_data["email"],
            # last_name=self.cleaned_data["last_name"],
            # first_name=self.cleaned_data["first_name"],
        )
        customer = CustomerModel(
            user=user,
            full_name=self.cleaned_data['full_name'],
            phone_number=self.cleaned_data['phone_number'],
            address=self.cleaned_data["address"],
        )
        customer.save()
