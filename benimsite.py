import streamlit as st
from PIL import Image
import os

# Sayfa ayarları
st.set_page_config(page_title="Özlemciğime 💖", page_icon="💌")


st.title("Bitanecik yıldıızım🌟💫")
st.write("benim aşkım yaparda ben altında kalır mıyım:PP")

st.markdown("---")

# 1. BÖLÜM: FOTOĞRAF EKLEME
st.header("TATLIŞ BİR FOTO SALDIRISI")

# Python'a dosyanın tam olarak nerede olduğunu zorla bulduruyoruz
klasor_yolu = os.path.dirname(os.path.abspath(__file__))
foto_yolu = os.path.join(klasor_yolu, "foto.jpeg")

# try-except OLMADAN doğrudan açmayı deniyoruz
foto = Image.open(foto_yolu)
st.image(foto, caption="Yanımda kollarımda sen olduğun sürece hayattaki hiçbirşey beni üzemez canım sevgilim", use_container_width=True)
st.markdown("---")

# 2. BÖLÜM: SORULAR VE ETKİLEŞİM
st.header("Şimdi sorma sırası bende 😝😝")

# Birinci Soru (Çoktan seçmeli)
soru1 = st.radio(
    "Sence seni ne kadar seviyorum?",
    ("Sadece çok", "Dünyalar kadar", "Gökteki yıldızları izlemeyi sevdiğimden, evrendeki herşeyden daha fazla"),
    index=None # İlk başta hiçbir şıkkın seçili olmaması için
)

# Cevaba göre tepki verme (if/else mantığı)
if soru1 == "Gökteki yıldızları izlemeyi sevdiğimden, evrendeki herşeyden daha fazla":
    st.success("NAAASSSIDA BİLİYO KENDİNİ YERİM 🥰")
    st.balloons() # Ekrandan balonlar uçar
elif soru1 is not None:
    st.warning("aaaşşkım cevap belli yahu git değiştir :P")

# İkinci Soru (Yazı yazma alanı)
st.write("Peki sence en çok hangi huyunu seviyorum?")
cevap = st.text_input("Tahminini buraya yaz:")

if cevap:
    # Ne yazarsa yazsın güzel bir mesaj gösterelim
    st.write(f"'{cevap}' da her özelliğin gibi benim için çok eşsiz ama ben seninle ilgili herşeye çok hayranım sevgilim")