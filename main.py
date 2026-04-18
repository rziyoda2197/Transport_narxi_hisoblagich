def transport_narxi(masofa, transport_turi):
    if masofa < 0:
        print("Masofa manfiy bo‘lishi mumkin emas")
        return

    transport_turi = transport_turi.lower()

    if transport_turi == "taksi":
        narx = 5000 + masofa * 2000
    elif transport_turi == "avtobus":
        narx = masofa * 3000
    elif transport_turi == "poezd":
        narx = 10000 + masofa * 1500
    else:
        print("Noto‘g‘ri transport turi")
        return

    print(f"Narx: {int(narx)} so‘m")
