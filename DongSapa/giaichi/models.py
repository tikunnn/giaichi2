import os
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from simple_history.models import HistoricalRecords
from django.forms.models import model_to_dict

# Create your models here.

PAYMENT_METHOD_CHOICES = [
    ("0", "Tiền Mặt"),
    ("1", "Chuyển Khoản"),
    ("2", "Luân Chuyển Nội Bộ"),
]

PROJECT_CHOICES = [
    ("0", "ĐÔNG SAPA - DỰ ÁN"),
    ("1", "NAM SAPA - DỰ ÁN"),
    ("2", "Ngoài"),
]

HANGMUC_CHOICES = [
    ("0", "Hàng Hóa"),
    ("1", "Mua Sắm Thiết Bị"),
    ("2", "Khác"),
    ("3", "Dự án  - công trình"),
    ("4", "Đồ Nghề"),
    ("5", "Chi Phí"),
    ("6", "Giao Nhận"),
    ("7", "Chi Phí N/A"),
    ("8", "Nội Bộ"),
    ("9", "Chế Độ"),
    ("10", "Giải Chi Âm"),
    ("11", "Tiếp Khách - GD Giao Tế"),
    ("12", "Công Tác"),
    ("13", "Xăng Dầu"),
    ("14", "Sửa Chữa - Bảo Dưỡng Xe"),
    ("15", "GC NB DUONG <-> ÂM"),
    ("16", "Sửa Chữa"),
    ("17", "LÃI VAY"),
    ("18", "Sổ Tiết Kiệm"),
    ("19", "Trái Phiếu"),
    ("20", "Gửi Tiền Mặt"),
    ("21", "Vật Tư Mua Ngoài"),
    ("22", "CP BAO CAO NOI BO DSP"),
    ("23", "TẠM ỨNG 141 "),
    ("24", "N/A MUA HÀNG -NSP "),
    ("25", "N/A BÁN HÀNG -NSP "),
    ("26", "CONG NAM SAPA "),
    ("27", "ĐÀU TƯ"),
    ("28", "CHI PHÍ CHÀNH XE "),
    ("29", "ĐI TỈNH & NGOÀI GIỜ"),
]

TINHTRANG_CHOICES = [
    ("KHOI_TAO", "KHỞI TẠO"),
    ("BAO_GIA", "BÁO GIÁ"),
    ("THUONG_THAO", "THƯƠNG THẢO"),
    ("THI_CONG", "THI CÔNG"),
    ("HOAN_THANH", "HOÀN THÀNH"),
    ("HUY", "HỦY"),
]

GUIDUYET_CHOICES = [("0", "Gửi TGĐ & TCKT "), ("1", "Gửi TP |GĐ ")]

GIAICHITHUOC_CHOICES = [("1", "Đông Sapa"), ("2", "Nam Sapa"), ("3", "Ngoài")]

PHONGBAN_CHOICES = [("0", "PHÒNG KẾ TOÁN ")]


class Phongban(models.Model):
    mapb = models.CharField(
        default="", blank=True, null=True, max_length=255, verbose_name="Mã Phòng Ban"
    )
    tenpb = models.CharField(
        default="", unique=True, max_length=255, verbose_name="Tên Phòng Ban"
    )
    ngaythanhlap = models.DateTimeField(verbose_name="Năm thành lập", null=True)
    conhansu = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Nhanvien(models.Model):
    manv = models.CharField(
        default="", unique=True, max_length=255, verbose_name="Mã Nhân Viên"
    )
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Tài Khoản Nhân Viên"
    )
    tennv = models.CharField(
        default="", max_length=255, verbose_name="Họ Tên Nhân Viên"
    )


class Cong_trinh_da(models.Model):
    choices_tinhtrang = TINHTRANG_CHOICES
    ten_cong_trinh = models.CharField(default="", max_length=255, null=True, blank=True)
    # loai_cong_trinh = models.ForeignKey(
    #     Loai_cong_trinh_da, on_delete=models.SET_NULL, null=True, blank=True)
    dia_chi = models.CharField(default="", max_length=255, null=True, blank=True)
    # khach_hang = models.ForeignKey(
    #     Khachhang_da, on_delete=models.SET_NULL, null=True, blank=True)
    goithau = models.CharField(default="", max_length=255, null=True, blank=True)
    han_muc_thi_cong = models.CharField(
        default="", max_length=1255, null=True, blank=True
    )
    # khu_vuc_mien = models.ForeignKey(
    #     Mien_tinh_da, on_delete=models.SET_NULL, null=True, blank=True)
    truongteam = models.ForeignKey(
        Nhanvien,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="truongteam_congtrinh",
    )
    kinhdoanh = models.ForeignKey(
        Nhanvien,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="kinhdoanh_congtrinh",
    )
    # nguonkhachhang = models.ForeignKey(
    #     Nguon_kh_da, on_delete=models.SET_NULL, null=True, blank=True)
    # loaikhachhang = models.ForeignKey(
    #     Loai_kh_da, on_delete=models.SET_NULL, null=True, blank=True)
    # hang = models.ManyToManyField(Nhanhieu_da, blank=True)
    # hemay = models.ManyToManyField(Hemay_da, blank=True)
    tinhtrang = models.CharField(
        default="KHOI_TAO",
        max_length=255,
        null=True,
        blank=True,
        choices=TINHTRANG_CHOICES,
    )
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.ten_cong_trinh

    class Meta:
        verbose_name = "CT_3. CÔNG TRÌNH"
        verbose_name_plural = "CT_3. CÔNG TRÌNH"
        ordering = ("id",)


class Giaichi(models.Model):
    congtrinh = models.ForeignKey(
        Cong_trinh_da, on_delete=models.CASCADE, blank=True, null=True
    )
    # code_na = models.ForeignKey(
    #     CODE_NA, on_delete=models.SET_NULL, blank=True, null=True)
    biennhan = models.CharField(default="", max_length=255, blank=True, null=True)
    nhanvien = models.ForeignKey(Nhanvien, on_delete=models.CASCADE)
    phongban = models.ForeignKey(
        Phongban,
        on_delete=models.CASCADE,
        related_name="related_primary_giaichi",
        null=True,
    )
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    guiduyet = models.CharField(
        max_length=20, choices=GUIDUYET_CHOICES, verbose_name="Trạng Thái Gửi Duyệt"
    )

    def get_guiduyet_display(self):
        return dict(GUIDUYET_CHOICES).get(self.guiduyet, "Chưa có thông tin")

    hangmuc = models.CharField(
        max_length=20, choices=HANGMUC_CHOICES, verbose_name="Hạng Mục"
    )
    noidungmota = RichTextUploadingField(null=True, max_length=500, blank=True)
    giaichithietbi = models.JSONField(
        blank=True, null=True, verbose_name="Trang Thiết Bị"
    )
    tieude = models.CharField(default="", max_length=500, null=False)
    ghichu = models.CharField(
        default="Thu Quy :", max_length=2000, null=True, blank=True
    )
    trangthaiduyetgiaichi = models.BooleanField(default=False, blank=False, null=False)
    trangthaiduyet_admin = models.BooleanField(default=False, blank=False, null=False)
    trangthaiduyet_kinhdoanh = models.BooleanField(
        default=False, blank=False, null=False
    )
    trangthaiduyet_pp = models.BooleanField(default=True, blank=False, null=False)
    trangthaiduyet_tp = models.BooleanField(default=False, blank=False, null=False)
    trangthaiduyet_tckt = models.BooleanField(default=True, blank=False, null=False)
    trangthaiduyet_sep = models.BooleanField(default=False)
    trangthaihuy = models.BooleanField(default=False, blank=False, null=False)
    trangthaihoanthanh = models.BooleanField(default=False, blank=False, null=False)
    noidungthanhtoan = models.CharField(null=True, blank=True, max_length=500)
    tiengiaichi = models.BigIntegerField(default=0)
    hinhthucthanhtoan = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=PAYMENT_METHOD_CHOICES,
        verbose_name="Hình Thức Thanh Toán",
    )

    def get_hinhthucthanhtoan_display(self):
        return dict(PAYMENT_METHOD_CHOICES).get(
            self.hinhthucthanhtoan, "Chưa có thông tin"
        )

    motathanhtoan = models.CharField(default="", blank=True, null=True, max_length=2255)
    macheck = models.CharField(default="", blank=True, null=True, max_length=2255)

    xacnhanthanhtoan = models.CharField(
        default="", blank=True, null=True, max_length=2255
    )
    check_duyet = models.BooleanField(
        null=True, blank=True, verbose_name="Check TGĐ/TCKT Duyệt"
    )
    trangthaiduyet_dsp = models.BooleanField(default=False, blank=False, null=False)
    trangthaiduyet_khac = models.BooleanField(default=False, blank=False, null=False)
    checkgiaichigiaonhan = models.BooleanField(default=False, blank=False, null=False)
    checkgiaichiduan = models.BooleanField(default=False, blank=False, null=False)
    giaichithuoc = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=GIAICHITHUOC_CHOICES,
        verbose_name="Hàng Hóa Thuộc",
    )
    vat = models.CharField(default=0, blank=True, null=True, max_length=255)
    giaingan = models.BooleanField(
        default=False, null=True, blank=True, verbose_name="Giải Ngân"
    )
    xacnhan_giaingan = models.BooleanField(
        default=False, null=True, blank=True, verbose_name="Xác Nhận Giải Ngân"
    )
    giaichiam = models.BooleanField(default=False, blank=True, null=True)
    thoigian_dsp = models.DateTimeField(null=True, blank=True)
    thoigian_khac = models.DateTimeField(null=True, blank=True)
    thoigian_check_giaonhan = models.DateTimeField(null=True, blank=True)
    thoigian_check_duan = models.DateTimeField(null=True, blank=True)
    thoigian_pp = models.DateTimeField(null=True, blank=True)
    thoigian_tp = models.DateTimeField(null=True, blank=True)
    thoigian_sep = models.DateTimeField(null=True, blank=True)
    thoigian_thanhtoan = models.DateTimeField(null=True, blank=True)
    thuocvecongty = models.ForeignKey(
        Phongban,
        on_delete=models.CASCADE,
        related_name="related_secondary_giaichi",
        null=True,
        blank=True,
    )
    check_chuyen_giaingan = models.BooleanField(default=False, null=True, blank=True)
    tkno = models.CharField(
        blank=True, null=True, max_length=200, verbose_name=" TK Nợ"
    )
    ytno = models.CharField(
        blank=True, null=True, max_length=200, verbose_name=" YT Nợ"
    )
    tkco = models.CharField(
        blank=True, null=True, max_length=200, verbose_name=" TK Có"
    )
    ytco = models.CharField(
        blank=True, null=True, max_length=200, verbose_name=" YT Có"
    )
    thongbaotao = models.BooleanField(default=False, null=True, blank=True)
    thongbao_check = models.BooleanField(default=False, null=True, blank=True)
    thongbao_duyet_pp = models.BooleanField(default=False, null=True, blank=True)
    thongbao_duyet_tp = models.BooleanField(default=False, null=True, blank=True)
    thongbao_duyet_sep = models.BooleanField(default=False, null=True, blank=True)
    thongbao_duyet_ht = models.BooleanField(default=False, null=True, blank=True)
    thongbao_duyet_huy = models.BooleanField(default=False, null=True, blank=True)
    history = HistoricalRecords()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def to_dict(self):
        data = model_to_dict(self)
        for field, value in data.items():
            if value is None or (isinstance(value, str) and value.strip() == ""):
                data[field] = "Chưa có thông tin"
        if self.nhanvien:
            data["nhanvien"] = self.nhanvien.tennv
        if self.hinhthucthanhtoan:
            data["hinhthucthanhtoan"] = self.get_hinhthucthanhtoan_display()

        return data


class Filegiaichis(models.Model):
    giaichi = models.ForeignKey(
        Giaichi, on_delete=models.CASCADE, related_name="filegiaichis"
    )
    files = models.FileField(null=True, blank=True, default="", upload_to="giaichi/")

    def delete(self, *args, **kwargs):
        # Xóa tệp liên quan
        file_path = self.files.path
        if os.path.exists(file_path):
            os.remove(file_path)

        # Xóa bản ghi Filegiaichis
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "FILE GIAI CHI"
        verbose_name_plural = "FILE GIAI CHI"

    def __int__(self):
        return self.giaichi


class TKco(models.Model):
    tentkco = models.CharField(default="", max_length=255, null=True, blank=True)
    mota = models.CharField(default="", max_length=255, null=True, blank=True)
    report_nsp = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "TK Có"
        verbose_name_plural = "TK Có"
        ordering = ("id",)

    def __int__(self):
        return self.tentkco


class TKno(models.Model):
    tentkno = models.CharField(default="", max_length=255, null=True, blank=True)
    mota = models.CharField(default="", max_length=255, null=True, blank=True)
    report_nsp = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "TK nợ"
        verbose_name_plural = "TK nợ"
        ordering = ("-id",)
        app_label = "tienmatnganhang"

    def __int__(self):
        return self.tentkno


class YTno(models.Model):
    tenytno = models.CharField(default="", max_length=255, null=True, blank=True)
    mota = models.CharField(default="", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "YT nợ"
        verbose_name_plural = "YT nợ"
        ordering = ("-id",)
        app_label = "tienmatnganhang"

    def __int__(self):
        return self.tenytno
