print("🕵️ Fake Fan Finder 👀")
print("-------------------------")
qAnime = input("What is your favorite Anime?")
if qAnime == "One piece":
    qChar = input("Oh really?! Name me any of the characters?")
    if qChar == "Nami":
        qJob = input(
            "You got that by pure chance. Okay then, what is her job on the ship?"
        )
        if qJob == "Navigator":
            qBounty = input("Hmph! What was her first bounty then?")
            if qBounty == "16000000 berries":
                print("Fine! You're a genuine fan")
            else:
                print("Haha! See, you're a fake fan!")
else:
    print("I thought so!")
