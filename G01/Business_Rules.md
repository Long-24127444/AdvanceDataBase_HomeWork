# BUSINESS RULES


| Mã | Phát biểu quy tắc | Loại | Thực thể liên quan | Ánh xạ vào mô hình | Nguồn |
|---|---|---|---|---|---|
| BR-ORD-01 | Mỗi đơn hàng phải do đúng một khách hàng tạo; mỗi khách hàng có thể tạo không hoặc nhiều đơn hàng. | Cấu trúc | DonHang, KhachHang | KhachHang 1 — N DonHang; mandatory phía DonHang (FK MaKH → KhachHang.MaND) | Đề §Quy trình 1 |
| BR-ORD-02 | Mỗi đơn hàng phải thuộc đúng một nhà hàng; mỗi nhà hàng có thể có không hoặc nhiều đơn hàng. | Cấu trúc | DonHang, NhaHang | NhaHang 1 — N DonHang; mandatory phía DonHang (FK MaNH → NhaHang.MaNH) | Đề §Quy trình 1 |
| BR-ORD-03 | Mỗi đơn hàng phải gồm ít nhất một dòng chi tiết đơn hàng; mỗi dòng chi tiết đơn hàng phải thuộc đúng một đơn hàng. | Cấu trúc | DonHang, ChiTietDonHang | DonHang 1 — N ChiTietDonHang; identifying relationship; PK ghép (MaDH, STT) | Đề §Quy trình 1 |
| BR-ORD-04 | Khi một đơn hàng bị xóa thì mọi dòng chi tiết đơn hàng của đơn đó bị xóa theo. | Cấu trúc | ChiTietDonHang, DonHang | Weak entity: ChiTietDonHang phụ thuộc tồn tại vào DonHang | [GĐ] |
| BR-ORD-05 | Mỗi dòng chi tiết đơn hàng phải tham chiếu đúng một món ăn; mỗi món ăn có thể xuất hiện trong không hoặc nhiều dòng chi tiết đơn hàng. | Cấu trúc | ChiTietDonHang, MonAn | MonAn 1 — N ChiTietDonHang (FK MaMon → MonAn.MaMon); N–N giữa DonHang và MonAn được phân rã qua ChiTietDonHang | Đề §Quy trình 1 |
| BR-ORD-06 | Mỗi dòng chi tiết đơn hàng chỉ tham chiếu món ăn thuộc nhà hàng của đơn hàng đó. | Ràng buộc | ChiTietDonHang, MonAn, DanhMuc, DonHang, NhaHang | Kiểm tra nhà hàng của MonAn (qua DanhMuc) trùng DonHang.MaNH | Đề §Quy trình 1 |
| BR-ORD-07 | Mỗi món ăn chỉ xuất hiện trong tối đa một dòng chi tiết đơn hàng của cùng một đơn hàng. | Ràng buộc | ChiTietDonHang, MonAn | Duy nhất (MaDH, MaMon) | [GĐ] |
| BR-ORD-08 | SoLuong của mỗi dòng chi tiết đơn hàng phải là số nguyên lớn hơn 0. | Ràng buộc | ChiTietDonHang | SoLuong: Số nguyên, SoLuong > 0 | Đề §Quy trình 1 |
| BR-ORD-09 | DonGia của mỗi dòng chi tiết đơn hàng bằng Gia của món ăn tại thời điểm khách hàng tạo đơn hàng. | Ràng buộc | ChiTietDonHang, MonAn | DonGia sao chép từ MonAn.Gia lúc đặt | G01-Scope §2.2; `[GĐ]` |
| BR-ORD-10 | Việc thay đổi Gia của món ăn không làm thay đổi DonGia của các dòng chi tiết đơn hàng đã tạo. | Ràng buộc | ChiTietDonHang, MonAn | DonGia không cập nhật theo MonAn.Gia | G01-Scope §2.2; `[GĐ]` |
| BR-ORD-11 | Chỉ khi món ăn có TrangThai là "Còn món" thì khách hàng mới được thêm món đó vào đơn hàng. | Điều kiện | MonAn, ChiTietDonHang | Kiểm tra MonAn.TrangThai khi thêm dòng chi tiết | [GĐ] |
| BR-ORD-12 | Chỉ khi nhà hàng đang tiếp nhận đơn thì khách hàng mới được tạo đơn hàng gửi đến nhà hàng đó. | Điều kiện | NhaHang, DonHang | Kiểm tra NhaHang.TrangThaiNhanDon khi tạo đơn | [GĐ] |
| BR-ORD-13 | TrangThai của đơn hàng chỉ nhận một trong các giá trị: "Chờ nhận đơn", "Đang chuẩn bị", "Đã chuẩn bị xong", "Đã phân công tài xế", "Đang giao", "Hoàn thành", "Đã hủy". | Ràng buộc | DonHang | DonHang.TrangThai: Liệt kê (G01-Scope §4.4) | Đề §Quy trình 2; `[GĐ]` |
| BR-ORD-14 | Mỗi đơn hàng khi được tạo có TrangThai là "Chờ nhận đơn". | Trạng thái | DonHang | Giá trị khởi đầu của DonHang.TrangThai | Đề §Quy trình 1; `[GĐ]` |
| BR-ORD-15 | TrangThai của đơn hàng chỉ được chuyển theo thứ tự: "Chờ nhận đơn", "Đang chuẩn bị", "Đã chuẩn bị xong", "Đã phân công tài xế", "Đang giao", "Hoàn thành". | Trạng thái | DonHang | Chuỗi trạng thái của DonHang.TrangThai | Đề §Quy trình 2; `[GĐ]` |
| BR-ORD-16 | Đơn hàng chỉ được chuyển từ "Chờ nhận đơn" sang "Đang chuẩn bị" khi nhà hàng nhận đơn. | Trạng thái | DonHang, NhaHang | Chuyển trạng thái do nhà hàng thực hiện | Đề §Quy trình 2 |
| BR-ORD-17 | Đơn hàng chỉ được chuyển từ "Đang chuẩn bị" sang "Đã chuẩn bị xong" khi nhà hàng thông báo hoàn tất món ăn. | Trạng thái | DonHang, NhaHang | Chuyển trạng thái do nhà hàng thực hiện | Đề §Quy trình 2 |
| BR-ORD-18 | Chỉ khi đơn hàng có TrangThai là "Chờ nhận đơn" thì khách hàng mới được hủy đơn hàng đó. | Điều kiện | DonHang, KhachHang | Chuyển "Chờ nhận đơn" → "Đã hủy" | [GĐ] |
| BR-ORD-19 | Đơn hàng có TrangThai là "Hoàn thành" hoặc "Đã hủy" không được chuyển sang trạng thái khác. | Trạng thái | DonHang | Hai trạng thái kết thúc của DonHang.TrangThai | [GĐ] |
| BR-DEL-01 | Mỗi đơn hàng có thể được giao bởi tối đa một tài xế; mỗi tài xế có thể giao không hoặc nhiều đơn hàng theo thời gian. | Cấu trúc | DonHang, TaiXe | TaiXe 1 — N DonHang; optional phía DonHang (FK MaTX → TaiXe.MaND, cho phép rỗng) | Đề §Quy trình 1, §Quy trình 2; `[GĐ]` |
| BR-DEL-02 | TrangThaiHoatDong của tài xế chỉ nhận một trong hai giá trị: "Rảnh" hoặc "Đang giao". | Ràng buộc | TaiXe | TaiXe.TrangThaiHoatDong: Liệt kê (G01-Scope §4.4) | G01-Scope §2.1; `[GĐ]` |
| BR-DEL-03 | Chỉ khi tài xế có TrangThaiHoatDong là "Rảnh" thì tài xế mới được phân công đơn hàng mới. | Điều kiện | TaiXe, DonHang | Kiểm tra TaiXe.TrangThaiHoatDong khi phân công | [GĐ] |
| BR-DEL-04 | Đơn hàng chỉ được chuyển từ "Đã chuẩn bị xong" sang "Đã phân công tài xế" khi có một tài xế "Rảnh" nhận đơn. | Trạng thái | DonHang, TaiXe | Gán DonHang.MaTX khi chuyển trạng thái | Đề §Quy trình 1, §Quy trình 2; `[GĐ]` |
| BR-DEL-05 | Khi đơn hàng chuyển sang "Đã phân công tài xế" thì TrangThaiHoatDong của tài xế được phân công chuyển thành "Đang giao". | Trạng thái | DonHang, TaiXe | Đồng bộ TaiXe.TrangThaiHoatDong với DonHang.TrangThai | [GĐ] |
| BR-DEL-06 | Đơn hàng chỉ được chuyển từ "Đã phân công tài xế" sang "Đang giao" khi tài xế đã lấy món tại nhà hàng. | Trạng thái | DonHang, TaiXe, NhaHang | Chuyển trạng thái do tài xế thực hiện | Đề §Quy trình 2; `[GĐ]` |
| BR-DEL-07 | Chỉ tài xế được phân công cho đơn hàng mới được cập nhật trạng thái giao hàng của đơn hàng đó. | Điều kiện | TaiXe, DonHang | Người cập nhật phải trùng DonHang.MaTX | Đề §Quy trình 2; `[GĐ]` |
| BR-DEL-08 | Đơn hàng chỉ được chuyển từ "Đang giao" sang "Hoàn thành" khi tài xế xác nhận đã giao thức ăn đến khách hàng. | Trạng thái | DonHang, TaiXe | Chuyển trạng thái do tài xế thực hiện | Đề §Quy trình 2; `[GĐ]` |
| BR-DEL-09 | Khi đơn hàng chuyển sang "Hoàn thành" thì TrangThaiHoatDong của tài xế giao đơn hàng đó chuyển thành "Rảnh". | Trạng thái | DonHang, TaiXe | Đồng bộ TaiXe.TrangThaiHoatDong với DonHang.TrangThai | [GĐ] |
| BR-DEL-10 | Khi tạo đơn hàng, DiaChiGiao của đơn phải được chọn từ một giá trị hiện có trong KhachHang.DiaChiGiaoHang của khách hàng đặt đơn. | Ràng buộc | DonHang, KhachHang | `DonHang.DiaChiGiao ∈ {KhachHang.DiaChiGiaoHang}` tại thời điểm tạo đơn | G01-Scope §6; `[GĐ]` |
| BR-DEL-11 | Khi tạo đơn hàng, hệ thống phải sao chép địa chỉ đã chọn vào DonHang.DiaChiGiao gồm SoNha, Duong, Phuong, Quan và ThanhPho. | Thủ tục | DonHang, KhachHang | `DonHang.DiaChiGiao` là thuộc tính phức hợp được chụp tại thời điểm tạo đơn | G01-Scope §6; `[GĐ]` |
| BR-DEL-12 | Việc sửa hoặc xóa KhachHang.DiaChiGiaoHang sau khi tạo đơn không được làm thay đổi DonHang.DiaChiGiao của đơn đã tạo. | Ràng buộc | DonHang, KhachHang | Bảo toàn ảnh chụp địa chỉ giao của đơn cũ | G01-Scope §6; `[GĐ]` |
| BR-PAY-01 | Mỗi đơn hàng phải có đúng một hồ sơ thanh toán hiện tại; mỗi hồ sơ thanh toán phải thuộc đúng một đơn hàng; khi thử lại, hệ thống cập nhật hồ sơ hiện tại thay vì tạo ThanhToan mới. | Cấu trúc | DonHang, ThanhToan | DonHang 1 — 1 ThanhToan, bắt buộc hai phía; ThanhToan.MaDH là FK bắt buộc và duy nhất | G01-Scope §2.3, §5; `[GĐ]` |
| BR-PAY-02 | PhuongThuc của thanh toán chỉ nhận một trong hai giá trị: "Thẻ tín dụng" hoặc "Ví điện tử". | Ràng buộc | ThanhToan | ThanhToan.PhuongThuc: Liệt kê (G01-Scope §4.4) | Đề §Quy trình 3 |
| BR-PAY-03 | TrangThai của thanh toán chỉ nhận một trong các giá trị: "Chờ thanh toán", "Thành công", "Thất bại". | Ràng buộc | ThanhToan | ThanhToan.TrangThai: Liệt kê (G01-Scope §4.4) | G01-Scope §2.3; `[GĐ]` |
| BR-PAY-04 | Mỗi thanh toán khi được tạo có TrangThai là "Chờ thanh toán". | Trạng thái | ThanhToan | Giá trị khởi đầu của ThanhToan.TrangThai | [GĐ] |
| BR-PAY-05 | Khi hồ sơ thanh toán đang ở trạng thái "Chờ thanh toán", TrangThai chỉ được chuyển sang "Thành công" hoặc "Thất bại" sau khi cổng thanh toán bên thứ ba trả kết quả. | Trạng thái | ThanhToan | `Chờ thanh toán → Thành công` hoặc `Chờ thanh toán → Thất bại`; không quản lý số dư ví | Đề §Quy trình 3; G01-Scope §3; `[GĐ]` |
| BR-PAY-06 | SoTien của thanh toán bằng TongTien của đơn hàng tương ứng. | Tính toán | ThanhToan, DonHang | ThanhToan.SoTien = DonHang.TongTien | [GĐ] |
| BR-PAY-07 | TongTienMon của đơn hàng bằng tổng của (SoLuong × DonGia) của các dòng chi tiết đơn hàng thuộc đơn đó. | Tính toán | DonHang, ChiTietDonHang | `DonHang.TongTienMon = Σ(SoLuong × DonGia)` | Đề §Quy trình 3 |
| BR-PAY-08 | TongTien của đơn hàng bằng TongTienMon cộng PhiGiaoHang trừ GiaTriGiamThucTe. | Tính toán | DonHang | `/TongTien = TongTienMon + PhiGiaoHang − GiaTriGiamThucTe` | Đề §Quy trình 3; `[GĐ]` |
| BR-PAY-09 | PhiGiaoHang của đơn hàng phải lớn hơn hoặc bằng 0. | Ràng buộc | DonHang | `PhiGiaoHang ≥ 0` | Đề §Quy trình 3; `[GĐ]` |
| BR-PAY-10 | GiaTriGiamThucTe của đơn hàng không được lớn hơn TongTienMon. | Ràng buộc | DonHang | `0 ≤ GiaTriGiamThucTe ≤ TongTienMon`, bảo đảm tiền giảm không vượt tiền món | `[GĐ]` |
| BR-PAY-11 | Mỗi đơn hàng có thể áp dụng tối đa một khuyến mãi; mỗi khuyến mãi có thể được áp dụng cho không hoặc nhiều đơn hàng. | Cấu trúc | DonHang, KhuyenMai | KhuyenMai 1 — N DonHang; optional phía DonHang (FK MaKM → KhuyenMai.MaKM, cho phép rỗng) | Đề §Quy trình 3; `[GĐ]` |
| BR-PAY-12 | GiaTriGiamThucTe của đơn hàng không áp dụng khuyến mãi bằng 0. | Tính toán | DonHang, KhuyenMai | `GiaTriGiamThucTe = 0` khi MaKM rỗng | Đề §Quy trình 3; `[GĐ]` |
| BR-PAY-13 | MaVoucher của mỗi khuyến mãi phải duy nhất. | Ràng buộc | KhuyenMai | MaVoucher: duy nhất | G01-Scope §2.3; `[GĐ]` |
| BR-PAY-14 | LoaiGiam của khuyến mãi chỉ nhận một trong hai giá trị: "Phần trăm" hoặc "Số tiền". | Ràng buộc | KhuyenMai | KhuyenMai.LoaiGiam: Liệt kê (G01-Scope §4.4) | G01-Scope §2.3; `[GĐ]` |
| BR-PAY-15 | Chỉ khi thời điểm tạo đơn hàng nằm trong khoảng từ NgayBatDau đến NgayKetThuc của khuyến mãi thì đơn hàng mới được áp dụng khuyến mãi đó. | Điều kiện | DonHang, KhuyenMai | So sánh DonHang.ThoiGianTao với NgayBatDau, NgayKetThuc | G01-Scope §6; `[GĐ]` |
| BR-PAY-16 | NgayBatDau của khuyến mãi phải nhỏ hơn hoặc bằng NgayKetThuc. | Ràng buộc | KhuyenMai | `NgayBatDau ≤ NgayKetThuc` | G01-Scope §6; `[GĐ]` |
| BR-PAY-17 | Chỉ khi TongTienMon của đơn hàng lớn hơn hoặc bằng DieuKienApDung của khuyến mãi thì đơn hàng mới được áp dụng khuyến mãi đó. | Điều kiện | DonHang, KhuyenMai | DieuKienApDung hiểu là giá trị tối thiểu của TongTienMon | [GĐ] |
| BR-PAY-18 | GiaTriGiamThucTe của đơn hàng áp dụng khuyến mãi loại "Phần trăm" bằng giá trị nhỏ nhất của TongTienMon × GiaTriGiam / 100, GiamToiDa và TongTienMon. | Tính toán | DonHang, KhuyenMai | `GiaTriGiamThucTe = min(TongTienMon × GiaTriGiam / 100, GiamToiDa, TongTienMon)` | G01-Scope §6; `[GĐ]` |
| BR-PAY-19 | GiaTriGiamThucTe của đơn hàng áp dụng khuyến mãi loại "Số tiền" bằng giá trị nhỏ hơn giữa GiaTriGiam và TongTienMon. | Tính toán | DonHang, KhuyenMai | `GiaTriGiamThucTe = min(GiaTriGiam, TongTienMon)` | G01-Scope §6; `[GĐ]` |
| BR-PAY-20 | GiaTriGiam của mỗi khuyến mãi phải lớn hơn 0. | Ràng buộc | KhuyenMai | `GiaTriGiam > 0` | G01-Scope §6; `[GĐ]` |
| BR-PAY-21 | Nếu LoaiGiam của khuyến mãi là "Phần trăm" thì GiaTriGiam phải nhỏ hơn hoặc bằng 100. | Ràng buộc | KhuyenMai | `LoaiGiam = "Phần trăm" ⇒ GiaTriGiam ≤ 100` | G01-Scope §6; `[GĐ]` |
| BR-PAY-22 | DieuKienApDung của mỗi khuyến mãi phải lớn hơn hoặc bằng 0. | Ràng buộc | KhuyenMai | `DieuKienApDung ≥ 0` | G01-Scope §6; `[GĐ]` |
| BR-PAY-23 | GiamToiDa của mỗi khuyến mãi phải lớn hơn hoặc bằng 0. | Ràng buộc | KhuyenMai | `GiamToiDa ≥ 0` | G01-Scope §6; `[GĐ]` |
| BR-PAY-24 | Chỉ hồ sơ thanh toán có TrangThai là "Thất bại" mới được thử lại; khi thử lại, TrangThai chuyển về "Chờ thanh toán". | Trạng thái | ThanhToan | Chuyển `Thất bại → Chờ thanh toán`; hồ sơ hiện tại được cập nhật, không tạo ThanhToan mới | G01-Scope §6; `[GĐ]` |
| BR-PAY-25 | ThoiGianCapNhat của ThanhToan phải được cập nhật khi hồ sơ được tạo, bắt đầu thử lại hoặc nhận kết quả từ cổng thanh toán. | Thủ tục | ThanhToan | Ghi thời điểm thay đổi trạng thái gần nhất của hồ sơ thanh toán hiện tại | G01-Scope §6; `[GĐ]` |
| BR-PAY-26 | Hồ sơ thanh toán có TrangThai là "Thành công" không được thử lại hoặc chuyển sang trạng thái khác. | Trạng thái | ThanhToan | "Thành công" là trạng thái kết thúc của ThanhToan.TrangThai | G01-Scope §6; `[GĐ]` |
| BR-REV-01 | Mỗi đánh giá phải thuộc đúng một đơn hàng; mỗi đơn hàng có thể có không hoặc nhiều đánh giá. | Cấu trúc | DanhGia, DonHang | `DonHang \|\| — o{ DanhGia`; mandatory phía DanhGia (FK MaDH); tối đa hai đánh giá được BR-REV-09 và BR-REV-10 kiểm soát | Đề §Quy trình 4; `[GĐ]` |
| BR-REV-02 | Mỗi đánh giá phải thuộc đúng một trong hai loại: đánh giá nhà hàng hoặc đánh giá tài xế. | Cấu trúc | DanhGia, DanhGiaNhaHang, DanhGiaTaiXe | Supertype/subtype: Disjoint, Total; discriminator DanhGia.LoaiDG | G01-Scope §4.2; `[GĐ]` |
| BR-REV-03 | Mỗi đánh giá nhà hàng phải dành cho đúng một nhà hàng; mỗi nhà hàng có thể có không hoặc nhiều đánh giá nhà hàng. | Cấu trúc | DanhGiaNhaHang, NhaHang | NhaHang 1 — N DanhGiaNhaHang; nối ở cấp subtype (FK MaNH) | Đề §Quy trình 4; `[GĐ]` |
| BR-REV-04 | Mỗi đánh giá tài xế phải dành cho đúng một tài xế; mỗi tài xế có thể có không hoặc nhiều đánh giá tài xế. | Cấu trúc | DanhGiaTaiXe, TaiXe | TaiXe 1 — N DanhGiaTaiXe; nối ở cấp subtype (FK MaTX) | Đề §Quy trình 4; `[GĐ]` |
| BR-REV-05 | Nhà hàng được đánh giá phải là nhà hàng của đơn hàng chứa đánh giá đó. | Ràng buộc | DanhGiaNhaHang, DonHang, NhaHang | DanhGiaNhaHang.MaNH = DonHang.MaNH | Đề §Quy trình 4 |
| BR-REV-06 | Tài xế được đánh giá phải là tài xế đã giao đơn hàng chứa đánh giá đó. | Ràng buộc | DanhGiaTaiXe, DonHang, TaiXe | DanhGiaTaiXe.MaTX = DonHang.MaTX | Đề §Quy trình 4 |
| BR-REV-07 | Chỉ khi đơn hàng có TrangThai là "Hoàn thành" thì khách hàng mới được đánh giá đơn hàng đó. | Điều kiện | DanhGia, DonHang | Kiểm tra DonHang.TrangThai khi tạo đánh giá | Đề §Quy trình 4 |
| BR-REV-08 | Chỉ khách hàng đã đặt đơn hàng mới được đánh giá đơn hàng đó. | Điều kiện | DanhGia, DonHang, KhachHang | Người đánh giá trùng DonHang.MaKH | Đề §Quy trình 4; `[GĐ]` |
| BR-REV-09 | Mỗi đơn hàng có tối đa một đánh giá nhà hàng. | Ràng buộc | DonHang, DanhGiaNhaHang | Duy nhất MaDH trong DanhGiaNhaHang | Đề §Quy trình 4; `[GĐ]` |
| BR-REV-10 | Mỗi đơn hàng có tối đa một đánh giá tài xế. | Ràng buộc | DonHang, DanhGiaTaiXe | Duy nhất MaDH trong DanhGiaTaiXe | Đề §Quy trình 4; `[GĐ]` |
| BR-REV-11 | SoSao của đánh giá phải là số nguyên từ 1 đến 5. | Ràng buộc | DanhGia | SoSao: Số nguyên, 1 ≤ SoSao ≤ 5 | G01-Scope §2.4; `[GĐ]` |
| BR-REV-12 | BinhLuan của đánh giá có thể để trống. | Ràng buộc | DanhGia | BinhLuan: không bắt buộc | [GĐ] |
| BR-USR-01 | Mỗi người dùng phải thuộc đúng một vai trò: khách hàng, tài xế hoặc chủ nhà hàng. | Cấu trúc | NguoiDung, KhachHang, TaiXe, ChuNhaHang | Supertype/subtype: Disjoint, Total | G01-Scope §4.2; `[GĐ]` |
| BR-USR-02 | LoaiND của người dùng chỉ nhận một trong các giá trị: "Khách hàng", "Tài xế", "Chủ nhà hàng". | Ràng buộc | NguoiDung | Subtype discriminator NguoiDung.LoaiND | G01-Scope §4.1, §4.4; `[GĐ]` |
| BR-USR-03 | SDT của mỗi người dùng phải duy nhất. | Ràng buộc | NguoiDung | SDT: duy nhất | [GĐ] |
| BR-USR-04 | Email của mỗi người dùng phải duy nhất. | Ràng buộc | NguoiDung | Email: duy nhất | [GĐ] |
| BR-USR-05 | Mỗi khách hàng phải có ít nhất một địa chỉ giao hàng. | Cấu trúc | KhachHang | {DiaChiGiaoHang}: thuộc tính đa trị, phức hợp | G01-Scope §6; `[GĐ]` |
| BR-USR-06 | Mỗi địa chỉ giao hàng gồm SoNha, Duong, Phuong, Quan và ThanhPho. | Cấu trúc | KhachHang | Thuộc tính phức hợp DiaChiGiaoHang gồm 5 thành phần | G01-Scope §6; `[GĐ]` |
| BR-USR-07 | Mỗi nhà hàng phải thuộc đúng một chủ nhà hàng; mỗi chủ nhà hàng sở hữu ít nhất một nhà hàng. | Cấu trúc | NhaHang, ChuNhaHang | ChuNhaHang 1 — N NhaHang; mandatory hai phía (FK MaChu → ChuNhaHang.MaND) | [GĐ] |
| BR-USR-08 | Mỗi địa chỉ nhà hàng gồm SoNha, Duong, Phuong, Quan và ThanhPho. | Cấu trúc | NhaHang | Thuộc tính phức hợp DiaChi gồm 5 thành phần | G01-Scope §6; `[GĐ]` |
| BR-USR-09 | Mỗi nhà hàng phải có ít nhất một khung giờ mở cửa. | Cấu trúc | NhaHang | {GioMoCua}: thuộc tính đa trị và phức hợp | G01-Scope §6; `[GĐ]` |
| BR-USR-10 | BienSoXe của mỗi tài xế phải duy nhất. | Ràng buộc | TaiXe | BienSoXe: duy nhất | [GĐ] |
| BR-USR-11 | Mỗi danh mục phải thuộc đúng một nhà hàng; mỗi nhà hàng phải có ít nhất một danh mục. | Cấu trúc | DanhMuc, NhaHang | NhaHang 1 — N DanhMuc; mandatory hai phía (FK MaNH) | [GĐ] |
| BR-USR-12 | Mỗi danh mục có thể có không hoặc một danh mục cha; mỗi danh mục có thể có không hoặc nhiều danh mục con. | Cấu trúc | DanhMuc | Quan hệ đệ quy DanhMuc 1 — N DanhMuc; vai DanhMucCha (optional) và DanhMucCon (FK MaDMCha) | G01-Scope §5; `[GĐ]` |
| BR-USR-13 | Danh mục con phải thuộc cùng nhà hàng với danh mục cha của nó. | Ràng buộc | DanhMuc, NhaHang | Kiểm tra MaNH của danh mục con bằng MaNH của danh mục cha | [GĐ] |
| BR-USR-14 | Mỗi món ăn phải thuộc đúng một danh mục; mỗi danh mục có thể có không hoặc nhiều món ăn. | Cấu trúc | MonAn, DanhMuc | DanhMuc 1 — N MonAn; mandatory phía MonAn (FK MaDM → DanhMuc.MaDM) | G01-Scope §5; `[GĐ]` |
| BR-USR-15 | Gia của món ăn phải lớn hơn 0. | Ràng buộc | MonAn | Gia > 0 | [GĐ] |
| BR-USR-16 | TrangThai của món ăn chỉ nhận một trong hai giá trị: "Còn món" hoặc "Hết món". | Ràng buộc | MonAn | MonAn.TrangThai: Liệt kê (G01-Scope §4.4) | G01-Scope §2.2; `[GĐ]` |
| BR-USR-17 | TrangThaiNhanDon của nhà hàng chỉ nhận một trong hai giá trị: "Đang nhận đơn" hoặc "Tạm ngừng nhận đơn". | Ràng buộc | NhaHang | NhaHang.TrangThaiNhanDon: Liệt kê (G01-Scope §4.4) | G01-Scope §4.4; `[GĐ]` |
| BR-USR-18 | Mỗi giá trị GioMoCua của nhà hàng phải gồm ThuTrongTuan, GioMo và GioDong. | Cấu trúc | NhaHang | `{GioMoCua}` là thuộc tính đa trị và phức hợp gồm 3 thành phần | G01-Scope §6; `[GĐ]` |
| BR-USR-19 | Trong mỗi khung GioMoCua của nhà hàng, GioMo phải nhỏ hơn GioDong. | Ràng buộc | NhaHang | `GioMo < GioDong` | G01-Scope §6; `[GĐ]` |

