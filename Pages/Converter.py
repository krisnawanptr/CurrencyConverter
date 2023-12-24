import streamlit as st
import requests


st.set_page_config(
    page_title="Converter",
    page_icon="💸",
)

# Dictionary untuk setiap denominasi mata uang dalam converter
denominasi = {
    'IDR': [100000, 75000, 50000, 20000, 10000, 5000, 2000, 1000],
    'AUD': [100, 50, 20, 10, 5, 2, 1],
    'INR': [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1],
    'CNY': [100, 50, 20, 10, 5, 1],
    'EUR': [500, 200, 100, 50, 20, 10, 5, 2, 1],
    'GBP': [50, 20, 10, 5, 2, 1],
    'KRW': [10000, 5000, 1000, 500, 100, 50, 10],
    'USD': [100, 50, 20, 10, 5, 1],
    'MYR': [100, 50, 20, 10, 5, 1],
    'SGD': [1000, 500, 200, 100, 50, 10],
}

# API yang digunakan untuk melakukan conversion
url = 'http://data.fixer.io/api/latest?access_key=7b0b15a68a8eb25a3b6c64f107153f63'

# Fungsi untuk mengkonversi unng
def get_exchange_rate(from_currency, to_currency):
    response = requests.get(url)
    rates = response.json()['rates']
    return rates[to_currency] / rates[from_currency]

# Fungsi untuk pemberian uang dengan menerapkan algoritma greedy
def pemberian_uang(jumlah, denominasi):
    st.write(f"\nTo give a fraction of {jumlah} is required:")
    for denom in denominasi:
        if jumlah >= denom:
            jml_pecahan = jumlah // denom
            st.write(f"{jml_pecahan} Franction of {denom}")
            jumlah -= jml_pecahan * denom
    
    st.write(f"Non-Exchangeable: {jumlah}")

# Fungsi main untuk melakukan conversion
def main():
    st.header("Easy Swap Converter")

    currencies = ['IDR', 'AUD', 'INR', 'CNY', 'EUR', 'GDP', 'KRW', 'USD', 'MYR', 'SGD']

    to_currency = st.selectbox("Select Destination Currency:", currencies)
    if to_currency:
        st.write(f"Currency Destination: {to_currency}")
    
    from_currency = st.selectbox("Select Home Currency:", currencies)
    if from_currency:
        st.write(f"Home Destination: {from_currency}")

    if 'show_input' not in st.session_state:
        st.session_state.show_input = False

    input_money = st.button("Input Money")

    if input_money:
        st.session_state.show_input = True

    if st.session_state.show_input:
        jumlah_mata_uang = {}
        for denom in denominasi[from_currency]:
            jml = st.number_input(f"Number of Currency {denom}:", value=0, format='%d')
            if jml < 0:
                st.error(f"The currency amount of {denom} must be non-negative.")
                return
            jumlah_mata_uang[denom] = jml

            jumlah = 0
            for denom, jml in jumlah_mata_uang.items():
                jumlah += denom * jml

        convert = st.button("Convert")
        if convert:
            exchange_rate = get_exchange_rate(from_currency, to_currency)
            jumlah_in_target_currency = jumlah * exchange_rate
            profit = (jumlah_in_target_currency * 0.02)
            jumlah_in_target_currency = jumlah_in_target_currency - profit

            st.write(f"Amount in {to_currency}: {int(jumlah_in_target_currency)}")

            st.write(f"Profit: {int(profit)}")

            pemberian_uang(int(jumlah_in_target_currency), denominasi[to_currency])

            st.session_state.show_input = False


if __name__ == "__main__":
    main()