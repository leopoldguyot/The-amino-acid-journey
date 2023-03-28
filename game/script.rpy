# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define glu = Character("Glucose")
define glu6 = Character("Glucose-6-phosphate")
define hex = Character("Hexokinase")
define liv = Character("Liver brigade")
define unk = Character("???")
define phos3 = Character("3-phosphoglycerate")
define dehy = Character("3-phosphoglycerate dehydrogenase")
define hydro = Character("3-phospho-hydroxypyruvate")
define mat = Character("Glutamate seller")
define phse = Character("3-phosphoserine-aminotransferase")
define seph = Character("Phosphoserine phosphatase")

# The game starts here.

label start:

    scene bg room

    "You wake up in an unknown place. You have absolutely no memory of what happened, the only thing you remember is your name: Glucose."

    show glucose at left:
        zoom 0.15

    glu "Where am I?"

    glu "What to do?"

    "Here are the questions you are asking yourself but unfortunately do not have the answer to. "

    glu "No choice, I'll have to walk around and hope to meet someone who can give me information."

    "You start walking around in the unknown place for long hours until you meet a nice-looking lady."

    show hexokinase at right:
        zoom 0.15

    glu "Hello Madam! Could you tell me where we currently are?"

    hex "Oh my poor child, you didn't see the sign when you arrived... Here we are on the outskirts of the cell. You just got absorbed. My name is Hexokinase. Little advice… If you want to live a good life you must become an amino acid. Don't worry, I will guide you and give you a little something."

    hide glucose
    show glucose-6-phosphate at left:
        zoom 0.15
    "At these words , Hexokinase hands you a bag which contains a phosphate group. Something changes in you; you feel that you are turning into Glucose-6-Phosphate. You barely have time to thank Hexokinase when she disappears. You can hear her whisper that you should follow the glycolysis."

    "Would you like to follow his advice?"

    menu :
        "Yes":
            jump glycolysis_starts
        "No !":
            jump glycogen_ending

label glycogen_ending:
    hide hexokinase
    show camion liver brigade at right:
        zoom 0.2
    "You decide not to take the advice of a stranger. After all, how do you know she's not lying? You continue to wander aimlessly around the cell until you come across a truck that says Liver Brigade on it.'"

    "A well-dressed men come out and say: "

    show liver brigadier at center:
        zoom 0.15

    liv " Hello! You have been selected to store energy with your colleagues."

    "You don't have time to react and you get locked in the truck. There are next to you many people who look like you. Finally you are locked in the liver, patiently waiting for your release day. "
    "You reached the Glycogen ending."
    return
label glycolysis_starts:
    hide hexokinase
    hide glucose-6-phosphate
    show 3-phosphoglycerate at left:
        zoom 0.15
    "Thanks to the advice and hints left by Hexokinase, you manage to start your social ascension and become a beautiful 3-phosphoglycerate. "

    phos3 "Hey guys, I'm feeling a little lost here. I don't know which way to go. Should I become Serine or Phosphoenolpyruvate?"

    menu :
        "Serine":
            jump serine
        "Phosphoenolpyruvate":
            jump phosphoenolpyruvate

label serine:
    "This humble 3-phosphoglycerate molecule was in a human cell. It was one of many metabolites circulating in the cytoplasm, without being particularly noticed. However, this molecule had higher ambitions and dreamed of becoming something more important."

    phos3 "Hello Madame 3-phosphoglycerate dehydrogenase! How beautiful you are! "

    show 3_phosphoglycerate deshydrogenase at right:
        zoom 0.15
    dehy "You impress me with your metabolic properties, little 3-phosphoglycerate. You have enormous potential, let me transform you with my magic potion of NAD+."

    "D-3-phosphoglycerate dehydrogenase then catalysed the conversion of 3-phospho-D-glycerate into 3-phospho-hydroxypyruvate, an even more important molecule in the energy metabolism of the cell. "

    "The 3-phospho-D-glycerate was delighted with its transformation into 3-phospho-hydroxypyruvate. It had succeeded in raising its social standing and had become an even more important molecule in the cell."
    hide 3_phosphoglycerate deshydrogenase

    hide 3-phosphoglycerate
    show 3-phospho-hydroxypyruvate at left:
        zoom 0.15
    "Soon after, it was Sunday, market day! "

    hydro "*It's a nice day, I'm going to go to the market! Oh but what do I see... it's the discount of the century!*"

    "The seller Glutamate was selling his properties at very attractive prices."
    show glutamate marchand at right:
        zoom 0.15
    hydro  "How can I use this glutamate packet?"

    mat "Go to Madame 3-Phosphoserine aminotransferase, she will know how to use them. You can find it in the cells of the liver, kidneys, brain or skeletal muscles."
    hide glutamate marchand

    show 3-phosphoserine at right:
        zoom 0.15
    "The 3-phospho-hydroxypyruvate arrived at the 3-phosphoserine-aminotransferase and opened its bag filled with small Glutamates. "

    hydro "How can I use them ?"

    phse "Close your eyes and let yourself be carried away. I will use the Glutamate you gave me to transform you, with my super powers, into 3-Phosphoserine and I will release 2-Oxoglutarate molecules."

    hydro "Sometimes things happen by chance !"

    "As she left the enzyme's office, it started to rain. The 3-Phosphoserine, now of high social standing, met its bodyguard, the Phosphoserine phosphatase. "

    seph "I'm going to hold your hand so that you don't slip on those H2O molecules."

    "They held hands and his bodyguard dephosphorylated the 3-Phosphoserine to Serine, which lost a phosphate, using the rain."

    seph "You can now help synthesise proteins, neurotransmitters, play a role in lipid metabolism or start the serine cycle. The choice is yours."


label phosphoenolpyruvate:


# TODO add color for mc