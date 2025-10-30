# app.py

import streamlit as st
import pandas as pd

# --- 0. Cài đặt và CSS Tùy chỉnh (ĐỊNH HÌNH UI) ---
st.set_page_config(
    page_title="Smart Move SG - Giao diện Chính",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Thêm CSS để mô phỏng giao diện Mobile, Card, và Header cố định
st.markdown("""
<style>
/* 1. Định hình khung App (Mobile View) */
.main .block-container {
    max-width: 420px; /* Chiều rộng hẹp */
    padding: 1rem 1rem 0 1rem;
}
section.main {
    background-color: #ffffff; /* Nền trắng */
}

/* 2. Ẩn Streamlit Header/Footer */
header { visibility: hidden; }
footer { visibility: hidden; }
.stDeployButton { visibility: hidden; }

/* 3. Tùy chỉnh màu sắc và bo góc cho Box Gợi ý (The Card) */
.stCardContainer {
    background-color: #f5f0fb; /* Màu nền Card (tím nhạt) */
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 20px;
}

/* 4. Định dạng Danh sách Lộ trình (Mô phỏng List Item) */
.route-item {
    display: flex;
    align-items: center;
    padding: 8px 0;
}
.route-number {
    background-color: #d1c4e9; /* Nền số thứ tự */
    color: #4B0082;
    font-weight: bold;
    border-radius: 50%;
    width: 25px;
    height: 25px;
    text-align: center;
    line-height: 25px;
    margin-right: 15px;
}
.route-name {
    flex-grow: 1;
    font-weight: 500;
}
.route-done {
    color: #5cb85c; /* Màu dấu tích xanh */
    font-size: 20px;
}
.route-pending {
    color: #cccccc; /* Màu ô vuông chưa tích */
    font-size: 20px;
}

/* 5. Giao diện Thanh Chat (Mô phỏng st.chat_input) */
div[data-testid="stChatInput"] {
    position: fixed;
    bottom: 0;
    width: 100%;
    max-width: 420px;
    left: 50%;
    transform: translateX(-50%);
    padding: 10px 10px;
    background-color: white;
    box-shadow: 0 -2px 5px rgba(0,0,0,0.05);
    z-index: 100;
    margin: 0;
}
.chat-placeholder {
    height: 70px; /* Tạo khoảng trống ở cuối trang cho thanh chat cố định */
}
</style>
""", unsafe_allow_html=True)


# --- 1. MÔ PHỎNG HEADER & NAVIGATION ---
# Dùng columns để đặt các icon/nút navigation
col_settings, col_nav, col_profile = st.columns([1, 4, 1])

with col_settings:
    st.markdown("⚙️", unsafe_allow_html=True) # Icon Cài đặt
with col_nav:
    st.markdown(
        f'<div style="text-align: center; font-size: 14px;">'
        f'<span style="padding: 5px 10px; border-radius: 15px; background-color: #e0e0e0;">Bot</span>'
        f'<span style="padding: 5px 10px; border-radius: 15px; color: #666;">Map</span>'
        f'</div>', 
        unsafe_allow_html=True
    )
with col_profile:
    st.markdown("👤", unsafe_allow_html=True) # Icon Profile

# --- 2. Vùng Giao diện Chính ---
st.markdown("---")
st.markdown("### Khi bạn cần một chuyến hành trình là lúc chúng tôi sẵn sàng.")


# --- 3. MÔ PHỎNG HỘP THÔNG TIN (THE CARD) ---
# Sử dụng st.container() và CSS để tạo box tím nhạt
with st.container(border=False):
    st.markdown('<div class="stCardContainer">', unsafe_allow_html=True)
    
    st.markdown(
        "**Lộ trình hôm nay**",
        unsafe_allow_html=True
    )
    st.markdown(
        "Chào bạn, dưới đây là lộ trình bạn đang chọn. Điểm đến tiếp theo là **Bưu điện Sài Gòn**. "
        "Thời tiết mát mẻ, tình hình giao thông thông thoáng. "
        "Chọn ngay xe bus 2 tầng để hóng gió đến bưu điện Sài Gòn liền thôi ❤️"
    )

    # Dữ liệu lộ trình (Mô phỏng List)
    route_data = [
        {"name": "Chợ Bến Thành", "done": True},
        {"name": "Khách sạn Caravelle", "done": True},
        {"name": "Bưu điện Sài Gòn", "done": False},
    ]

    for i, item in enumerate(route_data):
        icon = '☑️' if item['done'] else '⬜'
        color_class = 'route-done' if item['done'] else 'route-pending'
        
        st.markdown(
            f'<div class="route-item">'
            f'<span class="route-number">{i+1}</span>'
            f'<span class="route-name">{item["name"]}</span>'
            f'<span class="{color_class}">{icon}</span>'
            f'</div>',
            unsafe_allow_html=True
        )
    
    st.markdown('<p style="text-align: center; color: #8A2BE2; font-weight: 500; font-size: small;">Add more</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. MÔ PHỎNG KHU VỰC GỢI Ý CHATBOT ---
st.markdown("""
<p style="padding-left: 5px; margin-top: 15px; font-weight: 500;">
    Hãy cho tôi biết bạn muốn đi đâu? Tôi có thể gợi ý đường đi và phương tiện phù hợp với nhu cầu của bạn ^^
</p>
""", unsafe_allow_html=True)


# --- 5. MÔ PHỎNG THANH CHAT CỐ ĐỊNH (PHẢI DÙNG ST.CHAT_INPUT) ---
# Thêm khoảng trống để thanh chat cố định không che nội dung cuối
st.markdown('<div class="chat-placeholder"></div>', unsafe_allow_html=True)

# Lời nhắc cho thanh chat (Mô phỏng "Trò chuyện")
st.chat_input("Trò chuyện")

# --- MÔ PHỎNG CÁC NÚT TRUY VẤN NHANH (Right Screen) ---
# Đây là phần rất khó mô phỏng cùng lúc với màn hình chính,
# Chúng ta giả lập chúng xuất hiện khi nhấn vào nút 'Chat'
if st.sidebar.button("Mô phỏng Nút Truy vấn Nhanh"):
    st.markdown("## Truy vấn Nhanh (Mô phỏng Màn hình 2)")
    st.button("➕ Lộ trình hôm nay")
    st.button("➕ Tuyến đường")
    st.button("➕ Phương tiện")