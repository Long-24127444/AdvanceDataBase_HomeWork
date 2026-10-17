# CƠ SỞ DỮ LIỆU NÂNG CAO
## BÀI TẬP PHÂN TÍCH DỮ LIỆU
### (Mã bài tập: E01)

**Yêu cầu thực hiện:** NHÓM

---

**Bối cảnh:** Hệ thống đặt thức ăn nhanh (Grab Food)

Hệ thống đặt thức ăn nhanh của GrabFood có nhiệm vụ quản lý và xử lý các đơn đặt hàng của khách hàng từ nhiều nhà hàng khác nhau. Các yêu cầu của hệ thống cần được thiết kế để đảm bảo việc xử lý các đơn đặt hàng nhanh chóng, chính xác, đồng thời hỗ trợ quản lý các hoạt động liên quan như quản lý nhà hàng, tài xế giao hàng, khuyến mãi, và đánh giá dịch vụ.

Một số qui trình chính như:

1. **Đặt món ăn:**
   - Khách hàng tìm kiếm và chọn món ăn từ danh sách các nhà hàng có sẵn.
   - Khách hàng tạo đơn hàng, chọn món ăn và số lượng.
   - Đơn hàng được gửi đến nhà hàng và tài xế được phân công để giao hàng.

2. **Xử lý đơn hàng:**
   - Nhà hàng nhận đơn và bắt đầu chuẩn bị món ăn.
   - Tài xế đến nhà hàng lấy thức ăn sau khi nhà hàng thông báo hoàn tất.
   - Tài xế giao thức ăn đến địa chỉ của khách hàng và cập nhật trạng thái giao hàng.

3. **Thanh toán:**
   - Khách hàng thanh toán thông qua ứng dụng bằng cách sử dụng thẻ tín dụng hoặc ví điện tử.
   - Tổng tiền thanh toán bao gồm phí giao hàng và khuyến mãi (nếu có).

4. **Đánh giá dịch vụ:**
   - Sau khi nhận thức ăn, khách hàng có thể đánh giá nhà hàng và tài xế về chất lượng dịch vụ và thức ăn. Các đánh giá sẽ được ghi nhận để cải thiện dịch vụ.

---

**Yêu cầu:**

1. Điều tra nghiên cứu chi tiết các qui trình nghiệp vụ chính gợi ý như trên, thực hiện viết lại danh sách các qui tắc nghiệp vụ để xác định phạm vi cụ thể cho việc phân tích dữ liệu bài toán.
2. Dựa trên bảng qui tắc nghiệp vụ đã viết, thực hiện phân tích dữ liệu và biểu diễn bằng sơ đồ thực thể kết hợp theo ký hiệu Crow's Foot. **<u>Lưu ý</u>:** bắt buộc lược đồ ER kết quả phải mô phỏng được đầy đủ các khái niệm, mối quan hệ, ... của mô hình ER cơ bản và ER mở rộng.

---

**Hướng dẫn và sản phẩm nộp:**

- Trình bày kết quả file word, toàn bộ nội dung kết quả trên file báo cáo, không link qua phần mềm hay link gián tiếp để xem kết quả.
- Sản phẩm nộp: Báo cáo kết quả gồm: (1) Bảng mô tả qui tắc nghiệp vụ (business rules) đã xây dựng + (2) Mô hình ER đã thiết kế theo bảng mô tả qui tắc nghiệp vụ.
- **Đặt tên file:** `Mảnhóm_MãBT`
- Nộp lên moodle theo thời gian qui định.

---
*GV. TS. NGUYỄN TRẦN MINH THƯ*

# Phân tích yêu cầu

---

## 1. Phạm vi và danh mục thực thể

Nguồn chuẩn về phạm vi, thực thể, quan hệ và bản số là `G01_Scope_Entities.md`. Mô hình sử dụng đúng **14 thực thể** sau:

1. `NguoiDung`
2. `KhachHang`
3. `TaiXe`
4. `ChuNhaHang`
5. `NhaHang`
6. `DanhMuc`
7. `MonAn`
8. `DonHang`
9. `ChiTietDonHang`
10. `KhuyenMai`
11. `ThanhToan`
12. `DanhGia`
13. `DanhGiaNhaHang`
14. `DanhGiaTaiXe`

## 2. Thứ tự thực hiện và bàn giao

Các task phải được thực hiện theo thứ tự dưới đây để tên thực thể, thuộc tính, PK/FK và bản số không bị quyết định lại ở bước vẽ:

### T1-A. Business Rules

- Xây dựng bảng quy tắc nghiệp vụ có mã, nguồn, loại quy tắc, thực thể liên quan và ánh xạ vào mô hình.
- Bao phủ bốn quy trình trong đề: đặt và xử lý món, giao hàng, thanh toán và khuyến mãi, đánh giá; có thể dùng nhóm bổ trợ cho người dùng, nhà hàng và thực đơn.
- Mọi giả định riêng của nhóm phải được đánh dấu `[GĐ]`.

### T1-B. Từ điển dữ liệu

- Hoàn thiện mô tả thuộc tính, miền giá trị, PK và FK dự kiến cho đủ 14 thực thể dựa trên phạm vi và Business Rules đã chốt.
- Dùng `ThanhToan.ThoiGianCapNhat` cho thời điểm hồ sơ thanh toán hiện tại thay đổi trạng thái gần nhất; không dùng thuộc tính thời gian mơ hồ `[GĐ]`.
- Từ điển dữ liệu **phải hoàn thành trước khi bàn giao vẽ ERD**, để T2 không tự bổ sung hoặc thay đổi cấu trúc dữ liệu.

### T2. ERD cơ bản

- Vẽ các thực thể và quan hệ bằng ký hiệu Crow's Foot, thể hiện đúng bản số ở cả hai đầu quan hệ.
- Quan hệ N–N giữa đơn hàng và món ăn được phân rã qua `ChiTietDonHang`.
- Quan hệ `DonHang` — `DanhGia` được vẽ 1–0..N; giới hạn tối đa hai đánh giá được kiểm soát bởi Business Rules, không ghi `(0..2)` trên đường nối Crow's Foot.

### T3. EER

- Bổ sung hai nhóm supertype/subtype `[GĐ]`: `NguoiDung` → `KhachHang`, `TaiXe`, `ChuNhaHang` với discriminator `LoaiND`; `DanhGia` → `DanhGiaNhaHang`, `DanhGiaTaiXe` với discriminator `LoaiDG`. Cả hai nhóm đều Disjoint, Total.
- Thể hiện `ChiTietDonHang` là thực thể yếu, phụ thuộc tồn tại vào `DonHang`, có PK `(MaDH, STT)`.
- Thể hiện các thuộc tính phức hợp, đa trị, dẫn xuất và quan hệ đệ quy đã chốt trong T1-B.

### T4. Tổng hợp Word

- Tổng hợp phạm vi, Business Rules, Từ điển dữ liệu, ERD/EER và phần giải thích vào một file Word duy nhất.
- Giữ nguyên yêu cầu hành chính của đề về sản phẩm nộp, tên file, chèn trực tiếp nội dung vào Word và nộp trên Moodle.

## 3. Các cấu trúc EER phải được mô phỏng

- **Thực thể yếu:** `ChiTietDonHang`, được định danh bởi `DonHang` và khóa riêng phần `STT`.
- **Supertype/subtype:** hai nhóm `NguoiDung` và `DanhGia` nêu tại T3; đều Disjoint, Total và có discriminator `[GĐ]`.
- **Thuộc tính phức hợp:** `NhaHang.DiaChi`; `DonHang.DiaChiGiao`; từng giá trị của `KhachHang.DiaChiGiaoHang`, đều gồm `SoNha`, `Duong`, `Phuong`, `Quan`, `ThanhPho`.
- **Thuộc tính đa trị và phức hợp:** `KhachHang.DiaChiGiaoHang`; `NhaHang.GioMoCua`, trong đó mỗi khung gồm `ThuTrongTuan`, `GioMo`, `GioDong`.
- **Thuộc tính dẫn xuất:** `DonHang.TongTienMon`, `DonHang.GiaTriGiamThucTe` và `DonHang.TongTien`.
- **Quan hệ đệ quy:** `DanhMuc` cha–con.
