# Enterprise_sales_system
## Proje Tanıtımı

Bu proje, kurumsal satış verisini uçtan uca işleyen mini bir karar destek sistemi örneğidir. Sistem; sentetik veri üretimi, veri temizleme, analitik hesaplamalar ve yönetici özeti üretimi adımlarını tek bir akışta birleştirir.

### Amaç
- Satış performansını şehir, ürün ve ay bazında görünür hale getirmek
- Eksik ve uç değerli verilerle çalışabilen dayanıklı bir analiz hattı kurmak
- Karar almayı kolaylaştıran özet bir rapor ve Excel çıktısı üretmek

### Kullanılan Teknolojiler
- **Python**
- **NumPy**: vektörel hesaplama ve istatistik
- **Pandas**: veri temizleme, gruplayarak analiz ve raporlama

### İş Akışı
1. `generate_data()` ile örnek satış verisi oluşturulur
2. `clean_data()` ile eksik veriler doldurulur ve veri normalize edilir
3. `analyze_data()` ile şehir/ürün/ay kırılımlarında satış analizi yapılır
4. `generate_report()` ile en iyi/en zayıf performans metrikleri üretilir
5. Sonuçlar ekrana yazdırılır ve `sales_report.xlsx` olarak dışa aktarılır

### Üretilen Çıktılar
- Şehir bazlı toplam satış
- Ürün bazlı toplam satış
- Ay bazlı satış trendi
- Ortalama satış ve standart sapma
- Yönetici özeti (en iyi şehir, en kârlı ürün, en iyi ay vb.)
