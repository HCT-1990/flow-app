import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề app
st.title("App Cảnh Báo Lưu Lượng Nước")

# Nhập dữ liệu
st.header("Nhập lưu lượng nước (m³/h)")
current_flow = st.number_input("Lưu lượng hiện tại:", min_value=0.0, value=0.0, step=0.1)
threshold = st.number_input("Ngưỡng cảnh báo:", min_value=0.0, value=10.0, step=0.1)

# Kiểm tra cảnh báo
if current_flow > threshold:
    st.error(f"⚠️ CẢNH BÁO: Lưu lượng {current_flow} m³/h vượt ngưỡng {threshold} m³/h!")
else:
    st.success(f"Lưu lượng {current_flow} m³/h nằm trong giới hạn an toàn.")

# Lưu lịch sử vào DataFrame
if "history" not in st.session_state:
    st.session_state["history"] = pd.DataFrame(columns=["Lưu lượng", "Ngưỡng"])

if st.button("Lưu dữ liệu"):
    new_row = pd.DataFrame({"Lưu lượng": [current_flow], "Ngưỡng": [threshold]})
    st.session_state["history"] = pd.concat([st.session_state["history"], new_row], ignore_index=True)

# Hiển thị bảng lịch sử
st.subheader("Lịch sử nhập dữ liệu")
st.dataframe(st.session_state["history"])

# Vẽ biểu đồ
if not st.session_state["history"].empty:
    fig, ax = plt.subplots()
    ax.plot(st.session_state["history"]["Lưu lượng"], label="Lưu lượng")
    ax.plot(st.session_state["history"]["Ngưỡng"], label="Ngưỡng")
    ax.set_xlabel("Lần đo")
    ax.set_ylabel("m³/h")
    ax.legend()
    st.pyplot(fig)
