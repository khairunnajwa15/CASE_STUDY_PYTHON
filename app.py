import streamlit as st

from fms import (
    Food,
    find_food,
    add_food,
    search_food,
    calculate_total_price,
    place_order,
    calculate_total_available
)

from fcos import food_court


st.set_page_config(
    page_title="Food Management System",
    page_icon="🍔"
)


if "food_list" not in st.session_state:

    st.session_state.food_list = [
        Food("F001", "Nasi Lemak", 5.00, 20),
        Food("F002", "Nasi Goreng", 7.00, 15),
        Food("F003", "Mee Goreng", 6.00, 18),
        Food("F004", "Chicken Chop", 12.00, 10),
        Food("F005", "Burger", 8.00, 12)
    ]


st.sidebar.title("Food Management System")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Add Food",
        "View Food",
        "Search Food",
        "Place Order",
        "Food Court",
        "About"
    ]
)


# ADD FOOD
if menu == "Add Food":

    st.title("Add Food")

    food_id = st.text_input("Food ID")
    food_name = st.text_input("Food Name")
    price = st.text_input("Price")
    quantity = st.text_input("Quantity")

    if st.button("Add Food"):

        try:

            if food_id == "":
                st.error("Food ID cannot be empty.")

            elif food_name == "":
                st.error("Food Name cannot be empty.")

            elif price == "":
                st.error("Price cannot be empty.")

            elif quantity == "":
                st.error("Quantity cannot be empty.")

            else:

                price = float(price)
                quantity = int(quantity)

                if price <= 0:
                    st.error("Invalid price.")

                elif quantity < 0:
                    st.error("Invalid quantity.")

                else:

                    food = Food(
                        food_id,
                        food_name,
                        price,
                        quantity
                    )

                    if add_food(st.session_state.food_list, food):
                        st.success("Food added successfully!")
                    else:
                        st.error("Duplicate Food ID.")

        except ValueError:
            st.error("Price must be a number and quantity must be an integer.")

        except Exception as e:
            st.error(f"Error: {e}")


# VIEW FOOD
elif menu == "View Food":

    st.title("View Food")

    if len(st.session_state.food_list) == 0:

        st.error("No food available.")

    else:

        for food in st.session_state.food_list:
            st.write(str(food))

        total = calculate_total_available(
            st.session_state.food_list
        )

        st.info(f"Total Available Food: {total}")


# SEARCH FOOD
elif menu == "Search Food":

    st.title("Search Food")

    keyword = st.text_input("Enter food name:")

    if st.button("Search"):

        try:

            if keyword == "":
                st.error("Please enter food name.")

            else:

                result = search_food(
                    st.session_state.food_list,
                    keyword
                )

                if result:

                    for food in result:
                        st.write(str(food))

                else:
                    st.error("Food not found.")

        except Exception as e:
            st.error(f"Error: {e}")


# PLACE ORDER
elif menu == "Place Order":

    st.title("Place Order")

    food_id = st.text_input("Enter Food ID:")

    quantity = st.number_input(
        "Enter Order Quantity:",
        min_value=1,
        value=1
    )

    if st.button("Place Order"):

        try:

            food = find_food(
                st.session_state.food_list,
                food_id
            )

            if food is None:

                st.error("Food not found.")

            elif quantity <= 0:

                st.error("Invalid order quantity.")

            elif quantity > food.quantity:

                st.error("Insufficient stock.")

            else:

                total = calculate_total_price(
                    food,
                    quantity
                )

                place_order(
                    food,
                    quantity
                )

                st.success("Order placed successfully!")

                st.write(f"Food: {food.food_name}")
                st.write(f"Quantity: {quantity}")
                st.write(f"Total Price: RM {total:.2f}")
                st.write(f"Remaining Stock: {food.quantity}")

        except ValueError:
            st.error("Invalid quantity.")

        except Exception as e:
            st.error(f"Error: {e}")


# FOOD COURT
elif menu == "Food Court":

    food_court()


# ABOUT
elif menu == "About":

    st.title("About")

    st.write("Food Management System")
    st.write("Developed using Python and Streamlit.")
    st.write("This system is used to manage food and place orders.")
