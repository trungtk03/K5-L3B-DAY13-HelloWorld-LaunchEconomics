# Báo cáo cá nhân — VuXuanBach-2A202603803

## 1. Thông tin thành viên

- Họ tên: Vũ Xuân Bách
- MSSV: 2A202603803
- Email: bachvx.1709@gmail.com
- GitHub: bachvx1709
- Vai trong nhóm: Người gắn nhãn 2 · Người giữ hồ sơ (`ho_so_launch_v0.md`)

## 2. Phần việc phụ trách

- **Xuyên suốt A–E:** Giữ và cập nhật dần `report/team/ho_so_launch_v0.md` ngay sau mỗi checkpoint (đủ 7 mục trong 1 trang, đúng nhãn trạng thái, mỗi mục gắn 1 vai trò phụ trách cụ thể).
- **Nhiệm vụ C:** **Người gắn nhãn 2** — gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (không trao đổi), cùng Mạnh đối chiếu, tính tỉ lệ đồng thuận, thống nhất quy tắc phân biệt và điền 2 ca trong bảng khắc phục của `report/team/bang_loi.md`.
- **Nhiệm vụ D:** Phối hợp hoàn thiện `report/team/pilot_plan.yaml` và cập nhật Mục 6 của hồ sơ launch v0.
- **Nhiệm vụ E & Duyệt chéo Gate 2a:** Chốt hoàn chỉnh `report/team/ho_so_launch_v0.md` kèm đề xuất cuối trước 17:00; phối hợp hoàn thiện `report/team/group_report.md` và tham gia chấm nhóm bạn trong `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- **Nhiệm vụ C (Người gắn nhãn 2):** Đọc độc lập 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và gắn nhãn theo 5 loại Google PAIR trong 8 phút không trao đổi. Sau khi so nhãn với Nguyễn Duy Mạnh đạt đồng thuận `19/20 = 95%` (chỉ lệch Ca 8 và đã thống nhất quy tắc phân biệt), đồng thời hoàn thiện 2 dòng bảng khắc phục (Ca 3: Ngữ cảnh, Ca 4: Giới hạn hệ thống) trong `report/team/bang_loi.md`.
- **Xuyên suốt A–E (Người giữ hồ sơ):** Tổng hợp số liệu sau từng checkpoint vào `report/team/ho_so_launch_v0.md` (từ CP1–CP3 đến bản chốt đủ 7 mục trong 1 trang cho Gate 2a), đảm bảo đúng cột trạng thái (`Giả lập` / `Xong, có bằng chứng`), mỗi mục gắn đúng 1 vai trò phụ trách và chốt đề xuất **Go có điều kiện** kèm 3 điều kiện cụ thể.
- **Duyệt chéo Gate 2a:** Tham gia rà soát hồ sơ Nhóm 08 cùng cả nhóm và phối hợp chỉnh sửa đồng bộ `ho_so_launch_v0.md` sau phần phản biện.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commits `d6c9841`, `f3248c1` trên nhánh `main` (`report/team/bang_loi.md`: cột Nhãn người 2 độc lập 20/20 ca, đồng thuận `19/20 = 95%`, 2 ca khắc phục Ca 3 và Ca 4).
- Commits `3b50c97`, `ab31235` trên nhánh `main` (`report/team/ho_so_launch_v0.md`: hồ sơ launch v0 đủ 7 mục và đề xuất Go có điều kiện).
- `TEAM.md` (mục đóng góp của Vũ Xuân Bách) và tham gia duyệt chéo `report/team/phieu_cham.md`.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Dùng trợ lý AI (ChatGPT / Gemini) để tra cứu nhanh khung phân loại 5 nhóm lỗi Google PAIR và soát chính tả, độ ngắn gọn của bảng 1 trang `ho_so_launch_v0.md`.
- Tự kiểm tra bằng cách đọc trực tiếp từng ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` để gắn nhãn độc lập theo nguyên nhân gốc trước khi so với Mạnh, đồng thời đối chiếu mọi con số đưa lên `ho_so_launch_v0.md` với `bang_chi_phi.md`, `chi_so.md` và `pilot_plan.yaml`. *(Lưu ý: Bách rà lại đúng tên công cụ AI cá nhân đã dùng trước khi nộp LMS nếu có khác biệt).*

## 6. Tự đánh giá

- **Điểm làm tốt:** Giữ đúng nguyên tắc gắn nhãn độc lập đạt đồng thuận `95%` (`19/20`), cập nhật hồ sơ `ho_so_launch_v0.md` kịp mốc 17:00 để nhóm bảo vệ Gate 2a đúng giờ.
- **Điểm cần rút kinh nghiệm:** Cần kiểm tra kỹ hơn sự khác biệt giữa tỉ số CPS riêng (`0,37×`) và chi phí cả hệ thống (`0,49×`) cũng như mốc thời gian gom mẫu thực tế cho phạm vi `81,8%` (`≥ 10 ngày`) ngay từ lần điền đầu tiên.
