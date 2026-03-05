# ### Veri Temizleme (Pandas + Python)
# - Eksik verileri tespit et
# - Mantıklı stratejiyle doldur / sil
# - String kolonları normalize et
# - Yeni sütunlar üret (KDV’li satış vb.)
# - try/except ile hataya dayanıklı yap
# Burada:
# - if
# - fonksiyon
# - pandas ileri işlemler zorunlu

import pandas as pd

def clean_data(df):
    # Eksik verileri tespit et
    print("Eksik Veriler:")
    print(df.isnull().sum())
    
    # NaN değerleri doldur (örneğin, ortalama ile)
    df['SalesAmount'].fillna(df['SalesAmount'].mean(), inplace=True)
    
    # String kolonları normalize et (örneğin, ürün isimlerini küçük harfe çevir)
    df['Product'] = df['Product'].str.lower()
    
    # Yeni sütun üret (KDV'li satış tutarı)
    df['SalesAmountWithVAT'] = df['SalesAmount'] * 1.18  # KDV oranı %18
    
    return df