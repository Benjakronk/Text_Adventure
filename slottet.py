import random

# ---------- VARIABLER ----------

liv = 10
inventar = []
spiller = True

# ---------- DICTIONARY ----------
# Alt vi trenger å vite om en fiende ligger samlet på ett sted.

fiender = {
    "troll": {"liv": 8, "min_skade": 2, "maks_skade": 4},
    # OPPGAVE 6: legg til én fiende til her
}

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

    valg = spor("Går du inn i SLOTTET eller inn i SKOGEN? ")

    if valg == "slottet":

        print()
        print("Inngangshallen er kald og mørk.")
        print("Du ser en gammel tredør, og en trapp som går opp i mørket.")

        valg = spor("Velger du DØREN eller TRAPPEN? ")

        if valg == "døren":

            print()
            print("Bak døren står en stor kiste med jernbeslag.")

            # OPPGAVE 2: spør om spilleren vil åpne kisten.
            # Åpner hen den: legg "gullnøkkel" i inventar, og fortell hva hen fant.
            # Ellers: skriv at spilleren lar kisten stå.

        elif valg == "trappen":

            print()
            print("Halvveis opp reiser et stort troll seg foran deg.")
            print("INGEN PASSERER, brøler det.")

            troll = fiender["troll"]
            troll_liv = troll["liv"]

            # OPPGAVE 3: lag kampen her.
            # En while-løkke som går så lenge både trollet og spilleren lever.
            # Hver runde kan spilleren velge ANGRIP eller FLYKT.

            if troll_liv <= 0:

                print()
                print("Trollet faller. Bak det står en tung, låst dør.")

                # OPPGAVE 4: har spilleren "gullnøkkel" i inventar?
                # Ja: åpne døren, skriv seiersmeldingen, sett spiller = False.
                # Nei: fortell at døren er låst.

        else:
            print("Du blir stående. Ingenting skjer.")

    elif valg == "skogen":

        print()
        print("Trærne står tett. Noe rasler i buskene.")

        # OPPGAVE 5: lag to hendelser, og la terning(1, 2) avgjøre hvilken.
        # Den ene gir spilleren en helsedrikk.
        # Den andre koster liv.

    else:
        print("Du må velge SLOTTET eller SKOGEN.")

    # OPPGAVE 7: er liv 0 eller mindre?
    # Skriv GAME OVER, og stopp spillet.
