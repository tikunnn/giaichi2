from django import forms
from .models import Phongban, Nhanvien, Cong_trinh_da, Giaichi, Filegiaichis, TKco, TKno, YTno
from django.contrib.auth.models import User


class PhongbanForm(forms.ModelForm):
    class Meta:
        model = Phongban
        fields = ['mapb', 'tenpb', 'ngaythanhlap', 'conhansu']
        widgets = {
            'ngaythanhlap': forms.SelectDateWidget(years=range(1900, 2100)),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mapb'].widget.attrs.update(
            {'placeholder': 'Nhập mã phòng ban'})
        self.fields['tenpb'].widget.attrs.update(
            {'placeholder': 'Nhập tên phòng ban'})


class NhanvienForm(forms.ModelForm):
    class Meta:
        model = Nhanvien
        fields = ['manv', 'username', 'tennv']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['manv'].widget.attrs.update(
            {'placeholder': 'Nhập mã nhân viên'})
        self.fields['tennv'].widget.attrs.update(
            {'placeholder': 'Nhập họ tên nhân viên'})


class CongTrinhForm(forms.ModelForm):
    class Meta:
        model = Cong_trinh_da
        fields = ['ten_cong_trinh', 'dia_chi', 'goithau',
                  'han_muc_thi_cong', 'truongteam', 'kinhdoanh', 'tinhtrang']

    truongteam = forms.ModelChoiceField(
        queryset=Nhanvien.objects.all(), empty_label="Chọn Trưởng nhóm")
    kinhdoanh = forms.ModelChoiceField(
        queryset=Nhanvien.objects.all(), empty_label="Chọn Kinh doanh")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ten_cong_trinh'].widget.attrs.update(
            {'placeholder': 'Nhập tên công trình'})
        self.fields['dia_chi'].widget.attrs.update(
            {'placeholder': 'Nhập địa chỉ công trình'})


class GiaichiForm(forms.ModelForm):
    class Meta:
        model = Giaichi
        fields = ['congtrinh', 'biennhan', 'nhanvien', 'phongban', 'username', 'guiduyet',
                  'hangmuc', 'noidungmota', 'giaichithietbi', 'tieude', 'ghichu', 'tiengiaichi']

    congtrinh = forms.ModelChoiceField(
        queryset=Cong_trinh_da.objects.all(), empty_label="Chọn Công Trình")
    phongban = forms.ModelChoiceField(
        queryset=Phongban.objects.all(), empty_label="Chọn Phòng Ban")
    nhanvien = forms.ModelChoiceField(
        queryset=Nhanvien.objects.all(), empty_label="Chọn Nhân Viên")
    username = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label="Chọn Tài Khoản Nhân Viên")


class FilegiaichiForm(forms.ModelForm):
    class Meta:
        model = Filegiaichis
        fields = ['giaichi', 'files']

    giaichi = forms.ModelChoiceField(
        queryset=Giaichi.objects.all(), empty_label="Chọn Giải Chi")
    files = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['files'].widget.attrs.update(
            {'class': 'file-upload-input'})


class TKcoForm(forms.ModelForm):
    class Meta:
        model = TKco
        fields = ['tentkco', 'mota', 'report_nsp']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tentkco'].widget.attrs.update(
            {'placeholder': 'Nhập tên tài khoản'})
        self.fields['mota'].widget.attrs.update(
            {'placeholder': 'Mô tả tài khoản'})


class TKnoForm(forms.ModelForm):
    class Meta:
        model = TKno
        fields = ['tentkno', 'mota', 'report_nsp']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tentkno'].widget.attrs.update(
            {'placeholder': 'Nhập tên tài khoản nợ'})
        self.fields['mota'].widget.attrs.update(
            {'placeholder': 'Mô tả tài khoản nợ'})


class YTnoForm(forms.ModelForm):
    class Meta:
        model = YTno
        fields = ['tenytno', 'mota']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tenytno'].widget.attrs.update(
            {'placeholder': 'Nhập tên yếu tố nợ'})
        self.fields['mota'].widget.attrs.update(
            {'placeholder': 'Mô tả yếu tố nợ'})
