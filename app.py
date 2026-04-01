import streamlit as st
import pandas as pd
from datetime import datetime
import os

# =================配置部分=================
# 兼容本地和 Streamlit Cloud 的路径配置
import sys
if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    # 虚拟环境或 Streamlit Cloud
    CSV_DIR = 'z_house'
else:
    # 本地环境
    CSV_DIR = r'E:\Desktop\wq_flow\z_house'

CSV_FILE = os.path.join(CSV_DIR, 'hefei_house.csv')
st.set_page_config(page_title="合肥看房助手", layout="wide", page_icon="🏠")


# =================界面美化部分=================
def inject_custom_css():
    st.markdown("""
    <style>
    header[data-testid="stHeader"] {
        display: none;
    }

    .stApp {
        background: #f3f6fb;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 1.4rem;
        padding-bottom: 2rem;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8fbff 0%, #eef4ff 100%);
        border-right: 1px solid #dbe7f5;
    }

    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div {
        color: #1f2937 !important;
    }

    .page-header-wrap {
        background: #ddeafb;
        border: 1px solid #e5e7eb;
        border-radius: 20px;
        padding: 18px 20px 16px 20px;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.05);
        margin-bottom: 14px;
    }

    .main-title {
        font-size: 30px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 4px;
        line-height: 1.2;
    }

    .sub-title {
        font-size: 14px;
        color: #64748b;
        margin-bottom: 0;
    }

    .section-title {
        background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        padding: 12px 16px;
        border-radius: 14px;
        font-size: 17px;
        font-weight: 700;
        margin-top: 18px;
        margin-bottom: 12px;
        box-shadow: 0 10px 20px rgba(37, 99, 235, 0.18);
    }

    .mini-title {
        font-size: 15px;
        font-weight: 700;
        color: #0f172a;
        margin-top: 10px;
        margin-bottom: 8px;
        padding-left: 2px;
    }

    .admin-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 16px 16px 10px 16px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
        margin-bottom: 14px;
    }

    .compare-card {
        background: #ffffff;
        border: 1px solid #dbe4f0;
        border-radius: 18px;
        padding: 14px 16px 12px 16px;
        box-shadow: 0 10px 26px rgba(15, 23, 42, 0.05);
        margin-bottom: 14px;
    }

    .detail-box-title {
        font-size: 14px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 10px;
    }

    .sidebar-brand {
        background: #ddeafb;
        padding: 18px 14px;
        border-radius: 18px;
        color: white;
        font-size: 22px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 14px;
        box-shadow: 0 10px 20px rgba(59, 130, 246, 0.25);
    }

    .sidebar-tip {
        padding: 10px 12px;
        border-radius: 12px;
        background: #ffffff;
        border: 1px solid #dbe7f5;
        margin-bottom: 12px;
        font-size: 13px;
        color: #475569 !important;
    }

    label[data-testid="stWidgetLabel"] p {
        font-size: 14px !important;
        font-weight: 700 !important;
        color: #1f2937 !important;
    }

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="textarea"] > div {
        border-radius: 12px !important;
        border: 1px solid #d1d5db !important;
        background-color: #ffffff !important;
        min-height: 42px;
        box-shadow: none !important;
        transition: all 0.18s ease;
    }

    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="select"] > div:focus-within,
    div[data-baseweb="textarea"] > div:focus-within {
        border: 1px solid #2563eb !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
    }

    input, textarea {
        font-size: 14px !important;
    }

    div[data-testid="stNumberInput"] input {
        font-size: 14px !important;
    }

    .stButton > button,
    .stDownloadButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        border-radius: 12px !important;
        border: 1px solid transparent !important;
        padding: 0.66rem 1rem !important;
        font-size: 14px !important;
        font-weight: 800 !important;
        transition: all 0.18s ease-in-out !important;
        box-shadow: 0 8px 18px rgba(15, 23, 42, 0.06);
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 12px 22px rgba(15, 23, 42, 0.10);
    }

    div[data-testid="stDataFrame"] {
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid #e5e7eb;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
        background: white;
    }

    div[data-testid="stAlert"] {
        border-radius: 14px !important;
    }

    div[data-testid="metric-container"] {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 14px 12px;
        box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
    }

    details {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 8px 10px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
    }

    hr {
        border: none;
        height: 1px;
        background: #e5e7eb;
        margin: 16px 0;
    }

    .filter-title {
        font-size: 15px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 10px;
    }

    .score-badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: #eff6ff;
        color: #1d4ed8;
        font-size: 15px;
        font-weight: 800;
        border: 1px solid #bfdbfe;
    }

    .status-chip {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 800;
        border: 1px solid #e5e7eb;
        background: #f8fafc;
        color: #334155;
    }

    .hint-box {
        background: #f8fafc;
        border: 1px dashed #cbd5e1;
        border-radius: 12px;
        padding: 10px 12px;
        font-size: 13px;
        color: #475569;
        margin-top: 8px;
        margin-bottom: 8px;
    }
    </style>
    """, unsafe_allow_html=True)


def render_page_header(title, subtitle=""):
    st.markdown(
        f"""
        <div class="page-header-wrap">
            <div class="main-title">{title}</div>
            <div class="sub-title">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_section(title):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def render_mini_title(title):
    st.markdown(f'<div class="mini-title">{title}</div>', unsafe_allow_html=True)


def render_score_selector(key_prefix, default_score=5, label="综合评分 (1-10)"):
    score_key = f"{key_prefix}_score"
    minus_key = f"{key_prefix}_minus"
    plus_key = f"{key_prefix}_plus"

    if score_key not in st.session_state:
        st.session_state[score_key] = int(default_score)

    st.markdown(f"**{label}**")
    c1, c2, c3 = st.columns([1, 2, 1])

    with c1:
        if st.button("➖", key=minus_key, use_container_width=True):
            st.session_state[score_key] = max(1, st.session_state[score_key] - 1)

    with c2:
        st.markdown(
            f"""
            <div style="
                height:44px;
                border:1px solid #d1d5db;
                border-radius:12px;
                background:#ffffff;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:18px;
                font-weight:800;
                color:#2563eb;
                box-shadow:0 6px 14px rgba(15,23,42,0.04);
            ">
                {st.session_state[score_key]} 分
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        if st.button("➕", key=plus_key, use_container_width=True):
            st.session_state[score_key] = min(10, st.session_state[score_key] + 1)

    return st.session_state[score_key]


def style_status_text(status):
    if status == "考虑中":
        return "🟡 考虑中"
    if status == "准备谈价":
        return "🔵 准备谈价"
    if status == "已成交":
        return "🟢 已成交"
    if status == "已排除":
        return "🔴 已排除"
    return str(status)


# =================CSV 文件操作=================
def init_csv():
    if not os.path.exists(CSV_DIR):
        os.makedirs(CSV_DIR, exist_ok=True)

    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=[
            'id', 'view_date', 'community_name', 'district', 'total_price',
            'unit_price', 'area', 'layout', 'floor_info', 'orientation',
            'year_built', 'is_full5_unique', 'has_mortgage', 'school_quota',
            'decoration', 'landlord_reason', 'pros', 'cons', 'score', 'status', 'parking',
            'house_type',
            'property_rights_years', 'parking_info', 'property_management',
            'mortgage_info', 'loan_backup', 'occupancy_status', 'quality_issues',
            'decoration_materials', 'seizure_dispute', 'co_owners', 'hukou_migration',
            'land_grant_type',
            'land_usage_type'
        ])
        df.to_csv(CSV_FILE, index=False, encoding='utf-8-sig')
        print(f"✓ CSV 文件已创建：{CSV_FILE}")


def add_house(data):
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE, encoding='utf-8-sig')
    else:
        df = pd.DataFrame()

    if len(df) > 0:
        new_id = df['id'].max() + 1
    else:
        new_id = 1

    new_record = {
        'id': new_id,
        'view_date': data['view_date'],
        'community_name': data['community'],
        'district': data['district'],
        'total_price': data['total_price'],
        'unit_price': data['unit_price'],
        'area': data['area'],
        'layout': data['layout'],
        'floor_info': data['floor'],
        'orientation': data['orientation'],
        'year_built': data['year'],
        'is_full5_unique': data['full5'],
        'has_mortgage': data['mortgage'],
        'school_quota': data['school'],
        'decoration': data['decoration'],
        'landlord_reason': data['reason'],
        'pros': data['pros'],
        'cons': data['cons'],
        'score': data['score'],
        'status': data['status'],
        'parking': data['parking'],
        'house_type': data.get('house_type', ''),
        'property_rights_years': data.get('property_rights_years', ''),
        'parking_info': data.get('parking_info', ''),
        'property_management': data.get('property_management', ''),
        'mortgage_info': data.get('mortgage_info', ''),
        'loan_backup': data.get('loan_backup', ''),
        'occupancy_status': data.get('occupancy_status', ''),
        'quality_issues': data.get('quality_issues', ''),
        'decoration_materials': data.get('decoration_materials', ''),
        'seizure_dispute': data.get('seizure_dispute', ''),
        'co_owners': data.get('co_owners', ''),
        'hukou_migration': data.get('hukou_migration', ''),
        'land_grant_type': data.get('land_grant_type', '不确定'),
        'land_usage_type': data.get('land_usage_type', '不确定')
    }

    df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False, encoding='utf-8-sig')


def update_house(house_id, data):
    if not os.path.exists(CSV_FILE):
        return False

    df = pd.read_csv(CSV_FILE, encoding='utf-8-sig')
    mask = df['id'] == house_id
    if not mask.any():
        return False

    update_fields = {
        'view_date': data.get('view_date'),
        'community_name': data.get('community'),
        'district': data.get('district'),
        'total_price': data.get('total_price'),
        'unit_price': data.get('unit_price'),
        'area': data.get('area'),
        'layout': data.get('layout'),
        'floor_info': data.get('floor'),
        'orientation': data.get('orientation'),
        'year_built': data.get('year'),
        'is_full5_unique': data.get('full5'),
        'has_mortgage': data.get('mortgage'),
        'school_quota': data.get('school'),
        'decoration': data.get('decoration'),
        'landlord_reason': data.get('reason'),
        'pros': data.get('pros'),
        'cons': data.get('cons'),
        'score': data.get('score'),
        'status': data.get('status'),
        'parking': data.get('parking'),
        'house_type': data.get('house_type'),
        'property_rights_years': data.get('property_rights_years'),
        'parking_info': data.get('parking_info'),
        'property_management': data.get('property_management'),
        'mortgage_info': data.get('mortgage_info'),
        'loan_backup': data.get('loan_backup'),
        'occupancy_status': data.get('occupancy_status'),
        'quality_issues': data.get('quality_issues'),
        'decoration_materials': data.get('decoration_materials'),
        'seizure_dispute': data.get('seizure_dispute'),
        'co_owners': data.get('co_owners'),
        'hukou_migration': data.get('hukou_migration'),
        'land_grant_type': data.get('land_grant_type'),
        'land_usage_type': data.get('land_usage_type')
    }

    for field, value in update_fields.items():
        if value is not None and field in df.columns:
            df.loc[mask, field] = value

    df.to_csv(CSV_FILE, index=False, encoding='utf-8-sig')
    return True


def get_all_houses():
    if not os.path.exists(CSV_FILE):
        return pd.DataFrame()

    df = pd.read_csv(CSV_FILE, encoding='utf-8-sig')
    if not df.empty:
        df = df.sort_values('view_date', ascending=False).reset_index(drop=True)
    return df


def get_house_by_id(house_id):
    if not os.path.exists(CSV_FILE):
        return None

    df = pd.read_csv(CSV_FILE, encoding='utf-8-sig')
    result = df[df['id'] == house_id]
    if result.empty:
        return None
    return result.iloc[0]


def get_unique_communities():
    preset_communities = [
        "庐阳柳林苑", "阅庐春晓", "文一名门湖畔(西区)", "中国铁建国际城", "开元华庭"
    ]

    df = get_all_houses()
    existing_communities = []
    if not df.empty:
        existing_communities = df['community_name'].dropna().unique().tolist()

    all_communities = sorted(list(set(preset_communities + existing_communities)))
    return all_communities


def delete_house(house_id):
    if not os.path.exists(CSV_FILE):
        return

    df = pd.read_csv(CSV_FILE, encoding='utf-8-sig')
    df = df[df['id'] != house_id]
    df.to_csv(CSV_FILE, index=False, encoding='utf-8-sig')


# =================主界面=================
def main():
    init_csv()
    inject_custom_css()

    st.sidebar.markdown('<div class="sidebar-brand">🏠 合肥看房助手</div>', unsafe_allow_html=True)

    menu = ["📝 录入房屋信息", "📋 查看录入信息", "📊 房源对比", "🗑️ 管理数据"]
    choice = st.sidebar.radio("导航菜单", menu, index=0)

    # ================= 录入房屋信息 =================
    if choice == "📝 录入房屋信息":
        render_page_header("📝 房屋信息录入", "标准化录入房源信息，方便后续筛选、对比与决策")



        render_section("1. 基础信息")
        col1, col2, col3 = st.columns(3)

        with col1:
            view_date = st.date_input("看房日期", datetime.now())
            district = st.selectbox("区域",
                                    ["政务区", "滨湖区", "高新区", "蜀山区", "庐阳区", "包河区", "瑶海区", "其他"])
            existing_communities = get_unique_communities()
            community = st.selectbox("小区名称", existing_communities)
            house_type = st.selectbox("房屋类型", ["商品房", "回迁房"], help="商品房产权清晰，回迁房需确认土地性质")

        with col2:
            total_price = st.number_input("挂牌总价 (万)", min_value=0.0, step=1.0)
            area = st.number_input("建筑面积 (㎡)", min_value=0.0, step=1.0)
            unit_price = st.number_input("单价 (万/㎡)", min_value=0.0, step=0.1)
            parking = st.selectbox("地下停车场", ["有", "无", "不确定"])

        with col3:
            lc1, lc2, lc3 = st.columns(3)
            with lc1:
                layout_room = st.selectbox("几室", ["1 室", "2 室", "3 室", "4 室", "5 室", "6 室", "复式"], index=2,
                                           key="layout_room")
            with lc2:
                layout_hall = st.selectbox("几厅", ["1 厅", "2 厅", "3 厅"], index=1, key="layout_hall")
            with lc3:
                layout_bath = st.selectbox("几卫", ["1 卫", "2 卫", "3 卫"], index=0, key="layout_bath")

            layout = f"{layout_room}{layout_hall}{layout_bath}"

            fc1, fc2 = st.columns(2)
            with fc1:
                floor_current = st.selectbox("当前层", list(range(1, 34)), index=4, key="floor_current")
            with fc2:
                floor_total = st.selectbox("总层数", [6, 11, 18, 24, 26, 28, 30, 32, 33], index=2, key="floor_total")

            floor = f"{floor_current}/{floor_total}"
            orientation = st.selectbox("朝向", ["南", "东南", "东", "西南", "北", "其他"])
            year = st.number_input("建成年份", min_value=1980, max_value=2025, step=1, value=2015)



        render_section("2. 产权与交易")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            full5 = st.selectbox("满五唯一？", ["是", "否", "不确定"])
        with c2:
            mortgage = st.selectbox("有抵押？", ["无", "有 (可解)", "有 (难解)"])
        with c3:
            school = st.selectbox("学区占用？", ["未占用", "已占用", "不确定"])
        with c4:
            decoration = st.selectbox("装修情况", ["毛坯", "简装", "精装", "豪装"])

        lc1, lc2 = st.columns(2)
        with lc1:
            land_grant_type = st.selectbox("土地性质", ["出让", "划拨", "不确定"], index=0)
        with lc2:
            land_usage_type = st.selectbox("土地用途", ["纯住宅", "商住两用", "公寓", "不确定"], index=0)

        seizure_dispute = st.selectbox("查封/纠纷", ["无", "有查封", "有纠纷", "不确定"])
        co_owners = st.text_input("产权人情况", placeholder="如：单独所有/夫妻共同/与父母共有")
        hukou_migration = st.text_input("户口迁出安排", placeholder="如：过户前迁出/具体时间约定")



        render_section("3. 评价与备注")

        render_mini_title("🏠 房子基本情况")
        reason = st.text_input("房东出售原因")
        property_rights_years = st.number_input("产权剩余年限 (年)", min_value=0, max_value=70, step=1, value=50)
        parking_info = st.text_input("停车情况", placeholder="如：人车分流、车位充足/紧张、月租费用")
        property_management = st.text_input("物业信息", placeholder="物业是否欠费+物业名称 + 物业费 (元/㎡/月)")

        render_mini_title("💰 税费与贷款")
        mortgage_info = st.text_input("抵押情况详情", placeholder="如：有抵押可解押/银行能否带押过户")
        loan_backup = st.text_input("贷款备选方案", placeholder="如：交易不成定金全退/不批贷定金全退/部分退还")

        render_mini_title("🔍 房屋细节")
        occupancy_status = st.text_input("居住权与租赁状态", placeholder="如：无居住权/空置/租约到期时间")
        quality_issues = st.text_input("质量问题", placeholder="如：无漏水/墙角发霉已处理/水电正常/噪音")
        decoration_materials = st.text_input("装修材料清单", placeholder="精装房填写，毛坯房留空")

        pros = st.text_area("✅ 优点总结", placeholder="填写交通、商业、学校、采光、户型等优点")
        cons = st.text_area("❌ 缺点/风险总结", placeholder="填写噪音、税费、学区、贷款、朝向、环境等风险")

        st.markdown('<div class="hint-box">评分支持点击加减，更适合看房时快速给出主观判断。</div>',
                    unsafe_allow_html=True)
        score = render_score_selector("add_house", default_score=5, label="综合评分 (1-10)")
        status = st.selectbox("当前状态", ["考虑中", "已排除", "准备谈价", "已成交"])


        if st.button("💾 保存记录", type="primary", use_container_width=True):
            if not community:
                st.error("请填写小区名称！")
            else:
                data = {
                    'view_date': str(view_date), 'community': community, 'district': district,
                    'total_price': total_price, 'unit_price': unit_price, 'area': area,
                    'layout': layout, 'floor': floor, 'orientation': orientation, 'year': year,
                    'full5': full5, 'mortgage': mortgage, 'school': school, 'decoration': decoration,
                    'reason': reason, 'pros': pros, 'cons': cons, 'score': score, 'status': status,
                    'parking': parking,
                    'house_type': house_type,
                    'property_rights_years': property_rights_years,
                    'parking_info': parking_info,
                    'property_management': property_management,
                    'mortgage_info': mortgage_info,
                    'loan_backup': loan_backup,
                    'occupancy_status': occupancy_status,
                    'quality_issues': quality_issues,
                    'decoration_materials': decoration_materials,
                    'seizure_dispute': seizure_dispute,
                    'co_owners': co_owners,
                    'hukou_migration': hukou_migration,
                    'land_grant_type': land_grant_type,
                    'land_usage_type': land_usage_type
                }
                add_house(data)
                st.success("✅ 保存成功！")

    # ================= 查看录入信息 =================
    elif choice == "📋 查看录入信息":
        render_page_header("📋 已录入房源列表", "支持搜索、筛选、排序、编辑与导出")
        df = get_all_houses()

        if not df.empty:
            s1, s2, s3, s4 = st.columns(4)
            with s1:
                st.metric("房源总数", len(df))
            with s2:
                st.metric("考虑中", int((df["status"] == "考虑中").sum()))
            with s3:
                st.metric("准备谈价", int((df["status"] == "准备谈价").sum()))
            with s4:
                st.metric("已成交", int((df["status"] == "已成交").sum()))


            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                search = st.text_input("🔎 搜索小区/区域", placeholder="输入关键词")
            with col2:
                status_filter = st.multiselect("状态筛选", ["考虑中", "已排除", "准备谈价", "已成交"], default=[])
            with col3:
                sort_by = st.selectbox("排序方式", ["看房日期↓", "看房日期↑", "总价↓", "总价↑", "评分↓", "评分↑"])


            if search:
                df = df[
                    df['community_name'].str.contains(search, case=False, na=False) |
                    df['district'].str.contains(search, case=False, na=False)
                    ]
            if status_filter:
                df = df[df['status'].isin(status_filter)]

            if sort_by == "看房日期↓":
                df = df.sort_values('view_date', ascending=False)
            elif sort_by == "看房日期↑":
                df = df.sort_values('view_date', ascending=True)
            elif sort_by == "总价↓":
                df = df.sort_values('total_price', ascending=False)
            elif sort_by == "总价↑":
                df = df.sort_values('total_price', ascending=True)
            elif sort_by == "评分↓":
                df = df.sort_values('score', ascending=False)
            elif sort_by == "评分↑":
                df = df.sort_values('score', ascending=True)

            df_show = df.copy()
            df_show["status"] = df_show["status"].apply(style_status_text)
            df_show["score"] = df_show["score"].astype(int).astype(str) + " ⭐"

            st.info(f"📊 共 {len(df_show)} 条记录" + (f"（筛选后）" if search or status_filter else ""))

            display_cols = [
                'id', 'view_date', 'community_name', 'district', 'house_type',
                'total_price', 'area', 'layout', 'land_grant_type', 'land_usage_type',
                'is_full5_unique', 'has_mortgage', 'school_quota', 'score', 'status'
            ]

            st.dataframe(
                df_show[display_cols].reset_index(drop=True),
                use_container_width=True,
                height=420,
                hide_index=True
            )

            render_section("✏️ 编辑房源信息")
            edit_col1, edit_col2 = st.columns([1, 2])
            with edit_col1:
                edit_id = st.number_input(
                    "🔢 输入要编辑的房源 ID",
                    min_value=1,
                    step=1,
                    value=int(df['id'].min()) if not df.empty else 1
                )

            selected_house = get_house_by_id(edit_id)

            with edit_col2:
                if selected_house is not None:
                    st.success(
                        f"✅ 已选中：{selected_house['community_name']} - {selected_house['layout']} - {selected_house['total_price']}万")
                else:
                    st.error("❌ 该 ID 不存在，请检查后重新输入")

            if selected_house is not None:
                with st.form(key=f"edit_form_{edit_id}"):
                    st.markdown("##### 1️⃣ 基础信息")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        edit_community = st.text_input("小区名称", value=str(selected_house['community_name']))
                        edit_district = st.selectbox(
                            "区域",
                            ["政务区", "滨湖区", "高新区", "蜀山区", "庐阳区", "包河区", "瑶海区", "其他"],
                            index=["政务区", "滨湖区", "高新区", "蜀山区", "庐阳区", "包河区", "瑶海区", "其他"].index(
                                str(selected_house['district'])
                            ) if str(selected_house['district']) in ["政务区", "滨湖区", "高新区", "蜀山区", "庐阳区",
                                                                     "包河区", "瑶海区", "其他"] else 0
                        )
                        edit_house_type = st.selectbox(
                            "房屋类型",
                            ["商品房", "回迁房"],
                            index=["商品房", "回迁房"].index(str(selected_house['house_type']))
                            if str(selected_house['house_type']) in ["商品房", "回迁房"] else 0
                        )
                    with col2:
                        edit_total_price = st.number_input("总价 (万)", min_value=0.0, step=1.0,
                                                           value=float(selected_house['total_price']))
                        edit_area = st.number_input("面积 (㎡)", min_value=0.0, step=1.0,
                                                    value=float(selected_house['area']))
                        edit_unit_price = st.number_input("单价 (万/㎡)", min_value=0.0, step=0.1,
                                                          value=float(selected_house['unit_price']))
                        edit_parking = st.selectbox(
                            "地下停车场",
                            ["有", "无", "不确定"],
                            index=["有", "无", "不确定"].index(str(selected_house['parking']))
                            if str(selected_house['parking']) in ["有", "无", "不确定"] else 1
                        )
                    with col3:
                        edit_layout = st.text_input("户型", value=str(selected_house['layout']))
                        edit_floor = st.text_input("楼层", value=str(selected_house['floor_info']))
                        edit_orientation = st.selectbox(
                            "朝向",
                            ["南", "东南", "东", "西南", "北", "其他"],
                            index=["南", "东南", "东", "西南", "北", "其他"].index(str(selected_house['orientation']))
                            if str(selected_house['orientation']) in ["南", "东南", "东", "西南", "北", "其他"] else 0
                        )
                        edit_year = st.number_input("建成年份", min_value=1980, max_value=2025, step=1,
                                                    value=int(selected_house['year_built']))

                    st.markdown("##### 2️⃣ 产权与交易")
                    c1, c2, c3, c4 = st.columns(4)
                    with c1:
                        edit_full5 = st.selectbox(
                            "满五唯一？",
                            ["是", "否", "不确定"],
                            index=["是", "否", "不确定"].index(str(selected_house['is_full5_unique']))
                            if str(selected_house['is_full5_unique']) in ["是", "否", "不确定"] else 1
                        )
                    with c2:
                        edit_mortgage = st.selectbox(
                            "有抵押？",
                            ["无", "有 (可解)", "有 (难解)"],
                            index=["无", "有 (可解)", "有 (难解)"].index(str(selected_house['has_mortgage']))
                            if str(selected_house['has_mortgage']) in ["无", "有 (可解)", "有 (难解)"] else 0
                        )
                    with c3:
                        edit_school = st.selectbox(
                            "学区占用？",
                            ["未占用", "已占用", "不确定"],
                            index=["未占用", "已占用", "不确定"].index(str(selected_house['school_quota']))
                            if str(selected_house['school_quota']) in ["未占用", "已占用", "不确定"] else 0
                        )
                    with c4:
                        edit_decoration = st.selectbox(
                            "装修情况",
                            ["毛坯", "简装", "精装", "豪装"],
                            index=["毛坯", "简装", "精装", "豪装"].index(str(selected_house['decoration']))
                            if str(selected_house['decoration']) in ["毛坯", "简装", "精装", "豪装"] else 0
                        )

                    land_col1, land_col2 = st.columns(2)
                    with land_col1:
                        edit_land_grant = st.selectbox(
                            "土地性质",
                            ["出让", "划拨", "不确定"],
                            index=["出让", "划拨", "不确定"].index(str(selected_house['land_grant_type']))
                            if str(selected_house['land_grant_type']) in ["出让", "划拨", "不确定"] else 0
                        )
                    with land_col2:
                        edit_land_usage = st.selectbox(
                            "土地用途",
                            ["纯住宅", "商住两用", "公寓", "不确定"],
                            index=["纯住宅", "商住两用", "公寓", "不确定"].index(str(selected_house['land_usage_type']))
                            if str(selected_house['land_usage_type']) in ["纯住宅", "商住两用", "公寓", "不确定"] else 0
                        )

                    edit_seizure = st.selectbox(
                        "查封/纠纷",
                        ["无", "有查封", "有纠纷", "不确定"],
                        index=["无", "有查封", "有纠纷", "不确定"].index(str(selected_house['seizure_dispute']))
                        if str(selected_house['seizure_dispute']) in ["无", "有查封", "有纠纷", "不确定"] else 0
                    )
                    edit_co_owners = st.text_input("产权人情况", value=str(selected_house['co_owners']) if pd.notna(
                        selected_house['co_owners']) else "")
                    edit_hukou = st.text_input("户口迁出安排", value=str(selected_house['hukou_migration']) if pd.notna(
                        selected_house['hukou_migration']) else "")

                    st.markdown("##### 3️⃣ 房子基本情况")
                    edit_reason = st.text_input("房东出售原因",
                                                value=str(selected_house['landlord_reason']) if pd.notna(
                                                    selected_house['landlord_reason']) else "")
                    edit_property_years = st.number_input(
                        "产权剩余年限 (年)",
                        min_value=0,
                        max_value=70,
                        step=1,
                        value=int(selected_house['property_rights_years']) if pd.notna(
                            selected_house['property_rights_years']) else 50
                    )
                    edit_parking_info = st.text_input("停车情况", value=str(selected_house['parking_info']) if pd.notna(
                        selected_house['parking_info']) else "")
                    edit_property_mgmt = st.text_input("物业信息",
                                                       value=str(selected_house['property_management']) if pd.notna(
                                                           selected_house['property_management']) else "")

                    st.markdown("##### 4️⃣ 税费与贷款")
                    edit_mortgage_info = st.text_input("抵押情况详情",
                                                       value=str(selected_house['mortgage_info']) if pd.notna(
                                                           selected_house['mortgage_info']) else "")
                    edit_loan_backup = st.text_input("贷款备选方案",
                                                     value=str(selected_house['loan_backup']) if pd.notna(
                                                         selected_house['loan_backup']) else "")

                    st.markdown("##### 5️⃣ 房屋细节")
                    edit_occupancy = st.text_input("居住权与租赁状态",
                                                   value=str(selected_house['occupancy_status']) if pd.notna(
                                                       selected_house['occupancy_status']) else "")
                    edit_quality = st.text_input("质量问题", value=str(selected_house['quality_issues']) if pd.notna(
                        selected_house['quality_issues']) else "")
                    edit_deco_materials = st.text_input("装修材料清单",
                                                        value=str(selected_house['decoration_materials']) if pd.notna(
                                                            selected_house['decoration_materials']) else "")

                    st.markdown("##### 6️⃣ 评价与状态")
                    edit_pros = st.text_area("✅ 优点", value=str(selected_house['pros']) if pd.notna(
                        selected_house['pros']) else "")
                    edit_cons = st.text_area("❌ 缺点", value=str(selected_house['cons']) if pd.notna(
                        selected_house['cons']) else "")
                    edit_score = st.number_input("综合评分", min_value=1, max_value=10, step=1,
                                                 value=int(selected_house['score']))
                    edit_status = st.selectbox(
                        "当前状态",
                        ["考虑中", "已排除", "准备谈价", "已成交"],
                        index=["考虑中", "已排除", "准备谈价", "已成交"].index(str(selected_house['status']))
                        if str(selected_house['status']) in ["考虑中", "已排除", "准备谈价", "已成交"] else 0
                    )

                    submit_col1, submit_col2 = st.columns([1, 4])
                    with submit_col1:
                        submit_edit = st.form_submit_button("💾 保存修改", type="primary", use_container_width=True)
                    with submit_col2:
                        cancel_edit = st.form_submit_button("❌ 取消", use_container_width=True)

                    if submit_edit:
                        update_data = {
                            'view_date': str(selected_house['view_date']),
                            'community': edit_community,
                            'district': edit_district,
                            'total_price': edit_total_price,
                            'unit_price': edit_unit_price,
                            'area': edit_area,
                            'layout': edit_layout,
                            'floor': edit_floor,
                            'orientation': edit_orientation,
                            'year': edit_year,
                            'full5': edit_full5,
                            'mortgage': edit_mortgage,
                            'school': edit_school,
                            'decoration': edit_decoration,
                            'reason': edit_reason,
                            'pros': edit_pros,
                            'cons': edit_cons,
                            'score': edit_score,
                            'status': edit_status,
                            'parking': edit_parking,
                            'house_type': edit_house_type,
                            'property_rights_years': edit_property_years,
                            'parking_info': edit_parking_info,
                            'property_management': edit_property_mgmt,
                            'mortgage_info': edit_mortgage_info,
                            'loan_backup': edit_loan_backup,
                            'occupancy_status': edit_occupancy,
                            'quality_issues': edit_quality,
                            'decoration_materials': edit_deco_materials,
                            'seizure_dispute': edit_seizure,
                            'co_owners': edit_co_owners,
                            'hukou_migration': edit_hukou,
                            'land_grant_type': edit_land_grant,
                            'land_usage_type': edit_land_usage
                        }

                        if update_house(edit_id, update_data):
                            st.success("✅ 更新成功！")
                            st.rerun()
                        else:
                            st.error("❌ 更新失败，请重试")

                    if cancel_edit:
                        st.info("已取消编辑")

            st.download_button(
                label="📥 导出当前列表为 CSV",
                data=df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig'),
                file_name=f"hefei_house_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime='text/csv',
                use_container_width=True
            )

        else:
            st.warning("📭 暂无录入数据，请先添加记录。")

    # ================= 房源对比 =================
    elif choice == "📊 房源对比":
        render_page_header("📊 房源对比分析", "多条件筛选 + 对比总表 + 单套房源详情分析")
        df = get_all_houses()

        if not df.empty:

            st.markdown('<div class="filter-title">🔍 多条件筛选</div>', unsafe_allow_html=True)

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                filter_district = st.multiselect("区域", sorted(df['district'].dropna().unique()))
            with col2:
                filter_house_type = st.multiselect("房屋类型", sorted(df['house_type'].dropna().unique()))
            with col3:
                filter_status = st.multiselect("状态", sorted(df['status'].dropna().unique()))
            with col4:
                filter_layout = st.multiselect("户型", sorted(df['layout'].dropna().unique()))

            col5, col6, col7 = st.columns([1.4, 1.4, 1.6])

            price_data_min = float(df['total_price'].min())
            price_data_max = float(df['total_price'].max())
            if price_data_min == price_data_max:
                price_data_min = max(0, price_data_min - 50)
                price_data_max = price_data_max + 50

            area_data_min = float(df['area'].min())
            area_data_max = float(df['area'].max())
            if area_data_min == area_data_max:
                area_data_min = max(0, area_data_min - 20)
                area_data_max = area_data_max + 20

            with col5:
                st.markdown("**总价区间 (万)**")
                p1, p2 = st.columns(2)
                with p1:
                    price_min_input = st.number_input(
                        "最低总价",
                        min_value=0.0,
                        max_value=float(price_data_max),
                        value=float(price_data_min),
                        step=1.0,
                        key="compare_price_min",
                        label_visibility="collapsed"
                    )
                with p2:
                    price_max_input = st.number_input(
                        "最高总价",
                        min_value=0.0,
                        max_value=float(max(price_data_max, price_min_input)),
                        value=float(price_data_max),
                        step=1.0,
                        key="compare_price_max",
                        label_visibility="collapsed"
                    )

            with col6:
                st.markdown("**建筑面积区间 (㎡)**")
                a1, a2 = st.columns(2)
                with a1:
                    area_min_input = st.number_input(
                        "最小面积",
                        min_value=0.0,
                        max_value=float(area_data_max),
                        value=float(area_data_min),
                        step=1.0,
                        key="compare_area_min",
                        label_visibility="collapsed"
                    )
                with a2:
                    area_max_input = st.number_input(
                        "最大面积",
                        min_value=0.0,
                        max_value=float(max(area_data_max, area_min_input)),
                        value=float(area_data_max),
                        step=1.0,
                        key="compare_area_max",
                        label_visibility="collapsed"
                    )

            with col7:
                search_community = st.text_input("🔎 搜索小区名称", placeholder="输入小区关键词")

            price_range = (min(price_min_input, price_max_input), max(price_min_input, price_max_input))
            area_range = (min(area_min_input, area_max_input), max(area_min_input, area_max_input))

            st.markdown('<div class="hint-box">建议先按区域、总价、面积筛选，再结合评分和优缺点比较。</div>',
                        unsafe_allow_html=True)


            if filter_district:
                df = df[df['district'].isin(filter_district)]
            if filter_status:
                df = df[df['status'].isin(filter_status)]
            if filter_house_type:
                df = df[df['house_type'].isin(filter_house_type)]
            if filter_layout:
                df = df[df['layout'].isin(filter_layout)]
            if price_range and len(price_range) == 2:
                df = df[(df['total_price'] >= price_range[0]) & (df['total_price'] <= price_range[1])]
            if area_range and len(area_range) == 2:
                df = df[(df['area'] >= area_range[0]) & (df['area'] <= area_range[1])]
            if search_community:
                df = df[df['community_name'].str.contains(search_community, case=False, na=True)]

            st.info(f"📊 找到 {len(df)} 套符合条件的房源")


            st.markdown('<div class="filter-title">📋 房源对比总表</div>', unsafe_allow_html=True)

            df_show = df.copy()
            df_show["status"] = df_show["status"].apply(style_status_text)

            display_cols = [
                'id', 'community_name', 'district', 'house_type', 'total_price', 'unit_price',
                'area', 'layout', 'year_built', 'land_grant_type', 'land_usage_type', 'score', 'status'
            ]

            st.dataframe(
                df_show[display_cols],
                use_container_width=True,
                height=420,
                hide_index=True
            )


            if len(df) > 0:
                render_section("🔍 房源详情分析")
                selected_id = st.selectbox("选择房源 ID 查看详情", sorted(df['id'].unique()))
                if selected_id:
                    detail = df[df['id'] == selected_id].iloc[0]

                    top_left, top_mid, top_right = st.columns([2, 2, 1.2])

                    with top_left:

                        st.markdown('<div class="detail-box-title">🏘 基本信息</div>', unsafe_allow_html=True)
                        st.write(f"**小区名称：** {detail['community_name']}")
                        st.write(f"**所属区域：** {detail['district']}")
                        st.write(f"**房屋类型：** {detail['house_type']}")
                        st.write(f"**户型结构：** {detail['layout']}")
                        st.write(f"**楼层信息：** {detail['floor_info']}")
                        st.write(f"**朝向：** {detail['orientation']}")
                        st.write(f"**建成年份：** {int(detail['year_built'])}")


                    with top_mid:

                        st.markdown('<div class="detail-box-title">💰 价格指标</div>', unsafe_allow_html=True)
                        st.write(f"**挂牌总价：** {detail['total_price']} 万")
                        st.write(f"**建筑面积：** {detail['area']} ㎡")
                        st.write(f"**单价：** {detail['unit_price']} 万/㎡")
                        st.write(f"**产权剩余年限：** {detail.get('property_rights_years', 'N/A')} 年")
                        st.write(f"**物业信息：** {detail.get('property_management', 'N/A')}")
                        st.write(f"**停车情况：** {detail.get('parking_info', 'N/A')}")


                    with top_right:

                        st.markdown('<div class="detail-box-title">⭐ 综合结论</div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="score-badge">{int(detail["score"])} 分</div>', unsafe_allow_html=True)
                        st.write("")
                        st.markdown(f'<div class="status-chip">{style_status_text(detail["status"])}</div>',
                                    unsafe_allow_html=True)


                    d1, d2 = st.columns(2)
                    with d1:

                        st.markdown('<div class="detail-box-title">📜 产权与交易</div>', unsafe_allow_html=True)
                        st.write(f"**满五唯一：** {detail['is_full5_unique']}")
                        st.write(f"**抵押情况：** {detail['has_mortgage']}")
                        st.write(f"**学区占用：** {detail['school_quota']}")
                        st.write(f"**装修情况：** {detail['decoration']}")
                        st.write(f"**土地性质：** {detail.get('land_grant_type', 'N/A')}")
                        st.write(f"**土地用途：** {detail.get('land_usage_type', 'N/A')}")
                        st.write(f"**查封/纠纷：** {detail.get('seizure_dispute', 'N/A')}")
                        st.write(f"**产权人情况：** {detail.get('co_owners', 'N/A')}")
                        st.write(f"**户口迁出安排：** {detail.get('hukou_migration', 'N/A')}")


                    with d2:

                        st.markdown('<div class="detail-box-title">🔍 房屋细节</div>', unsafe_allow_html=True)
                        st.write(f"**房东出售原因：** {detail.get('landlord_reason', 'N/A')}")
                        st.write(f"**抵押详情：** {detail.get('mortgage_info', 'N/A')}")
                        st.write(f"**贷款备选方案：** {detail.get('loan_backup', 'N/A')}")
                        st.write(f"**居住权/租赁状态：** {detail.get('occupancy_status', 'N/A')}")
                        st.write(f"**质量问题：** {detail.get('quality_issues', 'N/A')}")
                        st.write(f"**装修材料：** {detail.get('decoration_materials', 'N/A')}")


                    e1, e2 = st.columns(2)
                    with e1:

                        st.markdown('<div class="detail-box-title">✅ 优点总结</div>', unsafe_allow_html=True)
                        st.write(detail['pros'])


                    with e2:

                        st.markdown('<div class="detail-box-title">❌ 缺点/风险总结</div>', unsafe_allow_html=True)
                        st.write(detail['cons'])


            st.download_button(
                label="📥 导出对比结果 CSV",
                data=df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig'),
                file_name='hefei_house_compare.csv',
                mime='text/csv',
                use_container_width=True
            )

        else:
            st.warning("暂无数据，请先去录入看房记录。")

    # ================= 数据管理 =================
    elif choice == "🗑️ 管理数据":
        render_page_header("🗑️ 数据管理", "全量查看、删除记录、辅助跳转编辑")
        df = get_all_houses()

        if not df.empty:
            render_section("📋 所有记录概览")
            df_manage = df[['id', 'community_name', 'view_date', 'district', 'total_price', 'status']].copy()
            df_manage["status"] = df_manage["status"].apply(style_status_text)

            st.dataframe(
                df_manage,
                use_container_width=True,
                height=320,
                hide_index=True
            )

            st.markdown("---")
            operation = st.radio("选择操作", ["🗑️ 删除记录", "✏️ 编辑记录"], horizontal=True)

            if operation == "🗑️ 删除记录":

                render_mini_title("删除房源")
                del_id = st.number_input("输入要删除的房源 ID", min_value=1, step=1)

                if del_id:
                    house_to_delete = get_house_by_id(del_id)
                    if house_to_delete is not None:
                        st.info(
                            f"🏠 将删除：**{house_to_delete['community_name']}** - {house_to_delete['layout']} - {house_to_delete['total_price']}万")
                    else:
                        st.error("❌ 该 ID 不存在")

                if st.button("确认删除", type="primary", use_container_width=True):
                    if get_house_by_id(del_id) is not None:
                        delete_house(del_id)
                        st.success(f"✅ ID 为 {del_id} 的记录已删除")
                        st.rerun()
                    else:
                        st.error("❌ 删除失败，ID 不存在")


            elif operation == "✏️ 编辑记录":

                st.info("💡 建议在「📋 查看录入信息」页面进行编辑，功能更完整")
                edit_id = st.number_input("输入要编辑的房源 ID", min_value=1, step=1)
                if st.button("跳转到编辑", use_container_width=True):
                    st.session_state['edit_target_id'] = edit_id
                    st.rerun()

        else:
            st.info("没有数据可管理。")


if __name__ == '__main__':
    main()