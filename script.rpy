define K = Character("Kauane")
define I = Character("Iara")
define R = Character("Raimundo")
define C = Character("Mãe Catirina")
define F = Character("Pai Francisco")
define audio.intro = 'audio/Musics/Intro.mp3'

transform slightleft:
    xalign 0.18
    yalign 1.0

label start:
    play music intro fadein 3.0

    scene car_bg

    show eileen happy at slightleft

    K "De novo, pra que?"

    # This ends the game.

    return
