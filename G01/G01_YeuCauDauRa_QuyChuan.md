# YÊU CẦU ĐẦU RA, QUY CHUẨN VÀ TIÊU CHÍ ĐẠT CỦA TỪNG TASK – BÀI E01 (GRABFOOD)

> Tài liệu này bổ sung cho `G01_PhanChiaTask.md`. Với mỗi task có 4 phần: **(A) Yêu cầu đầu ra → (B) Quy chuẩn phải tuân theo → (C) Mẫu/ví dụ → (D) Thế nào là đạt**.
> **Nguồn quy chuẩn:** giáo trình *Database Systems: Design, Implementation and Management* (Coronel, Rob) cho business rules, quy ước đặt tên và Crow's Foot; giáo trình *Modern Database Management* (Hoffer) và các slide EER phổ biến cho supertype/subtype; đề bài E01.
> **Phân biệt:** mục nào là **bắt buộc theo đề** thì ghi "(Đề)"; mục nào là **quy chuẩn học thuật** thì ghi "(Chuẩn)"; mục nào là **đề xuất riêng của nhóm** để thống nhất thì ghi "(Nhóm)".

---

## 0. QUY ƯỚC CHUNG CHO TOÀN NHÓM (áp dụng cho mọi task)

### 0.1. Quy ước đặt tên

| Đối tượng | Quy ước | Ví dụ đúng | Ví dụ sai |
|---|---|---|---|
| Thực thể | Danh từ, **số ít**, PascalCase, **không dấu**, khớp `G01_Scope_Entities.md` (Chuẩn: tên thực thể là danh từ quen thuộc với nghiệp vụ, ngắn và có nghĩa) | `DonHang`, `ChiTietDonHang` | `DonHangs`, `don_hang`, `Đơn hàng` |
| Thuộc tính | PascalCase, không dấu, mang nghĩa nghiệp vụ, không lặp lại tên thực thể trừ khóa | `TenMon`, `ThoiGianTao` | `ten`, `MonAn_Ten`, `Thuoc tinh 1` |
| Khóa chính | `Ma` + viết tắt thực thể: `MaND`, `MaNH`, `MaDM`, `MaMon`, `MaDH`, `MaKM`, `MaTT`, `MaDG`. Subtype dùng lại PK của supertype | `MaDH` | `ID`, `DonHang_ID` |
| Khóa ngoại | Trùng tên PK được tham chiếu. Riêng khi tham chiếu subtype (PK là `MaND`) hoặc cần phân vai, đặt tên theo vai trò và **ghi rõ tham chiếu**: `MaKH`, `MaTX`, `MaChu`, `MaDMCha` | `DonHang.MaKH → KhachHang.MaND` | FK không ghi nơi tham chiếu |
| Quan hệ | **Động từ/cụm động từ** chỉ rõ bản chất quan hệ (Chuẩn) | `đặt`, `thuộc về`, `gồm`, `giao` | `có`, `liên quan` (quá mơ hồ, chỉ dùng khi thật sự không có động từ tốt hơn) |
| Mã quy tắc | `BR-<NHÓM>-<NN>` | `BR-ORD-01` | `BR1`, `Rule_1` |
| Giá trị liệt kê (trạng thái...) | Viết hoa chữ cái đầu, tiếng Việt có dấu, thống nhất cách viết toàn tài liệu | `Đang giao` | `dang giao`, `DANG_GIAO` ở chỗ này và `Đang giao` ở chỗ khác |

**Danh sách thực thể cố định (không đổi giữa các phần):** `NguoiDung`, `KhachHang`, `TaiXe`, `ChuNhaHang`, `NhaHang`, `DanhMuc`, `MonAn`, `DonHang`, `ChiTietDonHang`, `KhuyenMai`, `ThanhToan`, `DanhGia`, `DanhGiaNhaHang`, `DanhGiaTaiXe`.

### 0.2. Quy ước trạng thái và giá trị liệt kê (Nhóm: chốt một lần, mọi người dùng chung)

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

### 0.3. Quy tắc phối hợp

1. **Nguồn sự thật duy nhất** về tên thực thể, quan hệ, bản số là `G01_Scope_Entities.md`. Muốn đổi → báo người phụ trách tài liệu này sửa trước.
2. Mọi sản phẩm phải **truy vết được**: mỗi bản số trên sơ đồ truy về ít nhất một mã `BR`; mỗi thuộc tính trong Data Dictionary truy về thực thể trong `G01_Scope_Entities.md`.
3. Khi hai phần mâu thuẫn, ưu tiên theo thứ tự: **Đề bài → quyết định mô hình đã chốt → `G01_Scope_Entities.md` → Business Rules → tài liệu quy chuẩn → Data Dictionary → ERD → EER**.
4. Thứ tự bàn giao bắt buộc: **Phạm vi và thực thể → Business Rules → Từ điển dữ liệu → ERD cơ bản → EER → Tổng hợp Word**. Từ điển dữ liệu phải hoàn thành trước khi giao vẽ ERD.

---

## T1-A. BUSINESS RULES (BR)

### A. Yêu cầu đầu ra (Đề)
Một **bảng Business Rules dạng văn bản, có đánh mã**, phân 4 nhóm theo đề, đủ để xác định phạm vi cụ thể cho phân tích dữ liệu.

| Nhóm theo đề | Mã | Phạm vi nội dung |
|---|---|---|
| Đặt và xử lý món | `BR-ORD-xx` | Khách chọn món, số lượng, đơn thuộc nhà hàng, nhà hàng nhận và chuẩn bị, trạng thái đơn, hủy đơn |
| Giao hàng | `BR-DEL-xx` | Phân công tài xế, tài xế lấy hàng, giao hàng, cập nhật trạng thái giao |
| Thanh toán và Khuyến mãi | `BR-PAY-xx` | Phương thức, trạng thái, công thức tổng tiền, áp dụng mã khuyến mãi |
| Đánh giá | `BR-REV-xx` | Điều kiện đánh giá, số sao, số lần đánh giá, đối tượng được đánh giá |
| Nhóm bổ trợ (Nhóm) | `BR-USR-xx` | Người dùng và vai trò (supertype/subtype), nhà hàng, thực đơn, danh mục. Gom vào đây những quy tắc không thuộc 4 nhóm trên |

### B. Quy chuẩn phải tuân theo

**B1. Tính chất của một quy tắc tốt (Chuẩn)**
1. **Chính xác, rõ ràng, đơn giản:** quy tắc phải viết chính xác, rõ ràng và đơn giản, đồng thời giúp xác định được thực thể, thuộc tính, quan hệ và ràng buộc.
2. **Nguyên tử:** mỗi quy tắc chỉ nói **một ý**. Nếu có chữ "và" nối hai ràng buộc độc lập thì tách thành hai quy tắc.
3. **Kiểm chứng được:** đọc xong có thể trả lời "đúng/sai" với một dữ liệu cụ thể. Cấm từ mơ hồ: "hợp lý", "nhanh chóng", "thường", "phù hợp", "khoảng".
4. **Có nguồn và có lý do:** mỗi quy tắc ghi nguồn (mục nào trong đề, hoặc "giả định nhóm") và được duyệt. Quy tắc là giả định của nhóm phải đánh dấu `[GĐ]`.
5. **Độc lập cài đặt:** không nhắc SQL, bảng, giao diện, tên màn hình.
6. **Không mâu thuẫn, không trùng lặp** với quy tắc khác và không vượt ra ngoài phạm vi Out-of-scope.

**B2. Cách chuyển nghiệp vụ thành quy tắc (Chuẩn)**
- **Danh từ → thực thể; động từ nối hai danh từ → quan hệ.** Quan hệ luôn hai chiều, nên cần phát biểu được **cả hai chiều** (một hoặc hai câu).
- Bản số suy ra từ từ khóa:

| Từ khóa trong câu | Nghĩa trên sơ đồ |
|---|---|
| "**phải** có / đúng một" | Mandatory One |
| "**có thể** có / không hoặc một" | Optional One |
| "**ít nhất một**" | Mandatory Many |
| "**có thể có nhiều** / không hoặc nhiều" | Optional Many |

**B3. Khuôn câu chuẩn (Nhóm)**

| Loại quy tắc | Khuôn câu |
|---|---|
| Quan hệ / bản số | "Mỗi `<A>` `<động từ>` `<số lượng>` `<B>`; mỗi `<B>` `<động từ ngược>` `<số lượng>` `<A>`." |
| Ràng buộc giá trị | "`<Thuộc tính>` của `<Thực thể>` phải `<điều kiện cụ thể>`." |
| Tính toán | "`<Thuộc tính>` bằng `<công thức>`." |
| Trạng thái | "`<Thực thể>` chỉ được chuyển từ trạng thái `<X>` sang `<Y>` khi `<điều kiện>`." |
| Điều kiện nghiệp vụ | "Chỉ khi `<điều kiện>` thì `<Thực thể>` mới được `<hành động>`." |

**B4. Cấu trúc bảng BR (Nhóm)**

| Cột | Nội dung |
|---|---|
| Mã | `BR-ORD-01`, đánh liên tục, không nhảy số, không dùng lại mã đã xóa |
| Phát biểu quy tắc | Một câu theo khuôn B3 |
| Loại | Cấu trúc / Ràng buộc / Tính toán / Trạng thái / Điều kiện / Thủ tục |
| Thực thể liên quan | Tên thực thể theo `G01_Scope_Entities.md` |
| Ánh xạ vào mô hình | Bản số, thuộc tính hoặc ràng buộc sinh ra (ví dụ: `NhaHang 1 — N DonHang`, mandatory phía `DonHang`) |
| Nguồn | Mục của đề hoặc `[GĐ]` |

### C. Mẫu

| Mã | Phát biểu quy tắc | Loại | Thực thể | Ánh xạ vào mô hình | Nguồn |
|---|---|---|---|---|---|
| BR-ORD-01 | Mỗi đơn hàng phải thuộc đúng một nhà hàng; mỗi nhà hàng có thể có nhiều đơn hàng. | Cấu trúc | DonHang, NhaHang | NhaHang 1 — N DonHang; mandatory phía DonHang | Đề §Quy trình 1 |
| BR-ORD-02 | Số lượng món trong mỗi dòng chi tiết đơn hàng phải lớn hơn 0. | Ràng buộc | ChiTietDonHang | `SoLuong > 0` | Đề §Quy trình 1 |
| BR-ORD-03 | Mỗi dòng chi tiết đơn hàng chỉ tham chiếu một món ăn thuộc nhà hàng của đơn hàng đó. | Ràng buộc | ChiTietDonHang, MonAn, DonHang | FK MaMon; kiểm tra cùng MaNH | Đề §Quy trình 1 |
| BR-ORD-04 | Chi tiết đơn hàng không tồn tại độc lập; xóa đơn hàng thì các dòng chi tiết của đơn đó bị xóa theo. | Cấu trúc | ChiTietDonHang, DonHang | Weak entity, identifying relationship | [GĐ] |
| BR-DEL-01 | Mỗi đơn hàng có thể được giao bởi tối đa một tài xế; mỗi tài xế có thể giao nhiều đơn hàng theo thời gian. | Cấu trúc | DonHang, TaiXe | TaiXe 1 — N DonHang; optional phía DonHang | Đề §Quy trình 2; `[GĐ]` |
| BR-DEL-02 | Chỉ tài xế có trạng thái "Rảnh" mới được phân công đơn hàng mới. | Điều kiện | TaiXe, DonHang | Ràng buộc trên `TrangThaiHoatDong` | [GĐ] |
| BR-DEL-03 | Đơn hàng chỉ chuyển sang "Đang giao" sau trạng thái "Đã phân công tài xế" và khi tài xế đã lấy món. | Trạng thái | DonHang, TaiXe | Chuỗi trạng thái có bước "Đã chuẩn bị xong" trước khi phân công | Đề §Quy trình 2; `[GĐ]` |
| BR-PAY-01 | Tổng tiền của đơn hàng bằng TongTienMon cộng PhiGiaoHang trừ GiaTriGiamThucTe. | Tính toán | DonHang | `TongTien = TongTienMon + PhiGiaoHang - GiaTriGiamThucTe` | Đề §Quy trình 3; `[GĐ]` |
| BR-PAY-02 | Mỗi đơn hàng có thể áp dụng tối đa một mã khuyến mãi. | Cấu trúc | DonHang, KhuyenMai | KhuyenMai 1 — N DonHang; optional phía DonHang | Đề §Quy trình 3; `[GĐ]` |
| BR-REV-01 | Khách hàng chỉ được đánh giá đơn hàng có trạng thái "Hoàn thành". | Điều kiện | DanhGia, DonHang | Ràng buộc thời điểm | Đề §Quy trình 4 |
| BR-REV-02 | Mỗi đánh giá thuộc đúng một đơn; mỗi đơn có 0..N đánh giá trên ERD, đồng thời tối đa một đánh giá nhà hàng và một đánh giá tài xế theo BR. | Cấu trúc | DonHang, DanhGia, DanhGiaNhaHang, DanhGiaTaiXe | `DonHang \|\| — o{ DanhGia`; giới hạn tối đa hai do BR kiểm soát | Đề §Quy trình 4; `[GĐ]` |
| BR-USR-01 | Mỗi người dùng phải thuộc đúng một vai trò: khách hàng, tài xế hoặc chủ nhà hàng. | Cấu trúc | NguoiDung | Supertype/subtype: Disjoint, Total | [GĐ] |

### D. Thế nào là đạt

**Đạt (bắt buộc):**
- [ ] Có đủ **4 nhóm theo đề**, mỗi nhóm **≥ 5 quy tắc**; tổng **≥ 25 quy tắc**.
- [ ] Mã đúng định dạng `BR-<NHÓM>-<NN>`, liên tục, không trùng.
- [ ] Mọi quy tắc theo đúng một khuôn câu ở B3, nguyên tử, không có từ mơ hồ.
- [ ] Bảng có đủ cột ở B4, trong đó cột **Ánh xạ vào mô hình** được điền cho quy tắc thuộc loại Cấu trúc.
- [ ] Mỗi **quan hệ** trong bảng quan hệ của `G01_Scope_Entities.md` có ít nhất một quy tắc, phát biểu được cả hai chiều.
- [ ] Có quy tắc cho từng mục: công thức Tổng tiền, chuỗi trạng thái đơn, điều kiện nhận đơn của tài xế, điều kiện và số lần đánh giá, hủy đơn, điều kiện khuyến mãi, ràng buộc kế thừa.
- [ ] Không quy tắc nào vi phạm Out-of-scope.
- [ ] Giả định của nhóm được đánh dấu `[GĐ]`.

**Tốt (nên có):**
- [ ] Có ghi chú các điểm đề bài chưa nói rõ và cách nhóm quyết định.
- [ ] Người làm ERD đọc xong vẽ được **mà không phải hỏi lại**.

---

## T1-B. DATA DICTIONARY (DD)

### A. Yêu cầu đầu ra (Đề)
**Bảng mô tả chi tiết cho từng thực thể**, gồm khóa chính (PK), khóa ngoại (FK), thuộc tính thường, thuộc tính phức hợp, thuộc tính đa trị (và dẫn xuất).

### B. Quy chuẩn phải tuân theo

**B1. Cấu trúc (Nhóm)**
1. **Một bảng cho mỗi thực thể** (đủ 14), đặt dưới tiêu đề `### <TênThựcThể> – <Loại: mạnh/yếu/supertype/subtype>`.
2. Cuối tài liệu có **bảng tổng hợp** liệt kê thực thể, PK, các FK.
3. Cột chuẩn:

| Cột | Nội dung |
|---|---|
| Thuộc tính | Tên theo quy ước 0.1 |
| Loại thuộc tính | Đơn / Phức hợp / Thành phần / Đa trị / Dẫn xuất |
| Kiểu dữ liệu (logic) | Chuỗi, Số nguyên, Số thực, Ngày giờ, Logic, Liệt kê |
| Miền giá trị / Độ dài | Khoảng giá trị, độ dài tối đa, danh sách giá trị liệt kê |
| Khóa | PK, FK, PK+FK (có ghi tham chiếu `→ Bảng.Cột`) |
| Bắt buộc | Có / Không |
| Mô tả | Một câu nghĩa nghiệp vụ |
| BR liên quan | Mã quy tắc |

**B2. Quy chuẩn nội dung (Chuẩn)**
- **Thuộc tính đơn trị, nguyên tử:** thuộc tính phức hợp phải **liệt kê các thành phần** (ví dụ `DiaChi` gồm `SoNha`, `Duong`, `Phuong`, `Quan`, `ThanhPho`); thuộc tính đa trị phải **gắn nhãn đa trị** và nêu cách thể hiện.
- **Thuộc tính dẫn xuất** ghi rõ **công thức** (ví dụ `TongTien = TongTienMon + PhiGiaoHang − GiaTriGiamThucTe`).
- Với `ThanhToan`, dùng `ThoiGianCapNhat` bắt buộc để ghi thời điểm hồ sơ thanh toán hiện tại thay đổi trạng thái gần nhất; không dùng tên chung chung `ThoiGian` `[GĐ]`.
- **Thực thể nên đạt 3NF trở lên;** thực thể nào dưới 3NF phải có lời giải thích. Kiểm tra nhanh: không có thuộc tính nào phụ thuộc vào thuộc tính không khóa khác.
- **Subtype:** PK đồng thời là FK trỏ tới supertype (`PK+FK`); chỉ liệt kê thuộc tính **riêng** của subtype, không lặp lại thuộc tính kế thừa.
- **Thực thể yếu:** PK ghép gồm PK của thực thể chủ (FK) và khóa riêng phần.
- Mọi FK phải có nơi tham chiếu tồn tại trong DD.

### C. Mẫu

**`DonHang` – Thực thể mạnh**

| Thuộc tính | Loại | Kiểu | Miền giá trị | Khóa | Bắt buộc | Mô tả | BR |
|---|---|---|---|---|---|---|---|
| MaDH | Đơn | Chuỗi | ≤ 15 ký tự | PK | Có | Mã định danh đơn hàng | BR-ORD-01 |
| ThoiGianTao | Đơn | Ngày giờ | – | – | Có | Thời điểm khách tạo đơn | BR-PAY-15 |
| TrangThai | Đơn | Liệt kê | Theo mục 0.2 | – | Có | Trạng thái xử lý hiện tại | BR-ORD-13 |
| DiaChiGiao | Phức hợp | – | Gồm SoNha, Duong, Phuong, Quan, ThanhPho | – | Có | Ảnh chụp địa chỉ giao tại thời điểm tạo đơn | BR-DEL-10, BR-DEL-11, BR-DEL-12 |
| SoNha | Thành phần | Chuỗi | ≤ 20 ký tự | – | Có | Số nhà của DiaChiGiao | BR-DEL-11 |
| Duong | Thành phần | Chuỗi | ≤ 100 ký tự | – | Có | Đường của DiaChiGiao | BR-DEL-11 |
| Phuong | Thành phần | Chuỗi | ≤ 100 ký tự | – | Có | Phường của DiaChiGiao | BR-DEL-11 |
| Quan | Thành phần | Chuỗi | ≤ 100 ký tự | – | Có | Quận của DiaChiGiao | BR-DEL-11 |
| ThanhPho | Thành phần | Chuỗi | ≤ 100 ký tự | – | Có | Thành phố của DiaChiGiao | BR-DEL-11 |
| PhiGiaoHang | Đơn | Số thực | ≥ 0 | – | Có | Phí giao áp dụng cho đơn | BR-PAY-09 |
| TongTienMon | Dẫn xuất | Số thực | ≥ 0 | – | Có | = Σ(SoLuong × DonGia) | BR-PAY-07 |
| GiaTriGiamThucTe | Dẫn xuất | Số thực | 0..TongTienMon | – | Có | Giá trị giảm thực tế sau khi áp dụng trần | BR-PAY-10, BR-PAY-12, BR-PAY-18, BR-PAY-19 |
| TongTien | Dẫn xuất | Số thực | ≥ 0 | – | Có | = TongTienMon + PhiGiaoHang − GiaTriGiamThucTe | BR-PAY-08 |
| MaKH | Đơn | Chuỗi | – | FK → KhachHang.MaND | Có | Khách đặt đơn | BR-ORD-01 |
| MaNH | Đơn | Chuỗi | – | FK → NhaHang.MaNH | Có | Nhà hàng nhận đơn | BR-ORD-02 |
| MaTX | Đơn | Chuỗi | – | FK → TaiXe.MaND | Không | Tài xế được phân công (rỗng khi chưa phân công) | BR-DEL-01 |
| MaKM | Đơn | Chuỗi | – | FK → KhuyenMai.MaKM | Không | Mã khuyến mãi áp dụng | BR-PAY-02 |

### D. Thế nào là đạt

**Đạt (bắt buộc):**
- [ ] Đủ **14 bảng thực thể** và bảng tổng hợp PK/FK.
- [ ] Mỗi bảng có đầy đủ các cột ở B1; PK và FK đúng với `G01_Scope_Entities.md`.
- [ ] Mọi thuộc tính phức hợp, đa trị, dẫn xuất mà `G01_Scope_Entities.md` nêu đều được **gắn nhãn đúng loại**; thành phần của thuộc tính phức hợp được liệt kê.
- [ ] Thuộc tính dẫn xuất có công thức.
- [ ] Subtype có PK+FK; thực thể yếu có PK ghép.
- [ ] Mọi FK trỏ đến PK có thật; không còn FK "treo".
- [ ] Thuộc tính liệt kê khớp mục 0.2.
- [ ] Cột BR liên quan được điền và mã BR tồn tại trong bảng BR.

**Tốt (nên có):**
- [ ] Có ghi chú kiểm tra 3NF cho các thực thể dễ nghi ngờ (`DonHang`, `ChiTietDonHang`).

---

## T2. ERD CƠ BẢN (CROW'S FOOT)

### A. Yêu cầu đầu ra (Đề)
**Sơ đồ ER theo ký hiệu Crow's Foot**, thể hiện các thực thể chính và mối quan hệ 1–1, 1–N, N–N (qua `DonHang` – `ChiTietDonHang` – `MonAn`), **đúng bản số** (Mandatory One, Optional One, Mandatory Many, Optional Many).

### B. Quy chuẩn phải tuân theo

**B1. Bộ ký hiệu bản số Crow's Foot (Chuẩn)**

| Ký hiệu đề ghi | Ý nghĩa | Hình dạng đầu đường nối |
|---|---|---|
| `\|\|` | Đúng một (Mandatory One) | Hai gạch song song |
| `\|o` | Không hoặc một (Optional One) | Một gạch và một vòng tròn |
| `}\|` | Một hoặc nhiều (Mandatory Many) | Chân chim và một gạch |
| `}>` (còn viết `}o`) | Không hoặc nhiều (Optional Many) | Chân chim và một vòng tròn |

**B2. Quy chuẩn vẽ**
1. **Thực thể:** hình chữ nhật, tên thực thể số ít ở trên cùng; thuộc tính bên dưới, **PK ở đầu danh sách** và gắn nhãn `PK`, FK gắn nhãn `FK`.
2. **Đường nối:** vẽ **liền nét** cho quan hệ **định danh** (identifying) và **nét đứt** cho quan hệ **không định danh** (non-identifying) (Chuẩn).
3. **Nhãn quan hệ:** mỗi đường nối ghi **một động từ** (ví dụ `đặt`, `thuộc về`, `gồm`), đọc theo một hướng nhất quán (trái sang phải, trên xuống dưới).
4. **Bản số ở cả hai đầu** của mọi đường nối, không bỏ sót đầu nào.
5. **Quan hệ N–N phải được phân rã** thành hai quan hệ 1–N qua thực thể trung gian (`ChiTietDonHang`). Không vẽ đường N–N trực tiếp.
6. **Không có quan hệ thừa** (quan hệ suy ra được từ các quan hệ khác, trừ khi cần thiết và có ghi chú).
7. **Bố cục:** thực thể có nhiều quan hệ nhất (`DonHang`) đặt giữa; hạn chế đường nối cắt nhau; các hình có kích thước đồng đều; chừa chỗ cho `NguoiDung` và `DanhGia` để T3 gắn supertype/subtype.
8. **Thuộc tính trên hình:** thể hiện **PK, FK và các thuộc tính chính**; danh sách đầy đủ để ở Data Dictionary.
9. Có **khung chú thích (legend)** ký hiệu bản số và loại đường nối.
10. **Xuất ảnh:** PNG, rộng ≥ 3000 px (hoặc ≥ 300 DPI), nền trắng, chữ đọc được khi in A4 ngang.
11. **Đánh giá:** vẽ `DonHang || — o{ DanhGia`. Giới hạn mỗi đơn tối đa một `DanhGiaNhaHang` và một `DanhGiaTaiXe` do BR kiểm soát; không ghi `(0..2)` trên đường nối Crow's Foot.
12. **Thanh toán:** vẽ `DonHang` — `ThanhToan` là 1–1 bắt buộc ở cả hai phía; đây là giả định của nhóm `[GĐ]` và `ThanhToan` là hồ sơ thanh toán hiện tại, không phải lịch sử các lần thử.

### C. Mẫu cách đọc bản số

`NhaHang ||——o{ DonHang` đọc: "Mỗi nhà hàng có thể có không hoặc nhiều đơn hàng; mỗi đơn hàng thuộc đúng một nhà hàng." (khớp `BR-ORD-02`).

`DonHang ||——o{ DanhGia` đọc: "Mỗi đơn hàng có thể có không hoặc nhiều đánh giá trên đường nối Crow's Foot; mỗi đánh giá thuộc đúng một đơn hàng." Giới hạn tối đa hai đánh giá được kiểm soát bởi BR-REV-09 và BR-REV-10.

### D. Thế nào là đạt

**Đạt (bắt buộc):**
- [ ] Đủ thực thể phần lõi và **mọi quan hệ** trong bảng quan hệ của `G01_Scope_Entities.md`, không thừa không thiếu.
- [ ] **Mọi đầu** đường nối có ký hiệu bản số đúng một trong bốn loại ở B1.
- [ ] Các quan hệ optional đúng quyết định: `TaiXe`–`DonHang`, `KhuyenMai`–`DonHang`, `DanhMuc` cha–con.
- [ ] Không còn quan hệ N–N trực tiếp; `DonHang`–`MonAn` đi qua `ChiTietDonHang`.
- [ ] Mỗi đường nối có nhãn động từ; PK và FK ghi rõ.
- [ ] Phân biệt được đường liền (định danh) và đường đứt (không định danh).
- [ ] Có legend; ảnh đạt chuẩn xuất ở B2.10.
- [ ] **Đối chiếu chéo:** mỗi bản số truy được về ít nhất một `BR`; mỗi FK trên hình trùng với Data Dictionary.

**Tốt (nên có):**
- [ ] Sơ đồ nằm vừa **một trang A4 ngang** mà vẫn đọc được.
- [ ] Bàn giao kèm file nguồn để T3 chỉnh sửa trực tiếp.

---

## T3. EER (ER MỞ RỘNG)

### A. Yêu cầu đầu ra (Đề)
Sơ đồ ERD **bổ sung các khái niệm mở rộng** trên cùng bản vẽ của T2 và **phần giải thích các thành phần EER**:
- Supertype/Subtype (Generalization/Specialization): `NguoiDung` → `KhachHang`, `TaiXe`, `ChuNhaHang`; `DanhGia` → `DanhGiaNhaHang`, `DanhGiaTaiXe`.
- Weak Entity: `ChiTietDonHang` phụ thuộc `DonHang`.
- Ràng buộc kế thừa: **Disjoint/Overlap** và **Total/Partial**.
- Cùng với: thuộc tính phức hợp, đa trị, dẫn xuất, quan hệ đệ quy (để mô phỏng "đầy đủ khái niệm ER cơ bản và mở rộng" như đề yêu cầu).

### B. Quy chuẩn phải tuân theo

**B1. Ký hiệu supertype/subtype (Chuẩn)**

| Thành phần | Cách vẽ |
|---|---|
| Quan hệ supertype/subtype | Một đường từ supertype đến **vòng tròn**, từ vòng tròn tỏa ra các đường đến từng subtype |
| **Disjoint** | Chữ **`d`** trong vòng tròn: một thể hiện của supertype chỉ thuộc một subtype |
| **Overlap** | Chữ **`o`** trong vòng tròn: một thể hiện có thể thuộc nhiều subtype |
| **Total** | **Đường đôi** từ supertype đến vòng tròn: mọi thể hiện của supertype phải thuộc ít nhất một subtype |
| **Partial** | **Đường đơn** từ supertype đến vòng tròn: thể hiện của supertype được phép không thuộc subtype nào |
| **Subtype discriminator** | Thuộc tính của supertype xác định subtype (`NguoiDung.LoaiND`, `DanhGia.LoaiDG`); với Disjoint, ghi giá trị cạnh đường nối đến mỗi subtype |
| Kế thừa | Subtype dùng lại PK của supertype và kế thừa thuộc tính chung; chỉ vẽ thuộc tính **riêng** trong subtype |

> **Lưu ý:** Các công cụ vẽ khác nhau dùng ký hiệu khác nhau cho EER, và Crow's Foot chuẩn không có ký hiệu riêng cho vòng tròn `d/o`. Vì vậy **bắt buộc có legend** nêu rõ quy ước nhóm dùng.

**B2. Quy ước nhóm cho các khái niệm còn lại (Nhóm, ghi vào legend)**

| Khái niệm | Cách thể hiện |
|---|---|
| Thực thể yếu | Hình chữ nhật **bo góc** (hoặc viền đôi) + nhãn `<<weak>>`; khóa riêng phần (`STT`) gạch chân nét đứt; nối với thực thể chủ bằng đường **liền nét** (identifying relationship) |
| Thuộc tính phức hợp | Ghi thuộc tính mẹ và các thành phần thụt lề: `DiaChi`, `DiaChiGiao`, mỗi giá trị `DiaChiGiaoHang` gồm `SoNha`, `Duong`, `Phuong`, `Quan`, `ThanhPho`; mỗi giá trị `GioMoCua` gồm `ThuTrongTuan`, `GioMo`, `GioDong` |
| Thuộc tính đa trị | Gắn ký hiệu `{ }` hoặc nhãn `(đa trị)` cạnh tên (`{DiaChiGiaoHang}`, `{GioMoCua}`) |
| Thuộc tính dẫn xuất | Tiền tố `/`: `/TongTienMon`, `/GiaTriGiamThucTe`, `/TongTien` |
| Quan hệ đệ quy | Đường nối từ `DanhMuc` về chính nó; đánh vai `DanhMucCha` và `DanhMucCon`; phía cha là optional |
| Quan hệ ở cấp supertype | Nối vào **supertype** khi mọi subtype tham gia (ví dụ `DonHang`–`DanhGia`) |
| Quan hệ ở cấp subtype | Nối vào **đúng subtype** khi chỉ subtype đó tham gia (ví dụ `DonHang`–`KhachHang`, `DonHang`–`TaiXe`) |

**B3. Quy chuẩn phần giải thích EER (Nhóm)**
Mỗi khái niệm một mục, đủ **5 ý**: (1) khái niệm là gì (một câu), (2) áp dụng ở thực thể nào, **chỉ rõ vị trí trên sơ đồ**, (3) ràng buộc kèm theo, (4) lý do thiết kế gắn với mã `BR`, (5) hệ quả khi chuyển sang mô hình quan hệ (ví dụ PK của subtype đồng thời là FK).

### C. Mẫu giải thích

> **Supertype/Subtype: `NguoiDung` → `KhachHang`, `TaiXe`, `ChuNhaHang`.**
> *(1)* Supertype chứa thuộc tính chung, subtype chứa thuộc tính riêng và kế thừa thuộc tính chung. *(2)* Vòng tròn phía dưới `NguoiDung` ở góc trên trái sơ đồ. *(3)* **Disjoint, Total:** một người dùng chỉ có đúng một vai trò, và không có người dùng nào không thuộc vai trò nào; discriminator là `LoaiND`. *(4)* Theo `BR-USR-01`. *(5)* Khi ánh xạ, `MaND` của mỗi subtype vừa là PK vừa là FK tham chiếu `NguoiDung.MaND`.

### D. Thế nào là đạt

**Đạt (bắt buộc):**
- [ ] Làm **trên cùng file** với T2, không vẽ file riêng.
- [ ] **Supertype/Subtype:** cả hai nhóm (`NguoiDung`, `DanhGia`) có vòng tròn, chữ `d`, đường đôi (Total), đúng với bảng ràng buộc trong `G01_Scope_Entities.md`.
- [ ] **Subtype discriminator** có mặt ở supertype; subtype không lặp lại thuộc tính kế thừa.
- [ ] **Weak entity** `ChiTietDonHang` vẽ khác thực thể thường, có identifying relationship liền nét và khóa riêng phần.
- [ ] Có đủ **thuộc tính phức hợp, đa trị, dẫn xuất** theo quy ước B2, khớp Data Dictionary.
- [ ] Có **quan hệ đệ quy** `DanhMuc` với vai trò rõ.
- [ ] Quan hệ gắn đúng cấp (supertype hay subtype), không gắn nhầm.
- [ ] Có **legend** đầy đủ mọi ký hiệu EER.
- [ ] Phần giải thích đủ **mỗi khái niệm một mục**, mỗi mục đủ 5 ý ở B3, và **chỉ được vị trí cụ thể** trên sơ đồ.
- [ ] Sơ đồ sau khi thêm lớp mở rộng **vẫn đọc rõ** (không chồng chữ, không rối đường).

**Tốt (nên có):**
- [ ] Có ghi chú vì sao chọn Disjoint/Total và vì sao `NhaHang` không phải subtype.
- [ ] Có phương án thay thế được cân nhắc và lý do loại (ví dụ `DanhGia` một thực thể duy nhất thay vì hai subtype).

---

## T4. TỔNG HỢP FILE WORD VÀ KIỂM TRA NỘP BÀI

### A. Yêu cầu đầu ra (Đề)
**Một file Word duy nhất** chứa toàn bộ kết quả, **không link ngoài**, gồm: trang bìa (tên bài tập, tên nhóm, thành viên, bảng phân công), Phần 1 (bảng quy tắc nghiệp vụ), Phần 2 (sơ đồ ERD/EER dạng ảnh nét + giải thích). Tên file `Mảnhóm_MãBT.docx`, ví dụ `Nhom01_E01.docx`. Nộp lên Moodle đúng hạn.

### B. Quy chuẩn phải tuân theo (Nhóm, nếu khoa/GV không quy định khác)

| Hạng mục | Quy chuẩn |
|---|---|
| Cấu trúc | Bìa → Mục lục → Phần 0 (Phạm vi và danh mục thực thể) → Phần 1 (Business Rules) → Phần 2 (Data Dictionary, ERD/EER, giải thích EER) |
| Đánh số | Heading nhiều cấp (1, 1.1, 1.2...); **bảng và hình có chú thích** ("Bảng 1. ...", "Hình 1. ...") và được nhắc trong văn bản |
| Phông chữ | Một phông duy nhất cho nội dung (ví dụ Times New Roman 13 pt, giãn dòng 1.3); bảng có thể 10–11 pt |
| Bảng | Có hàng tiêu đề, lặp lại tiêu đề khi sang trang, không bị tràn lề |
| Sơ đồ | Chèn dạng **ảnh PNG độ phân giải cao**, trang ngang nếu cần; phóng to vẫn đọc được chữ |
| Liên kết | **Không** có link ra phần mềm hay link gián tiếp để xem kết quả |
| Thuật ngữ | Thống nhất tuyệt đối theo mục 0.1 và 0.2 |
| Trang bìa | Tên bài tập, mã BT, tên nhóm, danh sách thành viên (họ tên, MSSV), **bảng phân công** ghi rõ ai làm phần nào |
| Tên file | `Nhom01_E01.docx` hoặc đúng mẫu `Mảnhóm_MãBT` mà GV quy định |

### C. Mẫu bảng phân công

| Thành viên | MSSV | Phần phụ trách | Mức hoàn thành |
|---|---|---|---|
| ... | ... | Phân tích đề, Phạm vi, Danh mục thực thể, Tổng hợp | 100% |
| ... | ... | Business Rules, Data Dictionary | 100% |
| ... | ... | ERD cơ bản | 100% |
| ... | ... | EER | 100% |

### D. Thế nào là đạt

**Đạt (bắt buộc):**
- [ ] Đủ **trang bìa, Phần 1, Phần 2**, đúng thứ tự.
- [ ] **Không có link ngoài**; toàn bộ sơ đồ chèn trực tiếp dạng ảnh.
- [ ] Sơ đồ rõ nét, đọc được chữ khi phóng to và khi in.
- [ ] **Nhất quán xuyên suốt:** tên thực thể, thuộc tính, trạng thái, bản số giống nhau giữa BR, DD, ERD, EER, giải thích.
- [ ] Mọi mã `BR` được nhắc trong DD/ERD/EER đều tồn tại trong bảng BR.
- [ ] Bảng phân công đúng người, đúng phần.
- [ ] Tên file đúng quy định; nộp đúng hạn trên Moodle.

**Tốt (nên có):**
- [ ] Một người ngoài nhóm đọc thử báo cáo và hiểu được hệ thống mà không cần hỏi.
- [ ] Chạy kiểm tra chéo theo bảng ở mục 5 trước khi nộp.

---

## T0. PHẠM VI VÀ DANH MỤC THỰC THỂ (`G01_Scope_Entities.md`, dành cho trưởng nhóm)

**Đạt (bắt buộc):**
- [ ] Có **mục tiêu**, **In-scope** (theo phân hệ/quy trình), **Out-of-scope** có lý giải (Đề: Task 1.1).
- [ ] Có **bảng thực thể** đủ 14 dòng: loại, mô tả, thuộc tính chính, PK.
- [ ] Có **ràng buộc kế thừa** (Disjoint/Total) cho từng nhóm supertype/subtype.
- [ ] Có **bảng quan hệ và bản số**.
- [ ] Có **bảng giá trị liệt kê** và **quy ước đặt tên** (mục 0.1 và 0.2).
- [ ] Số lượng thực thể ghi trong văn bản **khớp** số dòng trong bảng.
- [ ] Cả nhóm đã đọc và xác nhận trước khi chia việc.

---

## 5. BẢNG ĐỐI CHIẾU CHÉO TRƯỚC KHI NỘP

| Kiểm tra | Giữa | Câu hỏi |
|---|---|---|
| 1 | BR ↔ ERD | Mỗi bản số trên hình có ít nhất một `BR` hỗ trợ? Mỗi `BR` loại Cấu trúc có xuất hiện trên hình? |
| 2 | DD ↔ ERD | Mọi PK/FK trên hình khớp DD? Không thuộc tính nào chỉ có ở một bên? |
| 3 | `G01_Scope_Entities.md` ↔ ERD | Đủ 14 thực thể, đúng tên? |
| 4 | EER ↔ `G01_Scope_Entities.md` | Ràng buộc `d/o` và đường đơn/đôi khớp bảng ràng buộc kế thừa? |
| 5 | DD ↔ EER | Thuộc tính phức hợp, đa trị, dẫn xuất ở DD đều được đánh dấu trên sơ đồ? |
| 6 | Toàn bộ ↔ Đề | Mỗi yêu cầu ở Task 1.1 → 3.2 của đề có sản phẩm tương ứng? |
| 7 | Toàn bộ ↔ Out-of-scope | Không thực thể, thuộc tính hay quy tắc nào thuộc phạm vi đã loại trừ? |
