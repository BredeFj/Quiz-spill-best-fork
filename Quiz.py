# Quiz-spill
print("Velkommen til dette Quiz-spillet!")

# Spør brukeren om navn
navn = input("Hva heter du? ")

# Hils brukeren
print("Så kjekt at du vil være med " + navn + "!")

# Start poengsum på 0
poeng = 0

# Spørsmål 1
svar1 = input("Første spørsmål: Hva er hovedstaden i Norge? ")
if svar1.lower() == "oslo":
    print("Det er riktig! Godt jobbet :)")
    poeng +=1
else:
    print("Beklager, men det er feil svar.")

# Spørsmål 2
svar2 = input("Hva heter Norges nest største by? ")
if svar2.lower() =="bergen":
    print("Det er riktig! Godt jobbet :)")
    poeng +=1
else:
    print("Beklager, men det er feil svar.")

# Spørsmål 3
svar3 = input("Hva heter det beste fotballaget i Bergen? ")
if svar3.lower() == "brann":
    print("Det er riktig! Godt jobbet :)")
    poeng +=1
else:
    print("Beklager, men det er feil svar.")

# Avslutt og vis poengsum
print(f"Gratulerer {navn}! Du fikk {poeng} poeng!")
if poeng == 3:
    print("Godt jobbet! Du fikk full pott :)")
elif poeng == 2:
    print("Nokså bra jobbet. Nesten alt riktig :)")
elif poeng == 1:
    print("Du fikk 1 poeng riktig. Neste gang klarer du nok mer :)")
elif poeng == 0:
    print("Du fikk ingen riktige, men du har forhåpetligvis lært litt :)")