# Báo cáo cá nhân — NguyenHoangTrung-2A202603826

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hoàng Trung
- MSSV: 2A202603826
- Email: *(điền email)*
- Vai trong nhóm: Nhóm trưởng (chủ fork) · Người viết code (chặng 1: A–B) → Kiểm số & soát kỹ thuật (chặng 2: D–E)

## 2. Phần việc phụ trách

- Thiết lập và quản lý repo fork nhóm `K5-L3B-DAY13-HelloWorld-LaunchEconomics`, rà soát checklist trước khi push.
- **Nhiệm vụ A & B:** Viết code `src/lab13.py` cho A1 (3 phép thử đáp án biết trước), A2–A4 (mô hình chi phí, tách theo loại, chi phí cố định) và B1–B4 (bảng độ nhạy, giới hạn lần chạy, xem lại 100%).
- **Nhiệm vụ C:** Hỗ trợ chốt tài liệu A–B trong thời gian hai bạn gắn nhãn độc lập; cùng rà soát bảng khắc phục 5 ca.
- **Nhiệm vụ D *(cập nhật chi tiết sau khi đề công bố)*:** Đổi vai sang kiểm số và đối chiếu tính nhất quán của `report/team/pilot_plan.yaml` với số liệu A–B.
- **Nhiệm vụ E & Duyệt chéo Gate 2a:** Viết bảng rủi ro kinh tế trong `report/team/chi_so.md`, kiểm tra chạy chéo `src/lab13.py`, đại diện trình bày và điều phối trả lời câu hỏi hội đồng.

## 3. Đóng góp cụ thể

- **Khởi tạo repo & điều phối nhóm:** Tạo fork `K5-L3B-DAY13-HelloWorld-LaunchEconomics`, phân vai 2 chặng (đổi người viết code sau giải lao) trong `TEAM.md` và khởi tạo bộ 4 báo cáo cá nhân.
- **Chặng 1 (Nhiệm vụ A & B · Người viết code):** Cài đặt môi trường `src/.venv` và viết code `src/lab13.py` cho A1 (3 phép thử đạt `1,20 · 1,25 · 1,25`), A2 (`mo_hinh` tính CPS `4.472 đ` `simulated`, gấp `16,3×` hoá đơn `274,7 đ`), A3 (tách 4 loại + bảng tỉ lệ `ok` theo `attempt`), A4 (chi phí cố định 40 triệu đ/tháng), B1–B4 (9 kịch bản độ nhạy, cặp cộng tuyến tính `+46,3%`, chi phí cả hệ thống rẻ nhất ở giới hạn 2 lần `6.901.220 đ`, kịch bản xem lại 100% `11.743 đ` / `12.415 đ` `simulated`).
- **Chặng 2 (Nhiệm vụ D & E · Kiểm số & soát kỹ thuật):**
  - Chạy kiểm chứng chéo toàn bộ `src/lab13.py` (sau khi Đỗ Triệu Đức Phương hoàn thiện code D1, E1 và kiểm tra YAML) trên máy khác: chạy trọn vẹn từ đầu tới cuối, tất cả phép thử ĐẠT.
  - Tính tay đối chiếu toàn bộ 5 câu D1 (`1.251`, `DE=2,48 / 3.103 / 84 người`, trần `1.000`, trần `300`, MDE `+6 điểm`: `859` mẫu hiệu dụng với `m >= 299`, `DE = 6,96`, power `0,64` ở mức `+5 điểm`), tỉ lệ mở lại (`4,25%` toàn mẫu, `3,97%` phạm vi pilot) và 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`).
  - Rà soát kỹ thuật `report/team/pilot_plan.yaml` và toàn bộ thư mục `report/team/`: bổ sung nhãn `simulated` cho `quoc_te` và `doi_tac` trong `scope`, xác nhận `yaml.safe_load` hợp lệ, không còn dấu `?` ngoài chú thích, không có từ cấm, nguyên vẹn 2 file CSV và `lab13_starter.py`; phát hiện và cảnh báo sửa Mục 3 `ho_so_launch_v0.md` từ `0,37×` sang `0,49×` (cả hệ thống) kèm số bất lợi B4.
  - Hoàn thiện mục **E2 · Rủi ro kinh tế** (4 dòng rủi ro kinh tế nối trực tiếp với số liệu độ nhạy B1/B3/B4/A4 và event có `trace_id`) trong `report/team/chi_so.md`.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit `afe922b` (`src/lab13.py` — hoàn thiện Nhiệm vụ A và B).
- `report/team/chi_so.md` (bảng `E2 · Rủi ro kinh tế`, 4 dòng đầy đủ số liệu `simulated`, event đo lường và vai trò phụ trách).
- `report/team/pilot_plan.yaml` (soát kỹ thuật & bổ sung nhãn `simulated` trong trường `scope`).
- Kết quả chạy chéo `src/lab13.py` trên máy nhóm trưởng đạt đủ A1, A2–A4, B1–B4, D1, E1 và `yaml.safe_load`.
- *(Bổ sung commit hash chốt cuối buổi và phần duyệt chéo Gate 2a sau 17:45)*

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Dùng trợ lý AI (Antigravity / Gemini) để hỗ trợ phân công đầu việc theo rubric, cấu trúc khung hàm `src/lab13.py`, rà soát checklist kỹ thuật (nhãn `simulated`, từ cấm, tính nhất quán chéo giữa các file hồ sơ) và trình bày bảng rủi ro kinh tế E2.
- **Cách tự kiểm tra:** chạy trực tiếp `src/lab13.py` trên hai file CSV gốc `src/logix_runs.csv` và `src/logix_requests.csv` để mọi con số xuất phát từ code; kiểm tra đủ 3 phép thử A1; tính tay đối chiếu cỡ mẫu D1 (`co_mau`, `DE`, trần `c/ICC`, giải bất đẳng thức `m >= 299`); chạy `yaml.safe_load` và quét tự động dấu `?` cùng từ cấm trên toàn bộ `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đúng vai trò nhóm trưởng, người viết code chặng 1 (A–B) và người kiểm số/soát kỹ thuật chặng 2 (D–E), đảm bảo bàn giao code sạch cho thành viên chặng 2 và phát hiện kịp thời các điểm trừ tiềm ẩn (nhãn `simulated`, lỗi `0,37×` vs `0,49×`) trước giờ bảo vệ Gate 2a.
- Điểm cần tiếp tục hoàn thiện: phối hợp với Vũ Xuân Bách hoàn chỉnh Mục 3, 4, 6, 7 cùng đề xuất cuối trong `ho_so_launch_v0.md` trước 17:00, hoàn thành `phieu_cham.md` và `group_report.md`, sau đó điền email thành viên và commit chốt trước khi nộp LMS.
