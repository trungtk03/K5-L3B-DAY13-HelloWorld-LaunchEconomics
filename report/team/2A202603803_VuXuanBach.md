# Báo cáo cá nhân — VuXuanBach-2A202603803

## 1. Thông tin thành viên

- Họ tên: Vũ Xuân Bách
- MSSV: 2A202603803
- Email: 26ai.bachvx2@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2 · Người giữ hồ sơ (`ho_so_launch_v0.md`)

## 2. Phần việc phụ trách

- **Xuyên suốt A–E:** Giữ và cập nhật dần `report/team/ho_so_launch_v0.md` ngay sau mỗi checkpoint (đủ 7 mục trong 1 trang, đúng nhãn trạng thái, mỗi mục gắn 1 vai trò phụ trách cụ thể).
- **Nhiệm vụ C:** **Người gắn nhãn 2** — gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (không trao đổi), cùng Mạnh đối chiếu, tính tỉ lệ đồng thuận, thống nhất quy tắc phân biệt và điền 2 ca trong bảng khắc phục của `report/team/bang_loi.md`.
- **Nhiệm vụ D:** Phối hợp hoàn thiện `report/team/pilot_plan.yaml` và cập nhật Mục 6 của hồ sơ launch v0.
- **Nhiệm vụ E & Duyệt chéo Gate 2a:** Chốt hoàn chỉnh `report/team/ho_so_launch_v0.md` kèm đề xuất cuối trước 17:00; phối hợp hoàn thiện `report/team/group_report.md` và tham gia chấm nhóm bạn trong `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- **Nhiệm vụ C (CP3 — Người gắn nhãn 2):**
  - Gắn nhãn độc lập 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` theo 5 loại Google PAIR (nguyên nhân gốc).
  - Đối chiếu với Người gắn nhãn 1 (Nguyễn Duy Mạnh), đạt tỉ lệ đồng thuận **19/20 = 95%** (vượt ngưỡng 80%).
  - Thống nhất nhãn **Ngầm** cho ca lệch duy nhất (Ca 8) và viết 1 câu quy tắc phân biệt.
  - Điền 2 dòng bảng khắc phục trong `report/team/bang_loi.md`: **Ca 3 (Ngữ cảnh)** (đo bằng tỉ lệ ticket hỏi chưa nhận được tiền trên `refund_wallet_success` > 5%/tuần, phụ trách: *Quản lý sản phẩm*) và **Ca 4 (Giới hạn hệ thống)** (đo bằng event `handoff_foreign_carrier` > 10 ca/ngày, phụ trách: *Trưởng nhóm CSKH*).
- **Xuyên suốt A–E (Người giữ hồ sơ `ho_so_launch_v0.md`):**
  - Tổng hợp, đối chiếu số liệu từ `bang_chi_phi.md` (CP1–CP2), `bang_loi.md` (CP3), `pilot_plan.yaml` (CP4) và `chi_so.md` (CP5) vào đủ 7 mục của `report/team/ho_so_launch_v0.md` trước 17:00.
  - Gắn đúng nhãn trạng thái (`Giả lập` cho số từ cột `_simulated`, `Xong, có bằng chứng` cho các mục còn lại) và 1 vai trò phụ trách cụ thể cho từng mục.
  - Chốt đề xuất **Go có điều kiện** kèm 3 điều kiện cụ thể (kỹ thuật/an toàn, kinh tế/vận hành, nghiệm thu pilot), người phụ trách và ngày kiểm tra, không dùng từ "production".

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- `report/team/bang_loi.md` (commit `f3248c1`): cột `Nhãn người 2 (Bách)`, tỉ lệ đồng thuận `19/20 = 95%`, quy tắc Ca 8 và 2 dòng khắc phục (Ca 3, Ca 4).
- `report/team/ho_so_launch_v0.md` (commit `3b50c97` cho CP1–CP3; commit `ab31235` hoàn thiện đủ 7 mục + đề xuất `Go có điều kiện` cho Gate 2a).

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Sử dụng trợ lý AI trong IDE để hỗ trợ rà soát cấu trúc tài liệu, đối chiếu tính nhất quán số liệu giữa `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md` với `ho_so_launch_v0.md`.
- Tự kiểm tra lại toàn bộ 20 ca lỗi từ file đề bài gốc `.docx`, đối chiếu trực tiếp từng con số với bảng nguồn và đảm bảo đúng quy tắc nhãn `simulated` / không dùng từ cấm.

## 6. Tự đánh giá

- **Điểm làm tốt:** Phối hợp nhịp nhàng với các thành viên qua Git (chủ động fetch/rebase, giải quyết conflict sạch sẽ) và nắm chắc cách phân loại lỗi theo nguyên nhân gốc.
- **Điểm cần cải thiện:** Cần chủ động trao đổi và xác nhận lại thông tin với các thành viên ngay khi chuyển giao giữa các checkpoint để cả nhóm nắm rõ tiến độ và yêu cầu của nhau hơn.
