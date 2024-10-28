sales = ['$1.21', '$2.29', '$14.52', '$6.13', '$24.36', '$33.85', '$1.92']
sales = [sales[i].strip('$') for i in range(len(sales))]
print(max(sales))