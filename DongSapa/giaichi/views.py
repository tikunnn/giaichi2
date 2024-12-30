from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Giaichi, TKno, YTno, Phongban, Nhanvien
from django.template.loader import render_to_string
from django.forms.models import model_to_dict
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

# Create your views here.

# @method_decorator(login_required, name="dispatch")


class GiaiChiCreateAndUpdateView(View):
    model = Giaichi
    template_name = "giaichi_form.html"

    def post(self, request, *args, **kwargs):
        data = request.POST
        obj_id = kwargs.get("pk")
        nhanvien_instance = Nhanvien.objects.get(tennv=data.get("tennv"))
        valid_fields = {
            "nhanvien": nhanvien_instance,
            "hinhthucthanhtoan": data.get("hinhthucthanhtoan"),
            "motathanhtoan": data.get("motathanhtoan"),
            "tiengiaichi": data.get("tiengiaichi"),
            "giaichithuoc": data.get("giaichithuoccongty"),
            "ghichu": data.get("ghichu"),
            "tkno": data.get("tkno"),
            "ytno": data.get("ytno"),
            "guiduyet": data.get("guiduyet"),
            "tieude": data.get("tieude"),
            "vat": data.get("vat"),
            "noidungmota": data.get("editor"),
        }

        try:
            if obj_id:
                obj = get_object_or_404(self.model, id=obj_id)
                for key, value in valid_fields.items():
                    setattr(obj, key, value)
                obj.save()
                message = "Dữ liệu đã được cập nhật thành công"
            else:
                obj = self.model.objects.create(**valid_fields)
                message = "Dữ liệu đã được tạo thành công"

            return JsonResponse({
                "status": "Success",
                "message": message,
                "data": model_to_dict(obj),
            })

        except Exception as e:
            return JsonResponse({"status": "Error", "message": str(e)}, status=500)

    def get(self, request, *args, **kwargs):
        nhanvien = Nhanvien.objects.filter(id=1).first()
        phongban_list = Phongban.objects.all()
        giaichi_list = Giaichi.objects.all().order_by("-created_at")
        paginator = Paginator(giaichi_list, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "nhanvien": nhanvien,
            "phongban_list": phongban_list,
            "page_obj": page_obj,
        }
        return render(request, "giaichi_form.html", context)


class GiaichiDeleteView(View):
    model = Giaichi

    def post(self, request, *args, **kwargs):
        obj_id = kwargs.get("pk")
        try:
            obj = self.model.objects.get(id=obj_id)
            obj.delete()
            return JsonResponse(
                {
                    "status": "Success",
                    "message": f"Giải chi '{obj.tieude}' đã được xóa thành công!",
                }
            )
        except self.model.DoesNotExist:
            return JsonResponse(
                {"status": "Error", "message": "Bản ghi không tồn tại!"}, status=404
            )
        except Exception as e:
            print(f"Có lỗi xảy ra khi đang xóa giải chi ID: {
                  obj_id}: {str(e)}")
            return JsonResponse({"status": "Error", "message": str(e)}, status=500)


class GiaichiDetailView(View):
    model = Giaichi

    def get(self, request, *args, **kwargs):
        obj_id = kwargs.get("pk")

        try:
            obj = Giaichi.objects.get(id=obj_id)
            return JsonResponse({
                "status": "Success",
                "data": obj.to_dict()
            })
        except self.model.DoesNotExist:
            return JsonResponse(
                {"status": "Error", "message": "Bản ghi không tồn tại!"}, status=404
            )
