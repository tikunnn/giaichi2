$(document).ready(function () {
  reloadTable();
  $("form").submit(function (event) {
    event.preventDefault();
    var formData = new FormData(this);
    var itemId = $("#itemId").val();
    var url = itemId ? `update/${itemId}/` : "create/";
    $("form")
      .find("input, select, textarea")
      .each(function () {
        var name = $(this).attr("name");
        var value = $(this).val();

        if (value && name !== "csrfmiddlewaretoken") {
          formData.append(name, value);
        }
        if (name === "editor") {
          formData.append(name, CKEDITOR.instances["editor"].getData());
        }
      });

    for (const [key, value] of formData.entries()) {
      console.log(`${key}: ${value}`);
    }

    var fileInput = $('input[type="file"]')[0];
    if (fileInput && fileInput.files.length > 0) {
      formData.append("file", fileInput.files[0]);
    }
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
      url: url,
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      headers: {
        "X-CSRFToken": csrfToken,
      },
      success: function (response) {
        if (
          response.status == "Success" &&
          (typeof itemId === "undefined" || itemId == null)
        ) {
          $("#formModal").modal("hide");
          $("form")[0].reset();

          var newRow = $("<tr>", { id: "item-" + response.data.id })
            .append($("<td>").text(response.data.id))
            .append($("<td>").text(response.data.nhanvien))
            .append($("<td>").text(response.data.file_hoadon))
            .append($("<td>").text(response.data.hinhthucthanhtoan))
            .append($("<td>").text(response.data.nhanvien.email))
            .append($("<td>").text(response.data.tiengiaichi))
            .append($("<td>").text(response.data.thongtinnhanvien))
            .append($("<td>").text(response.data.giaichithuoc))
            .append($("<td>").text(response.data.so_bn))
            .append($("<td>").text(response.data.id_congno))
            .append($("<td>").text(response.data.ghichu))
            .append($("<td>").text(response.data.tkno))
            .append($("<td>").text(response.data.ytno))
            .append($("<td>").text(response.data.vat))
            .append($("<td>").text(response.data.giaichi))
            .append($("<td>").text(response.data.tieude))
            .append($("<td>").text(response.data.get_guiduyet_display))
            .append($("<td>").html(response.data.noidungmota))
            .append(
              $("<td>").html(`
            <div class="dropdown">
              <button class="btn btn-light btn-sm dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
              </button>
              <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <li><button class="delete-btn dropdown-item" data-id="${response.data.id}" type="button">Xóa</button></li>
                <li><button class="dropdown-item" onclick="updateRow(this)">Cập nhật</button></li>
              </ul>
            </div>
          `)
            );
          $("#item-body").append(newRow);
          $("#formModal").modal("hide");
          $("form")[0].reset();
          Swal.fire({
            icon: "success",
            title: "Success",
            text: "Tạo giải chi thành công!",
            confirmButtonText: "Đóng",
            confirmButtonColor: "#0066FF",
          });
          reloadTable();
        } else if (response.status == "Success" && itemId != null) {
          var rowToUpdate = $("#item-" + itemId);

          rowToUpdate
            .find("td:nth-child(2)")
            .text(response.data.nhanvien)
            .end()
            .find("td:nth-child(3)")
            .text(response.data.file_hoadon)
            .end()
            .find("td:nth-child(4)")
            .text(response.data.hinhthucthanhtoan)
            .end()
            .find("td:nth-child(5)")
            .text(response.data.nhanvien.email)
            .end()
            .find("td:nth-child(6)")
            .text(response.data.tiengiaichi)
            .end()
            .find("td:nth-child(7)")
            .text(response.data.thongtinnhanvien)
            .end()
            .find("td:nth-child(8)")
            .text(response.data.giaichithuoc)
            .end()
            .find("td:nth-child(9)")
            .text(response.data.so_bn)
            .end()
            .find("td:nth-child(10)")
            .text(response.data.id_congno)
            .end()
            .find("td:nth-child(11)")
            .text(response.data.ghichu)
            .end()
            .find("td:nth-child(12)")
            .text(response.data.tkno)
            .end()
            .find("td:nth-child(13)")
            .text(response.data.ytno)
            .end()
            .find("td:nth-child(14)")
            .text(response.data.vat)
            .end()
            .find("td:nth-child(15)")
            .text(response.data.giaichi)
            .end()
            .find("td:nth-child(16)")
            .text(response.data.tieude)
            .end()
            .find("td:nth-child(17)")
            .text(response.data.get_guiduyet_display)
            .end()
            .find("td:nth-child(18)")
            .html(response.data.noidungmota);

          $("#formModal").modal("hide");
          $("form")[0].reset();
          Swal.fire({
            icon: "success",
            title: "Success",
            text: "Cập nhật giải chi thành công!",
            confirmButtonText: "Đóng",
            confirmButtonColor: "#0066FF",
          });
          reloadTable();
        } else {
          Swal.fire({
            icon: "error",
            title: "Error",
            text: response.message || "Đã có lỗi xảy ra khi tạo giải chi!",
            confirmButtonText: "OK",
            confirmButtonColor: "#D33",
          });
        }
      },
      error: function () {
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "Đã có lỗi xảy ra khi tạo giải chi!",
          confirmButtonText: "OK",
          confirmButtonColor: "#D33",
        });
      },
    });
  });

  $(document).on("click", ".delete-btn", function (event) {
    var id = $(this).data("id");
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    Swal.fire({
      title: "Are you sure?",
      text: "Bạn có chắc chắn muốn xóa giải chi này không?",
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Xóa",
      cancelButtonText: "Hủy",
      confirmButtonColor: "#D33",
      cancelButtonColor: "#3085d6",
    }).then((result) => {
      if (result.isConfirmed) {
        $.ajax({
          url: `delete/${id}/`,
          type: "POST",
          headers: {
            "X-CSRFToken": csrfToken,
          },
          success: function (response) {
            if (response.status === "Success") {
              $("form")[0].reset();
              Swal.fire({
                icon: "success",
                title: "Success",
                text: "Xóa giải chi thành công!",
                confirmButtonText: "Đóng",
                confirmButtonColor: "#0066FF",
              });
              $(`#item-${id}`).remove();
              reloadTable();
            } else {
              Swal.fire({
                icon: "error",
                title: "Error",
                text: response.message || "Đã xảy ra lỗi khi xóa giải chi.",
                confirmButtonText: "OK",
                confirmButtonColor: "#D33",
              });
            }
          },
          error: function () {
            Swal.fire({
              icon: "error",
              title: "Error",
              text: "Không thể xóa giải chi do lỗi hệ thống.",
              confirmButtonText: "OK",
              confirmButtonColor: "#D33",
            });
          },
        });
      }
    });
  });

  $(document).on("click", ".edit-btn", function (event) {
    event.preventDefault();
    const button = event.target;
    const itemId = button.dataset.id;

    const formModal = new bootstrap.Modal(document.getElementById("formModal"));
    formModal.show();

    fetch(`/giaichi/${itemId}/`)
      .then((response) => response.json())
      .then((response) => {
        $("#itemId").val(response.data["id"]);
        document.getElementById("formModalLabel").innerText =
          "Cập Nhật Giải Chi";
        document.getElementsByName("tennv")[0].value =
          response.data["nhanvien"];
        dropdownHTTT = document.getElementById("hinhthucthanhtoan");
        dropdownCodeNA = document.getElementById("code-na");
        dropdownPhongBan = document.getElementById("luanchuyennoitbo-select");
        for (let option of dropdownHTTT.options) {
          if (option.text === response.data["hinhthucthanhtoan"]) {
            option.selected = true;
            break;
          }
        }
        document.getElementsByName("motathanhtoan")[0].value =
          response.data["motathanhtoan"];
        document.getElementsByName("tiengiaichi")[0].value =
          response.data["tiengiaichi"];
        document.getElementsByName("ghichu")[0].value = response.data["ghichu"];
        document.getElementsByName("tieude")[0].value = response.data["tieude"];
        if (CKEDITOR.instances["editor"]) {
          CKEDITOR.instances["editor"].setData(response.data["noidungmota"]);
        }
      })
      .catch((error) => console.error("Error loading data:", error));
  });
});

$(document).on("click", ".page-link-ajax", function (event) {
  event.preventDefault();

  var url = $(this).data("href");

  $.ajax({
    url: url,
    type: "GET",
    success: function (response) {
      $("#item-body").html(response.data.html);
      $(".pagination").html(response.data.pagination);
    },
    error: function () {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "Không thể tải dữ liệu phân trang.",
        confirmButtonText: "OK",
        confirmButtonColor: "#D33",
      });
    },
  });
});

function reloadTable() {
  $("#item-body").load(location.href + " #item-body > *");
}
