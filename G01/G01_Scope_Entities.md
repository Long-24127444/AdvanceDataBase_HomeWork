# PHẠM VI HỆ THỐNG

---

## 1. MỤC TIÊU HỆ THỐNG
Hệ thống có nhiệm vụ quản lý và xử lý toàn bộ vòng đời của đơn đặt hàng từ khách hàng, hỗ trợ các nhà hàng trong việc tiếp nhận món ăn, điều phối tài xế giao hàng, xử lý thanh toán và ghi nhận đánh giá dịch vụ sau khi hoàn tất.

---

## 2. PHẠM VI XỬ LÝ NẰM TRONG HỆ THỐNG (IN-SCOPE)

Phạm vi quản lý dữ liệu của bài toán tập trung vào 4 quy trình nghiệp vụ cốt lõi theo đề bài:

### 2.1. Phân hệ Quản lý Người dùng & Đối tác (User & Partner Management)
* **Người dùng chung - Supertype (`NguoiDung`):** Đây là thực thể cha quản lý thông tin định danh cơ bản (Mã người dùng, Họ tên, Số điện thoại, Email).
* **Khách hàng (`KhachHang`):** Quản lý địa chỉ giao hàng, lịch sử đặt hàng.
* **Tài xế (`TaiXe`):** Quản lý biển số xe và trạng thái hoạt động (Rảnh/Đang giao).
* **Chủ nhà hàng (`ChuNhaHang`):** Quản lý quan hệ sở hữu nhà hàng.
* **Nhà hàng (`NhaHang`):** Quản lý thông tin nhà hàng, giờ mở/đóng cửa, địa chỉ kinh doanh, trạng thái tiếp nhận đơn.

### 2.2. Phân hệ Thực đơn & Đặt món (Menu & Order Management)
* **Danh mục & Món ăn (`DanhMuc`, `MonAn`):** Quản lý thực đơn của từng nhà hàng (Tên món, Giá tiền, Trạng thái còn/hết món).
* **Đơn hàng (`DonHang`):** Quản lý chuỗi trạng thái *Chờ nhận đơn → Đang chuẩn bị → Đã chuẩn bị xong → Đã phân công tài xế → Đang giao → Hoàn thành* và trạng thái kết thúc *Đã hủy*, cùng thời gian tạo đơn, địa chỉ giao được chụp tại thời điểm đặt và tổng chi phí.
* **Chi tiết đơn hàng (`ChiTietDonHang`):** Lưu trữ danh sách món ăn, số lượng và đơn giá thực tế tại thời điểm khách đặt hàng.

### 2.3. Phân hệ Thanh toán & Khuyến mãi (Payment & Promotion)
* **Khuyến mãi (`KhuyenMai`):** Quản lý các mã giảm giá (Mã voucher, Phần trăm giảm/Số tiền giảm, Điều kiện áp dụng, Giá trị giảm tối đa).
* **Thanh toán (`ThanhToan`):** Ghi nhận hồ sơ thanh toán hiện tại của đơn hàng (Phương thức: *Thẻ tín dụng, Ví điện tử*; trạng thái: *Chờ thanh toán, Thành công, Thất bại*), không lưu danh sách từng lần thử thanh toán; `ThoiGianCapNhat` ghi thời điểm hồ sơ thay đổi trạng thái gần nhất `[GĐ]`.
* **Tính toán chi phí:** Tự động tính `TongTien = TongTienMon + PhiGiaoHang - GiaTriGiamThucTe`.

### 2.4. Phân hệ Đánh giá Dịch vụ (Review & Rating)
* **Đánh giá Nhà hàng (`DanhGiaNhaHang`):** Cho phép khách hàng chấm điểm sao (1 - 5 sao) và để lại bình luận về chất lượng món ăn/dịch vụ của nhà hàng sau khi hoàn tất đơn hàng.
* **Đánh giá Tài xế (`DanhGiaTaiXe`):** Cho phép khách hàng chấm điểm sao và bình luận về thái độ, thời gian giao hàng của tài xế.

---

## 3. PHẠM VI KHÔNG XỬ LÝ TRONG HỆ THỐNG (OUT-OF-SCOPE)

Để tập trung vào mô hình hóa dữ liệu cốt lõi và tránh làm phình to bài toán, các tính năng sau đây được **loại trừ khỏi phạm vi thiết kế**:

1. **Quản lý biến động số dư Ví điện tử / Ngân hàng:** Hệ thống chỉ lưu trạng thái kết quả giao dịch thanh toán thành công/thất bại từ cổng thanh toán bên thứ ba, không quản lý quy trình nạp/rút tiền hay số dư ví của khách hàng.
2. **Theo dõi vị trí GPS thời gian thực (Real-time Tracking):** Hệ thống không lưu tọa độ GPS liên tục trong quá trình di chuyển; phạm vi hiện tại cũng không có thuộc tính địa chỉ của `TaiXe`.
3. **Phân hệ Nhắn tin / Gọi điện (In-app Chat & Calling):** Không lưu trữ nhật ký cuộc gọi hoặc tin nhắn trò chuyện giữa Khách hàng, Tài xế và Nhà hàng.
4. **Hệ thống đề xuất món ăn tự động (AI Recommendation System):** Không xử lý dữ liệu gợi ý món ăn nâng cao dựa trên thuật toán học máy.
5. **Quản lý kho nguyên liệu của Nhà hàng:** Không quản lý tồn kho chi tiết (như số lượng thịt, rau, gia vị...) bên trong bếp của nhà hàng.

## 4. DANH MỤC THỰC THỂ (ENTITY LIST)

Dựa trên phạm vi hệ thống, bài toán gồm **14 thực thể**.

### 4.1. Bảng danh mục thực thể

| # | Thực thể | Loại | Mô tả | Thuộc tính chính | PK |
|---|---|---|---|---|---|
| 1 | `NguoiDung` | Supertype | Thông tin định danh chung của mọi người dùng hệ thống | MaND, HoTen, SDT, Email, LoaiND | MaND |
| 2 | `KhachHang` | Subtype của `NguoiDung` | Người đặt món, đánh giá dịch vụ | DiaChiGiaoHang (đa trị, phức hợp) | MaND |
| 3 | `TaiXe` | Subtype của `NguoiDung` | Người nhận đơn và giao hàng | BienSoXe, TrangThaiHoatDong (Rảnh/Đang giao) | MaND |
| 4 | `ChuNhaHang` | Subtype của `NguoiDung` | Chủ sở hữu/quản lý nhà hàng | (kế thừa từ `NguoiDung`) | MaND |
| 5 | `NhaHang` | Thực thể mạnh | Nhà hàng bán món trên hệ thống | MaNH, TenNH, DiaChi (phức hợp), GioMoCua (đa trị và phức hợp), TrangThaiNhanDon | MaNH |
| 6 | `DanhMuc` | Thực thể mạnh | Nhóm món ăn trong thực đơn nhà hàng, có thể phân cấp cha–con | MaDM, TenDM | MaDM |
| 7 | `MonAn` | Thực thể mạnh | Món ăn trong thực đơn | MaMon, TenMon, Gia, TrangThai (Còn/Hết) | MaMon |
| 8 | `DonHang` | Thực thể mạnh | Đơn đặt món của khách | MaDH, ThoiGianTao, TrangThai, DiaChiGiao (phức hợp), PhiGiaoHang, TongTienMon (dẫn xuất), GiaTriGiamThucTe (dẫn xuất), TongTien (dẫn xuất) | MaDH |
| 9 | `ChiTietDonHang` | Thực thể yếu (phụ thuộc `DonHang`) | Từng dòng món trong đơn | STT, SoLuong, DonGia (tại thời điểm đặt) | (MaDH, STT) |
| 10 | `KhuyenMai` | Thực thể mạnh | Mã giảm giá | MaKM, MaVoucher, LoaiGiam, GiaTriGiam, DieuKienApDung, GiamToiDa, NgayBatDau, NgayKetThuc | MaKM |
| 11 | `ThanhToan` | Thực thể mạnh | Hồ sơ thanh toán hiện tại của một đơn hàng `[GĐ]` | MaTT, PhuongThuc, TrangThai, SoTien, ThoiGianCapNhat | MaTT |
| 12 | `DanhGia` | Supertype | Thông tin chung của một đánh giá | MaDG, LoaiDG, SoSao (1–5), BinhLuan, ThoiGian | MaDG |
| 13 | `DanhGiaNhaHang` | Subtype của `DanhGia` | Đánh giá chất lượng món ăn/nhà hàng | (kế thừa từ `DanhGia`) | MaDG |
| 14 | `DanhGiaTaiXe` | Subtype của `DanhGia` | Đánh giá thái độ, thời gian giao của tài xế | (kế thừa từ `DanhGia`) | MaDG |

### 4.2. Ràng buộc kế thừa (Supertype / Subtype)

| Supertype | Subtype | Discriminator | Disjoint / Overlap | Total / Partial |
|---|---|---|---|---|
| `NguoiDung` | `KhachHang`, `TaiXe`, `ChuNhaHang` | `LoaiND` | Disjoint (mỗi người chỉ một vai trò) | Total (mỗi người dùng phải thuộc một vai trò) `[GĐ]` |
| `DanhGia` | `DanhGiaNhaHang`, `DanhGiaTaiXe` | `LoaiDG` | Disjoint (mỗi đánh giá chỉ dành cho một đối tượng) | Total `[GĐ]` |

### 4.3. Quy ước đặt tên

- Tên thực thể và thuộc tính dùng danh từ số ít, PascalCase, không dấu; tên phải khớp đúng bảng 4.1.
- PK dùng `Ma` + viết tắt thực thể; subtype dùng lại PK của supertype. FK trùng tên PK được tham chiếu, trừ các tên theo vai trò như `MaKH`, `MaTX`, `MaChu`, `MaDMCha` và phải ghi rõ đích tham chiếu.
- Tên quan hệ dùng động từ hoặc cụm động từ có nghĩa nghiệp vụ. Mã Business Rule có dạng `BR-<NHOM>-<NN>` và liên tục trong từng nhóm.

### 4.4. Giá trị liệt kê và miền hữu hạn

| Thuộc tính | Giá trị cho phép |
|---|---|
| `NguoiDung.LoaiND` | Khách hàng, Tài xế, Chủ nhà hàng |
| `DanhGia.LoaiDG` | Nhà hàng, Tài xế |
| `DonHang.TrangThai` | Chờ nhận đơn → Đang chuẩn bị → Đã chuẩn bị xong → Đã phân công tài xế → Đang giao → Hoàn thành; hoặc Đã hủy |
| `NhaHang.TrangThaiNhanDon` | Đang nhận đơn, Tạm ngừng nhận đơn |
| `ThanhToan.PhuongThuc` | Thẻ tín dụng, Ví điện tử |
| `ThanhToan.TrangThai` | Chờ thanh toán, Thành công, Thất bại |
| `TaiXe.TrangThaiHoatDong` | Rảnh, Đang giao |
| `MonAn.TrangThai` | Còn món, Hết món |
| `KhuyenMai.LoaiGiam` | Phần trăm, Số tiền |
| `DanhGia.SoSao` | Số nguyên từ 1 đến 5 |

## 5. QUAN HỆ, BẢN SỐ VÀ PK/FK

> `[GĐ]` đánh dấu bản số hoặc cấu trúc quan hệ do nhóm chốt khi đề bài chỉ nêu quan hệ nghiệp vụ nhưng không quy định chi tiết cách mô hình hóa.

| # | Quan hệ hai chiều | Bản số | PK/FK dự kiến | BR hỗ trợ |
|---|---|---|---|---|
| 1 | Mỗi `NhaHang` thuộc đúng một `ChuNhaHang`; mỗi `ChuNhaHang` sở hữu ít nhất một `NhaHang` `[GĐ]`. | `ChuNhaHang` 1..N — 1 `NhaHang` | `NhaHang.MaChu → ChuNhaHang.MaND` | BR-USR-07 |
| 2 | Mỗi `DanhMuc` thuộc đúng một `NhaHang`; mỗi `NhaHang` có ít nhất một `DanhMuc` `[GĐ]`. | `NhaHang` 1..N — 1 `DanhMuc` | `DanhMuc.MaNH → NhaHang.MaNH` | BR-USR-11 |
| 3 | Mỗi `DanhMuc` có 0..1 danh mục cha; mỗi danh mục cha có 0..N danh mục con `[GĐ]`. | `DanhMuc` cha 0..N — 0..1 `DanhMuc` con | `DanhMuc.MaDMCha → DanhMuc.MaDM`, cho phép rỗng | BR-USR-12 |
| 4 | Mỗi `MonAn` thuộc đúng một `DanhMuc`; mỗi `DanhMuc` có 0..N `MonAn` `[GĐ]`. | `DanhMuc` 0..N — 1 `MonAn` | `MonAn.MaDM → DanhMuc.MaDM` | BR-USR-14 |
| 5 | Mỗi `DonHang` do đúng một `KhachHang` tạo; mỗi `KhachHang` tạo 0..N `DonHang`. | `KhachHang` 0..N — 1 `DonHang` | `DonHang.MaKH → KhachHang.MaND` | BR-ORD-01 |
| 6 | Mỗi `DonHang` thuộc đúng một `NhaHang`; mỗi `NhaHang` có 0..N `DonHang`. | `NhaHang` 0..N — 1 `DonHang` | `DonHang.MaNH → NhaHang.MaNH` | BR-ORD-02 |
| 7 | Mỗi `DonHang` gồm ít nhất một `ChiTietDonHang`; mỗi `ChiTietDonHang` thuộc đúng một `DonHang`. | `DonHang` 1..N — 1 `ChiTietDonHang` | `ChiTietDonHang.MaDH → DonHang.MaDH`; PK yếu `(MaDH, STT)` | BR-ORD-03, BR-ORD-04 |
| 8 | Mỗi `ChiTietDonHang` tham chiếu đúng một `MonAn`; mỗi `MonAn` xuất hiện trong 0..N `ChiTietDonHang`. | `MonAn` 0..N — 1 `ChiTietDonHang` | `ChiTietDonHang.MaMon → MonAn.MaMon` | BR-ORD-05 |
| 9 | Mỗi `DonHang` có 0..1 `TaiXe`; mỗi `TaiXe` giao 0..N `DonHang` theo thời gian `[GĐ]`. | `TaiXe` 0..N — 0..1 `DonHang` | `DonHang.MaTX → TaiXe.MaND`, cho phép rỗng | BR-DEL-01 |
| 10 | Mỗi `DonHang` dùng 0..1 `KhuyenMai`; mỗi `KhuyenMai` được dùng cho 0..N `DonHang` `[GĐ]`. | `KhuyenMai` 0..N — 0..1 `DonHang` | `DonHang.MaKM → KhuyenMai.MaKM`, cho phép rỗng | BR-PAY-11 |
| 11 | Mỗi `DonHang` có đúng một `ThanhToan`; mỗi `ThanhToan` thuộc đúng một `DonHang` `[GĐ]`. | 1 — 1, bắt buộc hai phía | `ThanhToan.MaDH → DonHang.MaDH`, bắt buộc và duy nhất | BR-PAY-01 |
| 12 | Mỗi `DanhGia` thuộc đúng một `DonHang`; mỗi `DonHang` có 0..N `DanhGia` trên quan hệ Crow's Foot `[GĐ]`. | `DonHang \|\| — o{ DanhGia` | `DanhGia.MaDH → DonHang.MaDH` | BR-REV-01, BR-REV-09, BR-REV-10 |
| 13 | Mỗi `DanhGiaNhaHang` dành cho đúng một `NhaHang`; mỗi `NhaHang` có 0..N `DanhGiaNhaHang` `[GĐ]`. | `NhaHang` 0..N — 1 `DanhGiaNhaHang` | `DanhGiaNhaHang.MaDG → DanhGia.MaDG` (PK+FK); `MaNH → NhaHang.MaNH` | BR-REV-03 |
| 14 | Mỗi `DanhGiaTaiXe` dành cho đúng một `TaiXe`; mỗi `TaiXe` có 0..N `DanhGiaTaiXe` `[GĐ]`. | `TaiXe` 0..N — 1 `DanhGiaTaiXe` | `DanhGiaTaiXe.MaDG → DanhGia.MaDG` (PK+FK); `MaTX → TaiXe.MaND` | BR-REV-04 |

> Trên ERD cơ bản, quan hệ `DonHang` — `DanhGia` dùng Crow's Foot 1–0..N. Giới hạn tối đa hai đánh giá không đặt trên đường nối: mỗi đơn tối đa một `DanhGiaNhaHang` và tối đa một `DanhGiaTaiXe` theo BR-REV-09 và BR-REV-10.

## 6. CẤU TRÚC THUỘC TÍNH VÀ CÔNG THỨC ĐÃ CHỐT

- `KhachHang.DiaChiGiaoHang` là thuộc tính đa trị và phức hợp. `NhaHang.DiaChi` và `DonHang.DiaChiGiao` là thuộc tính phức hợp. Mỗi địa chỉ gồm `SoNha`, `Duong`, `Phuong`, `Quan`, `ThanhPho`.
- Khi tạo đơn, địa chỉ giao được chọn từ một giá trị hiện có của `KhachHang.DiaChiGiaoHang` rồi sao chép vào `DonHang.DiaChiGiao`; sửa hoặc xóa địa chỉ của khách sau đó không làm đổi đơn cũ `[GĐ]`.
- `NhaHang.GioMoCua` là thuộc tính đa trị và phức hợp; mỗi khung gồm `ThuTrongTuan`, `GioMo`, `GioDong`. Mỗi nhà hàng có ít nhất một khung và `GioMo < GioDong` `[GĐ]`.
- `ThanhToan.ThoiGianCapNhat` là thời điểm hồ sơ thanh toán hiện tại thay đổi trạng thái gần nhất. Khi tạo hồ sơ, giá trị này là thời điểm tạo; khi nhận kết quả hoặc bắt đầu thử lại, hệ thống cập nhật giá trị này `[GĐ]`.
- Chỉ hồ sơ thanh toán `Thất bại` được thử lại. Khi thử lại, trạng thái chuyển về `Chờ thanh toán`; trạng thái `Thành công` là trạng thái kết thúc `[GĐ]`.
- `TongTienMon = Σ(SoLuong × DonGia)`.
- Không có khuyến mãi: `GiaTriGiamThucTe = 0`.
- Khuyến mãi phần trăm: `GiaTriGiamThucTe = min(TongTienMon × GiaTriGiam / 100, GiamToiDa, TongTienMon)`.
- Khuyến mãi số tiền: `GiaTriGiamThucTe = min(GiaTriGiam, TongTienMon)`.
- `TongTien = TongTienMon + PhiGiaoHang - GiaTriGiamThucTe`.
- Miền khuyến mãi: `GiaTriGiam > 0`; nếu `LoaiGiam = "Phần trăm"` thì `GiaTriGiam ≤ 100`; `DieuKienApDung ≥ 0`; `GiamToiDa ≥ 0`; `NgayBatDau ≤ NgayKetThuc` `[GĐ]`.

