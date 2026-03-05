#### Karar Destek Katmanı
# - En iyi / en kötü şehir
# - En kârlı ürün
# - Riskli bölgeler (düşük ortalama)
# - Yöneticiye okunabilir özet üret
# Bool + if + dict + tuple kullanımı

def generate_report(city_sales, product_sales, month_sales, performance_scores):
    report = {
        'Best City': city_sales.idxmax(),
        'Worst City': city_sales.idxmin(),
        'Most Profitable Product': product_sales.idxmax(),
        'Least Profitable Product': product_sales.idxmin(),
        'Best Month': month_sales.idxmax(),
        'Worst Month': month_sales.idxmin(),
        'Average Sales': performance_scores['mean_sales'],
        'Sales Std Dev': performance_scores['std_sales']
    }
    
    return report