import streamlit as st

st.set_page_config(page_title=" คำนวณเลขง่ายๆ",  layout="centered")

a = float(input("กรอกตัวเลขแรก: "))
b = float(input("กรอกตัวเลขที่สอง: "))

print("ผลบวก:", a + b)
print("ผลลบ:", a - b)
print("ผลคูณ:", a * b)
print("ผลหาร:", a / b)
