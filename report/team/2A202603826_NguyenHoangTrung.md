# Báo cáo cá nhân — NguyenHoangTrung-2A202603826

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hoàng Trung
- MSSV: 2A202603826
- Email: 26ai.trungnh@vinuni.edu.vn
- GitHub: trungtk03
- Vai trong nhóm: Nhóm trưởng (chủ fork) · Người viết code (chặng 1: A–B) → Kiểm số & soát kỹ thuật (chặng 2: D–E)

## 2. Phần việc phụ trách

- Thiết lập và quản lý repo fork nhóm `K5-L3B-DAY13-HelloWorld-LaunchEconomics`, rà soát checklist trước khi push.
- **Nhiệm vụ A & B:** Viết code `src/lab13.py` cho A1 (3 phép thử đáp án biết trước), A2–A4 (mô hình chi phí, tách theo loại, chi phí cố định) và B1–B4 (bảng độ nhạy, giới hạn lần chạy, xem lại 100%).
- **Nhiệm vụ C:** Hỗ trợ chốt tài liệu A–B trong thời gian hai bạn gắn nhãn độc lập; cùng rà soát bảng khắc phục 5 ca.
- **Nhiệm vụ D:** Đổi vai sang kiểm số và đối chiếu tính nhất quán của `report/team/pilot_plan.yaml` với số liệu A–B.
- **Nhiệm vụ E & Duyệt chéo Gate 2a:** Viết bảng rủi ro kinh tế E2 trong `report/team/chi_so.md`, kiểm tra chạy chéo `src/lab13.py`, đại diện trình bày và trả lời câu hỏi hội đồng, hoàn thiện `report/team/phieu_cham.md` và `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- **Khởi tạo repo & điều phối nhóm:** Tạo fork `K5-L3B-DAY13-HelloWorld-LaunchEconomics`, phân vai 2 chặng (đổi người viết code sau giải lao) trong `TEAM.md` và khởi tạo bộ 4 báo cáo cá nhân.
- **Chặng 1 (Nhiệm vụ A & B · Người viết code):** Cài đặt môi trường `src/.venv` và viết code `src/lab13.py` cho A1 (3 phép thử đạt `1,20 · 1,25 · 1,25`), A2 (`mo_hinh` tính CPS `4.472 đ` `simulated`, gấp `16,3×` hoá đơn `274,7 đ`), A3 (tách 4 loại + bảng tỉ lệ `ok` theo `attempt`), A4 (chi phí cố định 40 triệu đ/tháng), B1–B4 (9 kịch bản độ nhạy, cặp cộng tuyến tính `+46,3%`, chi phí cả hệ thống rẻ nhất ở giới hạn 2 lần `6.901.220 đ`, kịch bản xem lại 100% `11.743 đ` / `12.415 đ` `simulated`).
- **Chặng 2 (Nhiệm vụ D & E · Kiểm số & soát kỹ thuật):**
  - Chạy kiểm chứng chéo toàn bộ `src/lab13.py` (gồm code D1, E1 và kiểm tra YAML của Đỗ Triệu Đức Phương) trên máy nhóm trưởng: chạy trọn vẹn từ đầu tới cuối, tất cả phép thử ĐẠT.
  - Tính tay đối chiếu toàn bộ 5 câu D1 (`1.251`, `DE=2,48 / 3.103 / 84 người`, trần `1.000`, trần `300`, MDE `+6 điểm`: `859` mẫu hiệu dụng với `m >= 299`, `DE = 6,96`, power `0,64` ở mức `+5 điểm`), tỉ lệ mở lại (`4,25%` toàn mẫu, `3,97%` phạm vi pilot) và 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`).
  - Hoàn thiện mục **E2 · Rủi ro kinh tế** (4 dòng rủi ro kinh tế nối trực tiếp với số liệu độ nhạy B1/B3/B4/A4 và event có `trace_id`) trong `report/team/chi_so.md`.
  - Rà soát kỹ thuật toàn bộ `report/team/*`: bổ sung nhãn `simulated` đầy đủ trong `pilot_plan.yaml`, đồng bộ mốc `≥ 10 ngày` cho phạm vi `81,8%` và sửa Mục 3 `ho_so_launch_v0.md` từ `0,37×` sang `0,49×` (cả hệ thống) kèm xem lại phân tầng sau phản biện Gate 2a.
- **Duyệt chéo Gate 2a & Đóng gói:** Đại diện nhóm bảo vệ hồ sơ và trả lời câu hỏi hội đồng; đọc repo và chấm hồ sơ Nhóm 08 (`25112026`, `30/30`, Go có điều kiện) trong `report/team/phieu_cham.md`; viết báo cáo nhóm `report/team/group_report.md` và soát toàn bộ checklist nộp bài.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit `27acbd9` (`TEAM.md` và khởi tạo 4 báo cáo cá nhân).
- Commit `afe922b` (`src/lab13.py` — hoàn thiện Nhiệm vụ A và B).
- Commit `23a0087` (`report/team/chi_so.md` bảng `E2 · Rủi ro kinh tế`, soát `report/team/pilot_plan.yaml`, cập nhật `TEAM.md`).
- Commit `6ae3b79` và bản hoàn chỉnh `report/team/phieu_cham.md` (chấm Nhóm 08: `30/30`), `report/team/group_report.md` và bản đồng bộ cuối `report/team/ho_so_launch_v0.md`.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Dùng trợ lý AI (Antigravity / Gemini) để hỗ trợ phân công đầu việc theo rubric, cấu trúc khung hàm `src/lab13.py`, rà soát checklist kỹ thuật (nhãn `simulated`, từ cấm, tính nhất quán chéo giữa các file hồ sơ), biên tập bảng rủi ro kinh tế E2, phiếu chấm dựa trên repo thật của Nhóm 08 và báo cáo nhóm.
- **Cách tự kiểm tra:** chạy trực tiếp `src/lab13.py` trên hai file CSV gốc `src/logix_runs.csv` và `src/logix_requests.csv` để mọi con số xuất phát từ code; kiểm tra đủ 3 phép thử A1; tính tay đối chiếu cỡ mẫu D1 (`co_mau`, `DE`, trần `c/ICC`, giải bất đẳng thức `m >= 299`); đọc trực tiếp 5 file hồ sơ trên repo của Nhóm 08 trước khi chấm; chạy `yaml.safe_load` và quét tự động dấu `?` cùng từ cấm trên toàn bộ `report/team/`.

## 6. Tự đánh giá

- Hoàn thành trọn vẹn vai trò nhóm trưởng, người viết code chặng 1 (A–B), người kiểm số/soát kỹ thuật chặng 2 (D–E), người bảo vệ Gate 2a và đóng gói nộp bài; đảm bảo mọi file trong `SUBMISSION.md` đều đầy đủ, thống nhất số liệu và không vi phạm quy tắc lab.
- Điểm rút kinh nghiệm: cần rà kỹ ngay từ đầu các mốc thời gian gom mẫu theo lưu lượng sau khi thu hẹp phạm vi (`81,8%` → `≥ 10 ngày` thay vì `8 ngày`) và tránh nhầm tỉ số CPS riêng (`0,37×`) với chi phí cả hệ thống (`0,49×`) khi tổng hợp trang hồ sơ v0.
