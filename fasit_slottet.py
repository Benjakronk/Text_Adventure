"""
FASIT - Det glemte slottet

En mulig løsning på de sju kodeoppgavene i steg 2. Ikke den eneste riktige.
De frivillige ekstrautfordringene (helsedrikk i kamp, poeng, nye steder,
flere avslutninger) er med vilje ikke tatt med her.

Til lærer: elevfilen heter slottet.py og ligger i samme mappe.
"""

import random

# ---------- VARIABLER ----------

liv = 10
inventar = []
spiller = True

# ---------- DICTIONARY ----------
# Alt vi trenger å vite om en fiende ligger samlet på ett sted.

fiender = {
    "troll": {"liv": 8, "min_skade": 2, "maks_skade": 4},
    "rotte": {"liv": 2, "min_skade": 1, "maks_skade": 2},        # OPPGAVE 6
}

# ---------- FUNKSJONER ----------

def vis_status():
    # OPPGAVE 1
    print("Liv:", liv)

    if len(inventar) == 0:
        print("Sekken er tom.")
    else:
        print("I sekken:")
        for ting in inventar:
            print(" -", ting)


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

            # OPPGAVE 2
            svar = spor("Vil du ÅPNE kisten? ")

            if svar == "åpne":
                if "gullnøkkel" in inventar:
                    print("Kisten er allerede tom. Du har tatt det som lå her.")
                else:
                    inventar.append("gullnøkkel")
                    print("Lokket knirker opp.")
                    print("Inni ligger en liten GULLNØKKEL. Du legger den i sekken.")
            else:
                print("Du lar kisten stå urørt.")

        elif valg == "trappen":

            print()
            print("Halvveis opp reiser et stort troll seg foran deg.")
            print("INGEN PASSERER, brøler det.")

            troll = fiender["troll"]
            troll_liv = troll["liv"]

            # OPPGAVE 3
            while troll_liv > 0 and liv > 0:

                svar = spor("ANGRIP eller FLYKT? ")

                if svar == "angrip":

                    skade = terning(1, 4)
                    troll_liv = troll_liv - skade
                    print("Du treffer trollet for", skade, "skade.")

                    if troll_liv > 0:
                        tilbake = terning(troll["min_skade"], troll["maks_skade"])
                        liv = liv - tilbake
                        print("Trollet slår tilbake, og du mister", tilbake, "liv.")
                        print("Liv igjen:", liv)

                elif svar == "flykt":
                    print("Du kaster deg ned trappen igjen.")
                    break

                else:
                    print("Trollet venter. Du må velge.")

            if troll_liv <= 0:

                print()
                print("Trollet faller. Bak det står en tung, låst dør.")

                # OPPGAVE 4
                if "gullnøkkel" in inventar:
                    print("Nøkkelen passer. Låsen klikker.")
                    print("Bak døren ligger slottets gamle skattkammer.")
                    print("Du har funnet skatten. DU VANT!")
                    spiller = False
                else:
                    print("Døren er låst. Et sted i slottet finnes en nøkkel.")

        else:
            print("Du blir stående. Ingenting skjer.")

    elif valg == "skogen":

        print()
        print("Trærne står tett. Noe rasler i buskene.")

        # OPPGAVE 5 og 6
        hendelse = terning(1, 2)

        if hendelse == 1:
            if "helsedrikk" in inventar:
                print("Du leter i gresset, men finner ingenting denne gangen.")
            else:
                inventar.append("helsedrikk")
                print("Du finner en liten flaske i gresset.")
                print("Det er en HELSEDRIKK. Du legger den i sekken.")
        else:
            rotte = fiender["rotte"]
            skade = terning(rotte["min_skade"], rotte["maks_skade"])
            liv = liv - skade
            print("En diger rotte kaster seg mot leggen din.")
            print("Du rister den av deg, men mister", skade, "liv.")

    else:
        print("Du må velge SLOTTET eller SKOGEN.")

    # OPPGAVE 7
    if liv <= 0:
        print()
        print("GAME OVER")
        spiller = False
