# Báo cáo cá nhân — NguyenDuyManh-2A202603806

## 1. Thông tin thành viên

- Họ tên: Nguyễn Duy Mạnh
- MSSV: 2A202603806
- Email: *(điền email)*
- Vai trong nhóm: Người gắn nhãn 1 · Theo dõi điều kiện "Xong khi" (QA)

## 2. Phần việc phụ trách

- **Nhiệm vụ A & B:** Đọc đề, theo dõi điều kiện "Xong khi" của từng checkpoint; kiểm tra giới hạn ≤ 3 dòng/câu có số và nhãn `simulated` trên toàn bộ con số tính từ cột `_simulated`.
- **Nhiệm vụ C:** **Người gắn nhãn 1** — gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (không trao đổi), cùng Bách so nhãn, tính tỉ lệ đồng thuận (≥ 80%), viết quy tắc phân biệt các ca lệch và hoàn thiện 3 ca trong bảng khắc phục của `report/team/bang_loi.md`.
- **Nhiệm vụ D *(cập nhật chi tiết sau khi đề công bố)*:** Phụ trách phần lập luận thiết kế và kiểm tra đủ cấu trúc điều kiện/luật dừng cho `report/team/pilot_plan.yaml`.
- **Nhiệm vụ E & Duyệt chéo Gate 2a:** Lập danh sách ≥ 6 event có `trace_id` và kiểm tra chéo ánh xạ chỉ số–event trong `report/team/chi_so.md`; tham gia chấm nhóm bạn trong `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

Ở phần A và B, mình chạy kiểm tra `src/lab13.py` và rà lại toàn bộ `report/team/bang_chi_phi.md`. Ba phép thử A1 đều đạt (`1,20`, `1,25`, `1,25`), các bảng từ A2 đến A4 và B1 đến B4 đủ dòng, mọi con số lấy từ cột `_simulated` đều có nhãn `simulated`, câu trả lời không vượt quá 3 dòng và đều kèm số. File cũng không chứa từ cấm theo quy tắc 5 trong `README.md` và không ghi "cả đội".

Sang phần C trong `report/team/bang_loi.md`, mình đóng vai người gắn nhãn 1 và gắn độc lập toàn bộ 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` theo 5 loại của Google PAIR, bám theo nguyên nhân gốc. Cột của người gắn nhãn 2 (Vũ Xuân Bách) được để trống để hai bạn so nhãn sau. Trong bảng khắc phục 5 ca, mình phụ trách điền 3 ca: Ca 9 (Do người dùng), Ca 7 (Hệ thống) và Ca 17 (Ngầm). Mỗi ca đều có event phát hiện, ngưỡng, tần suất cụ thể và gắn cho đúng một vai trò (`PM trợ lý hoàn phí`, `Kỹ sư trưởng agent`, `Kế toán trưởng`).

Ở phần D (`report/team/pilot_plan.yaml`), mình viết phần lập luận cho 5 câu kiểm tra "tách được tác động" (D2) với cách chia theo nhân viên (`20 + 20`, phân tầng theo 12 depot) và nêu rõ đánh đổi khi nâng MDE lên `+6 điểm` (nếu tác động thật chỉ là `+5 điểm` thì power giảm còn khoảng `0,64`). Trước khi đặt ngưỡng an toàn, mình chạy script kiểm tra trực tiếp `src/logix_requests.csv`: tỉ lệ `mo_lai_trong_7_ngay` là `4,25%` trên toàn mẫu (`51/1.200`) và `3,97%` trong phạm vi `noi_dia` + `hang_nang` (`39/982`), nhờ đó tránh đặt ngưỡng cứng gây dừng sớm ngay tuần đầu. Mình điền tiếp các trường `owner`, `scope`, `assignment`, `identifiability`, 3 `stop_rules` (an toàn, chi phí, mức độ sử dụng) đủ 4 vế `NẾU`, `TRONG`, `THÌ`, `KHÔNG THÌ`, cùng `interim_looks`, `rollback`, `decision_date` và `simulated_inputs`. Ba trường cỡ mẫu D1 được để lại cho Phương xác nhận sau khi chạy `TODO CP4` trong `src/lab13.py`.

Ở phần E (`report/team/chi_so.md`), mình lập danh sách 11 event đều có `trace_id` (`refund_request_created`, `agent_run_completed`, `agent_suggestion_shown`, `staff_review_decision`, `staff_rework_completed`, `refund_ledger_write`, `handoff_to_staff`, `input_validation_failed`, `ticket_closed`, `ticket_reopened`, `audit_sample_checked`). Sau đó mình viết mục kiểm tra chéo để chỉ rõ từng chỉ số ở bảng E1 (chính, dùng, an toàn, hai chỉ số tự đề xuất) và phần giờ nhân viên thật thay thế `_simulated` sẽ lấy từ event nào.

Phần duyệt chéo Gate 2a (`report/team/phieu_cham.md`) sẽ điền trực tiếp lúc 17:00 khi nhóm nhận hồ sơ của nhóm bạn.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- `report/team/bang_loi.md`: cột `Nhãn người 1 (Mạnh)` đủ 20/20 ca lỗi theo Google PAIR và 3 dòng bảng khắc phục (Ca 9, Ca 7, Ca 17).
- `report/team/pilot_plan.yaml`: chú thích D2, phần đánh đổi MDE 6 điểm, tỉ lệ mở lại `4,25%` (`51/1.200`) và `3,97%` (`39/982`), cùng các mục `owner`, `scope`, `assignment`, `identifiability`, 3 `stop_rules`, `interim_looks`, `rollback`, `decision_date`, `simulated_inputs`.
- `report/team/chi_so.md`: bảng 11 event có `trace_id` và phần kiểm tra chéo giữa chỉ số và event.
- `TEAM.md`: mục đóng góp và bằng chứng của thành viên 3 (`NguyenDuyManh-2A202603806`).

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

Mình dùng trợ lý AI (Antigravity / Gemini) để rà yêu cầu đề bài, soát các điều kiện QA (nhãn `simulated`, giới hạn tối đa 3 dòng mỗi câu, từ cấm theo quy tắc 5 trong `README.md`, đủ 4 vế luật dừng), đối chiếu 5 loại lỗi Google PAIR và lên danh sách 11 event có `trace_id`.

Mình tự kiểm tra lại bằng cách chạy `src/lab13.py` và viết script đọc thẳng `src/logix_requests.csv` để xác nhận 3 phép thử A1 đạt và tỉ lệ `mo_lai_trong_7_ngay` (`51/1.200 = 4,25%`, `39/982 = 3,97%`). Ngoài ra mình kiểm tra file YAML bằng `yaml.safe_load`, đọc từng mô tả ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` để soát nguyên nhân gốc, và tìm trên toàn bộ thư mục `report/team/` để chắc chắn không dính từ cấm hay ghi `cả đội`.

## 6. Tự đánh giá

Làm tốt: bám đúng vai trò QA và người gắn nhãn 1; giữ đúng nguyên tắc độc lập khi không điền thay phần của Bách hay bịa kết quả duyệt chéo; luật dừng bám vào tỉ lệ mở lại thực tế (`4,25%` và `3,97%`) và đủ 4 vế; 11 event đo được cả chỉ số E1 lẫn giờ nhân viên thật thay cho cột `simulated`.

Cần làm tiếp với nhóm: so cột `Nhãn người 1` với `Nhãn người 2` của Vũ Xuân Bách để tính tỉ lệ đồng thuận và chốt 2 ca khắc phục còn lại; phối hợp Đỗ Triệu Đức Phương điền nốt 3 trường cỡ mẫu D1 (`n_per_arm`, `design_effect`, `clusters_per_arm`) vào `report/team/pilot_plan.yaml` sau khi chạy `TODO CP4` trong `src/lab13.py`.
