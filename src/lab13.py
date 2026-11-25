"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from pathlib import Path
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26             # đồng cho 1.000 token đầu vào
GIA_RA = 130             # đồng cho 1.000 token đầu ra
GIA_TOOL = 15            # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000        # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000         # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng / tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    r1 = so_lan_chay_ky_vong(0.8, 2)
    r2 = so_lan_chay_ky_vong(0.8)
    r3 = he_so_chi_phi_moi_viec_thanh_cong(0.8, 3)
    assert abs(r1 - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(r2 - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(r3 - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')
    print(f'  - Tối đa 2 lần (p=0,8):           {r1:.2f}')
    print(f'  - Chạy đến khi đúng (p=0,8):      {r2:.2f}')
    print(f'  - Hệ số chi phí, tối đa 3 lần:    {r3:.2f}')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def in_nhiem_vu_a(runs, reqs):
    print('\n=== A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    kq = mo_hinh(runs, reqs)
    tong_tool = int(runs['tool_calls'].sum())
    phut_xem = reqs['phut_xem_lai_simulated'].sum()
    phut_lam = reqs['phut_lam_lai_simulated'].sum()
    print(f"Token (mọi lần chạy):                 {kq['token']:>12,.0f} đ  [đo từ trace]")
    print(f"Tool ({tong_tool:,} lần gọi):                 {kq['tool']:>12,.0f} đ  [đo từ trace]")
    print(f"  Trong đó, lần chạy thứ 2 và 3:      {kq['chay_lai']:>12,.0f} đ  [đo từ trace]")
    print(f"Xem lại ({phut_xem:,.0f} phút):                  {kq['xem_lai']:>12,.0f} đ  [simulated]")
    print(f"Làm lại ({phut_lam:,.0f} phút):                {kq['lam_lai']:>12,.0f} đ  [simulated]")
    print(f"Tổng chi phí:                         {kq['tong']:>12,.0f} đ  [có phần simulated]")
    print(f"Số việc thành công:                   {kq['thanh_cong']:>12,d} / {len(reqs):,d}")
    print(f"Chi phí mỗi việc thành công (CPS):    {kq['cps']:>12,.0f} đ  [simulated]")
    print(f"Hoá đơn token + tool / yêu cầu:       {kq['hoa_don_moi_yc']:>12,.1f} đ  [đo từ trace]")
    print(f"Tỉ lệ CPS / hoá đơn mỗi yêu cầu:      {kq['cps'] / kq['hoa_don_moi_yc']:>12.1f}×  [simulated]")
    print(f"Tỉ trọng làm lại:                     {kq['lam_lai'] / kq['tong'] * 100:>11.1f}%  [simulated]")
    print(f"Tỉ trọng xem lại:                     {kq['xem_lai'] / kq['tong'] * 100:>11.1f}%  [simulated]")
    print(f"Tổng tỉ trọng giờ nhân viên:          {(kq['xem_lai'] + kq['lam_lai']) / kq['tong'] * 100:>11.1f}%  [simulated]")

    khong_tc = len(reqs) - kq['thanh_cong']
    he_thong_moi_yc = (kq['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f"Chi phí cả hệ thống / yêu cầu:        {he_thong_moi_yc:>12,.0f} đ ({he_thong_moi_yc / BASELINE:.2f}× baseline)  [simulated]")

    print('\n=== A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    print(f"{'Loại':12s} {'Số YC':>7s} {'Thành công':>11s} {'Lần/YC':>8s} {'CPS [sim]':>12s} {'So 12.000đ':>11s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        tl_tc = r['thanh_cong'] / len(sub) * 100
        lan_yc = sub['so_lan_chay'].mean()
        print(f"{loai:12s} {len(sub):>7d} {tl_tc:>10.1f}% {lan_yc:>8.2f} {r['cps']:>11,.0f}đ {r['cps'] / BASELINE:>10.2f}×")

    print('\nTỉ lệ status == ok theo loại và lần thử (attempt):')
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(int)
    bang_ok = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print(bang_ok.reindex(['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']).round(1).to_string())

    print('\n=== A4 · CHI PHÍ CỐ ĐỊNH (PHẠM VI noi_dia + hang_nang) ===')
    sub_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pilot = mo_hinh(runs, sub_pilot)
    print(f"Trong mẫu: {kq_pilot['thanh_cong']}/{len(reqs)} việc thành công; CPS biến đổi = {kq_pilot['cps']:,.0f} đ [simulated]")
    for nhan, khoi_luong in [('45.000 yêu cầu/tháng', 45_000), ('Một nửa khối lượng (22.500)', 22_500)]:
        viec_thang = khoi_luong * kq_pilot['thanh_cong'] / len(reqs)
        co_dinh_viec = CHI_PHI_CO_DINH / viec_thang
        tong_cps = kq_pilot['cps'] + co_dinh_viec
        print(
            f"  {nhan:28s} | {viec_thang:>8,.0f} việc/tháng | "
            f"cố định {co_dinh_viec:>6,.0f} đ | tổng {tong_cps:>6,.0f} đ ({tong_cps / BASELINE:.2f}×) [simulated]"
        )


def in_nhiem_vu_b(runs, reqs):
    goc = mo_hinh(runs, reqs)['cps']

    print('\n=== B1 · BẢNG ĐỘ NHẠY (ĐỔI TỪNG YẾU TỐ) ===')
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':  dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':  dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên +25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':     dict(max_lan_chay=1),
    }
    print(f"{'Gốc (A2)':28s} {goc:>10,.0f} đ")
    ket_qua_b1 = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1) * 100
        ket_qua_b1[ten] = (cps, pct)
        print(f"{ten:28s} {cps:>10,.0f} đ  ({pct:+6.1f}%)  [simulated]")

    print('\n=== B2 · ĐỔI MỘT CẶP VÀ XẾP HẠNG ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    pct_cap = (cps_cap / goc - 1) * 100
    print(f"Giá token gấp đôi + Xem lại gấp đôi: {cps_cap:,.0f} đ ({pct_cap:+.1f}%) [simulated]")
    tong_rieng = ket_qua_b1['Giá token gấp đôi'][1] + ket_qua_b1['Tỉ lệ xem lại gấp đôi'][1]
    print(f"  Tổng hai tác động riêng:           {tong_rieng:+.1f}% (khớp do mô hình cộng tuyến tính)")
    xep_hang = [
        ('Số ca làm lại', abs(ket_qua_b1['Số ca làm lại gấp đôi'][1])),
        ('Tỉ lệ xem lại', abs(ket_qua_b1['Tỉ lệ xem lại gấp đôi'][1])),
        ('Lương nhân viên', abs(ket_qua_b1['Lương nhân viên +25%'][1])),
        ('Giá token', abs(ket_qua_b1['Giá token gấp đôi'][1])),
    ]
    xep_hang.sort(key=lambda x: x[1], reverse=True)
    print('  Xếp hạng top 3 yếu tố ảnh hưởng mạnh nhất: ' + ' · '.join(
        f'{i + 1}. {ten} ({muc:.1f}%)' for i, (ten, muc) in enumerate(xep_hang[:3])
    ))

    print('\n=== B3 · GIỚI HẠN CHẠY LẠI VÀ CHI PHÍ CẢ HỆ THỐNG ===')
    print(f"{'Giới hạn':10s} {'Tổng trợ lý [sim]':>18s} {'Không TC':>10s} {'Cả hệ thống [sim]':>19s} {'CPS [sim]':>12s}")
    for k in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - r['thanh_cong']
        ca_he_thong = r['tong'] + khong_tc * BASELINE
        print(f"{f'{k} lần':10s} {r['tong']:>17,.0f}đ {khong_tc:>10d} {ca_he_thong:>18,.0f}đ {r['cps']:>11,.0f}đ")

    print('\n=== B4 · NẾU PHẢI XEM LẠI 100% (PHẠM VI noi_dia + hang_nang) ===')
    sub_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pilot = runs[runs['request_id'].isin(sub_pilot['request_id'])]
    yc_co_ok = int(runs_pilot[runs_pilot['status'] == 'ok']['request_id'].nunique())
    so_lam_lai = int((sub_pilot['ket_qua'] == 'lam_lai').sum())
    thanh_cong = int((sub_pilot['ket_qua'] == 'thanh_cong').sum())
    tien_token_tool = (
        runs_pilot['tokens_in'] / 1000 * GIA_VAO
        + runs_pilot['tokens_out'] / 1000 * GIA_RA
        + runs_pilot['tool_calls'] * GIA_TOOL
    ).sum()
    tien_xem_100 = yc_co_ok * 5 * LUONG_PHUT

    phut_ll_tb_all = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(
        f"Phạm vi noi_dia + hang_nang: {len(sub_pilot)} YC | có ≥1 lần ok: {yc_co_ok} | "
        f"lam_lai: {so_lam_lai} | thanh_cong: {thanh_cong} | token+tool: {tien_token_tool:,.0f} đ"
    )
    for nhan, phut_ll in [('Giả định đề (9 phút/ca làm lại)', 9.0), (f'Trung bình dữ liệu ({phut_ll_tb_all:.1f} phút/ca)', phut_ll_tb_all)]:
        tien_ll = so_lam_lai * phut_ll * LUONG_PHUT
        tong = tien_token_tool + tien_xem_100 + tien_ll
        cps = tong / thanh_cong
        hoa_von_phut = (BASELINE * thanh_cong - tien_token_tool - tien_ll) / (yc_co_ok * LUONG_PHUT)
        print(
            f"  {nhan:38s}: tổng {tong:>10,.0f} đ → CPS = {cps:>6,.0f} đ ({cps / BASELINE:.2f}×) [simulated] "
            f"| hoà vốn xem lại ≤ {hoa_von_phut:.1f} phút"
        )


# ---------- Nhiệm vụ D1 · Cỡ mẫu cho ba cách chia (Chặng 2 · Đỗ Triệu Đức Phương) ----------
def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ p1 và p2 (kiểm định hai phía)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil(
        (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        / (p2 - p1) ** 2
    )


def in_nhiem_vu_d(reqs):
    print('\n=== D1 · CỠ MẪU CHO BA CÁCH CHIA (baseline=0,70 · alpha=0,05 · power=0,80 · ICC=0,02) ===')
    p1, alpha, power, icc = 0.70, 0.05, 0.80, 0.02
    n_a = co_mau(p1, 0.75, alpha, power)
    de_75 = 1 + (75 - 1) * icc
    n_b = math.ceil(n_a * de_75)
    nv_moi_nhom = math.ceil(n_b / 75)
    tran_20 = 20 / icc
    n_eff_20_75 = 20 * 75 / de_75
    tran_6 = 6 / icc

    n_6pp = co_mau(p1, 0.76, alpha, power)
    m_e = math.ceil((n_6pp * (1 - icc)) / (20 - n_6pp * icc))
    de_e = 1 + (m_e - 1) * icc
    n_eff_e = 20 * m_e / de_e

    # Đối chiếu bằng statsmodels (power thực tế nếu tác động thật chỉ là +5 điểm với n = 859)
    es_5pp = proportion_effectsize(0.75, 0.70)
    pw_at_5pp = NormalIndPower().power(effect_size=es_5pp, nobs1=n_6pp, alpha=alpha, ratio=1.0)
    don_moi_nguoi_ngay = 1500 / 40
    so_ngay_gom_du = math.ceil(m_e / don_moi_nguoi_ngay)

    print(f"  a) Chia theo yêu cầu (+5 điểm):        {n_a:,d} yêu cầu/nhóm (tràn tác động cao trên cùng nhân viên)")
    print(f"  b) Theo nhân viên, m = 75:             DE = {de_75:.2f}; cần {n_b:,d} YC/nhóm → {nv_moi_nhom} người/nhóm (tổng {nv_moi_nhom * 2} > 40: không đủ)")
    print(f"  c) 20 nhân viên/nhóm (trần c/ICC):     tối đa {tran_20:,.0f} < {n_a:,d} (m=75 chỉ còn {n_eff_20_75:,.0f} mẫu hiệu dụng: không đạt +5 điểm)")
    print(f"  d) 6 depot/nhóm (trần c/ICC):          tối đa {tran_6:,.0f} < {n_a:,d} (và chỉ 6 cụm < 20: loại)")
    print(f"  e) Mức chênh +6 điểm ({n_6pp}/nhóm), 20 NV: m ≥ {m_e} YC/người (DE = {de_e:.2f}, n_hiệu_dụng = {n_eff_e:.1f})")
    print(f"     → Power nếu tác động thật +5 điểm (statsmodels, n={n_6pp}): {pw_at_5pp:.2f} ({pw_at_5pp * 100:.1f}%)")
    print(f"     → Thời gian gom mẫu bước 20+20 người ({don_moi_nguoi_ngay:.1f} đơn/người/ngày): cần ≥ {so_ngay_gom_du} ngày (7 ngày chỉ được ~{7 * don_moi_nguoi_ngay:.0f} < {m_e})")

    mo_lai_all = (reqs['mo_lai_trong_7_ngay'] == 1).mean() * 100
    so_mo_lai_all = int((reqs['mo_lai_trong_7_ngay'] == 1).sum())
    sub_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    mo_lai_pilot = (sub_pilot['mo_lai_trong_7_ngay'] == 1).mean() * 100
    so_mo_lai_pilot = int((sub_pilot['mo_lai_trong_7_ngay'] == 1).sum())
    print(
        f"  Tỉ lệ mo_lai_trong_7_ngay hiện tại:    toàn mẫu {mo_lai_all:.2f}% ({so_mo_lai_all}/{len(reqs)}) "
        f"| phạm vi noi_dia+hang_nang {mo_lai_pilot:.2f}% ({so_mo_lai_pilot}/{len(sub_pilot)})"
    )


# ---------- Nhiệm vụ E1 · Tính thử 3 chỉ số trên 1.200 yêu cầu ----------
def in_nhiem_vu_e1(reqs):
    print('\n=== E1 · TÍNH THỬ BA CHỈ SỐ TRÊN 1.200 YÊU CẦU (ĐỢT CHẠY THỬ, CHƯA CÓ ĐỐI CHỨNG) ===')
    mask_chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    so_chinh = int(mask_chinh.sum())
    tl_chinh = mask_chinh.mean() * 100

    xem = reqs[reqs['duoc_xem_lai'] == 1]
    so_bo_qua = int(xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum())
    tl_bo_qua = (so_bo_qua / len(xem)) * 100

    so_an_toan = int((reqs['mo_lai_trong_7_ngay'] == 1).sum())
    tl_an_toan = (so_an_toan / len(reqs)) * 100

    print(f"  Chính (% đóng 24h & không mở lại 7 ngày): {tl_chinh:6.2f}% ({so_chinh}/{len(reqs)})")
    print(f"  Dùng  (Tỉ lệ bỏ qua gợi ý sua + bo):      {tl_bo_qua:6.2f}% ({so_bo_qua}/{len(xem)})")
    print(f"  An toàn (Tỉ lệ mở lại trong 7 ngày):      {tl_an_toan:6.2f}% ({so_an_toan}/{len(reqs)})")


def kiem_tra_pilot_plan(yaml_path=None):
    print('\n=== KIỂM TRA HỢP LỆ report/team/pilot_plan.yaml ===')
    if yaml_path is None:
        yaml_path = Path(__file__).resolve().parent.parent / 'report' / 'team' / 'pilot_plan.yaml'
    try:
        import yaml
    except ImportError:
        print('  [Bỏ qua] Chưa cài pyyaml trong môi trường hiện tại.')
        return
    with open(yaml_path, encoding='utf-8') as f:
        raw_lines = f.readlines()
    non_comment_q = [i + 1 for i, line in enumerate(raw_lines) if not line.lstrip().startswith('#') and '?' in line]
    data = yaml.safe_load(''.join(raw_lines))
    pilot = data['pilot']
    pm = pilot['primary_metric']
    rules = pilot['stop_rules']
    assert not non_comment_q, f'Còn dấu ? ở dòng: {non_comment_q}'
    assert len(rules) >= 3, 'Cần ít nhất 3 luật dừng'
    for idx, rule in enumerate(rules, 1):
        for clause in ['NẾU', 'TRONG', 'THÌ', 'KHÔNG THÌ']:
            assert clause in rule, f'Luật dừng #{idx} thiếu vế {clause}'
    print(
        f"  ĐẠT · yaml.safe_load hợp lệ, không còn dấu ?, {len(rules)} luật dừng đủ 4 vế "
        f"(n_per_arm={pm['n_per_arm']}, DE={pm['design_effect']}, clusters_per_arm={pm['clusters_per_arm']})"
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs)
    in_nhiem_vu_d(reqs)
    in_nhiem_vu_e1(reqs)
    kiem_tra_pilot_plan()
