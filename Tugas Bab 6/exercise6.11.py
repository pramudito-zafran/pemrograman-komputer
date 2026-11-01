# Membuat dictionary mengenai kota-kota
kota_kota = {
    'surabaya': {
        'negara': 'indonesia',
        'populasi': '287.886.782',
        'fakta': 'Salah satu kota terpanas di Indonesia',
    },
    'paris': {
        'negara': 'Prancis',
        'populasi': '2,100,000',
        'fakta': 'Ada menara ikonik yang disebut menara eiffel.',
    },
    'new york': {
        'negara': 'Amerika',
        'populasi': '8,330,000',
        'fakta': 'Disebut kota yang tidak pernah tidur',
    }
}

# 2. Loop untuk kota dan informasi-informasinya
for kota, info_kota in kota_kota.items():
    print(f"\nKota: {kota.title()}")
    
    negara = info_kota['negara']
    populasi = info_kota['populasi']
    fakta = info_kota['fakta']
    
    print(f"- negara: {negara}")
    print(f"- populasi: {populasi}")
    print(f"- fakta: {fakta}")
