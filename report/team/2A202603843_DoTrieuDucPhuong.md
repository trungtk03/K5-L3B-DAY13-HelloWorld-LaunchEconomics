# Báo cáo cá nhân — DoTrieuDucPhuong-2A202603843

## 1. Thông tin thành viên

- Họ tên: Đỗ Triệu Đức Phương
- MSSV: 2A202603843
- Email: *(điền email)*
- Vai trong nhóm: Người kiểm số (chặng 1: A–B) → Người viết code (chặng 2: D–E)

## 2. Phần việc phụ trách

- **Nhiệm vụ A & B:** Tính tay đối chiếu các con số mẫu từ dữ liệu trace, kiểm tra quy tắc tử số/mẫu số và tính đối xứng bảng độ nhạy; điền đầy đủ bảng và câu trả lời A2, A3, A4, B1–B4 vào `report/team/bang_chi_phi.md`.
- **Nhiệm vụ C:** Hoàn thiện `report/team/bang_chi_phi.md` trong 8 phút hai bạn gắn nhãn độc lập; cùng phản biện bảng khắc phục 5 ca.
- **Nhiệm vụ D *(cập nhật chi tiết sau khi đề công bố)*:** Đảm nhận vai **Người viết code chặng 2** trong `src/lab13.py` (`TODO CP4`), kiểm tra tính hợp lệ của `report/team/pilot_plan.yaml`.
- **Nhiệm vụ E & Duyệt chéo Gate 2a:** Tính thử 3 chỉ số (chính, dùng, an toàn) và đề xuất bổ sung chỉ số dùng/an toàn vào `report/team/chi_so.md`; tham gia chấm nhóm bạn trong `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- **Chặng 1 (CP1–CP2 · Nhiệm vụ A–B · Người kiểm số):**
  - Đối chiếu độc lập toàn bộ phép tính A1–A4 và B1–B4 trực tiếp từ `src/logix_runs.csv` (1.624 lần chạy) và `src/logix_requests.csv` (1.200 yêu cầu) với log chạy `src/lab13.py` của nhóm trưởng.
  - Kiểm tra quy tắc tử số (mọi lần chạy kể cả lỗi) / mẫu số (chỉ `ket_qua == 'thanh_cong'`), tính đối xứng giảm một nửa = ½ tăng gấp đôi ở B1, tính cộng tuyến tính ở B2, đối chiếu chi phí cả hệ thống ở B3 và hai kịch bản làm lại (`9 phút` vs `15,3 phút`) ở B4.
  - Hoàn thiện `report/team/bang_chi_phi.md` đầy đủ A1, A2, A3, A4, B1, B2, B3, B4, gắn nhãn `simulated` cho mọi con số phát sinh từ cột `_simulated` và giữ mọi câu trả lời ≤ 3 dòng có số.
- **Chặng 2 (CP3–CP5 · Nhiệm vụ C–E):** *(Cập nhật sau khi hoàn thành)*

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- `report/team/bang_chi_phi.md`: hoàn chỉnh toàn bộ bảng và câu trả lời A1–A4, B1–B4 (A2 CPS `4.472 đ` `[simulated]`, gấp `16,3×` hoá đơn `274,7 đ`; A3 loại `quoc_te` `22.515 đ` = `1,88×`; A4 `4.599 đ` và `5.784 đ` `[simulated]`; B1–B2 top 3 làm lại `51,8%`, xem lại `40,7%`, lương `23,1%`; B3 giới hạn `2 lần` rẻ nhất cả hệ thống `6.901.220 đ` `[simulated]`; B4 xem lại 100% đạt `11.743 đ` / `12.415 đ` `[simulated]`).
- *(Cập nhật commit hash và bằng chứng chặng 2 `src/lab13.py`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/phieu_cham.md` sau khi hoàn thành)*

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Sử dụng trợ lý AI (Antigravity / Gemini) hỗ trợ đối chiếu công thức từ dữ liệu CSV gốc, soát nhãn `simulated`, kiểm tra quy tắc trình bày (≤ 3 dòng/câu, không dùng từ cấm) và biên tập bảng `report/team/bang_chi_phi.md`.
- Tự kiểm tra bằng cách chạy đối chiếu độc lập trên `src/logix_runs.csv` và `src/logix_requests.csv` so với output `src/lab13.py` và số tham chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (mọi số khớp trong sai số < 0,01%, dưới ngưỡng cho phép 2%).

## 6. Tự đánh giá

- *(Tự nhận xét điểm làm tốt và điểm cần cải thiện)*
