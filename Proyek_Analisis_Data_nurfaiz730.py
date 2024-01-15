import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('PROYEK ANALISIS DATA:bar_chart:') 

st.header('Pertanyaan Bisnis')
st.write("1. Kapan Puncak Waktu Penyewaan Sepeda?\n\n"
         "2. Bagaimana Korelasi Antara Kondisi Cuaca dan Jumlah Sepeda yang Disewa?")

st.header('Hasil Analisis dan Visualisasi')
st.write("1. Visualisasi Pertayaan Bisnis Pertama")
# URL GitHub
url_cleaned_hourly_data = "https://raw.githubusercontent.com/nurfaiz730/Proyek_Analisis_Data/main/cleaned_hourly_data.csv"

# Load data dari GitHub
data = pd.read_csv(url_cleaned_hourly_data)

# Visualisasi tren mingguan
weekly_trend = data.groupby('weekday')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='weekday', y='cnt', data=weekly_trend, marker='o', ax=ax)
plt.title('Tren Rata-rata Jumlah Sepeda Disewa per Hari dalam Seminggu')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Jumlah Rata-rata Sepeda Disewa')

# Menampilkan plot menggunakan st.pyplot()
st.pyplot(fig)

# Visualisasi tren bulanan
monthly_trend = data.groupby('mnth')['cnt'].mean().reset_index()
fig_monthly, ax_monthly = plt.subplots(figsize=(12, 6))
sns.lineplot(x='mnth', y='cnt', data=monthly_trend, marker='o', ax=ax_monthly)
plt.title('Tren Rata-rata Jumlah Sepeda Disewa per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Rata-rata Sepeda Disewa')

# Menampilkan plot menggunakan st.pyplot(fig)
st.pyplot(fig_monthly)

st.write("2. Visualisasi Pertayaan Bisnis Kedua")
# URL GitHub
url_cleaned_hourly_data = "https://raw.githubusercontent.com/nurfaiz730/Proyek_Analisis_Data/main/cleaned_hourly_data.csv"

# Load data dari GitHub
data = pd.read_csv(url_cleaned_hourly_data)

# Konversi tipe data weather_category menjadi kategori
data['weathersit'] = data['weathersit'].astype('category')

# Visualisasi korelasi antara suhu, kelembapan, dan jumlah sepeda yang disewa dengan hue berdasarkan kondisi cuaca
fig_corr, ax_corr = plt.subplots(figsize=(14, 8))
sns.scatterplot(data=data, x='temp', y='cnt', hue='weathersit', palette='viridis', size='hum', sizes=(20, 200), ax=ax_corr)
plt.title('Korelasi Antara Suhu, Kondisi Cuaca, dan Jumlah Sepeda Disewa')
plt.xlabel('Suhu Normalisasi')
plt.ylabel('Jumlah Sepeda Disewa Normalisasi')
plt.legend(title='Kondisi Cuaca')

# Menampilkan plot menggunakan st.pyplot(fig_corr)
st.pyplot(fig_corr)


# Link Google Drive yang diberikan
google_drive_link = "https://drive.google.com/file/d/1Ni2O606EU-OZMMgEHYZ3_t4xILzRNErV/view?usp=drive_link"

# Dapatkan ID file dari link
file_id_start = google_drive_link.find("/file/d/") + len("/file/d/")
file_id_end = google_drive_link.find("/view", file_id_start)
google_drive_file_id = google_drive_link[file_id_start:file_id_end]

# Ubah ID file menjadi URL yang dapat diakses langsung
direct_url = f"https://drive.google.com/uc?id={google_drive_file_id}"

# Tampilkan gambar di Sidebar Streamlit
with st.sidebar:
    st.image(direct_url, caption="Google Drive Image", use_column_width=True)
    st.header('Mokhamad Nur Faizin')
    st.subheader('ID Dicoding : nurfaiz730')



st.caption('Copyright (Mokhamad Nur Faizin) 2023')