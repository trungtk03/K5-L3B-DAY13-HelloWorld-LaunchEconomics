# Team

## Thông tin nhóm

- Tên nhóm: HelloWorld
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-HelloWorld-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/trungtk03/K5-L3B-DAY13-HelloWorld-LaunchEconomics · nhánh `main` · commit chốt: *(cập nhật hash commit cuối sau khi push)*

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Hoàng Trung | 2A202603826 | 26ai.trungnh@vinuni.edu.vn | trungtk03 | Nhóm trưởng (chủ fork) · Người viết code (chặng 1: A–B) → Kiểm số & soát kỹ thuật (chặng 2: D–E) |
|   2 | Đỗ Triệu Đức Phương | 2A202603843 | 2023600426@st.haui.edu.vn | ducphuong2005 | Người kiểm số (chặng 1: A–B) → Người viết code (chặng 2: D–E) |
|   3 | Nguyễn Duy Mạnh | 2A202603806 | 26ai.manhnd9@vinuni.edu.vn | hnamyud | Người gắn nhãn 1 · Theo dõi điều kiện "Xong khi" (QA) |
|   4 | Vũ Xuân Bách | 2A202603803 | bachvx.1709@gmail.com | bachvx1709 | Người gắn nhãn 2 · Người giữ hồ sơ (`ho_so_launch_v0.md`) |

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

- **Thiết lập repo & Chặng 1 (A–B · Người viết code):**
  - Tạo fork repo nhóm `K5-L3B-DAY13-HelloWorld-LaunchEconomics`, lập bảng phân công 4 vai (đổi người viết code sau giải lao) trong `TEAM.md` và khởi tạo 4 file báo cáo cá nhân theo đúng mẫu.
  - Viết hoàn chỉnh code Nhiệm vụ A (A1–A4) và B (B1–B4) trong `src/lab13.py`: đạt đủ 3 phép thử A1 (`1,20 · 1,25 · 1,25`), tính đầy đủ bảng A2 (`4.373.585 đ`, `978` việc thành công, CPS `4.472 đ` `simulated`, gấp `16,3×` hoá đơn `274,7 đ`), A3 theo 4 loại yêu cầu + tỉ lệ `ok` theo `attempt`, A4 chi phí cố định (`4.599 đ` và `5.784 đ` `simulated`), B1–B4 (độ nhạy, cộng tuyến tính, chi phí cả hệ thống rẻ nhất ở giới hạn 2 lần `6.901.220 đ`, xem lại 100% `11.743 đ` / `12.415 đ` `simulated`).
- **Chặng 2 (D–E · Kiểm số & soát kỹ thuật):**
  - Chạy kiểm chứng chéo toàn bộ `src/lab13.py` (gồm code D1, E1 và kiểm tra `pilot_plan.yaml` do Đỗ Triệu Đức Phương bổ sung) trên máy của nhóm trưởng: xác nhận chạy trọn vẹn từ đầu tới cuối, không lỗi.
  - Kiểm số bằng tay toàn bộ 5 câu D1 (`1.251`, `DE=2,48 / 3.103 / 84 người`, trần `1.000`, trần `300`, MDE `+6 điểm`: `859` mẫu hiệu dụng với `m >= 299`, `DE = 6,96`, power `0,64` ở mức `+5 điểm`), tỉ lệ mở lại (`4,25%` toàn mẫu, `3,97%` phạm vi pilot) và 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`).
  - Rà soát kỹ thuật toàn bộ `report/team/*`: bổ sung nhãn `simulated` còn thiếu cho `quoc_te`/`doi_tac` trong trường `scope` của `report/team/pilot_plan.yaml`; xác nhận `yaml.safe_load` hợp lệ, không còn dấu `?` ngoài chú thích, không có từ cấm trong `report/team/`, không sửa `src/logix_runs.csv`, `src/logix_requests.csv` và `src/lab13_starter.py`; phát hiện và báo sửa lỗi `0,37×` → `0,49×` (cả hệ thống) ở Mục 3 của `ho_so_launch_v0.md`.
  - Hoàn thiện bảng **E2 · Rủi ro kinh tế** (4 dòng rủi ro có tác động đã tính kèm nhãn `simulated`, dấu hiệu đo được gắn với event có `trace_id`, hành động và 1 vai trò phụ trách) trong `report/team/chi_so.md`.

### Bằng chứng

- `src/lab13.py` (commit `afe922b` cho A–B; chạy chéo xác nhận toàn bộ A–B–D–E1 đạt)
- `report/team/chi_so.md` (commit `23a0087`: hoàn thiện bảng `E2 · Rủi ro kinh tế`)
- `report/team/pilot_plan.yaml` (soát kỹ thuật, bổ sung nhãn `simulated` và đồng bộ mốc `≥ 10 ngày` cho phạm vi `81,8%`)
- `report/team/phieu_cham.md` (commit `6ae3b79` và bản chốt chấm Nhóm 08 đạt `30/30`), `report/team/group_report.md`, `TEAM.md` và `report/team/2A202603826_NguyenHoangTrung.md`

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
- **Chặng 2 (D–E · Người viết code chặng 2):**
  - Viết hoàn chỉnh `TODO CP4` và `E1` trong `src/lab13.py`: tính cỡ mẫu 5 câu D1 (`1.251`, `DE=2,48 / 3.103 / 84 người`, trần `1.000`, trần `300`, MDE +6 điểm `859` mẫu hiệu dụng với `m >= 299` đơn/người, `DE=6,96`, cần ≥ 8 ngày gom mẫu ở bước 20+20 người), đối chiếu power `0,64` bằng `statsmodels`, tính tỉ lệ `mo_lai_trong_7_ngay` (`4,25%` toàn mẫu; `3,97%` phạm vi pilot), tính thử 3 chỉ số E1 và viết hàm kiểm tra hợp lệ `report/team/pilot_plan.yaml`.
  - Hoàn thiện mục D1 và điền các trường `n_per_arm: 859`, `design_effect: 6.96`, `clusters_per_arm: 20` (xoá hết dấu `?`) trong `report/team/pilot_plan.yaml`; đồng bộ chi tiết bước rollout 8 ngày và điều kiện bật luật dừng theo slide D1/D3.
  - Điền bảng đặc tả chỉ số E1 (3 chỉ số tính thử: `82,83%`, `27,12%`, `4,25%` và 2 chỉ số dùng/an toàn tự đề xuất khớp danh sách event) trong `report/team/chi_so.md`.

### Bằng chứng

- `report/team/bang_chi_phi.md` (commit `d7c79a6`: hoàn chỉnh A1, A2, A3, A4, B1, B2, B3, B4)
- `src/lab13.py` (commit `d445e73`: hoàn thiện `co_mau`, `in_nhiem_vu_d`, `in_nhiem_vu_e1`, `kiem_tra_pilot_plan`)
- `report/team/pilot_plan.yaml` (điền đủ D1, chốt `n_per_arm=859`, `design_effect=6.96`, `clusters_per_arm=20`, không còn `?`, hợp lệ `yaml.safe_load`)
- `report/team/chi_so.md` (hoàn thiện bảng E1: 3 chỉ số tính thử + 2 chỉ số tự đề xuất) và tham gia duyệt chéo `report/team/phieu_cham.md`
- `report/team/2A202603843_DoTrieuDucPhuong.md` (commit `e373d71`)

## NguyenDuyManh-2A202603806

### Phần việc phụ trách

- **Phần A & B:** Theo dõi điều kiện "Xong khi", kiểm tra giới hạn ≤ 3 dòng/câu có số và nhãn `simulated` trên mọi số từ cột `_simulated`.
- **Phần C:** **Người gắn nhãn 1** — gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, cùng Bách đối chiếu tính tỉ lệ đồng thuận (≥ 80%), viết quy tắc phân biệt và điền 3 ca trong bảng khắc phục của `report/team/bang_loi.md`.
- **Phần D (khi công bố đề):** Phụ trách phần lập luận thiết kế và rà soát điều kiện/luật dừng trong `report/team/pilot_plan.yaml`.
- **Phần E & Duyệt chéo:** Lập danh sách ≥ 6 event có `trace_id` và kiểm tra chéo chỉ số–event trong `report/team/chi_so.md`; tham gia chấm tiêu chí hội đồng trong `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- Phần A và B (QA): chạy kiểm tra `src/lab13.py` và soát `report/team/bang_chi_phi.md`. Ba phép thử A1 đạt (`1,20`, `1,25`, `1,25`), đủ 9 dòng A2, 4 dòng A3, bảng A4, 9 dòng B1 cùng B2, B3, B4. Toàn bộ số tính từ cột `_simulated` đều có nhãn `simulated`, câu trả lời tối đa 3 dòng có số, không vi phạm quy tắc 5 trong `README.md` và không ghi "cả đội".
- Phần C (Người gắn nhãn 1): gắn nhãn độc lập 20/20 ca lỗi theo 5 loại Google PAIR (`Do người dùng`: 1, 6, 9, 14; `Hệ thống`: 2, 7, 8, 15, 20; `Ngữ cảnh`: 3, 10, 16, 18; `Giới hạn hệ thống`: 4, 11, 13, 19; `Ngầm`: 5, 12, 17) trong `report/team/bang_loi.md`, đối chiếu cùng Bách đạt đồng thuận `19/20 = 95%`. Điền 3 dòng khắc phục (Ca 9: Do người dùng, Ca 7: Hệ thống, Ca 17: Ngầm) có event phát hiện, ngưỡng, tần suất và một vai trò phụ trách.
- Phần D: viết phần D2 (5 câu kiểm tra "tách được tác động"), nêu đánh đổi khi chia theo nhân viên 20 + 20 và nâng MDE từ 5 lên 6 điểm (power còn khoảng 0,64 ở mức 5 điểm), kiểm tra tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu, `3,97%` phạm vi pilot), rồi điền `owner`, `scope`, `assignment`, `identifiability`, 3 `stop_rules` đủ 4 vế `NẾU`, `TRONG`, `THÌ`, `KHÔNG THÌ`, `interim_looks`, `rollback`, `decision_date` và `simulated_inputs` trong `report/team/pilot_plan.yaml`.
- Phần E: lập danh sách event có `trace_id` (đồng bộ cả các event phát hiện lỗi từ `bang_loi.md`) và viết mục kiểm tra chéo cho mọi chỉ số E1 (chính, dùng, an toàn, chỉ số tự đề xuất, cùng giờ nhân viên thật thay `_simulated`) trong `report/team/chi_so.md`.
- Duyệt chéo Gate 2a (`report/team/phieu_cham.md`): cập nhật trực tiếp lúc 17:00 khi nhận hồ sơ của nhóm bạn.

### Bằng chứng

- Commit `0f334ae` trên nhánh `main`
- `report/team/bang_loi.md` (cột Nhãn người 1 đủ 20 ca độc lập, đồng thuận `19/20 = 95%` và 3 dòng khắc phục Ca 9, 7, 17)
- `report/team/pilot_plan.yaml` (phần D2, đánh đổi, tỉ lệ mở lại `4,25%` và `3,97%`, `identifiability`, 3 `stop_rules`, `rollback`, `simulated_inputs`)
- `report/team/chi_so.md` (danh sách 13 event có `trace_id` và kiểm tra chéo chỉ số với event)
- `report/team/2A202603806_NguyenDuyManh.md` (báo cáo cá nhân)

## VuXuanBach-2A202603803

### Phần việc phụ trách

- **Xuyên suốt A–E:** **Người giữ hồ sơ** — cập nhật dần `report/team/ho_so_launch_v0.md` sau từng checkpoint (đủ 7 mục, đúng trạng thái, 1 vai trò phụ trách, không dùng từ cấm).
- **Phần C:** **Người gắn nhãn 2** — gắn nhãn độc lập 20 ca lỗi (không trao đổi), cùng Mạnh so nhãn, thống nhất quy tắc cho ca lệch và điền 2 ca trong bảng khắc phục của `report/team/bang_loi.md`.
- **Phần D (khi công bố đề):** Phối hợp chốt nội dung `report/team/pilot_plan.yaml` và cập nhật Mục 6 của hồ sơ launch v0.
- **Phần E & Duyệt chéo:** Chốt trọn vẹn 1 trang `report/team/ho_so_launch_v0.md` kèm đề xuất cuối trước 17:00; cùng Trung hoàn thiện `report/team/group_report.md` và tham gia chấm `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- **Phần C (Người gắn nhãn 2):** Gắn nhãn độc lập 20/20 ca lỗi theo 5 loại Google PAIR trong `report/team/bang_loi.md` (không trao đổi trước khi so nhãn), đối chiếu cùng Nguyễn Duy Mạnh đạt tỉ lệ đồng thuận `19/20 = 95%`, thống nhất quy tắc phân biệt Ca 8 và hoàn thiện 2 ca khắc phục còn lại (Ca 3: Ngữ cảnh, Ca 4: Giới hạn hệ thống) có ngưỡng đo được và một vai trò phụ trách.
- **Xuyên suốt A–E (Người giữ hồ sơ):** Cập nhật liên tục `report/team/ho_so_launch_v0.md` từ CP1–CP3 đến bản chốt Gate 2a (đủ 7 mục trong 1 trang, đúng nhãn trạng thái `Giả lập` / `Xong, có bằng chứng`, mỗi mục gắn một vai trò phụ trách, chốt đề xuất **Go có điều kiện** kèm 3 điều kiện cụ thể và thời hạn kiểm tra).
- **Duyệt chéo Gate 2a:** Tham gia đối chiếu hồ sơ Nhóm 08 và hoàn thiện tổng hợp nhóm.

### Bằng chứng

- Commits `d6c9841`, `f3248c1` (`report/team/bang_loi.md`: cột Nhãn người 2 độc lập 20/20 ca, đồng thuận `95%`, 2 dòng khắc phục Ca 3 và Ca 4)
- Commits `3b50c97`, `ab31235` (`report/team/ho_so_launch_v0.md`: hồ sơ launch v0 đủ 7 mục và đề xuất Go có điều kiện)
- `report/team/2A202603803_VuXuanBach.md` (báo cáo cá nhân)
