#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from PIL import Image
from pathlib import Path
import time
import random

st.set_page_config(
    page_title="❤️ Will You Be My Girlfriend?",
    page_icon="💖",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(180deg,#fff0f6,#ffe4ec,#fff7fb);
}

h1,h2,h3,p{
    text-align:center;
}

.title{
    font-size:42px;
    color:#ff4d88;
    font-weight:bold;
}

.subtitle{
    font-size:20px;
    color:#666;
    margin-bottom:20px;
}

.card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 5px 18px rgba(0,0,0,.12);
    margin-bottom:25px;
}

img{
    border-radius:20px;
}

.stButton>button{
    width:100%;
    border-radius:30px;
    background:#ff4d88;
    color:white;
    font-size:18px;
    border:none;
    padding:12px;
}

.stButton>button:hover{
    background:#ff6ea8;
    color:white;
}

.footer{
    text-align:center;
    font-size:30px;
    color:#ff4d88;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------

st.markdown(
"""
<div class="title" style="text-align:center;">
❤️ ถึงน้องแตงโมที่รัก ❤️
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="subtitle" style="text-align:center;">
สาวแว่นที่สวย เก่ง ฉลาด น่ารัก สดใส
รักสัตว์ ขยัน อดทน กินเผ็ดมากกกก 🌶️

เค้ามีบางอย่างอยากบอกเธอมานานแล้ว...
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------- Gallery ----------------

st.subheader("📸 ความทรงจำของเรา")

image_folder = Path("images")

images = [
    "1.jpg",
    "2.jpg",
    "3.jpg",
    "4.jpg",
    "5.jpg",
    "6.jpg",
    "7.jpg",
    "10.jpg",
    "9.jpg",
    "8.jpg"
]

for file in images:
    img = Image.open(image_folder / file)
    st.image(
        img,
        use_container_width=True
    )

st.divider()

# ---------------- Message ----------------

message = """
ตั้งแต่วันที่เราได้รู้จักกัน

ทุกช่วงเวลาที่ได้คุย ได้เจอ ได้หัวเราะด้วยกัน

มันกลายเป็นความทรงจำที่มีค่ามากสำหรับเรา

เธอทำให้วันธรรมดา ๆ ของเราพิเศษขึ้นเสมอ

และวันนี้...

เราอยากบอกความรู้สึกที่อยู่ในใจมานานแล้ว ❤️
"""

st.markdown(
f"""
<div class="card" style="text-align:center;font-size:20px;line-height:2;">
{message.replace(chr(10),"<br>")}
</div>
""",
unsafe_allow_html=True
)

st.subheader("💌 ข้อความถึงหวานจุย อิอิ")

if st.button("กดเพื่ออ่านข้อความลับ ❤️"):
    with st.spinner("กำลังเปิดหัวใจ..."):
        time.sleep(2)

    st.success("""
❤️ เราชอบเธอนะ ❤️

ขอบคุณที่เข้ามาเป็นรอยยิ้มในทุกวัน

ไม่รู้ว่าอนาคตจะเป็นยังไง

แต่เราอยากมีเธออยู่ในทุกช่วงเวลาต่อจากนี้

😊💖
""")

st.divider()

# ---------------- คำถามสำคัญ ----------------

question_img = Image.open("images/99.jpg")
st.image(question_img, use_container_width=True)

st.markdown(
    """
    <div class="card" style="text-align:center;">
        <h2>🌹 มีข้อความสำคัญจะบอก อิอิ</h2>
        <p style="font-size:20px;">
        คิดดี ๆ นะ 😆<br>
        มีตัวประกันอยู่ที่บ้านแล้วนะ อิอิ ❤️
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("💖 เป็นแฟนกันนะคะ")

col1, col2 = st.columns(2)

with col1:
    yes = st.button("ตกลง ❤️")

with col2:
    no = st.button("<<<< 😆")

if yes:
    st.balloons()

    st.success("""
🎉 เย้!!! ❤️❤️❤️

ตั้งแต่วินาทีนี้เป็นต้นไป

ขอให้เราได้ดูแลเธอนะ

จะคอยอยู่ข้าง ๆ

คอยเป็นกำลังใจ

คอยทำให้เธอยิ้ม

และรักเธอให้มากขึ้นทุกวัน ❤️
""")

    st.markdown(
        """
        <div class="card" style="text-align:center;">
        <h2>🥹 ขอบคุณนะ</h2>
        <p style="font-size:20px;">
        ขอบคุณที่ตอบตกลง<br><br>

        ต่อจากนี้...<br>

        ขอให้ทุกวันของเรา<br>

        เต็มไปด้วยรอยยิ้ม ความสุข<br>

        และความทรงจำดี ๆ ด้วยกันนะ ❤️
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

if no:

    texts = [

        "แน่ใจนะ 🥺",

        "ลองคิดอีกทีได้ไหม ❤️",

        "กดผิดหรือเปล่า 🤭",

        "ฟ้าจะผ่าาาาาาาา เปรี้ยงงงงงงง ⚡",

        "โกปิ๊กับโนชกำลังเดินไปหาแล้ว 🐶",

        "ปุ่มนี้ไม่ค่อยแนะนำให้กดนะ 😂",

        "เอาใหม่ ๆ ยังมีโอกาส ❤️",

        "ขอให้ลองอ่านใหม่อีกรอบน้า 🥹",

        "ตอบใหม่ได้ไหม เค้าตื่นเต้น 🥺"
    ]

    st.warning(random.choice(texts))

st.divider()

# ---------------- ถ้าตอบตกลง ----------------
st.write("")
st.markdown("## 💕 ความทรงจำบทใหม่ของเรา 💕")
question_img = Image.open("images/say_yes1.jpg")
st.image(question_img, use_container_width=True)

st.markdown(
    """
    <div class="card" style="text-align:center;">
        <h2 style="color:#ff4d88;">She said YESSSSSSSS! ❤️</h2>
        <p style="font-size:20px; line-height:1.8;">
            จากวันนี้...<br>
            ขอให้เราได้สร้างความทรงจำดี ๆ ด้วยกันอีกเยอะ ๆ<br><br>

            ขอบคุณที่เข้ามาในชีวิตของเรา
            และขอบคุณที่ทำให้ทุกวันมีความหมาย ❤️
            
    </div>
    """,
    unsafe_allow_html=True
)

st.snow()
st.markdown("❤️ 💖 💕 💗 💞 💓")

st.write("")

st.markdown(
"""
<div class="footer">
❤️ ❤️ ❤️ ❤️ ❤️
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div style="text-align:center;
font-size:22px;
color:#ff4d88;
font-weight:bold;
margin-top:15px;">
❤️ 30 / 06 / 2026 ❤️
</div>
""",
unsafe_allow_html=True
)

st.write("")
st.caption("Made with ❤️ by Someone who loves Tangmo")


# In[ ]:




