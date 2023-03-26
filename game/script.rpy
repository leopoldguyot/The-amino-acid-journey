# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define glu = Character("Glucose")
define hex = Character("Hexokinase")
define liv = Character("Liver brigade")
define unk = Character("???")
# The game starts here.

label start:

    scene bg room

    "You wake up in an unknown place. You have absolutely no memory of what happened, the only thing you remember is your name: Glucose."

    show glu

    glu "Where am I?"

    glu "What to do?"

    "Here are the questions you are asking yourself but unfortunately do not have the answer to. "

    glu "No choice, I'll have to walk around and hope to meet someone who can give me information."

    "You start walking around in the unknown place for long hours until you meet a nice-looking lady."

    show hex

    glu "Hello Madam! Could you tell me where we currently are?"

    hex "Oh my poor child, you didn't see the sign when you arrived... Here we are on the outskirts of the cell. You just got absorbed. My name is Hexokinase. Little advice… If you want to live a good life you must become an amino acid. Don't worry, I will guide you and give you a little something."

    "At these words , Hexokinase hands you a bag which contains a phosphate group. Something changes in you; you feel that you are turning into Glucose-6-Phosphate. You barely have time to thank Hexokinase when she disappears. You can hear her whisper that you should follow the glycolysis."

    "Would you like to follow his advice?"

    menu :
        "Yes":
            jump glycolysis_starts
        "No !":
            jump glycogen_ending

label glycogen_ending:
    "You decide not to take the advice of a stranger. Aftem*r all, how do you know she's not lying? You continue to wander aimlessly around the cell until you come across a truck that says Liver Brigade on it.'"

    "A well-dressed men come out and say: "

    show well_dressed

    liv " Hello! You have been selected to store energy with your colleagues."

    "You don't have time to react and you get locked in the truck. There are next to you many people who look like you. Finally you are locked in the liver, patiently waiting for your release day. "
    "You reach the Glycogen ending"
    return
label glycolysis_starts:

    "En allant vers la droite glucose croisa Godzilla !"
    show godzilla
    "voilà."
    return
