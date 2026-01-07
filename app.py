import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="Onko-Game: Kişiselleştirilmiş Oyun Reçetesi", page_icon="🎮")

# Başlık ve Giriş
st.title("Onko-Game: Oyunlaştırma Profil Analizi")
st.markdown("""
Bu uygulama, kemoterapi sürecindeki bireylerin **Oyunlaştırma Kullanıcı Tipleri Ölçeği (Hexad)** kullanılarak analiz edilmesini ve kişiye özel aktivite/oyun önerilmesini sağlar.
""")

st.divider()

# Yan Menü (Hasta Bilgileri)
with st.sidebar:
    st.header("Hasta Bilgileri")
    ad_soyad = st.text_input("Ad Soyad / Protokol No")
    yas = st.number_input("Yaş", min_value=18, max_value=100, step=1)
    cinsiyet = st.selectbox("Cinsiyet", ["Kadın", "Erkek", "Diğer"])
    
    st.info("Not: Bu veriler sisteme kaydedilmez, sadece anlık hesaplama içindir.")

# Ölçek Soruları (1-7 Likert)
st.subheader("Lütfen aşağıdaki ifadelere ne kadar katıldığınızı belirtiniz.")
st.caption("1: Kesinlikle Katılmıyorum ... 7: Tamamen Katılıyorum")

# Soruları Listeleyelim
questions = [
    "1. Başkalarına yeni durumlara uyum sağlamaları için yardım etmeyi severim.",
    "2. Yeni şeyler denemekten hoşlanırım.",
    "3. Başkalarının maddi-manevi iyi olması benim için önemlidir.",
    "4. Karşılığında kazanılacak bir ödül olduğunda rekabetten hoşlanırım.",
    "5. Bir topluluğun parçası olduğumu hissetmek benim için önemlidir.",
    "6. Bağımsız olmak benim için önemlidir.",
    "7. Ödül beni tatmin ediyorsa çaba gösteririm.",
    "8. Kendi yolumu izlemek benim için önemlidir.",
    "9. Grup aktivitelerinden hoşlanırım.",
    "10. Çoğunlukla merakımın beni yönlendirmesine izin veririm.",
    "11. Zorlukların üstesinden gelmekten hoşlanırım.",
    "12. Başkalarına yardım edebilirsem bu beni mutlu eder.",
    "13. Hayatımdaki mevcut durumumu sorgulamaktan hoşlanırım.",
    "14. Kurallara uymaktan hoşlanmam.",
    "15. Bir problemi çözmeden bırakmak beni rahatsız eder.",
    "16. Görevlerimi eksiksiz bir şekilde yerine getirmek benim için önemlidir.",
    "17. Bir takımın parçası olmaktan hoşlanırım.",
    "18. Kendimi asi biri olarak görürüm.",
    "19. Diğer insanlarla etkileşim içinde olmak benim için önemlidir.",
    "20. Bilgimi başkalarıyla paylaşmaktan hoşlanırım.",
    "21. Zor görevleri başarmayı severim.",
    "22. Ödüller benim için önemli bir motivasyon kaynağıdır."
]

answers = []

# Soruları Ekrana Basma Döngüsü
for i, q in enumerate(questions):
    val = st.slider(f"{q}", 1, 7, 4, key=i)
    answers.append(val)

# HESAPLAMA BUTONU
if st.button("Profili Analiz Et ve Oyun Öner"):
    
    # Skorları Hesapla (Python listeleri 0'dan başlar, o yüzden soru no - 1 yapıyoruz)
    # Philanthropist: 12, 1, 20, 3 (4 Madde)
    philanthropist_raw = answers[11] + answers[0] + answers[19] + answers[2]
    philanthropist_score = (philanthropist_raw / 28) * 100
    
    # Socialiser: 19, 17, 5, 9 (4 Madde)
    socialiser_raw = answers[18] + answers[16] + answers[4] + answers[8]
    socialiser_score = (socialiser_raw / 28) * 100
    
    # Free Spirit: 8, 2, 10, 6 (4 Madde)
    freespirit_raw = answers[7] + answers[1] + answers[9] + answers[5]
    freespirit_score = (freespirit_raw / 28) * 100
    
    # Achiever: 11, 16, 15, 21 (4 Madde)
    achiever_raw = answers[10] + answers[15] + answers[14] + answers[20]
    achiever_score = (achiever_raw / 28) * 100
    
    # Disruptor: 13, 18, 14 (3 Madde -> 21 Puan üzerinden)
    disruptor_raw = answers[12] + answers[17] + answers[13]
    disruptor_score = (disruptor_raw / 21) * 100
    
    # Player: 4, 7, 22 (3 Madde -> 21 Puan üzerinden)
    player_raw = answers[3] + answers[6] + answers[21]
    player_score = (player_raw / 21) * 100
    
    # Sonuçları Sözlük Yapısına Al
    scores = {
        "Yardımsever (Philanthropist)": philanthropist_score,
        "Sosyalleşen (Socialiser)": socialiser_score,
        "Özgür Ruh (Free Spirit)": freespirit_score,
        "Başarı Odaklı (Achiever)": achiever_score,
        "Sorgulayan (Disruptor)": disruptor_score,
        "Oyuncu (Player)": player_score
    }
    
    # En yüksek puanı bul
    best_profile = max(scores, key=scores.get)
    max_score = scores[best_profile]
    
    st.divider()
    st.success(f"Analiz Tamamlandı! Baskın Profiliniz: **{best_profile}** (Puan: {max_score:.1f})")
    
    # Profil Detayı ve Grafik
    st.write("Profil Dağılımınız:")
    st.bar_chart(pd.DataFrame.from_dict(scores, orient='index', columns=['Puan']))
    
    # OYUN REÇETESİ MANTIĞI
    st.header(f"💊 Sizin İçin Oyun Reçetesi: {best_profile}")
    
    if "Yardımsever" in best_profile:
        st.info("**Önerilen Oyun Türleri:** Takım oyunları, kelime bulmacaları, hikayeli oyunlar.")
        st.markdown("""
        * 📱 **Wordscapes** (Kelime Bulmaca - Sakinleştirici)
        * 📱 **Hay Day** (Yardımlaşma ve Çiftlik)
        * 📱 **Terra Nil** (Doğayı iyileştirme oyunu)
        """)
        
    elif "Sosyalleşen" in best_profile:
        st.info("**Önerilen Oyun Türleri:** Çok oyunculu, sohbet imkanı olan veya yanınızdakiyle oynayabileceğiniz oyunlar.")
        st.markdown("""
        * 📱 **Uno!** (Online veya arkadaşlarla)
        * 📱 **Tabu / Kelime Anlat** (Refakatçinizle oynayın)
        * 📱 **Among Us** (Sosyal çıkarım oyunu)
        """)
        
    elif "Özgür Ruh" in best_profile:
        st.info("**Önerilen Oyun Türleri:** Keşif, yaratıcılık, açık dünya, boyama.")
        st.markdown("""
        * 📱 **Minecraft (Yaratıcı Mod)** (İnşa et ve gez)
        * 📱 **Monument Valley** (Görsel keşif - *Ücretli ama önerilir*)
        * 📱 **Sky: Children of the Light** (Görsel şölen ve uçma hissi)
        * 📱 **Happy Color** (Sayılarla Boyama)
        """)
        
    elif "Başarı Odaklı" in best_profile:
        st.info("**Önerilen Oyun Türleri:** Level atlamalı, beceri gerektiren, net hedefleri olan oyunlar.")
        st.markdown("""
        * 📱 **Candy Crush Saga** (Bölüm geçme hazzı)
        * 📱 **2048** (Mantık ve skor)
        * 📱 **Brain Training (Lumosity vb.)** (Zihin egzersizi)
        """)
        
    elif "Sorgulayan" in best_profile:
        st.info("**Önerilen Oyun Türleri:** Strateji, savaş, düzeni değiştirme.")
        st.markdown("""
        * 📱 **Angry Birds** (Yıkım fiziği)
        * 📱 **Plague Inc.** (Strateji simülasyonu)
        * 📱 **Clash of Clans** (Kendi köyünü koruma)
        """)
        
    elif "Oyuncu" in best_profile:
        st.info("**Önerilen Oyun Türleri:** Puan toplama, ödül avcılığı, rekor kırma.")
        st.markdown("""
        * 📱 **Subway Surfers** (Sonsuz koşu ve altın toplama)
        * 📱 **Fruit Ninja** (Refleks ve puan)
        * 📱 **Temple Run**
        """)

    st.warning("Lütfen tabletinizde yüklü olan yukarıdaki oyunlardan birini seçerek 30 dakika oynayınız.")
