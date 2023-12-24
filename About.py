import streamlit as st

st.set_page_config(
    page_title="About Us",
    page_icon="👋",
)


with st.container():
    st.subheader("Hi:wave:")
    st.title("Welcome to Easy Swap!")
    st.write("This is a free web-based currency converter designed to assist money changers in Bali to conduct transactions more effectively and efficiently. Our platform aims to simplify the currency exchange process, providing a convenient tool for seamless conversions. Whether for tourists or businesses, we strive to enhance the experience of exchanging currencies in Bali.")


with st.container():
    st.write("---")
    st.header("Why Us?")
    st.markdown("""
        - **Real-Time Currency Conversion**  
            We provide current and accurate currency exchange rates, enabling swift and precise transactions.

        - **Accessibility**  
            Our web-based tool allows users to access it from any location.

        - **Simplified Process**  
            Easy Swap aims to simplify the currency exchange process, making it more efficient and effective for our users.

        - **Simple and User-Friendly Interface**  
            Easy Swap boasts a simple and user-friendly interface. Its intuitive design allows users to quickly acclimate and utilize the tool seamlessly.
    """)