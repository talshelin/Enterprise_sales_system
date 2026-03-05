# ### Analitik Motor (NumPy + Pandas)

# - NumPy ile:
#     - normalize edilmiş matrisler
#     - performans skorları
# - Pandas ile:
#     - şehir bazlı satış
#     - ürün bazlı satış
#     - ay bazlı trend
#     - GroupBy + agg yoğun kullanılır
#  Loop YOK → vektörel düşünce

import numpy as np
import pandas as pd

def analyze_data(df):
    # Şehir bazlı satış
    city_sales = df.groupby('City')['SalesAmount'].sum()
    
    # Ürün bazlı satış
    product_sales = df.groupby('Product')['SalesAmount'].sum()
    
    # Ay bazlı trend
    month_sales = df.groupby('Month')['SalesAmount'].sum()
    
    # Performans skorları (örneğin, satışların ortalaması ve standart sapması)
    performance_scores = {
        'mean_sales': np.mean(df['SalesAmount']),
        'std_sales': np.std(df['SalesAmount'])
    }
    
    return city_sales, product_sales, month_sales, performance_scores