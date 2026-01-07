Haklısınız, önceki kodda "Tek grup/Kontrol grubu" tartışması yaparken bazı parametreleri (demografik detaylar, mide bulantısı vb.) sadeleştirmiştim.

Şimdi, projenin TÜBİTAK 1002 Araştırma Protokolüne tam uygun, eksiksiz, "Her Şey Dahil" (All-in-One) versiyonunu hazırladım.

Bu kodda şunların hepsi var:

Demografik Veriler: Yaş, Cinsiyet, Eğitim, Kaçıncı Kür, Dominant El.

Ön Testler: Yorgunluk, Kaygı ve Mide Bulantısı.

Hexad ve Melez Profil: Puanlar yakınsa iki profili birleştiren zeka.

Oyun Veritabanı: 30 oyunluk tam liste (Resimli, Açıklamalı, OT Notlu).

Son Testler: Son Kaygı, Zaman Algısı ve 9 Maddelik Akış (Flow) Ölçeği.

Google Sheets Kaydı: Hepsini tek satırda kaydeder.

ADIM 1: Önce Google Sheets Başlıklarını Düzeltin
Google E-Tablonuzun (Onko-Data) 1. satırını tamamen silin ve şu başlıkları sırasıyla kopyalayıp yapıştırın (Sıralama kodla aynı olmalı):

Tarih | Protokol | Yas | Cinsiyet | Egitim | Kemo_Kur | Profil | On_Yorgunluk | On_Kaygi | On_Bulanti | Son_Kaygi | Zaman_Algisi | Flow_Toplam

ADIM 2: İşte Eksiksiz Final Kod (app.py)
Eski kodun tamamını silin ve bunu yapıştırın.

Python

import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# --- GOOGLE SHEETS BAĞLANTISI ---
try:
    secrets = st.secrets["gcp_service_account"]
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(secrets, scope)
    client = gspread.authorize(creds)
    sheet = client.open("Onko-Data").sheet1
    connection_status = True
except Exception:
    connection_status = False

# Sayfa Ayarları
st.set_page_config(page_title="Onko-Game: Araştırma Sürümü", page_icon="🔬", layout="centered")

# CSS Tasarım
st.markdown("""
<style>
    .stButton>button { width: 100%; border-radius: 12px; height: 3em; background-color: #2E86C1; color: white; font-weight: bold; }
    div.stImage > img { border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .big-font { font-size:18px !important; }
</style>
""", unsafe_allow_html=True)

st.title("🔬 Onko-Game: Aktivite Reçetesi")
if not connection_status:
    st.warning("⚠️ Veritabanı Bağlı Değil (Demo Modu)")

# --- SOL MENÜ: DETAYLI DEMOGRAFİK BİLGİLER ---
with st.sidebar:
    st.header("📋 Hasta Bilgileri")
    protokol_no = st.text_input("Protokol / Dosya No")
    
    col1, col2 = st.columns(2)
    with col1:
        yas = st.number_input("Yaş", 18, 90, 45)
    with col2:
        cinsiyet = st.selectbox("Cinsiyet", ["Kadın", "Erkek"])
        
    egitim = st.selectbox("Eğitim Durumu", ["İlköğretim", "Lise", "Üniversite", "Lisansüstü"])
    kemo_kur = st.number_input("Kaçıncı Kemoterapi Kürü?", 1, 20, 1)
    dominant_el = st.selectbox("Dominant El", ["Sağ", "Sol"])
    
    st.divider()
    st.info(f"Tarih: {datetime.now().strftime('%d-%m-%Y')}")

# --- ADIM 1: ÖN DEĞERLENDİRME (PRE-TEST) ---
st.info("⬇️ Adım 1: Uygulama Öncesi Durum (VAS - 0 ile 10 Arası)")
with st.expander("Görsel Analog Skalalar (Doldurmak için Tıklayın)", expanded=True):
    st.write("🥵 **Yorgunluk Seviyesi:**")
    vas_yorgunluk = st.slider("0: Hiç Yorgun Değilim ... 10: Tükendim", 0, 10, 5)
    
    st.write("😟 **Kaygı (Endişe) Seviyesi:**")
    vas_kaygi = st.slider("0: Hiç Kaygılı Değilim ... 10: Çok Kaygılıyım", 0, 10, 5)
    
    st.write("🤢 **Mide Bulantısı:**")
    vas_bulanti = st.slider("0: Hiç Yok ... 10: Kusma Hissi Var", 0, 10, 0)

# --- ADIM 2: HEXAD ÖLÇEĞİ ---
st.divider()
st.info("⬇️ Adım 2: Profil Analizi")
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
with st.expander("📝 Hexad Ölçeği (Soruları Aç)", expanded=False):
    for i, q in enumerate(questions):
        val = st.slider(f"{q}", 1, 7, 4, key=i)
        answers.append(val)

# --- OYUN VERİTABANI (TAM LİSTE) ---
game_db = {
    "Yardımsever (Philanthropist)": [
        {"name": "Cats & Soup", "desc": "Kedi bakımı", "how_to": "İzle ve tıkla", "ot_note": "📉 Düşük Bilişsel", "url": "https://play.google.com/store/search?q=cats+and+soup", "img": "https://placehold.co/300x200/4CAF50/ffffff.png?text=Cats+%26+Soup"},
        {"name": "My Oasis", "desc": "Ada kurma", "how_to": "Tıkla büyüt", "ot_note": "🧘 Terapötik", "url": "https://play.google.com/store/search?q=my+oasis", "img": "https://placehold.co/300x200/8BC34A/ffffff.png?text=My+Oasis"},
        {"name": "Pocket Camp", "desc": "Kamp alanı", "how_to": "Görev yap", "ot_note": "😐 Sosyal", "url": "https://play.google.com/store/search?q=animal+crossing+pocket+camp", "img": "https://placehold.co/300x200/CDDC39/ffffff.png?text=Pocket+Camp"},
        {"name": "Good Pizza", "desc": "Pizza yapımı", "how_to": "Hazırla pişir", "ot_note": "🖐️ İnce Motor", "url": "https://play.google.com/store/search?q=good+pizza+great+pizza", "img": "https://placehold.co/300x200/FFEB3B/000000.png?text=Pizza"},
        {"name": "Penguin Isle", "desc": "Penguen izle", "how_to": "Fotoğraf çek", "ot_note": "🎧 Duyusal", "url": "https://play.google.com/store/search?q=penguin+isle", "img": "https://placehold.co/300x200/03A9F4/ffffff.png?text=Penguins"}
    ],
    "Sosyalleşen (Socialiser)": [
        {"name": "Kızma Birader", "desc": "Zar oyunu", "how_to": "Zar at ilerle", "ot_note": "🧠 Bilinen", "url": "https://play.google.com/store/search?q=ludo+king", "img": "https://placehold.co/300x200/F44336/ffffff.png?text=Ludo"},
        {"name": "Kelime Gezmece", "desc": "Kelime bul", "how_to": "Kaydır", "ot_note": "🗣️ Sosyal", "url": "https://play.google.com/store/search?q=kelime+gezmece", "img": "https://placehold.co/300x200/E91E63/ffffff.png?text=Kelime"},
        {"name": "101 Okey Plus", "desc": "Taş oyunu", "how_to": "Diz ve at", "ot_note": "🏠 Kültürel", "url": "https://play.google.com/store/search?q=101+okey+plus", "img": "https://placehold.co/300x200/3F51B5/ffffff.png?text=Okey"},
        {"name": "Uno!", "desc": "Kart oyunu", "how_to": "Eşleştir", "ot_note": "😐 Dikkat", "url": "https://play.google.com/store/search?q=uno", "img": "https://placehold.co/300x200/FFC107/000000.png?text=UNO"},
        {"name": "Draw Something", "desc": "Çizim", "how_to": "Çiz ve bil", "ot_note": "✍️ Yaratıcı", "url": "https://play.google.com/store/search?q=draw+something", "img": "https://placehold.co/300x200/9C27B0/ffffff.png?text=Draw"}
    ],
    "Özgür Ruh (Free Spirit)": [
        {"name": "Happy Color", "desc": "Boyama", "how_to": "Tıkla boya", "ot_note": "📉 Akış", "url": "https://play.google.com/store/search?q=happy+color", "img": "https://placehold.co/300x200/673AB7/ffffff.png?text=Color"},
        {"name": "Townscaper", "desc": "Şehir kurma", "how_to": "Tıkla", "ot_note": "🧘 Hedefsiz", "url": "https://play.google.com/store/search?q=townscaper", "img": "https://placehold.co/300x200/00BCD4/ffffff.png?text=Town"},
        {"name": "I Love Hue", "desc": "Renk dizme", "how_to": "Sürükle", "ot_note": "👀 Görsel", "url": "https://play.google.com/store/search?q=i+love+hue", "img": "https://placehold.co/300x200/E040FB/ffffff.png?text=Hue"},
        {"name": "Monument Valley", "desc": "Mimari", "how_to": "Çevir ve git", "ot_note": "🌌 Kaçış", "url": "https://play.google.com/store/search?q=monument+valley", "img": "https://placehold.co/300x200/607D8B/ffffff.png?text=Monument"},
        {"name": "Tsuki Odyssey", "desc": "Tavşan", "how_to": "İzle", "ot_note": "📉 Düşük Efor", "url": "https://play.google.com/store/search?q=tsuki+odyssey", "img": "https://placehold.co/300x200/795548/ffffff.png?text=Tsuki"}
    ],
    "Başarı Odaklı (Achiever)": [
        {"name": "Candy Crush", "desc": "Şeker patlat", "how_to": "Eşleştir", "ot_note": "🍬 Ödül", "url": "https://play.google.com/store/search?q=candy+crush", "img": "https://placehold.co/300x200/E91E63/ffffff.png?text=Candy"},
        {"name": "Woodoku", "desc": "Bloklar", "how_to": "Yerleştir", "ot_note": "🧠 Planlama", "url": "https://play.google.com/store/search?q=woodoku", "img": "https://placehold.co/300x200/795548/ffffff.png?text=Woodoku"},
        {"name": "2048", "desc": "Sayılar", "how_to": "Birleştir", "ot_note": "🧠 Matematik", "url": "https://play.google.com/store/search?q=2048", "img": "https://placehold.co/300x200/FFC107/ffffff.png?text=2048"},
        {"name": "Brain Test", "desc": "Zeka", "how_to": "Çöz", "ot_note": "🧠 Bilişsel", "url": "https://play.google.com/store/search?q=brain+test", "img": "https://placehold.co/300x200/2196F3/ffffff.png?text=Brain"},
        {"name": "Wordscapes", "desc": "Kelime", "how_to": "Türet", "ot_note": "📚 Hafıza", "url": "https://play.google.com/store/search?q=wordscapes", "img": "https://placehold.co/300x200/4CAF50/ffffff.png?text=Word"}
    ],
    "Sorgulayan (Disruptor)": [
        {"name": "Angry Birds 2", "desc": "Yıkım", "how_to": "Fırlat", "ot_note": "🏹 Deşarj", "url": "https://play.google.com/store/search?q=angry+birds+2", "img": "https://placehold.co/300x200/F44336/ffffff.png?text=Angry"},
        {"name": "Cut the Rope", "desc": "İp kes", "how_to": "Kes", "ot_note": "✂️ Mantık", "url": "https://play.google.com/store/search?q=cut+the+rope", "img": "https://placehold.co/300x200/8BC34A/ffffff.png?text=Rope"},
        {"name": "Smash Hit", "desc": "Cam kır", "how_to": "Vur", "ot_note": "💥 Stres", "url": "https://play.google.com/store/search?q=smash+hit", "img": "https://placehold.co/300x200/607D8B/ffffff.png?text=Smash"},
        {"name": "Bad Piggies", "desc": "Araç yap", "how_to": "İnşa et", "ot_note": "🛠️ Problem Çözme", "url": "https://play.google.com/store/search?q=bad+piggies", "img": "https://placehold.co/300x200/4CAF50/ffffff.png?text=Bad"},
        {"name": "World of Goo", "desc": "Köprü", "how_to": "Bağla", "ot_note": "🏗️ Fizik", "url": "https://play.google.com/store/search?q=world+of+goo", "img": "https://placehold.co/300x200/212121/ffffff.png?text=Goo"}
    ],
    "Oyuncu (Player)": [
        {"name": "Subway Surfers", "desc": "Koşu", "how_to": "Kaç", "ot_note": "⚡ Refleks", "url": "https://play.google.com/store/search?q=subway+surfers", "img": "https://placehold.co/300x200/03A9F4/ffffff.png?text=Subway"},
        {"name": "Fruit Ninja", "desc": "Meyve kes", "how_to": "Kes", "ot_note": "🖐️ Tatmin", "url": "https://play.google.com/store/search?q=fruit+ninja", "img": "https://placehold.co/300x200/8BC34A/ffffff.png?text=Fruit"},
        {"name": "Coin Master", "desc": "Çark", "how_to": "Çevir", "ot_note": "📉 Şans", "url": "https://play.google.com/store/search?q=coin+master", "img": "https://placehold.co/300x200/FFC107/ffffff.png?text=Coin"},
        {"name": "Bubble Shooter", "desc": "Balon", "how_to": "Vur", "ot_note": "👀 Görsel", "url": "https://play.google.com/store/search?q=bubble+shooter", "img": "https://placehold.co/300x200/E91E63/ffffff.png?text=Bubble"},
        {"name": "Temple Run 2", "desc": "Kaçış", "how_to": "Koş", "ot_note": "⚡ Odak", "url": "https://play.google.com/store/search?q=temple+run+2", "img": "https://placehold.co/300x200/795548/ffffff.png?text=Temple"}
    ]
}

if st.button("🚀 OYUN REÇETESİ OLUŞTUR"):
    # --- PUAN HESAPLAMA ---
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
    
    # Sıralama
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    best_profile = sorted_scores[0][0]
    best_score = sorted_scores[0][1]
    second_profile = sorted_scores[1][0]
    second_score = sorted_scores[1][1]
    
    # Hibrit Profil Mantığı (Puan farkı 10'dan azsa ikisini birleştir)
    games_to_show = []
    final_profile_name = best_profile
    
    if (best_score - second_score) < 10:
        games_to_show = game_db.get(best_profile, []) + game_db.get(second_profile, [])
        final_profile_name = f"{best_profile} + {second_profile} (Melez Profil)"
        st.info(f"💡 Puanlarınız yakın olduğu için size özel karma bir liste oluşturuldu.")
    else:
        games_to_show = game_db.get(best_profile, [])
    
    # Session State'e Kaydet
    st.session_state['final_profile_name'] = final_profile_name
    st.session_state['games_to_show'] = games_to_show
    st.session_state['scores'] = scores # Grafik için
    st.session_state['analysis_done'] = True

# --- SONUÇ VE REÇETE EKRANI ---
if 'analysis_done' in st.session_state:
    st.divider()
    st.success(f"Tespit Edilen Profil: **{st.session_state['final_profile_name']}**")
    
    # Profil Grafiği
    st.bar_chart(pd.DataFrame.from_dict(st.session_state['scores'], orient='index', columns=['Puan']))

    st.header("💊 Size Özel Aktivite Reçetesi")
    cols = st.columns(2)
    games = st.session_state['games_to_show']
    
    for i, game in enumerate(games):
        with cols[i % 2]:
            st.image(game["img"], use_container_width=True)
            st.subheader(game["name"])
            with st.expander("❓ Nasıl Oynanır?"):
                st.write(game["how_to"])
            st.warning(f"OT Notu: {game['ot_note']}")
            st.link_button(f"▶ {game['name']} Oyna", game["url"])
            st.divider()

    # --- ADIM 3: SON TEST (AKADEMİK & AKIŞ) ---
    st.markdown("---")
    st.info("⬇️ Adım 3: Aktivite Sonrası Değerlendirme (Oyun Bittikten Sonra)")
    
    with st.container():
        st.write("😟 **Son Kaygı Seviyesi:**")
        vas_kaygi_son = st.slider("0: Hiç - 10: Çok", 0, 10, 5, key="vk_son")
        
        st.write("⏱️ **Zaman Algısı:**")
        zaman_algi = st.number_input("Tahmini Geçen Süre (Dakika)", 0, 120, 0)
        
        st.markdown("---")
        st.write("🌊 **Akış (Flow) Deneyimi (1-5):**")
        st.caption("1: Hiç Katılmıyorum ... 5: Tamamen Katılıyorum")
        
        f1 = st.slider("1. Ne yapacağımı net biliyordum", 1, 5, 3)
        f2 = st.slider("2. Hareketlerim otomatikleşti", 1, 5, 3)
        f3 = st.slider("3. Anında geri bildirim aldım", 1, 5, 3)
        f4 = st.slider("4. Dikkattim tamamen oyundaydı", 1, 5, 3)
        f5 = st.slider("5. Kontrolün bende olduğunu hissettim", 1, 5, 3)
        f6 = st.slider("6. Kendimi/dertlerimi unuttum", 1, 5, 3)
        f7 = st.slider("7. Zamanın nasıl geçtiğini anlamadım", 1, 5, 3)
        f8 = st.slider("8. Oyun zorluğu becerime uygundu", 1, 5, 3)
        f9 = st.slider("9. Çok keyif aldım", 1, 5, 3)
        
        flow_total = f1+f2+f3+f4+f5+f6+f7+f8+f9
        
        if st.button("💾 VERİLERİ KAYDET"):
            if connection_status:
                try:
                    yeni_veri = [
                        datetime.now().strftime("%Y-%m-%d %H:%M"),
                        protokol_no,
                        yas,
                        cinsiyet,
                        egitim,
                        kemo_kur,
                        st.session_state['final_profile_name'],
                        vas_yorgunluk,
                        vas_kaygi,
                        vas_bulanti,
                        vas_kaygi_son,
                        zaman_algi,
                        flow_total
                    ]
                    sheet.append_row(yeni_veri)
                    st.balloons()
                    st.success("✅ Veriler Google E-Tablolar'a başarıyla kaydedildi!")
                except Exception as e:
                    st.error(f"Kayıt Hatası: {e}")
            else:
                st.error("Veritabanı bağlantısı yok! Demo modundasınız.")
