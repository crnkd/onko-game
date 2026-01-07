import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="Onko-Game: Kişiselleştirilmiş Oyun Reçetesi", page_icon="🧩", layout="centered")

# CSS: Tasarımı Güzelleştirme
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
</style>
""", unsafe_allow_html=True)

# --- BAŞLIK VE GÜVENLİK UYARISI ---
st.title("🧩 Onko-Game Asistanı")
st.markdown("**Kişiselleştirilmiş Aktivite ve Oyunlaştırma Reçetesi**")

with st.expander("⚠️ DİKKAT: Ergoterapist Güvenlik Notları (Okumak için Tıklayınız)", expanded=False):
    st.error("""
    1. **Mide Bulantısı:** Oyun sırasında baş dönmesi veya mide bulantısı hissederseniz hemen bırakınız ve uzağa odaklanınız.
    2. **Fiziksel Pozisyon:** Damar yolu takılı kolunuzu aktif kullanmayınız. Tableti bir stand üzerinde veya diğer elinizle tutunuz.
    3. **Göz Sağlığı:** Her 20 dakikada bir 20 saniye boyunca ekrandan uzaklaşıp 6 metre uzağa bakınız (20-20-20 Kuralı).
    4. **İçerik:** Bu sistemde yer alan oyunlar; şiddet, kan ve medikal travma öğelerinden arındırılmış olup bilişsel/motor seviyenize uygun seçilmiştir.
    """)

st.divider()

# --- YAN MENÜ ---
with st.sidebar:
    st.header("Hasta Bilgileri")
    ad_soyad = st.text_input("Ad Soyad / Protokol No")
    yas = st.number_input("Yaş", 18, 90, 40)
    st.info("Veriler sisteme kaydedilmez, anlık analiz içindir.")

# --- SORULAR (HEXAD) ---
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
with st.expander("📝 Ölçeği Doldurmak İçin Tıklayınız (22 Soru)", expanded=True):
    for i, q in enumerate(questions):
        val = st.slider(f"{q}", 1, 7, 4, key=i)
        answers.append(val)

# --- 30 OYUNLUK ERGOTERAPİ ONAYLI VERİTABANI (NASIL OYNANIR EKLENDİ) ---
game_db = {
    "Yardımsever (Philanthropist)": [
        {"name": "Cats & Soup", "desc": "Sakinleştirici kedi bakımı.", "how_to": "Kedilerin çorba yapmasını izleyin, biriken altınlara tıklayarak onlara yeni kıyafetler ve eşyalar alın.", "ot_note": "📉 Düşük Bilişsel Yük", "url": "https://play.google.com/store/search?q=cats+and+soup", "img": "https://placehold.co/300x200/4CAF50/ffffff.png?text=Cats+%26+Soup"},
        {"name": "My Oasis", "desc": "Kendi adanızı büyütün.", "how_to": "Ekrana her dokunduğunuzda puan kazanırsınız. Bu puanlarla adanıza yeni hayvanlar ve ağaçlar ekleyin.", "ot_note": "🧘 Terapötik / Olumlama", "url": "https://play.google.com/store/search?q=my+oasis", "img": "https://placehold.co/300x200/8BC34A/ffffff.png?text=My+Oasis"},
        {"name": "Pocket Camp", "desc": "Kamp alanı kurun.", "how_to": "Ormandaki hayvanların istedikleri meyve veya balıkları toplayıp onlara verin, karşılığında hediye alın.", "ot_note": "😐 Sosyal İzolasyona Karşı", "url": "https://play.google.com/store/search?q=animal+crossing+pocket+camp", "img": "https://placehold.co/300x200/CDDC39/ffffff.png?text=Pocket+Camp"},
        {"name": "Good Pizza", "desc": "Pizza dükkanı işletin.", "how_to": "Müşteri ne istiyorsa (Örn: Sadece peynir) hamurun üzerine sürükleyin, fırına verin ve kutulayıp servis edin.", "ot_note": "🖐️ İnce Motor Becerisi", "url": "https://play.google.com/store/search?q=good+pizza+great+pizza", "img": "https://placehold.co/300x200/FFEB3B/000000.png?text=Pizza+Shop"},
        {"name": "Penguin Isle", "desc": "Penguenleri izleyin.", "how_to": "Sadece penguenlerin fotoğrafını çekin ve yaşam alanlarını genişletmek için butona basın.", "ot_note": "🎧 Duyusal Regülasyon", "url": "https://play.google.com/store/search?q=penguin+isle", "img": "https://placehold.co/300x200/03A9F4/ffffff.png?text=Penguins"}
    ],
    "Sosyalleşen (Socialiser)": [
        {"name": "Kızma Birader", "desc": "Klasik zar oyunu.", "how_to": "Sıranız gelince zarı atın. 6 gelirse piyonunuzu oyuna sokun ve tüm piyonları merkeze götürmeye çalışın.", "ot_note": "🧠 Bilinen Aktivite", "url": "https://play.google.com/store/search?q=ludo+king", "img": "https://placehold.co/300x200/F44336/ffffff.png?text=Kizma+Birader"},
        {"name": "Kelime Gezmece", "desc": "Kelime bulmaca.", "how_to": "Parmağınızı harflerin üzerinde kaydırarak anlamlı kelimeler oluşturun. Yanınızdaki kişiden yardım alabilirsiniz.", "ot_note": "🗣️ Refakatçi ile Oynanabilir", "url": "https://play.google.com/store/search?q=kelime+gezmece", "img": "https://placehold.co/300x200/E91E63/ffffff.png?text=Kelime+Gezmece"},
        {"name": "101 Okey Plus", "desc": "Geleneksel taş oyunu.", "how_to": "Istakanızdaki taşları aynı renk veya sıralı sayılar olacak şekilde dizin (Örn: 1-2-3 veya Kırmızı 5-5-5).", "ot_note": "🏠 Ev Ortamı Hissi", "url": "https://play.google.com/store/search?q=101+okey+plus", "img": "https://placehold.co/300x200/3F51B5/ffffff.png?text=101+Okey"},
        {"name": "Uno!", "desc": "Kart eşleştirme.", "how_to": "Ortadaki kartın rengi veya sayısı neyse, elinizdeki uygun kartı üzerine atın. Kartınız kalmayınca kazanırsınız.", "ot_note": "😐 Orta Seviye Dikkat", "url": "https://play.google.com/store/search?q=uno", "img": "https://placehold.co/300x200/FFC107/000000.png?text=UNO"},
        {"name": "Draw Something", "desc": "Çizerek anlatma.", "how_to": "Size verilen kelimeyi (Örn: Elma) parmağınızla çizin, karşı tarafın tahmin etmesini bekleyin.", "ot_note": "✍️ Yaratıcı İletişim", "url": "https://play.google.com/store/search?q=draw+something", "img": "https://placehold.co/300x200/9C27B0/ffffff.png?text=Ciz+Bakalim"}
    ],
    "Özgür Ruh (Free Spirit)": [
        {"name": "Happy Color", "desc": "Sayılarla boyama.", "how_to": "Resimdeki gri alanlara tıklayın. Hangi numara yazıyorsa o rengi seçip boyayın. Hata yapma şansınız yok.", "ot_note": "📉 Hata Yok / Saf Akış", "url": "https://play.google.com/store/search?q=happy+color", "img": "https://placehold.co/300x200/673AB7/ffffff.png?text=Happy+Color"},
        {"name": "Townscaper", "desc": "Kasaba kurma.", "how_to": "Ekrana rastgele dokunun. Her dokunuşunuzda oraya otomatik olarak şirin bir bina veya yol eklenir.", "ot_note": "🧘 Hedefsiz Oyun", "url": "https://play.google.com/store/search?q=townscaper", "img": "https://placehold.co/300x200/00BCD4/ffffff.png?text=Townscaper"},
        {"name": "I Love Hue", "desc": "Renkleri sıralama.", "how_to": "Kare şeklindeki renkleri parmağınızla sürükleyerek, tonlarına göre (koyudan açığa) doğru sıraya dizin.", "ot_note": "👀 Görsel Algı", "url": "https://play.google.com/store/search?q=i+love+hue", "img": "https://placehold.co/300x200/E040FB/ffffff.png?text=Renkler"},
        {"name": "Monument Valley", "desc": "Mimari gezi.", "how_to": "Karakterin yürümesi için yollara tıklayın. Bazen yolları birleştirmek için mimariyi parmağınızla çevirmeniz gerekir.", "ot_note": "🌌 İmgelesel Kaçış", "url": "https://play.google.com/store/search?q=monument+valley", "img": "https://placehold.co/300x200/607D8B/ffffff.png?text=Monument"},
        {"name": "Tsuki Odyssey", "desc": "Tavşanın hayatı.", "how_to": "Bu oyunda yapacak çok şey yok. Sadece tavşanınızın havuç toplamasını izleyin ve ona yeni eşyalar alın.", "ot_note": "📉 Çok Düşük Efor", "url": "https://play.google.com/store/search?q=tsuki+odyssey", "img": "https://placehold.co/300x200/795548/ffffff.png?text=Tsuki"}
    ],
    "Başarı Odaklı (Achiever)": [
        {"name": "Candy Crush", "desc": "Şeker eşleştirme.", "how_to": "Aynı renkteki en az 3 şekeri yan yana veya üst üste getirmek için parmağınızla kaydırın.", "ot_note": "🍬 Anlık Ödül Sistemi", "url": "https://play.google.com/store/search?q=candy+crush", "img": "https://placehold.co/300x200/E91E63/ffffff.png?text=Candy+Crush"},
        {"name": "Woodoku", "desc": "Blok yerleştirme.", "how_to": "Aşağıdaki ahşap blokları yukarıdaki boş kutulara sürükleyin. Satır veya sütun dolunca bloklar yok olur.", "ot_note": "🧠 Planlama", "url": "https://play.google.com/store/search?q=woodoku", "img": "https://placehold.co/300x200/795548/ffffff.png?text=Woodoku"},
        {"name": "2048", "desc": "Sayı birleştirme.", "how_to": "Parmağınızı sağa-sola kaydırarak aynı sayıları çarpıştırın (2+2=4, 4+4=8). Amaç 2048'e ulaşmak.", "ot_note": "🧠 Matematiksel Muhakeme", "url": "https://play.google.com/store/search?q=2048", "img": "https://placehold.co/300x200/FFC107/ffffff.png?text=2048"},
        {"name": "Brain Test", "desc": "Zeka soruları.", "how_to": "Soruyu okuyun ve ekrandaki nesneleri hareket ettirerek cevabı bulmaya çalışın. Mantık dışı düşünmeniz gerekebilir.", "ot_note": "🧠 Bilişsel Egzersiz", "url": "https://play.google.com/store/search?q=brain+test", "img": "https://placehold.co/300x200/2196F3/ffffff.png?text=Brain+Test"},
        {"name": "Wordscapes", "desc": "Kelime türetme.", "how_to": "Aşağıdaki çarktaki harfleri parmağınızla birleştirerek yukarıdaki boş kutulara uygun kelimeleri bulun.", "ot_note": "📚 Kelime Hafızası", "url": "https://play.google.com/store/search?q=wordscapes", "img": "https://placehold.co/300x200/4CAF50/ffffff.png?text=Wordscapes"}
    ],
    "Sorgulayan (Disruptor)": [
        {"name": "Angry Birds 2", "desc": "Sapanla yıkım.", "how_to": "Kuşu sapanla geri çekin, nişan alın ve bırakın. Amaç karşıdaki domuzcukların kulelerini yıkmak.", "ot_note": "🏹 Deşarj Olma", "url": "https://play.google.com/store/search?q=angry+birds+2", "img": "https://placehold.co/300x200/F44336/ffffff.png?text=Angry+Birds"},
        {"name": "Cut the Rope", "desc": "İp kesmece.", "how_to": "Parmağınızı makas gibi kullanarak ipleri kesin. Şekerin sallanarak aşağıdaki yeşil canavarın ağzına düşmesini sağlayın.", "ot_note": "✂️ Neden-Sonuç İlişkisi", "url": "https://play.google.com/store/search?q=cut+the+rope", "img": "https://placehold.co/300x200/8BC34A/ffffff.png?text=Cut+The+Rope"},
        {"name": "Smash Hit", "desc": "Cam kırma.", "how_to": "Otomatik ilerlerken karşınıza çıkan cam engellere dokunarak metal bilye fırlatın ve onları kırın.", "ot_note": "💥 Stres Atma", "url": "https://play.google.com/store/search?q=smash+hit", "img": "https://placehold.co/300x200/607D8B/ffffff.png?text=Smash+Hit"},
        {"name": "Bad Piggies", "desc": "Araç yapımı.", "how_to": "Verilen parçaları (tekerlek, motor) birleştirerek bir araç yapın ve bitiş çizgisine ulaşmaya çalışın.", "ot_note": "🛠️ Yaratıcı Problem Çözme", "url": "https://play.google.com/store/search?q=bad+piggies", "img": "https://placehold.co/300x200/4CAF50/ffffff.png?text=Bad+Piggies"},
        {"name": "World of Goo", "desc": "Köprü kurma.", "how_to": "Siyah yapışkan topları birbirine ekleyerek sağlam bir kule veya köprü oluşturup boruya ulaşın.", "ot_note": "🏗️ Fizik Kuralları", "url": "https://play.google.com/store/search?q=world+of+goo", "img": "https://placehold.co/300x200/212121/ffffff.png?text=World+of+Goo"}
    ],
    "Oyuncu (Player)": [
        {"name": "Subway Surfers", "desc": "Sonsuz koşu.", "how_to": "Karakter otomatik koşar. Sağa-sola geçmek veya zıplamak için parmağınızı kaydırın. Trenlere çarpmayın.", "ot_note": "⚡ Dikkat: Hızlı Refleks", "url": "https://play.google.com/store/search?q=subway+surfers", "img": "https://placehold.co/300x200/03A9F4/ffffff.png?text=Subway"},
        {"name": "Fruit Ninja", "desc": "Meyve kesme.", "how_to": "Ekrana gelen meyveleri parmağınızla (bıçak gibi) kesin. Arada çıkan bombalara dokunmayın.", "ot_note": "🖐️ Hızlı Tatmin", "url": "https://play.google.com/store/search?q=fruit+ninja", "img": "https://placehold.co/300x200/8BC34A/ffffff.png?text=Fruit+Ninja"},
        {"name": "Coin Master", "desc": "Çark çevirme.", "how_to": "Sadece kırmızı butona basarak çarkı çevirin. Gelen paralarla köyünüzdeki binaları tamir edin.", "ot_note": "📉 Şans Faktörü", "url": "https://play.google.com/store/search?q=coin+master", "img": "https://placehold.co/300x200/FFC107/ffffff.png?text=Coin+Master"},
        {"name": "Bubble Shooter", "desc": "Balon patlatma.", "how_to": "Aşağıdaki renkli topu, yukarıdaki aynı renkli topların arasına fırlatın. En az 3 tane olunca patlarlar.", "ot_note": "👀 Görsel Takip", "url": "https://play.google.com/store/search?q=bubble+shooter", "img": "https://placehold.co/300x200/E91E63/ffffff.png?text=Bubble"},
        {"name": "Temple Run 2", "desc": "Tapınaktan kaçış.", "how_to": "Arkanızdaki canavardan kaçarken zıplamak için yukarı, kaymak için aşağı kaydırın. Telefonu sağa-sola eğerek altın toplayın.", "ot_note": "⚡ Odaklanma", "url": "https://play.google.com/store/search?q=temple+run+2", "img": "https://placehold.co/300x200/795548/ffffff.png?text=Temple+Run"}
    ]
}

# --- HESAPLAMA VE EKRANA BASMA ---
if st.button("🚀 Profili Analiz Et ve Oyun Öner"):
    
    # Hesaplamalar
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
    max_score = scores[best_profile]
    
    # SONUÇ GÖSTERİMİ
    st.divider()
    st.success(f"Analiz Tamamlandı! Baskın Profiliniz: **{best_profile}**")
    
    # Grafik
    st.bar_chart(pd.DataFrame.from_dict(scores, orient='index', columns=['Puan']))
    
    # REÇETE KISMI
    st.header(f"💊 Sizin İçin Reçete Edilen Oyunlar")
    st.info("Aşağıdaki oyunlardan birini seçebilirsiniz. 'Nasıl Oynanır' butonuna tıklayarak kuralları görebilirsiniz.")
    
    games_to_show = game_db.get(best_profile, [])
    
    # 2 Kolonlu Düzen
    cols = st.columns(2)
    
    for i, game in enumerate(games_to_show):
        with cols[i % 2]:
            st.image(game["img"], use_container_width=True)
            st.subheader(game["name"])
            st.caption(game["desc"])
            
            # NASIL OYNANIR (AÇILIR KUTU)
            with st.expander("❓ Nasıl Oynanır?"):
                st.write(game["how_to"])
            
            st.warning(f"OT Notu: {game['ot_note']}")
            st.link_button(f"▶ {game['name']} Oyna", game["url"])
            st.divider()
