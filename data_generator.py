# - `np.random` ile:
#     - müşteri ID
#     - ürün
#     - şehir
#     - satış tutarı
#     - ay bilgisi üret
#     - NaN değerler koy 
#     - uç değerler üret 

import numpy as np
import pandas as pd

def generate_data(num_samples=1000, num_outliers=50, nan_ratio=0.1):
    # Müşteri ID
    customer_ids = np.random.randint(1000, 9999, size=num_samples)
    
    # Ürün
    products = np.random.choice(['Ürün A', 'Ürün B', 'Ürün C', 'Ürün D'], size=num_samples)
    
    # Şehir
    cities = np.random.choice(['İstanbul', 'Ankara', 'İzmir', 'Bursa'], size=num_samples)
    
    # Satış Tutarı
    sales_amounts = np.random.uniform(10, 1000, size=num_samples)
    
    # Ay Bilgisi
    months = np.random.choice(['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran'], size=num_samples)
    
    # NaN Değerler ekle
    num_nans = int(num_samples * nan_ratio)
    nan_indices = np.random.choice(num_samples, num_nans, replace=False)
    sales_amounts[nan_indices] = np.nan
    
    # Uç Değerler ekle
    outlier_indices = np.random.choice(num_samples, num_outliers, replace=False)
    sales_amounts[outlier_indices] *= 10  # Uç değerleri artır
    
    # DataFrame oluştur
    data = pd.DataFrame({
        'CustomerID': customer_ids,
        'Product': products,
        'City': cities,
        'SalesAmount': sales_amounts,
        'Month': months
    })
    
    return data