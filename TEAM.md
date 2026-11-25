# Team

## Thông tin nhóm

- Tên nhóm: HelloWorld
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-HelloWorld-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/trungtk03/K5-L3B-DAY13-HelloWorld-LaunchEconomics · nhánh `main` · commit chốt: *(cập nhật trước khi nộp)*

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Hoàng Trung | 2A202603826 | *(điền email)* | trungtk03 | Nhóm trưởng (chủ fork) · Người viết code (chặng 1: A–B) → Kiểm số & soát kỹ thuật (chặng 2: D–E) |
|   2 | Đỗ Triệu Đức Phương | 2A202603843 | *(điền email)* | *(điền GitHub)* | Người kiểm số (chặng 1: A–B) → Người viết code (chặng 2: D–E) |
|   3 | Nguyễn Duy Mạnh | 2A202603806 | *(điền email)* | *(điền GitHub)* | Người gắn nhãn 1 · Theo dõi điều kiện "Xong khi" (QA) |
|   4 | Vũ Xuân Bách | 2A202603803 | *(điền email)* | *(điền GitHub)* | Người gắn nhãn 2 · Người giữ hồ sơ (`ho_so_launch_v0.md`) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py` (Trung chặng 1: A–B; Phương chặng 2: D–E sau giờ giải lao).
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng (Phương chặng 1: A–B; Trung chặng 2: D–E).
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3 (Mạnh).
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3 (Bách).

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng `report/team/MSSV_HoTen.md`:

- `report/team/2A202603826_NguyenHoangTrung.md`
- `report/team/2A202603843_DoTrieuDucPhuong.md`
- `report/team/2A202603806_NguyenDuyManh.md`
- `report/team/2A202603803_VuXuanBach.md`

## NguyenHoangTrung-2A202603826

### Phần việc phụ trách

- Tạo fork repo nhóm, quản lý nhánh/merge/push và kiểm tra checklist trước khi nộp.
- **Phần A & B:** Viết code `src/lab13.py` (A1 ba phép thử, A2–A4 mô hình chi phí và chi phí cố định, B1–B4 bảng độ nhạy).
- **Phần C:** Hoàn thiện CP1–CP2 trong lúc hai bạn gắn nhãn độc lập; phản biện bảng khắc phục 5 ca.
- **Phần D (khi công bố đề):** Chuyển sang vai kiểm số/rà tính nhất quán số liệu với `report/team/pilot_plan.yaml`.
- **Phần E & Duyệt chéo:** Viết bảng rủi ro kinh tế trong `report/team/chi_so.md`, test chạy chéo `src/lab13.py` trên máy khác, đại diện trình bày và điều phối trả lời hội đồng Gate 2a.

### Đóng góp cụ thể

- *(Cập nhật sau khi hoàn thành từng checkpoint)*

### Bằng chứng

- *(Ghi commit hash, file và bảng đã hoàn thành)*

## DoTrieuDucPhuong-2A202603843

### Phần việc phụ trách

- **Phần A & B:** Người kiểm số — tính tay đối chiếu số liệu từ trace, tự kiểm tra đối xứng bảng độ nhạy, điền hoàn chỉnh `report/team/bang_chi_phi.md` (A2, A3, A4, B1–B4).
- **Phần C:** Hoàn thiện `report/team/bang_chi_phi.md` song song trong 8 phút gắn nhãn độc lập; cùng rà soát bảng khắc phục 5 ca.
- **Phần D (khi công bố đề):** Nhận vai **Người viết code chặng 2** trong `src/lab13.py` (`TODO CP4`), chạy kiểm tra hợp lệ `report/team/pilot_plan.yaml`.
- **Phần E & Duyệt chéo:** Tính thử 3 chỉ số và đề xuất thêm chỉ số dùng/an toàn trong `report/team/chi_so.md`; tham gia chấm tiêu chí hội đồng trong `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- **Chặng 1 (A–B · Người kiểm số):**
  - Đối chiếu độc lập từ hai file CSV gốc (`src/logix_runs.csv`, `src/logix_requests.csv`) với kết quả chạy `src/lab13.py` của Trung: xác nhận 3 phép thử A1 đạt (`1,20 · 1,25 · 1,25`), khớp toàn bộ số liệu A2 (`4.373.585 đ`, `978` việc thành công, CPS `4.472 đ` `[simulated]`, gấp `16,3×` hoá đơn `274,7 đ`), A3, A4 (`4.599 đ` ở 45.000 yc/tháng và `5.784 đ` ở nửa khối lượng `[simulated]`), B1–B4 (lệch < 0,01% so với số tham chiếu).
  - Kiểm tra tính đối xứng bảng độ nhạy B1 (`+5,6% / −2,8%`; `+40,7% / −20,3%`; `+51,8% / −25,9%`), tính cộng tuyến tính B2 (`+46,3%`), chênh lệch tối ưu CPS vs cả hệ thống ở B3 (`1 lần` vs `2 lần`), và cả hai kịch bản làm lại (`9 phút` và `15,3 phút`) kèm ngưỡng hoà vốn ở B4.
  - Điền hoàn chỉnh `report/team/bang_chi_phi.md` (A1–A4, B1–B4), đảm bảo đầy đủ nhãn `simulated`, mỗi câu trả lời ≤ 3 dòng có số, không dùng từ cấm.
- **Chặng 2 (C–E):** *(Cập nhật sau khi hoàn thành CP3–CP5)*

### Bằng chứng

- `report/team/bang_chi_phi.md` (hoàn chỉnh A1, A2, A3, A4, B1, B2, B3, B4)
- *(Bổ sung commit hash và các file chặng 2 sau khi push)*

## NguyenDuyManh-2A202603806

### Phần việc phụ trách

- **Phần A & B:** Theo dõi điều kiện "Xong khi", kiểm tra giới hạn ≤ 3 dòng/câu có số và nhãn `simulated` trên mọi số từ cột `_simulated`.
- **Phần C:** **Người gắn nhãn 1** — gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, cùng Bách đối chiếu tính tỉ lệ đồng thuận (≥ 80%), viết quy tắc phân biệt và điền 3 ca trong bảng khắc phục của `report/team/bang_loi.md`.
- **Phần D (khi công bố đề):** Phụ trách phần lập luận thiết kế và rà soát điều kiện/luật dừng trong `report/team/pilot_plan.yaml`.
- **Phần E & Duyệt chéo:** Lập danh sách ≥ 6 event có `trace_id` và kiểm tra chéo chỉ số–event trong `report/team/chi_so.md`; tham gia chấm tiêu chí hội đồng trong `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- *(Cập nhật sau khi hoàn thành từng checkpoint)*

### Bằng chứng

- *(Ghi commit hash, file và bảng đã hoàn thành)*

## VuXuanBach-2A202603803

### Phần việc phụ trách

- **Xuyên suốt A–E:** **Người giữ hồ sơ** — cập nhật dần `report/team/ho_so_launch_v0.md` sau từng checkpoint (đủ 7 mục, đúng trạng thái, 1 vai trò phụ trách, không dùng từ cấm).
- **Phần C:** **Người gắn nhãn 2** — gắn nhãn độc lập 20 ca lỗi (không trao đổi), cùng Mạnh so nhãn, thống nhất quy tắc cho ca lệch và điền 2 ca trong bảng khắc phục của `report/team/bang_loi.md`.
- **Phần D (khi công bố đề):** Phối hợp chốt nội dung `report/team/pilot_plan.yaml` và cập nhật Mục 6 của hồ sơ launch v0.
- **Phần E & Duyệt chéo:** Chốt trọn vẹn 1 trang `report/team/ho_so_launch_v0.md` kèm đề xuất cuối trước 17:00; cùng Trung hoàn thiện `report/team/group_report.md` và tham gia chấm `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- *(Cập nhật sau khi hoàn thành từng checkpoint)*

### Bằng chứng

- *(Ghi commit hash, file và bảng đã hoàn thành)*
