import streamlit as st
import random

st.title("🍔 FastChain - Quick Food Order System")

menu = {
    "Burger": 5.99,
    "Fries": 2.99,
    "Soda": 1.49,
    "Pizza": 6.99
}

st.header("📋 Menu")
selected_items = []
total = 0

for item, price in menu.items():
    qty = st.number_input(f"{item} (${price})", min_value=0, step=1)
    if qty > 0:
        selected_items.append((item, qty, price * qty))
        total += price * qty

if st.button("Place Order"):
    st.subheader("🧾 Order Summary")
    for item, qty, subtotal in selected_items:
        st.write(f"{qty} x {item} - ${subtotal:.2f}")
    st.write(f"**Total: ${total:.2f}**")
    st.success(f"🎉 Order placed! Estimated delivery in {random.randint(10, 30)} mins")

