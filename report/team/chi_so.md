# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (`994/1.200`) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Chỉ số trong đợt chạy thử là **27,12%** (`48/177`) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (`51/1.200`; trong phạm vi `noi_dia` + `hang_nang`: `3,97%`, `39/982`) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được mở bằng trợ lý | Số `request_id` có event `agent_suggestion_shown` chia tổng `refund_request_created` thuộc `arm == treatment` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần và số ca hoàn trùng | Số đơn có `lech_tien != 0` chia tổng mẫu 100 đơn/tuần từ `audit_sample_checked`, kết hợp đếm ca trùng theo `idempotency_key` và `request_id` từ `refund_ledger_write` | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent. *(Nguyễn Duy Mạnh lập 11 event cho các chỉ số ở bảng E1, đo giờ nhân viên thật thay cột `_simulated` và theo dõi lỗi ở Nhiệm vụ C).*

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `depot`, `loai`, `so_tien_vnd`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `pricing_version`, `trace_id` | Sau mỗi lần chạy của agent (kể cả lần `loi`) |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiện trên màn hình nhân viên |
| `staff_review_decision` | Giao diện nhân viên | `request_id`, `staff_id`, `quyet_dinh_xem_lai` (`giu`/`sua`/`bo`), `phut_xem_lai_thuc`, `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Hệ thống CSKH | `request_id`, `staff_id`, `phut_lam_lai_thuc`, `ly_do`, `trace_id` | Khi nhân viên làm lại xong ca sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien_vnd`, `ket_qua` (`ok`/`loi`), `trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi trợ lý chuyển yêu cầu sang nhân viên |
| `input_validation_failed` | App khách / Agent | `request_id`, `field`, `error_code`, `trace_id` | Khi đầu vào khách nhập sai định dạng (mã vận đơn, STK) |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `dong_trong_24h`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | App khách / CSKH | `request_id`, `reopened_at`, `reason`, `mo_lai_trong_7_ngay`, `trace_id` | Khi khách mở lại yêu cầu sau khi đã đóng |
| `audit_sample_checked` | Hệ thống kiểm toán / Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `lech_tien`, `trace_id` | Khi kế toán kiểm tra mẫu 100 đơn/tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính (`% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày`): tính được khi nối qua `trace_id` từ `refund_request_created` (tổng yêu cầu theo `arm`), `ticket_closed` (`dong_trong_24h == 1`) và không có `ticket_reopened` với `mo_lai_trong_7_ngay == 1`.
- Chỉ số dùng (`Tỉ lệ bỏ qua gợi ý`): lấy từ `staff_review_decision`, chia số bản ghi có `quyet_dinh_xem_lai` là `sua` hoặc `bo` cho tổng số bản ghi `staff_review_decision`.
- Chỉ số an toàn (`Tỉ lệ lỗi lọt đến khách`): chia số bản ghi `ticket_reopened` (`mo_lai_trong_7_ngay == 1`) cho tổng yêu cầu từ `refund_request_created`, nối qua `trace_id`.
- Chỉ số dùng tự đề xuất (ví dụ `% yêu cầu nhóm can thiệp mở bằng trợ lý`): lấy số `request_id` có `agent_suggestion_shown` chia cho tổng `refund_request_created` thuộc `arm == treatment`.
- Chỉ số an toàn tự đề xuất (ví dụ `% đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần` và `số ca hoàn trùng`): tính từ `audit_sample_checked` (`lech_tien != 0` trên tổng mẫu kiểm tra) kết hợp đối soát `refund_ledger_write` theo `idempotency_key` và `request_id`.
- Chi phí thật thay số `simulated` sau tuần 1: cộng `tokens_in`, `tokens_out`, `tool_calls` từ `agent_run_completed`, ghép với `phut_xem_lai_thuc` (`staff_review_decision`) và `phut_lam_lai_thuc` (`staff_rework_completed`) theo `trace_id`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`). Mọi con số tính từ cột `_simulated` đều ghi nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy #1) | CPS tăng **+51,8%**, từ `4.472 đ` lên **6.787 đ/việc** (`simulated`, B1); làm lại hiện chiếm **51,8%** tổng chi phí A2 (`simulated`) | Tỉ lệ làm lại hằng tuần (`staff_rework_completed` ÷ `refund_request_created`) > **7%** (đợt chạy thử trong phạm vi `noi_dia` + `hang_nang`: **4,9%**, `48/982`) hoặc `phut_lam_lai_thuc` trung bình > **15 phút/ca** | Thu hẹp pilot về chỉ `noi_dia`, rà 20 `trace_id` làm lại gần nhất để sửa lỗi gốc và giữ trần 2 lần chạy | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài hoặc tỉ lệ xem lại tăng gấp đôi (yếu tố nhạy #2) | Xem lại gấp đôi làm CPS tăng **+40,7%** lên **6.292 đ** (`simulated`, B1). Xem lại 100% ở `noi_dia` + `hang_nang` đẩy CPS lên **11.743 đ = 0,98×** (9 phút làm lại) hoặc **12.415 đ = 1,03×** (`15,3 phút` theo dữ liệu), vượt baseline `12.000 đ` nếu xem lại > **4,8–5,1 phút** (`simulated`, B4) | % yêu cầu phát sinh `staff_review_decision` vẫn > **50%** vào cuối bước rollout `0,25`, hoặc trung bình `phut_xem_lai_thuc` > **4,8 phút/lần** | Áp dụng lộ trình giảm tỉ lệ xem lại theo bậc khi tỉ lệ `sua + bo` < **15%** trong 1 tuần; tối ưu giao diện tóm tắt để kéo `phut_xem_lai_thuc` xuống dưới 4 phút | Trưởng nhóm CSKH |
| Khối lượng giao dịch phạm vi pilot thấp hơn dự kiến (rủi ro chi phí cố định) | Định phí `40 triệu đ/tháng` cộng thêm **+1.185 đ/việc** ở `45.000 YC/tháng` (tổng **4.599 đ = 0,38×**, `simulated`, A4) nhưng tăng gấp đôi lên **+2.370 đ/việc** nếu khối lượng giảm một nửa (tổng **5.784 đ = 0,48×**, `simulated`, A4) | Số việc thành công hằng tuần (nối `refund_request_created` + `ticket_closed` không `ticket_reopened`) đạt dưới **50%** kế hoạch của phạm vi `noi_dia` + `hang_nang` | Tạm dừng mở rộng pilot, rà soát hợp đồng hạ tầng để giảm định phí `40 triệu đ/tháng` hoặc chuyển sang gói tính theo lưu lượng | Kế toán trưởng |
| Không giới hạn chạy tối ưu hoặc để lọt loại `quoc_te` vào pilot | Cắt còn 1 lần chạy tuy cho CPS thấp nhất (`4.111 đ`) nhưng đẩy thêm **85 ca** sang nhân viên, làm tổng chi phí cả hệ thống tăng **+548.561 đ** (`7.449.781 đ` so với mức rẻ nhất **6.901.220 đ** ở giới hạn 2 lần, `simulated`, B3); để lọt `quoc_te` đẩy CPS lên **22.515 đ = 1,88×** (`simulated`, A3) | Phát sinh bản ghi `agent_run_completed` có `attempt > 2` hoặc có `loai` là `quoc_te`/`doi_tac` trong báo cáo đối soát hằng ngày | Khoá cứng cấu hình `max_attempts = 2` và bộ lọc định tuyến chỉ nhận `noi_dia` + `hang_nang`; chuyển thẳng `quoc_te`, `doi_tac` sang `handoff_to_staff` | Kỹ sư trưởng agent |
