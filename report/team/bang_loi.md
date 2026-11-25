# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Duy Mạnh (2A202603806) · Người gắn nhãn 2: Vũ Xuân Bách (2A202603803) *(gắn độc lập trong 8 phút, không trao đổi trước khi so nhãn)*

| Ca | Nhãn người 1 (Mạnh) | Nhãn người 2 (Bách) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | ... |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại. *(Cập nhật sau khi Mạnh và Bách so nhãn)*:

- Xếp loại theo nguyên nhân gốc gây ra lỗi, tách khỏi phần việc cần sửa sau đó.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". *(Mạnh điền 3 ca: 9, 7, 17; Bách điền 2 ca còn lại: Ngữ cảnh, Giới hạn hệ thống).*

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (kèm `trace_id`, mã lỗi định dạng mã đơn); cảnh báo khi vượt 2% tổng yêu cầu/ngày | Nhận diện mã đơn sàn TMĐT để tự tra sang mã vận đơn LogiX; nếu không tra được thì hiện hướng dẫn kèm ảnh vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Job đối soát mỗi giờ giữa tin nhắn "đã hoàn tiền" và bản ghi `refund_ledger_write` (`ket_qua == ok`) cùng `trace_id`; ngưỡng 0 ca lệch (báo ngay khi ≥ 1 ca) | Chỉ gửi thông báo "đã hoàn tiền thành công" sau khi sổ cái trả `ok` kèm `idempotency_key`; nếu API 503 sau tối đa 2 lần thử lại thì báo "đang xử lý" và tạo event `handoff_to_staff` | Kỹ sư trưởng agent |
| ... | Ngữ cảnh | *(Vũ Xuân Bách điền)* | *(Vũ Xuân Bách điền)* | ... |
| ... | Giới hạn hệ thống | *(Vũ Xuân Bách điền)* | *(Vũ Xuân Bách điền)* | ... |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu ngẫu nhiên 100 đơn/tuần so với bảng giá hiện hành; cảnh báo khi hơn 1% số đơn lệch tiền | Xoá bộ nhớ đệm ngay khi có bảng giá mới và lưu `pricing_version` vào mọi `trace_id` để đối chiếu | Kế toán trưởng |
