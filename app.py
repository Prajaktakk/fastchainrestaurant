import streamlit as st
import random
import datetime
import io

st.set_page_config(page_title="FastChain 🍔", layout="centered")

# Session initialization
if 'orders' not in st.session_state:
    st.session_state.orders = []

# Menu
menu = {
    "Burgers": {"Cheeseburger": 5.99, "Veg Burger": 4.99},
    "Sides": {"Fries": 2.99, "Nuggets": 3.99},
    "Drinks": {"Soda": 1.49, "Coffee": 2.49}
}

# UI
st.title("🍔 FastChain - Fast Food in a Click")
name = st.text_input("👤 Your Name:")
note = st.text_area("📝 Any notes for the kitchen?")

st.header("📋 Select Your Items")
selected_items = []
total = 0

for category, items in menu.items():
    with st.expander(category):
        for item, price in items.items():
            qty = st.number_input(f"{item} - ${price}", min_value=0, step=1, key=item)
            if qty > 0:
                selected_items.append((item, qty, price * qty))
                total += price * qty

# Order placement
if st.button("✅ Place Order"):
    if not name:
        st.warning("Please enter your name to place an order.")
    elif not selected_items:
        st.warning("Select at least one item.")
    else:
        delivery_time = random.randint(10, 30)
        order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order = {
            "name": name,
            "items": selected_items,
            "total": total,
            "note": note,
            "time": order_time,
            "eta": delivery_time
        }
        st.session_state.orders.append(order)

        # Show confirmation
        st.success(f"Order placed! ETA: {delivery_time} mins")
        st.subheader("🧾 Order Summary")
        for item, qty, subtotal in selected_items:
            st.write(f"{qty} x {item} - ${subtotal:.2f}")
        st.write(f"**Total: ${total:.2f}**")
        st.write(f"🕒 Ordered At: {order_time}")
        if note:
            st.write(f"📝 Note: {note}")

        # Generate downloadable receipt
        receipt_text = f"FastChain Receipt - {order_time}\nName: {name}\n"
        for item, qty, subtotal in selected_items:
            receipt_text += f"{qty} x {item} - ${subtotal:.2f}\n"
        receipt_text += f"\nTotal: ${total:.2f}\nETA: {delivery_time} mins\n"
        if note:
            receipt_text += f"Note: {note}\n"

        receipt_bytes = io.BytesIO()
        receipt_bytes.write(receipt_text.encode())
        receipt_bytes.seek(0)

        st.download_button("📄 Download Receipt", data=receipt_bytes, file_name="receipt.txt")

# Show session history
if st.checkbox("📜 View My Session Orders"):
    st.subheader("🧾 Session Order History")
    for order in st.session_state.orders:
        st.markdown(f"**{order['name']}** - {order['time']} - ${order['total']:.2f} (ETA: {order['eta']} mins)")

