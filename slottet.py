import random

# ---------- VARIABLER ----------

liv = 10
inventar = []
spiller = True
sted = "ute"        # hvor spilleren er akkurat nå

# ---------- DICTIONARY ----------
# Alt vi trenger å vite om en fiende ligger samlet på ett sted.

fiender = {
    "troll": {"liv": 8, "min_skade": 2, "maks_skade": 4},
    # OPPGAVE 6: legg til én fiende til her
}

# Trollets liv lages her oppe, utenfor løkken.
# Da husker spillet det, og et beseiret troll forblir dødt.
troll_liv = fiender["troll"]["liv"]

# ---------- FUNKSJONER ----------

def vis_status():
    # OPPGAVE 1: skriv ut liv, og alt spilleren har i sekken
    pass


def terning(minste, storste):
    """Gir et tilfeldig heltall fra minste til og med storste."""
    return random.randint(minste, storste)


def spor(sporsmal):
    """Stiller et spørsmål og gjør svaret om til små bokstaver."""
    return input(sporsmal).lower().strip()


# ---------- SPILLET ----------

print("DET GLEMTE SLOTTET")
print()
print("Du våkner utenfor et forlatt slott.")
print("Porten står på gløtt.")

while spiller:

    print()
    vis_status()
    print()

    # Hver runde sjekker vi hvor spilleren står, og viser bare det stedet.
    # Spilleren flytter seg ved at vi gir sted en ny verdi.

    if sted == "ute":

        valg = spor("Går du inn i SLOTTET eller inn i SKOGEN? ")

        if valg == "slottet":
            sted = "hallen"
        elif valg == "skogen":
            sted = "skogen"
        else:
            print("Du må velge SLOTTET eller SKOGEN.")

    elif sted == "hallen":

        print("Inngangshallen er kald og mørk.")
        print("Du ser en gammel tredør, og en trapp som går opp i mørket.")

        valg = spor("Velger du DØREN, TRAPPEN, eller går du UT? ")

        if valg == "døren":
            sted = "rommet"
        elif valg == "trappen":
            sted = "trappen"
        elif valg == "ut":
            sted = "ute"
        else:
            print("Du blir stående. Ingenting skjer.")

    elif sted == "rommet":

        print("Du står i et lite rom. En stor kiste med jernbeslag står mot veggen.")

        valg = spor("Vil du ÅPNE kisten, eller gå TILBAKE til hallen? ")

        if valg == "åpne":
            # OPPGAVE 2: legg "gullnøkkel" i inventar, og fortell hva spilleren fant.
            # Ligger nøkkelen allerede i sekken, er kisten tom.
            pass
        elif valg == "tilbake":
            sted = "hallen"
        else:
            print("Du blir stående. Ingenting skjer.")

    elif sted == "trappen":

        if troll_liv > 0:

            print("Halvveis opp reiser et stort troll seg foran deg.")
            print("INGEN PASSERER, brøler det.")

            troll = fiender["troll"]

            # OPPGAVE 3: lag kampen her.
            # En while-løkke som går så lenge både trollet og spilleren lever.
            # Hver runde kan spilleren velge ANGRIP eller FLYKT.

        else:
            print("Trollet ligger fortsatt på trappen der du slo det ned.")

        if troll_liv <= 0:

            print()
            print("Trollet er beseiret. Bak det står en tung, låst dør.")

            # OPPGAVE 4: har spilleren "gullnøkkel" i inventar?
            # Ja: åpne døren, skriv seiersmeldingen, sett spiller = False.
            # Nei: fortell at døren er låst.

        # Vant du ikke, går du ned til hallen igjen.
        sted = "hallen"

    elif sted == "skogen":

        print("Trærne står tett. Noe rasler i buskene.")

        valg = spor("Vil du LETE i buskene, eller gå TILBAKE til slottet? ")

        if valg == "lete":
            # OPPGAVE 5: lag to hendelser, og la terning(1, 2) avgjøre hvilken.
            # Den ene gir spilleren en helsedrikk.
            # Den andre koster liv.
            pass
        elif valg == "tilbake":
            sted = "ute"
        else:
            print("Du blir stående. Ingenting skjer.")

    # OPPGAVE 7: er liv 0 eller mindre?
    # Skriv GAME OVER, og stopp spillet.
