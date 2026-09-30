import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


food_menu = {
    "Nasi Lemak": 5.00,
    "Nasi Goreng": 7.00,
    "Mee Goreng": 6.00,
    "Chicken Chop": 12.00,
    "Burger": 8.00,
    "French Fries": 5.00,
    "Sandwich": 6.00,
    "Fried Chicken": 9.00,
    "Teh Ais": 3.00,
    "Milo Ais": 4.00
}


def food_court():
    st.title("Food Court Ordering System")

    st.write("Select your food and generate your receipt.")

    number = st.number_input(
        "Enter number of food items:",
        min_value=1,
        max_value=10,
        value=1
    )

    selections = []

    for i in range(int(number)):
        food = st.selectbox(
            f"Select Food {i + 1}:",
            list(food_menu.keys()),
            key=f"food_{i}"
        )

        quantity = st.number_input(
            f"Quantity for {food}:",
            min_value=1,
            value=1,
            key=f"quantity_{i}"
        )

        selections.append((food, quantity))

    if st.button("Generate Receipt"):

        if not selections:
            st.error("Please select food.")
            return

        data = []

        for food, quantity in selections:
            price = food_menu[food]
            total = price * quantity

            data.append({
                "Food": food,
                "Price": price,
                "Quantity": quantity,
                "Total": total
            })

        df = pd.DataFrame(data)

        st.subheader("Receipt")

        st.dataframe(df)

        total_price = df["Total"].sum()

        st.write(f"### Total Price: RM {total_price:.2f}")

        st.success("Order successfully generated!")


    st.subheader("Food Price Bar Chart")

    names = list(food_menu.keys())
    prices = list(food_menu.values())

    fig, ax = plt.subplots()

    ax.bar(names, prices)

    ax.set_title("Food Price Bar Chart")
    ax.set_xlabel("Food Name")
    ax.set_ylabel("Price (RM)")

    plt.xticks(rotation=45)

    for i, price in enumerate(prices):
        ax.text(i, price, f"RM{price:.2f}", ha="center", va="bottom")

    st.pyplot(fig)
