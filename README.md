#  Chatbot Baligooo – Asisten Wisata Bali

**Baligooo** adalah chatbot berbasis **Streamlit** dan **AI Google Gemini 2.5 Flash** yang berperan sebagai **asisten wisata virtual** untuk membantu pengguna menemukan **tempat wisata terbaik di Bali**.  
Chatbot ini dapat memberikan **rekomendasi destinasi, tips perjalanan, dan informasi lokasi** berdasarkan data wisata yang tersimpan di database lokal.

---

## Getting Started

###  Prerequisites
Pastikan Anda sudah menginstal **Python (versi 3.9 atau lebih baru)**.  
Disarankan untuk menggunakan **Miniconda** atau **Conda** agar lebih mudah dalam pengelolaan environment.

---

###  Installation

####  1. Install Miniconda (jika belum ada)
Unduh dan instal Miniconda dari situs resmi:  
[https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

---

####  2. Buat Environment Baru
Buka terminal atau Anaconda Prompt, lalu jalankan:
```bash
conda create -n baligooo-env python=3.9
conda activate baligooo-env

### Install Requirements
Arahkan ke direktori proyek dan instal paket yang diperlukan:
```bash
pip install -r requirements.txt
```
### Run the Streamlit Application
```bash
streamlit run chatbot.py

Aplikasi akan terbuka di web browser.

### Tampilan awal
![alt text](/awal.png)Tampilan awal 
Lakukan input pertanyaan.

### Percakapan dengan Baligooo
![alt text](/hasil.png)
Hasil akan memberikan rekomendasi yang user minta 
