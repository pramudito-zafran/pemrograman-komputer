# Sungai ikonik di masing-masing negara
sungai_sungai = {
    'nil': 'mesir',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# 1. Loop untuk kalimat sungai
print("====Kalimat Sungai====")
for sungai, negara in sungai_sungai.items():
    print(f"Sungai {sungai.title()} mengalir di {negara.title()}.")

# 2. Loop untuk nama sungai
print("\n====Nama Sungai====")
for sungai in sungai_sungai.keys():
    print(sungai.title())

# 3. Loop untuk nama negara
print("\n====Nama Negara====")
for negara in sungai_sungai.values():
    print(negara.title())