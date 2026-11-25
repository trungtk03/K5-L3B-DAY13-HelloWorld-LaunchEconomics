# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: HelloWorld · Lớp: K5-L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | `4.472 đ` chung; `3.414 đ` biến đổi (`noi_dia` + `hang_nang`), `4.599 đ` gồm cố định ở 45.000 yêu cầu/tháng (`simulated`) | Giả lập | Kế toán trưởng |
| 2 · Ba yếu tố nhạy nhất | `1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương nhân viên (+23,1%)` (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | `0,37×` chung (`4.472 đ` vs `12.000 đ`); `0,38×` phạm vi `noi_dia` + `hang_nang` gồm cố định; `quoc_te` `1,88×` bị loại (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đóng 24h không mở lại: `82,83%` (`994/1.200`); bỏ qua gợi ý: `27,12%` (`48/177`); lỗi lọt khách: `4,25%` (`3,97%` ở `noi_dia`+`hang_nang`); đủ `11` event có `trace_id` | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận `19/20 (95%)`; đủ 5 loại PAIR có event đo và vai trò phụ trách | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | Chia theo nhân viên `20 + 20`, MDE `+6 điểm`, `m ≥ 299` yêu cầu/nhân viên (8 ngày gom mẫu + 7 ngày theo dõi), đủ 3 luật dừng (an toàn, chi phí, sử dụng) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → CPS `6.787 đ` (`+51,8%`, `simulated`); xem lại 100% → CPS `11.743–12.415 đ` (`0,98–1,03×` baseline, `simulated`) | Giả lập | Kế toán trưởng |

**Đề xuất:** **Go có điều kiện** (chỉ duyệt chạy pilot phạm vi `noi_dia` + `hang_nang`, giới hạn `max_attempts = 2`, loại `quoc_te` và `doi_tac`).

- **Điều kiện 1 (Kỹ thuật & An toàn):** Khoá `max_attempts = 2`, bộ lọc định tuyến loại `quoc_te`/`doi_tac`, và bật kiểm tra `idempotency_key` trước khi báo hoàn tiền thành công — Phụ trách: **Kỹ sư trưởng agent** — Kiểm tra: **Trước ngày mở pilot (Ngày 0)**.
- **Điều kiện 2 (Kinh tế & Vận hành):** Giữ tỉ lệ `staff_review_decision` dưới `50%` và thời gian xem lại trung bình dưới `4,8 phút/lần` bằng lộ trình giảm xem lại theo bậc; thay thế số `simulated` bằng giờ nhân viên thật sau tuần 1 — Phụ trách: **Trưởng nhóm CSKH** — Kiểm tra: **Ngày 7 của pilot**.
- **Điều kiện 3 (Nghiệm thu pilot):** Đạt tối thiểu `299` yêu cầu/nhân viên trên `20 + 20` nhân viên và không chạm 3 luật dừng trong `pilot_plan.yaml` — Phụ trách: **Giám đốc vận hành LogiX-VN** — Kiểm tra: **Ngày 15 (kết thúc cửa sổ 7 ngày)**.
