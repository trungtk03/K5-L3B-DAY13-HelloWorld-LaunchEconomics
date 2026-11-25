# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): 07 (HelloWorld · L3B)
- Nhóm được chấm: 08 (25112026 · L3B — `https://github.com/huydn8816/K5-L3B-DAY13-25112026-LaunchEconomics`)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất **Go có điều kiện** khớp số liệu: chi phí cả hệ thống `5.865 đ/YC = 0,49×` (đã cộng `222` ca không thành công, `simulated`), phạm vi `noi_dia + hang_nang` gồm định phí `4.599 đ = 0,38×` (`simulated`). Nêu thẳng 3 điểm bất lợi (xem lại 100% lên `11.743 đ = 0,98×` / `12.415 đ = 1,03×` `simulated`; power còn `0,64` ở mức `+5 điểm`; mở lại nền `4,25%`) kèm 5 điều kiện có người phụ trách và ngày kiểm tra (`2026-12-04` → `2026-12-22`). Trả lời câu hỏi phản biện tại buổi đúng (`8.607 đ`, `+92,5%`). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi mục phụ thuộc cột `_simulated` trong `ho_so_launch_v0.md` (Mục 1, 2, 3, 7) đều ghi trạng thái `Giả lập` và gắn nhãn `[simulated]`; `pilot_plan.yaml` liệt kê đủ 4 khoản ở `simulated_inputs`. Phạm vi thu hẹp về `noi_dia` (`0,22×`) + `hang_nang` (`0,69×`), loại `quoc_te` (`1,88×`, thành công `27,3%`, ok tụt `30,0% → 11,4% → 2,2%`) và `doi_tac` (`0,85×`, điều khoản riêng). Không dùng từ cấm, không khẳng định "đã nâng chỉ số" khi chưa có đối chứng. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên theo nhân viên `20 + 20` (đủ 20 cụm/nhóm), đối chứng đồng thời tại 12 depot, phân tầng theo depot, giảm spillover bằng quyền `staff_id` + log, chốt trước `decision_date: 2027-01-05` và `interim_looks` chỉ kiểm tra an toàn. Tính đủ 5 câu D1 (`n_per_arm = 859`, `DE = 6,96`, `m ≥ 299`, MDE `0,06`, nêu rõ power `0,64` ở mức 5 điểm). Đủ 3 luật dừng đúng 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` có ngưỡng phù hợp nền `4,25%`, thời hạn (`3 ngày`, `2 tuần`, `1 tuần`), người dừng (`Giám đốc vận hành`, `PM`, `Trưởng nhóm CSKH`) và rollback `30 phút`. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** **Go có điều kiện**

**Lý do:** Hồ sơ `ho_so_launch_v0.md` và `pilot_plan.yaml` của Nhóm 08 đầy đủ 7 mục, số liệu chính xác, gắn nhãn `simulated` rõ ràng, không bỏ qua các con số bất lợi (`0,98–1,03×` khi xem lại 100%, power `0,64` ở mức 5 điểm, mở lại nền `4,25%`) và thiết kế pilot tách được tác động với 20 cụm/nhóm cùng 3 luật dừng có người chịu trách nhiệm cụ thể. Hội đồng duyệt **Go có điều kiện** theo đúng 5 điều kiện Nhóm 08 đã cam kết (lưu ý nhỏ: khi chạy pilot cần bỏ chữ `[simulated]` ở luật dừng chi phí `> 8.000 đ` sau khi đã chuyển sang đo giờ nhân viên thật từ tuần 2, và đảm bảo bước `0,50` chạy đủ ≥ 10 ngày cho phạm vi `81,8%` `noi_dia + hang_nang` để gom đủ `299` đơn/người).

**Một câu hỏi cho đội trình:** Nếu hai yếu tố bất lợi nhất trong bảng độ nhạy xảy ra cùng lúc, chi phí mỗi việc thành công là bao nhiêu?

**Câu trả lời của đội trình (ghi lại tại buổi):** Làm lại gấp đôi và xem lại gấp đôi cùng lúc: 8.607 đ (+92,5%) = 0,72× của 12.000 đ (simulated), bằng tổng hai tác động riêng (+51,8% + 40,7%) vì mô hình cộng tuyến tính. Con số này vượt ngưỡng 8.000 đ, nên luật dừng chi phí sẽ kích hoạt và thu hẹp về noi_dia.
