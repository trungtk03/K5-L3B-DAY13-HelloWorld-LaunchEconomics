# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: HelloWorld (Nhóm 07)
- Lớp: K5-L3B
- Repo nhóm: `https://github.com/trungtk03/K5-L3B-DAY13-HelloWorld-LaunchEconomics` (nhánh `main`)
- Thành viên: xem `TEAM.md` (Nguyễn Hoàng Trung, Đỗ Triệu Đức Phương, Nguyễn Duy Mạnh, Vũ Xuân Bách)

## 2. Mục tiêu và cách tiếp cận

- Xây dựng bộ **hồ sơ launch v0** cho trợ lý hoàn phí LogiX-VN (12 depot, 40 nhân viên CSKH, ~1.500 yêu cầu/ngày) trên mẫu dữ liệu giả lập `1.200` yêu cầu (`1.624` lần chạy) để bảo vệ trước hội đồng **Gate 2a** (chỉ duyệt kế hoạch pilot).
- Nhóm tổ chức làm việc theo 4 vai chuẩn của lab và **đổi người viết code sau giờ giải lao**: Chặng 1 (A–B) Trung viết `src/lab13.py`, Phương kiểm số và lập `bang_chi_phi.md`; Chặng 2 (D–E) Phương tiếp quản code D1/E1/YAML, Trung kiểm số và viết E2; Mạnh (gắn nhãn 1 + QA) và Bách (gắn nhãn 2 + giữ hồ sơ) thực hiện gắn nhãn độc lập 20 ca lỗi và cập nhật dần hồ sơ.

## 3. Giải pháp

- **Nhiệm vụ A & B — Mô hình chi phí & độ nhạy** ([`src/lab13.py`](../../src/lab13.py), [`report/team/bang_chi_phi.md`](bang_chi_phi.md)): hoàn thiện 3 hàm A1 đạt 3/3 phép thử (`1,20 · 1,25 · 1,25`), viết hàm `mo_hinh` cộng mọi lần chạy kể cả lần lỗi ở tử số và chỉ chia số việc `thanh_cong` ở mẫu số, tách 4 loại yêu cầu (A3), cộng định phí `40 triệu đ/tháng` (A4), chạy 9 kịch bản độ nhạy (B1–B2), chi phí cả hệ thống theo giới hạn 1–2–3 lần chạy (B3) và kịch bản xem lại 100% (B4).
- **Nhiệm vụ C — Phân loại lỗi & khắc phục** ([`report/team/bang_loi.md`](bang_loi.md)): hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR trong 8 phút (không trao đổi), đối chiếu đạt đồng thuận `19/20 = 95%`, thống nhất quy tắc cho ca lệch (Ca 8) và xây dựng bảng khắc phục 5 ca (đủ 5 loại) có event/ngưỡng đo được và 1 vai trò phụ trách.
- **Nhiệm vụ D — Kế hoạch pilot** ([`report/team/pilot_plan.yaml`](pilot_plan.yaml)): tính đủ 5 câu cỡ mẫu D1 và kiểm chứng power bằng `statsmodels`, trả lời 5 câu tách tác động D2, tính tỉ lệ mở lại nền trước khi đặt 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` và kiểm tra hợp lệ bằng `yaml.safe_load`.
- **Nhiệm vụ E & Duyệt chéo Gate 2a** ([`report/team/chi_so.md`](chi_so.md), [`report/team/ho_so_launch_v0.md`](ho_so_launch_v0.md), [`report/team/phieu_cham.md`](phieu_cham.md)): tính thử 3 chỉ số E1, đề xuất 2 chỉ số dùng/an toàn, lập 13 event có `trace_id` kèm kiểm tra chéo, viết 4 dòng rủi ro kinh tế E2, tổng hợp 1 trang hồ sơ launch v0 và chấm chéo Nhóm 08 (`25112026`).

## 4. Kết quả

- **Chi phí (`simulated`):** CPS toàn mẫu là **`4.472 đ`** (`4.373.585 đ ÷ 978` việc thành công), gấp **16,3×** hoá đơn token + tool (`274,7 đ/YC`); giờ nhân viên chiếm **92,5%** (làm lại `51,8%`, xem lại `40,7%`). Khi cộng `222` ca không thành công × `12.000 đ`, chi phí cả hệ thống là **`5.865 đ/YC = 0,49×`** baseline `12.000 đ`. Trong phạm vi `noi_dia + hang_nang`, CPS biến đổi **`3.414 đ`**, cộng định phí `40 triệu/tháng` ở `45.000 YC/tháng` là **`4.599 đ = 0,38×`** (`5.784 đ = 0,48×` ở nửa khối lượng).
- **Độ nhạy & giới hạn (`simulated`):** Top 3 yếu tố nhạy nhất là **số ca làm lại (`+51,8%`)**, **tỉ lệ xem lại (`+40,7%`)**, **lương nhân viên (`+23,1%`)**; giá token gấp đôi chỉ `+5,6%`. Giới hạn **2 lần chạy** rẻ nhất cho cả hệ thống (**`6.901.220 đ`**). Nếu phải xem lại 100%, CPS lên **`11.743 đ = 0,98×`** (`9 phút` làm lại) hoặc **`12.415 đ = 1,03×`** (`15,3 phút` theo dữ liệu).
- **Chỉ số đợt chạy thử (chưa có đối chứng):** đóng 24h không mở lại **`82,83%`** (`994/1.200`), bỏ qua gợi ý **`27,12%`** (`48/177`), mở lại 7 ngày **`4,25%`** (`51/1.200`; phạm vi pilot `3,97%`).
- **Pilot & Đề xuất cuối (`ho_so_launch_v0.md`):** chia ngẫu nhiên theo nhân viên **`20 + 20`** phân tầng 12 depot, chấp nhận **MDE `+6 điểm`** (`n_per_arm = 859`, `DE = 6,96`, `m ≥ 299` YC/người; power còn **`0,64`** nếu tác động thật `+5 điểm`). Đề xuất: **Go có điều kiện** cho pilot phạm vi `noi_dia + hang_nang` (loại `quoc_te` `1,88×` và `doi_tac` `0,85×`), khoá `max_attempts = 2` kèm 3 điều kiện có vai trò phụ trách và ngày kiểm tra.
- **Kết quả duyệt chéo Gate 2a:** Nhóm 07 đã chấm Nhóm 08 (`25112026`) đạt **`30/30`** với quyết định **Go có điều kiện** trong `report/team/phieu_cham.md`. Phía phản biện cho Nhóm 07 chỉ ra 2 điểm quan trọng về thời gian gom mẫu thực tế cho phạm vi `81,8%` (`≥ 10 ngày` thay vì `8 ngày` ở bước `0,50`) và mốc kiểm tra Điều kiện 2 (đổi từ `Ngày 7` sang cuối bước `0,25` kết hợp xem lại phân tầng theo rủi ro); nhóm đã tiếp thu và cập nhật đồng bộ vào `ho_so_launch_v0.md` và `pilot_plan.yaml`.

## 5. Khó khăn và cách xử lý

- **Môi trường Python trên máy Windows:** máy chưa cài sẵn thư viện khoa học dữ liệu và bước giải nén `scipy`/`statsmodels` vào `src/.venv` mất nhiều thời gian → tạo môi trường ảo riêng `src/.venv` (được `.gitignore` bỏ qua), cài đủ `src/requirements.txt` và chạy kiểm chứng chéo trên nhiều máy.
- **Không đủ cỡ mẫu cụm cho MDE +5 điểm:** với 40 nhân viên (`20/nhánh`) và `ICC = 0,02`, trần cỡ mẫu hiệu dụng chỉ là `c/ICC = 1.000 < 1.251` → nhóm chọn chia theo nhân viên để giữ 20 cụm và kiểm soát spillover, chấp nhận MDE `+6 điểm` (`m ≥ 299`), đồng thời ghi rõ rủi ro power còn `0,64` ở mức `+5 điểm`.
- **Mâu thuẫn giữa xem lại để giữ an toàn và chi phí B4:** xem lại 100% đẩy CPS lên `0,98–1,03×` (`simulated`), nhưng `hang_nang` không xem lại có tỉ lệ mở lại tới `10,57%` (`0%` khi xem lại) → áp dụng **xem lại phân tầng** (giữ 100% cho `hang_nang`, hạ theo bậc cho `noi_dia` chỉ khi đạt điều kiện an toàn, kéo tổng xem lại về ~`37%`).

## 6. Tổng hợp đóng góp

Chi tiết đóng góp và bằng chứng commit của từng thành viên nằm trong `TEAM.md` và 4 báo cáo cá nhân trong `report/team/`:
- **Nguyễn Hoàng Trung (`2A202603826`):** Nhóm trưởng, lập repo fork, viết code A–B (`src/lab13.py`), kiểm số/soát kỹ thuật chặng 2 (D–E), viết bảng rủi ro E2 (`chi_so.md`), đại diện bảo vệ Gate 2a và chốt `phieu_cham.md`, `group_report.md`.
- **Đỗ Triệu Đức Phương (`2A202603843`):** Kiểm số chặng 1 và hoàn thiện `bang_chi_phi.md` (A1–A4, B1–B4); đổi vai viết code chặng 2 (`co_mau`, D1, E1, kiểm tra YAML) trong `src/lab13.py`, hoàn thiện D1 trong `pilot_plan.yaml` và bảng chỉ số E1 trong `chi_so.md`.
- **Nguyễn Duy Mạnh (`2A202603806`):** QA xuyên suốt A–E, người gắn nhãn 1 (20 ca lỗi + 3 ca khắc phục Ca 9, 7, 17 trong `bang_loi.md`), viết D2/đánh đổi/3 luật dừng trong `pilot_plan.yaml` và danh sách 13 event có `trace_id` trong `chi_so.md`.
- **Vũ Xuân Bách (`2A202603803`):** Người gắn nhãn 2 (20 ca lỗi + 2 ca khắc phục Ca 3, 4 trong `bang_loi.md`, đồng thuận `19/20 = 95%`), giữ và hoàn thiện `ho_so_launch_v0.md` xuyên suốt CP1–CP5.

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu giờ nhân viên đang là `simulated`:** `92,5%` chi phí hiện phụ thuộc hai cột `phut_xem_lai_simulated` và `phut_lam_lai_simulated`; cần thay toàn bộ bằng `phut_xem_lai_thuc` và `phut_lam_lai_thuc` đo từ `staff_review_decision` và `staff_rework_completed` sau tuần đầu của pilot để tính lại CPS thật.
- **Đánh đổi power và thời gian gom mẫu:** MDE `+6 điểm` làm power giảm còn `0,64` nếu tác động thật là `+5 điểm`, và với `81,8%` lưu lượng thuộc `noi_dia + hang_nang`, bước `0,50` cần chạy tối thiểu `10 ngày` + `7 ngày` cửa sổ mở lại; có thể cải thiện độ chính xác ở pilot tiếp theo bằng phương pháp giảm phương sai (CUPED theo năng suất lịch sử từng nhân viên).
- **Đồng bộ hoá cảnh báo tự động cho lỗi ngầm:** tiếp tục triển khai kiểm toán mẫu 100 đơn/tuần (`audit_sample_checked`) gắn `pricing_version` vào `trace_id` để bắt các ca lệch tiền mà khách không mở lại ticket.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`statsmodels.stats.power`) và `proportion_effectsize` (`statsmodels.stats.proportion`)
- Tài liệu Lab 13 AI20K K5 (`docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`)
