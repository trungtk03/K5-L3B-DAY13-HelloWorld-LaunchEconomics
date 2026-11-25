# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py` và đã kiểm số đối chiếu trực tiếp từ `src/logix_runs.csv` (1.624 lần chạy) và `src/logix_requests.csv` (1.200 yêu cầu). Mọi con số tính từ cột `_simulated` đều ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm | Trạng thái |
| --- | ---: | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 | ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 | ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 | ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token (5.771.712 vào; 734.774 ra) | 245.585 | `logix_runs.csv` (mọi lần chạy) | đo từ trace |
| Tool (5.600 lần gọi) | 84.000 | `logix_runs.csv` (mọi lần chạy) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | `attempt > 1` | đo từ trace |
| Xem lại (890 phút) | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại (1.132 phút) | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | tổng 4 khoản trên | có phần simulated |
| Số việc thành công | 978 / 1.200 | `ket_qua == 'thanh_cong'` | đo từ trace |
| Chi phí mỗi việc thành công (CPS) | 4.472 | `4.373.585 ÷ 978` | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | `(245.585 + 84.000) ÷ 1.200` | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? CPS (`4.472 đ`, `simulated`) gấp **16,3 lần** hoá đơn token + tool mỗi yêu cầu (`274,7 đ`, đo từ trace). Khi cộng thêm 222 ca không thành công chuyển nhân viên (`12.000 đ`/ca), chi phí cả hệ thống là **5.865 đ/yêu cầu = 0,49×** baseline `12.000 đ` (`simulated`).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại** chiếm tỉ trọng lớn nhất với **51,8%** (`2.264.000 đ`, `simulated`), kế đến là **xem lại** **40,7%** (`1.780.000 đ`, `simulated`); tổng giờ nhân viên chiếm **92,5%** tổng chi phí (`simulated`).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: | ---: |
| `noi_dia` | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| `hang_nang` | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| `quoc_te` | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| `doi_tac` | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`** không đáng để trợ lý xử lý vì CPS lên tới **22.515 đ = 1,88×** nhân viên tự làm (`simulated`) và chỉ thành công **27,3%**. Chạy lại tới 3 lần không giúp vì tỉ lệ `status == ok` giảm mạnh qua từng lần thử (**30,0% → 11,4% → 2,2%**); **`doi_tac`** (`10.215 đ = 0,85×`, `simulated`) cũng sát ngưỡng và có điều khoản riêng nên loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi `noi_dia` + `hang_nang`)

Trong mẫu: **900 / 1.200** việc thành công trong phạm vi `noi_dia` + `hang_nang`; CPS biến đổi = **3.414 đ** (`3.072.513 đ ÷ 900`, `simulated`). Chi phí cố định trợ lý = `40.000.000 đ/tháng`.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi kết luận ở quy mô đầy đủ (**4.599 đ = 0,38×**, `simulated`) hay một nửa khối lượng (**5.784 đ = 0,48×**, `simulated`), vì vẫn rẻ hơn mức `12.000 đ`. Tuy nhiên chi phí cố định tăng gấp đôi khi khối lượng giảm nửa (`1.185 đ → 2.370 đ/việc`), nên giai đoạn pilot khối lượng thấp cần ghi rõ đã cộng cố định hay chưa.

## B1 · Đổi từng yếu tố

Gốc (A2): **4.472 đ** (`simulated`). Kiểm tra đối xứng: mỗi kịch bản giảm một nửa giảm đúng bằng ½ mức tăng của kịch bản gấp đôi (`+5,6% / −2,8%`; `+40,7% / −20,3%`; `+51,8% / −25,9%` — ĐẠT).

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (`simulated`) | Thay đổi (%) (`simulated`) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có `attempt > 2`; yêu cầu có `so_lan_chay > 2` coi là `chuyen_nhan_vien` | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%, `simulated`)**, khớp đúng tổng hai tác động riêng (`+5,6% + 40,7% = +46,3%`) do mô hình chi phí là hàm cộng tuyến tính theo từng khoản.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. Số ca làm lại (+51,8%, `simulated`) · 2. Tỉ lệ xem lại (+40,7%, `simulated`) · 3. Lương nhân viên (+23,1%, `simulated`)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = Tổng chi phí trợ lý + `12.000 đ` × số yêu cầu không thành công (nhân viên làm thay).

| Giới hạn | Tổng chi phí trợ lý (`simulated`) | Số yêu cầu không thành công | Chi phí cả hệ thống (`simulated`) | Chi phí mỗi việc thành công (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **Giới hạn 2 lần** rẻ nhất cho cả công ty (**6.901.220 đ**, `simulated`), **không trùng** giới hạn cho CPS thấp nhất (**1 lần**, `4.111 đ`, `simulated`). Cắt xuống 1 lần đẩy thêm **85 yêu cầu** (`319 − 234`) sang nhân viên làm thay với giá `12.000 đ`/ca, khiến tổng chi phí cả hệ thống tăng thêm **548.561 đ** (`7.449.781 đ`, `simulated`).

## B4 · Nếu phải xem lại tất cả

Phạm vi `noi_dia` + `hang_nang`: **982** yêu cầu · **948** yêu cầu có ≥ 1 lần `status == ok` (× 5 phút × 2.000 đ = `9.480.000 đ`, `simulated`) · **48** ca `lam_lai` · **900** việc `thanh_cong` · token + tool = `224.513 đ` (đo từ trace).

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với giả định đề `9 phút/ca` làm lại, tổng `10.568.513 đ` → CPS = **11.743 đ = 0,98×** (`simulated`, hoà vốn xem lại ≤ **5,1 phút**). Dùng trung bình dữ liệu `15,3 phút/ca` làm lại, tổng `11.173.054 đ` → CPS = **12.415 đ = 1,03×** (`simulated`, hoà vốn xem lại ≤ **4,8 phút**).
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% gần như không tiết kiệm (thậm chí đắt hơn nhân viên tự làm) vì tiền xem lại (`9.480.000 đ`, `simulated`) chiếm **85–90%** tổng chi phí. Pilot phải đo được tỉ lệ xem lại giảm an toàn xuống mức nào và thời gian mỗi lần xem lại có rút dưới **4,8–5,1 phút** được không.
