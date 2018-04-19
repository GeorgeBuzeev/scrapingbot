import NFProvider from provider

nfProvider = NFProvider([
"https://www.95c.ru/catalog/dlya_sauny/elektrokamenki/",
'https://www.95c.ru/catalog/dlya_sauny/drovyanye_pechi/'
])

ateliesaunProv = AteliesaunProvider()

providers = [nfProvider, ateliesaunProv]

allProducts = []
for provider in providers:
    allProducts.append(provider.get_products())

filteredProducts = []
for product in allProducts:
    if product.brand == "tylo":
        filteredProducts.append(product)
print(filteredProducts)
