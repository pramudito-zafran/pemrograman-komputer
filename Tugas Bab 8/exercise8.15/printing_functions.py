def cetak_model(desain_belum_dicetak, model_selesai):
    """Simulasi mencetak setiap desain sampai tidak ada yang tersisa."""
    while desain_belum_dicetak:
        desain_saat_ini = desain_belum_dicetak.pop()
        print(f"Mencetak model: {desain_saat_ini}")
        model_selesai.append(desain_saat_ini)

def tampilkan_model_selesai(model_selesai):
    """Menampilkan semua model yang telah berhasil dicetak."""
    print("\nModel-model berikut telah selesai dicetak:")
    for model in model_selesai:
        print(model)
