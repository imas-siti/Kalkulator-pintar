import streamlit as st

st.title("💰 Kalkulator Cuan UMKM")

modal = st.number_input("Masukkan harga beli (modal utama)", min_value=0)
biaya_lain = st.number_input("Biaya tambahan (ongkir, listrik, dll)", min_value=0)
persentase_untung = st.slider("Target untung (%)", min_value=0, max_value=100, value=30)

total_modal = modal + biaya_lain
harga_jual = total_modal * (1 + persentase_untung / 100)
untung_bersih = harga_jual - total_modal

st.subheader("📊 Hasil Perhitungan:")
st.write(f"Total Modal: Rp{total_modal:,.0f}")
st.write(f"Harga Jual Disarankan: Rp{harga_jual:,.0f}")
st.write(f"Untung Bersih: Rp{untung_bersih:,.0f}")
