def postTaxPrice(price):
    res = price * 1.1
    return int(res)

print(postTaxPrice(120), "yen")
print(postTaxPrice(980), "yen")
