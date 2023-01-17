password = "kanza hashmi"

print("Hello Alu Tasin.")
user = str(input("Enter your password:"))
counter = 1

while user != password:

    if counter == 2:
        print("Hey Alu, ami tomar khalu, etai tomar last chance. Ebar jodi hoy bhul, kedekete pabe na kul")

    if counter == 3:
        print("Ha ha ha. Tor game ekhon amar dokhole. Ber ho tui")
        exit(1)

    user = str(input("Enter again: "))

    counter = counter + 1

print("Login Successful.Enjoy your visit to Alamin's Game")
