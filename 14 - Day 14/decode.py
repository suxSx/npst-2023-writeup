# Boktitlene og deres lengder
boktitler = [
    "Norrøn arverett og samfunnsstruktur",
    "Radium og radioaktive stoffer, samt nyere opdagelser angaaende straaler",
    "Undertrykking av objekter med høy luminans ved hjelp av en romlig lysmodulator under avbildning med CCD- og lysforsterkningskamera",
    "Om den yngre Jernalder i Norge : 1. afdeling",
    "Storlogens Konstitution og Tillægslove",
    "Sild- og saltfiskretter"
]

# Tuppelverdier fra notatet
tuppelverdier = [
    (55, 1, 2, 1), (65, 17, 6, 3), (19, 3, 8, 1), (13, 5, 6, 2), (14, 11, 4, 8), (27, 32, 12, 2),
    (9, 7, 12, 3), (82, 5, 2, 8), (78, 3, 11, 1), (71, 5, 1, 8), (76, 1, 6, 2), (92, 1, 1, 1),
    (50, 2, 1, 5), (15, 1, 1, 1), (82, 16, 10, 4), (23, 6, 1, 1), (34, 16, 7, 1), (92, 11, 3, 2),
    (50, 5, 6, 1), (1, 3, 5, 12), (42, 2, 1, 1), (15, 3, 1, 3), (23, 8, 1, 2), (90, 2, 5, 1),
    (83, 1, 1, 2), (59, 29, 9, 4), (93, 4, 1, 16), (82, 8, 3, 5), (39, 1, 1, 8), (77, 7, 9, 1),
    (93, 8, 6, 8), (1, 1, 3, 6), (83, 10, 8, 1), (23, 1, 1, 1), (69, 2, 9, 2), (76, 12, 3, 4),
    (7, 1, 3, 1), (3, 9, 9, 2), (19, 1, 6, 10), (93, 14, 7, 5), (13, 31, 7, 10), (3, 1, 9, 2),
    (7, 2, 6, 1), (23, 19, 4, 3), (50, 6, 5, 11)
]

def analytics(boktitler):
    for boktittel in boktitler:
        print(f"({len(boktittel)}) - {boktittel} ")


# Funksjon for å dekode tuppelverdiene
def dekode_tuppelverdier(tuppelverdier, boktitler):
    dekodet_tekst = ""
    for tuppel in tuppelverdier:
        bok_index = (tuppel[0] - 1) % len(boktitler)  # Velger bok basert på modulos
        bokstav_index = tuppel[3] - 1  # Bokstavindex i tittelen
        boktittel = boktitler[bok_index]
        if bokstav_index < len(boktittel):
            dekodet_tekst += boktittel[bokstav_index]
        else:
            dekodet_tekst += "?"  # Ukjent bokstav
    return dekodet_tekst


# Dekodere tuppelverdiene
dekodet_tekst = dekode_tuppelverdier(tuppelverdier, boktitler)

print(analytics(boktitler))
print(dekodet_tekst)
