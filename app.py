import streamlit as st
import pandas as pd
from datetime import datetime

# Sayfa Ayarları
st.set_page_config(page_title="Onko-Game: Araştırma Sürümü", page_icon="🔬", layout="centered")

# CSS Tasarım
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    div.stImage > img {
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- BAŞLIK ---
st.title("🔬 Onko-Game: Klinik Araştırma Modülü")
st.markdown("**Kemoterapi Hastaları İçin Oyunlaştırma Temelli Müdahale Sistemi**")

# --- SOL MENÜ: DETAYLI HASTA BİLGİLERİ ---
with st.sidebar:
    st.header("📋 Katılımcı Bilgileri")
    protokol_no = st.text_input("Protokol / Dosya No")
    
    col1, col2 = st.columns(2)
    with col1:
        yas = st.number_input("Yaş", 18, 90, 45)
    with col2:
        cinsiyet = st.selectbox("Cinsiyet", ["Kadın", "Erkek"])
    
    egitim = st.selectbox("Eğitim Durumu", ["İlköğretim", "Lise", "Üniversite", "Lisansüstü"])
    kemo_kur = st.number_input("Kaçıncı Kemoterapi Kürü?", 1, 20, 1)
    dominant_el = st.radio("Dominant El", ["Sağ", "Sol"])
    damar_yolu = st.radio("Damar Yolu Hangi Kolda?", ["Sağ", "Sol", "Port/Diğer"])
    
    st.divider()
    st.info(f"Tarih: {datetime.now().strftime('%d-%m-%Y')}")
    st.caption("Not: Bu form TÜBİTAK projesi veri toplama sürecinde kullanılacaktır.")

# --- BÖLÜM 1: ÖN DEĞERLENDİRME (PRE-TEST) ---
st.info("⬇️ Adım 1: Uygulama Öncesi Değerlendirme")
with st.expander("Görsel Analog Skalalar (VAS) - Açmak için Tıklayın", expanded=True):
    st.write("Lütfen şu anki hislerinizi 0 ile 10 arasında puanlayınız.")
    
    st.markdown("---")
    st.write("🥵 **Şu an ne kadar YORGUN hissediyorsunuz?**")
    vas_yorgunluk = st.slider("0: Hiç Yorgun Değilim ... 10: Çok Yorgunum", 0, 10, 5)
    
    st.markdown("---")
    st.write("😟 **Şu an ne kadar KAYGILI (Endişeli) hissediyorsunuz?**")
    vas_kaygi = st.slider("0: Hiç Kaygılı Değilim ... 10: Çok Kaygılıyım", 0, 10, 5)
    
    st.markdown("---")
    st.write("🤢 **Şu an MİDE BULANTINIZ var mı?**")
    vas_bulanti = st.slider("0: Yok ... 10: Çok Şiddetli", 0, 10, 0)

# --- BÖLÜM 2: OYUNCU TİPİ ANALİZİ ---
st.divider()
st.info("⬇️ Adım 2: Profil Belirleme ve Oyun Reçetesi")

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
with st.expander("📝 Hexad Ölçeği (22 Soru) - Açmak için Tıklayın", expanded=False):
    for i, q in enumerate(questions):
        val = st.slider(f"{q}", 1, 7, 4, key=i)
        answers.append(val)

# OYUN VERİTABANI
game_db = {
    "Yardımsever (Philanthropist)": [
        {"name": "Cats & Soup", "desc": "Sakinleştirici kedi bakımı.", "how_to": "Kedilerin çorba yapmasını izleyin, biriken altınlara tıklayarak onlara yeni kıyafetler alın.", "ot_note": "📉 Düşük Bilişsel Yük", "url": "https://play.google.com/store/search?q=cats+and+soup", "img": "https://placehold.co/300x200/4CAF50/ffffff.png?text=Cats+%26+Soup"},
        {"name": "My Oasis", "desc": "Kendi adanızı büyütün.", "how_to": "Ekrana her dokunduğunuzda puan kazanırsınız. Adanıza yeni hayvanlar ekleyin.", "ot_note": "🧘 Terapötik / Olumlama", "url": "https://play.google.com/store/search?q=my+oasis", "img": "https://placehold.co/300x200/8BC34A/ffffff.png?text=My+Oasis"},
        {"name": "Pocket Camp", "desc": "Kamp alanı kurun.", "how_to": "Hayvanların istedikleri meyve veya balıkları toplayıp onlara verin.", "ot_note": "😐 Sosyal İzolasyona Karşı", "url": "https://play.google.com/store/search?q=animal+crossing+pocket+camp", "img": "https://placehold.co/300x200/CDDC39/ffffff.png?text=Pocket+Camp"},
        {"name": "Good Pizza", "desc": "Pizza dükkanı işletin.", "how_to": "Müşteri ne istiyorsa hamurun üzerine sürükleyin, fırına verin.", "ot_note": "🖐️ İnce Motor Becerisi", "url": "https://play.google.com/store/search?q=good+pizza+great+pizza", "img": "https://placehold.co/300x200/FFEB3B/000000.png?text=Pizza+Shop"},
        {"name": "Penguin Isle", "desc": "Penguenleri izleyin.", "how_to": "Penguenlerin fotoğrafını çekin ve yaşam alanlarını genişletin.", "ot_note": "🎧 Duyusal Regülasyon", "url": "https://play.google.com/store/search?q=penguin+isle", "img": "https://placehold.co/300x200/03A9F4/ffffff.png?text=Penguins"}
    ],
    "Sosyalleşen (Socialiser)": [
        {"name": "Kızma Birader", "desc": "Klasik zar oyunu.", "how_to": "Sıranız gelince zarı atın ve piyonları merkeze götürün.", "ot_note": "🧠 Bilinen Aktivite", "url": "https://play.google.com/store/search?q=ludo+king", "img": "https://placehold.co/300x200/F44336/ffffff.png?text=Kizma+Birader"},
        {"name": "Kelime Gezmece", "desc": "Kelime bulmaca.", "how_to": "Parmağınızı harflerin üzerinde kaydırarak kelimeler oluşturun.", "ot_note": "🗣️ Refakatçi ile Oynanabilir", "url": "https://play.google.com/store/search?q=kelime+gezmece", "img": "https://placehold.co/300x200/E91E63/ffffff.png?text=Kelime+Gezmece"},
        {"name": "101 Okey Plus", "desc": "Geleneksel taş oyunu.", "how_to": "Istakanızdaki taşları aynı renk veya sıralı sayılar olacak şekilde dizin.", "ot_note": "🏠 Ev Ortamı Hissi", "url": "https://play.google.com/store/search?q=101+okey+plus", "img": "https://placehold.co/300x200/3F51B5/ffffff.png?text=101+Okey"},
        {"name": "Uno!", "desc": "Kart eşleştirme.", "how_to": "Ortadaki kartın rengi veya sayısı neyse, elinizdeki uygun kartı atın.", "ot_note": "😐 Orta Seviye Dikkat", "url": "https://play.google.com/store/search?q=uno", "img": "https://placehold.co/300x200/FFC107/000000.png?text=UNO"},
        {"name": "Draw Something", "desc": "Çizerek anlatma.", "how_to": "Verilen kelimeyi çizin, karşı tarafın tahmin etmesini bekleyin.", "ot_note": "✍️ Yaratıcı İletişim", "url": "https://play.google.com/store/search?q=draw+something", "img": "https://placehold.co/300x200/9C27B0/ffffff.png?text=Ciz+Bakalim"}
    ],
    "Özgür Ruh (Free Spirit)": [
        {"name": "Happy Color", "desc": "Sayılarla boyama.", "how_to": "Resimdeki numaralı alanlara tıklayıp uygun renkle boyayın.", "ot_note": "📉 Hata Yok / Saf Akış", "url": "https://play.google.com/store/search?q=happy+color", "img": "https://placehold.co/300x200/673AB7/ffffff.png?text=Happy+Color"},
        {"name": "Townscaper", "desc": "Kasaba kurma.", "how_to": "Ekrana dokunun, her dokunuşta otomatik bina oluşur.", "ot_note": "🧘 Hedefsiz Oyun", "url": "https://play.google.com/store/search?q=townscaper", "img": "https://placehold.co/300x200/00BCD4/ffffff.png?text=Townscaper"},
        {"name": "I Love Hue", "desc": "Renkleri sıralama.", "how_to": "Kare renkleri sürükleyerek tonlarına göre sıralayın.", "ot_note": "👀 Görsel Algı", "url": "https://play.google.com/store/search?q=i+love+hue", "img": "https://placehold.co/300x200/E040FB/ffffff.png?text=Renkler"},
        {"name": "Monument Valley", "desc": "Mimari gezi.", "how_to": "Karakterin yürümesi için yollara tıklayın, mimariyi çevirin.", "ot_note": "🌌 İmgelesel Kaçış", "url": "https://play.google.com/store/search?q=monument+valley", "img": "https://placehold.co/300x200/607D8B/ffffff.png?text=Monument"},
        {"name": "Tsuki Odyssey", "desc": "Tavşanın hayatı.", "how_to": "Tavşanınızın günlük hayatını izleyin ve evini dekore edin.", "ot_note": "📉 Çok Düşük Efor", "url": "https://play.google.com/store/search?q=tsuki+odyssey", "img": "https://placehold.co/300x200/795548/ffffff.png?text=Tsuki"}
    ],
    "Başarı Odaklı (Achiever)": [
        {"name": "Candy Crush", "desc": "Şeker eşleştirme.", "how_to": "Aynı renk şekerleri yan yana getirmek için kaydırın.", "ot_note": "🍬 Anlık Ödül Sistemi", "url": "https://play.google.com/store/search?q=candy+crush", "img": "https://placehold.co/300x200/E91E63/ffffff.png?text=Candy+Crush"},
        {"name": "Woodoku", "desc": "Blok yerleştirme.", "how_to": "Ahşap blokları boş kutulara sürükleyin, satırları doldurun.", "ot_note": "🧠 Planlama", "url": "https://play.google.com/store/search?q=woodoku", "img": "https://placehold.co/300x200/795548/ffffff.png?text=Woodoku"},
        {"name": "2048", "desc": "Sayı birleştirme.", "how_to": "Aynı sayıları çarpıştırarak büyütün (2+2=4).", "ot_note": "🧠 Matematiksel Muhakeme", "url": "https://play.google.com/store/search?q=2048", "img": "https://placehold.co/300x200/FFC107/ffffff.png?text=2048"},
        {"name": "Brain Test", "desc": "Zeka soruları.", "how_to": "Ekrandaki nesneleri hareket ettirerek cevabı bulun.", "ot_note": "🧠 Bilişsel Egzersiz", "url": "https://play.google.com/store/search?q=brain+test", "img": "https://placehold.co/300x200/2196F3/ffffff.png?text=Brain+Test"},
        {"name": "Wordscapes", "desc": "Kelime türetme.", "how_to": "Harfleri birleştirerek kelimeleri bulun.", "ot_note": "📚 Kelime Hafızası", "url": "https://play.google.com/store/search?q=wordscapes", "img": "https://placehold.co/300x200/4CAF50/ffffff.png?text=Wordscapes"}
    ],
    "Sorgulayan (Disruptor)": [
        {"name": "Angry Birds 2", "desc": "Sapanla yıkım.", "how_to": "Kuşu sapanla fırlatıp kuleleri yıkın.", "ot_note": "🏹 Deşarj Olma", "url": "https://play.google.com/store/search?q=angry+birds+2", "img": "https://placehold.co/300x200/F44336/ffffff.png?text=Angry+Birds"},
        {"name": "Cut the Rope", "desc": "İp kesmece.", "how_to": "İpleri keserek şekeri canavarın ağzına düşürün.", "ot_note": "✂️ Neden-Sonuç İlişkisi", "url": "https://play.google.com/store/search?q=cut+the+rope", "img": "https://placehold.co/300x200/8BC34A/ffffff.png?text=Cut+The+Rope"},
        {"name": "Smash Hit", "desc": "Cam kırma.", "how_to": "İlerlerken cam engellere bilye fırlatıp kırın.", "ot_note": "💥 Stres Atma", "url": "https://play.google.com/store/search?q=smash+hit", "img": "https://placehold.co/300x200/607D8B/ffffff.png?text=Smash+Hit"},
        {"name": "Bad Piggies", "desc": "Araç yapımı.", "how_to": "Parçaları birleştirerek araç yapın ve hedefe ulaşın.", "ot_note": "🛠️ Yaratıcı Problem Çözme", "url": "https://play.google.com/store/search?q=bad+piggies", "img": "https://placehold.co/300x200/4CAF50/ffffff.png?text=Bad+Piggies"},
        {"name": "World of Goo", "desc": "Köprü kurma.", "how_to": "Topları birbirine ekleyerek köprü oluşturun.", "ot_note": "🏗️ Fizik Kuralları", "url": "https://play.google.com/store/search?q=world+of+goo", "img": "https://placehold.co/300x200/212121/ffffff.png?text=World+of+Goo"}
    ],
    "Oyuncu (Player)": [
        {"name": "Subway Surfers", "desc": "Sonsuz koşu.", "how_to": "Sağa-sola kaydırarak engellerden kaçın ve altın toplayın.", "ot_note": "⚡ Dikkat: Hızlı Refleks", "url": "https://play.google.com/store/search?q=subway+surfers", "img": "https://placehold.co/300x200/03A9F4/ffffff.png?text=Subway"},
        {"name": "Fruit Ninja", "desc": "Meyve kesme.", "how_to": "Ekrana gelen meyveleri parmağınızla kesin.", "ot_note": "🖐️ Hızlı Tatmin", "url": "https://play.google.com/store/search?q=fruit+ninja", "img": "https://placehold.co/300x200/8BC34A/ffffff.png?text=Fruit+Ninja"},
        {"name": "Coin Master", "desc": "Çark çevirme.", "how_to": "Butona basarak çarkı çevirin ve köyünüzü geliştirin.", "ot_note": "📉 Şans Faktörü", "url": "https://play.google.com/store/search?q=coin+master", "img": "https://placehold.co/300x200/FFC107/ffffff.png?text=Coin+Master"},
        {"name": "Bubble Shooter", "desc": "Balon patlatma.", "how_to": "Aynı renk topları vurup patlatın.", "ot_note": "👀 Görsel Takip", "url": "https://play.google.com/store/search?q=bubble+shooter", "img": "https://placehold.co/300x200/E91E63/ffffff.png?text=Bubble"},
        {"name": "Temple Run 2", "desc": "Tapınaktan kaçış.", "how_to": "Engellerden kaçmak için zıplayın veya kayın.", "ot_note": "⚡ Odaklanma", "url": "https://play.google.com/store/search?q=temple+run+2", "img": "https://placehold.co/300x200/795548/ffffff.png?text=Temple+Run"}
    ]
}

# --- BUTON VE HESAPLAMA ---
if st.button("🚀 ANALİZİ BAŞLAT VE OYUN ÖNER"):
    
    # Hesaplama
    philanthropist_score = ((answers[11] + answers[0] + answers[19] + answers[2]) / 28) * 100
    socialiser_score = ((answers[18] + answers[16] + answers[4] + answers[8]) / 28) * 100
    freespirit_score = ((answers[7] + answers[1] + answers[9] + answers[5]) / 28) * 100
    achiever_score = ((answers[10] + answers[15] + answers[14] + answers[20]) / 28) * 100
    disruptor_score = ((answers[12] + answers[17] + answers[13]) / 21) * 100
    player_score = ((answers[3] + answers[6] + answers[21]) / 21) * 100
    
    scores = {
        "Yardımsever (Philanthropist)": philanthropist_score,
        "Sosyalleşen (Socialiser)": socialiser_score,
        "Özgür Ruh (Free Spirit)": freespirit_score,
        "Başarı Odaklı (Achiever)": achiever_score,
        "Sorgulayan (Disruptor)": disruptor_score,
        "Oyuncu (Player)": player_score
    }
    
    best_profile = max(scores, key=scores.get)
    
    # --- SONUÇ ALANI ---
    st.divider()
    st.success(f"Analiz Tamamlandı! Baskın Profil: **{best_profile}**")
    
    # Grafik
    st.bar_chart(pd.DataFrame.from_dict(scores, orient='index', columns=['Puan']))
    
    # OYUN LİSTESİ
    st.header(f"💊 Önerilen Oyun Reçetesi")
    st.info("Hastanın tabletinde aşağıdaki oyunlardan biri açılacaktır.")
    
    games_to_show = game_db.get(best_profile, [])
    cols = st.columns(2)
    
    for i, game in enumerate(games_to_show):
        with cols[i % 2]:
            st.image(game["img"], use_container_width=True)
            st.subheader(game["name"])
            st.caption(game["desc"])
            with st.expander("❓ Nasıl Oynanır?"):
                st.write(game["how_to"])
            st.warning(f"OT Notu: {game['ot_note']}")
            st.link_button(f"▶ {game['name']} Oyna", game["url"])
            st.divider()

    # --- BÖLÜM 3: SON DEĞERLENDİRME (POST-TEST) ---
    st.markdown("---")
    st.info("⬇️ Adım 3: Uygulama Sonrası Değerlendirme (Oyun Bittikten Sonra Doldurulacak)")
    
    with st.container():
        st.write("⏱️ **Zaman Algısı:**")
        tahmin_sure = st.number_input("Sizce ne kadar süredir oynuyorsunuz? (Dakika)", 0, 120, 0)
        
        st.write("🌊 **Akış (Flow) Deneyimi:**")
        akıs_puan = st.slider("Oyuna kendimi ne kadar kaptırdım? (0: Hiç - 10: Tamamen)", 0, 10, 5)
        
        st.write("😟 **Şu anki Kaygı Seviyesi (Son-Test):**")
        vas_kaygi_son = st.slider("0: Hiç Kaygılı Değilim ... 10: Çok Kaygılıyım", 0, 10, 5, key="vas_son")
        
        if st.button("💾 Verileri Kaydet (Demo)"):
            st.toast("Veriler başarıyla sisteme işlendi!", icon="✅")
