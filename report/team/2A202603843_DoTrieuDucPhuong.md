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
- **Chặng 2 (CP4–CP5 · Nhiệm vụ D–E · Người viết code chặng 2):**
  - Triển khai `co_mau`, `in_nhiem_vu_d`, `in_nhiem_vu_e1` và `kiem_tra_pilot_plan` trong `src/lab13.py` (tính đủ 5 câu D1, đối chiếu power `0,64` bằng `statsmodels`, tính thời gian gom mẫu ≥ 8 ngày ở bước 20+20 người theo slide D1, tính thử 3 chỉ số E1 và kiểm tra `yaml.safe_load`).
  - Hoàn thiện phần D1 và chốt `n_per_arm: 859`, `design_effect: 6.96`, `clusters_per_arm: 20` trong `report/team/pilot_plan.yaml`, đồng bộ điều kiện luật dừng ở bước 4/10/20 người và chi phí biến đổi chưa cộng 40 triệu cố định.
  - Hoàn thiện bảng E1 trong `report/team/chi_so.md` với 3 chỉ số tính thử (`82,83%`, `27,12%`, `4,25%`) và 2 chỉ số dùng/an toàn tự đề xuất khớp danh sách event.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- `report/team/bang_chi_phi.md`: hoàn chỉnh toàn bộ bảng và câu trả lời A1–A4, B1–B4 (A2 CPS `4.472 đ` `[simulated]`, gấp `16,3×` hoá đơn `274,7 đ`; A3 loại `quoc_te` `22.515 đ` = `1,88×`; A4 `4.599 đ` và `5.784 đ` `[simulated]`; B1–B2 top 3 làm lại `51,8%`, xem lại `40,7%`, lương `23,1%`; B3 giới hạn `2 lần` rẻ nhất cả hệ thống `6.901.220 đ` `[simulated]`; B4 xem lại 100% đạt `11.743 đ` / `12.415 đ` `[simulated]`).
- `src/lab13.py`: hoàn thiện phần D1 (`1.251`, `3.103 / 84 người`, trần `1.000`, trần `300`, MDE +6 điểm `859` mẫu hiệu dụng với `m >= 299`, `DE = 6,96`, power `0,64` ở mức +5 điểm), tính thử E1 (`82,83%`, `27,12%`, `4,25%`) và hàm kiểm tra `report/team/pilot_plan.yaml`.
- `report/team/pilot_plan.yaml`: điền đủ D1, chốt `n_per_arm: 859`, `design_effect: 6.96`, `clusters_per_arm: 20`, không còn dấu `?`, hợp lệ `yaml.safe_load`.
- `report/team/chi_so.md`: hoàn thiện bảng E1 (3 chỉ số tính thử + 2 chỉ số tự đề xuất khớp kiểm tra chéo event).
- *(Cập nhật commit hash cuối và `report/team/phieu_cham.md` sau duyệt chéo Gate 2a)*

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Sử dụng trợ lý AI (Antigravity / Gemini) hỗ trợ đối chiếu công thức từ dữ liệu CSV gốc, soát nhãn `simulated`, kiểm tra quy tắc trình bày (≤ 3 dòng/câu, không dùng từ cấm) và biên tập bảng `report/team/bang_chi_phi.md`.
- Tự kiểm tra bằng cách chạy đối chiếu độc lập trên `src/logix_runs.csv` và `src/logix_requests.csv` so với output `src/lab13.py` và số tham chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (mọi số khớp trong sai số < 0,01%, dưới ngưỡng cho phép 2%).

## 6. Tự đánh giá

- **Điểm làm tốt:**
  - kiểm số độc lập trực tiếp trên hai file CSV gốc cho toàn bộ phần A–B và iết code chặng 2 (`co_mau`, D1, E1, kiểm tra hợp lệ `pilot_plan.yaml`) trong `src/lab13.py`.
- **Điểm cần cải thiện:**
  - Khi thao tác git từ thư mục con `src/`, cần chú ý đường dẫn (`git add -A` hoặc ra thư mục gốc) để tránh sót file ở `report/team/` và `TEAM.md`.
  