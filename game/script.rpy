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
define phosphoserine = Character("3-phosphoserine")
define seph = Character("Phosphoserine phosphatase")
define phmu = Character("Phosphoglycerate mutase")
define eno = Character("Enolase")
define phos2 = Character("2-phosphoglycerate")
define phpy = Character("Phosphoenolpyruvate")
define Phosphoenolpyruvate_transaminase = Character("Phosphoenolpyruvate transaminase")
define Pyruvate_kinase = Character("Pyruvate kinase")
define Tyrosine_aminotransferase = Character("Tyrosine aminotransferase")
define Pyruvate = Character("Pyruvate")
define Alanine_transaminase = Character("Alanine transaminase")
define Glutamic_acid = Character("Glutamic acid")
define Acetyl_CoA = Character("Acetyl-CoA")
define Pyruvate_Dehydrogenase = Character("Pyruvate Dehydrogenase")
define Citrate = Character("Citrate")
define Aconitase = Character("Aconitase")
define Isocitrate = Character("Isocitrate")
define Suspicious_man = Character("Suspicious man")
define Oxoglutarate_Dehydrogenase = Character("Oxoglutarate Dehydrogenase")
define alpha_ketoglutarate = Character("Alpha-ketoglutarate")
define Glutamate = Character("Glutamate")
define Glutamine = Character("Glutamine")
define Pyrroline = Character("1-Pyrroline-5-carboxylic acid")
define Ornithine_aminotransferase = Character("Ornithine aminotransferase")
define Ornithine = Character("Ornithine")
define Arginine = Character("Arginine")
define Proline = Character("Proline")
define Alanine = Character("Alanine")

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

    phos3 "I'm feeling a little lost here. I don't know which way to go. Should I become Serine or Phosphoenolpyruvate?"

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

    "3-phosphoglycerate dehydrogenase then catalysed the conversion of 3-phosphoglycerate into 3-phospho-hydroxypyruvate, an even more important molecule in the energy metabolism of the cell. "

    "The 3-phosphoglycerate was delighted with its transformation into 3-phospho-hydroxypyruvate. It had succeeded in raising its social standing and had become an even more important molecule in the cell."
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

    show phosphoserine transferase at right:
        zoom 0.45
    "The 3-phospho-hydroxypyruvate arrived at the 3-phosphoserine-aminotransferase and opened its bag filled with small Glutamates. "

    hydro "How can I use them ?"

    phse "Close your eyes and let yourself be carried away. I will use the Glutamate you gave me to transform you, with my super powers, into 3-Phosphoserine and I will release 2-Oxoglutarate molecules."

    hide 3-phospho-hydroxypyruvate
    show 3-phosphoserine at left:
        zoom 0.15

    phosphoserine "Sometimes things happen by chance !"

    hide phosphoserine transferase
    "As she left the enzyme's office, it started to rain. The 3-Phosphoserine, now of high social standing, met its bodyguard, the Phosphoserine phosphatase. "
    show phosphoserine phosphatase at right:
        zoom 0.15
    seph "I'm going to hold your hand so that you don't slip on those H2O molecules."

    "They held hands and his bodyguard dephosphorylated the 3-Phosphoserine to Serine, which lost a phosphate, using the rain."

    hide 3-phosphoserine
    show serine at left:
        zoom 0.5

    seph "You can now help synthesise proteins, neurotransmitters, play a role in lipid metabolism or start the serine cycle. The choice is yours."
    hide serine
    hide phosphoserine phosphatase
    show serine at center:
        zoom 0.54
    "You reached the Serine ending!"
    return


label phosphoenolpyruvate:

    "As she continued her journey, 3-phosphoglutarate met Phosphoglycerate mutase, who told her it’d help her transform into an amino acid."
    "But quickly, an argument began. "
    phos3 "Hey, Phosphoglycerate mutase, why do you keep turning me into something bigger? Don't you like me the way I am?"

    show Phosphoglycerate mutase at right:
        zoom 0.15

    phmu "Oh, come on, 3-Phosphoglycerate! It's not that I don't like you. It's just that I have a job to do."

    phos3 "But why do you have to make me bigger? Can't you turn me into something smaller or cuter?"

    phmu "I'm sorry, little buddy, but that's not how it works. Besides, you're already pretty cute in your own way."

    phos3 "Cute? Are you serious? I'm just a boring old molecule."

    phmu "Hey now, don't be so hard on yourself. You may not be the flashiest molecule out there, but you play an important role in the process of glycolysis."

    phos3 "Yeah, I guess you're right. But still, couldn't you at least turn me into something with a better name? 2-Phosphoglycerate sounds so much cooler."

    phmu "*chuckles* I know, right? I can't take credit for the name, but I have to admit, it does have a certain ring to it."

    phos3 "Ugh, fine. Go ahead and do your thing, but just remember that I'm watching you."

    phmu  "Don't worry, little buddy. You'll always be my favorite 3-Phosphoglycerate."

    hide 3-phosphoglycerate
    show 2-phosphoglycérate at left:
        zoom 0.15
    "In a magical momentum you turn into a 2-Phosphoglycerate"


    show enolase at left:
        zoom 0.15

    eno   "Excuse me, gentlemen. Sorry to interrupt your little chat, but I have a job to do as well."

    phos2 "Oh, hey Enolase. I was wondering when you were going to show up. Watch it, Enolase. You know I'm the coolest molecule in this pathway."

    eno "Oh, please. You're just a stepping stone on the way to something much more exciting."

    phos2 "Excuse me? I am not a stepping stone. I am a vital part of this process."

    eno "*grinning* Relax, I'm just teasing you. But let's be real, the real star of the show is me. I'm the one who transforms you into the highly reactive Phosphoenolpyruvate."

    "The Enolase ate the 2-Phosphoglycerate through its catalytic site and then spit out a Phosphoenolpyruvate."

    hide 2-phosphoglycerate
    show phosphoénolpyruvate at left:
        zoom 0.15

    phpy "But you are crazy in the head! Do it more gently next time, I was shaken like in a washing machine."

    "Enolase and phosphoglycerate mutase went away discussing what they were going to do with their evening, you were now alone."

    phpy "Let's continue this adventure! What can I do now ?"

    "Two molecules approaches"
    show Phosphoenolpyruvate transaminase at center:
        zoom 0.15
    Phosphoenolpyruvate_transaminase "Hey there, Phosphoenolpyruvate! Come with me, it will be funny. I can transform you with the help of the enzyme Phosphoenolpyruvate transaminase."
    show Pyruvate kinase at center:
        zoom 0.15
    Pyruvate_kinase "Welcome, Phosphoenolpyruvate! I can help you accomplish your journey. We'll undergo a dephosphorylation reaction, and you'll be transformed into a super molecule !"

    phpy "*Who should I trust? Phosphoenolpyruvate transaminase or Pyruvate kinase ? The choice is difficult...*"

    menu:
        "Go with Phosphoenolpyruvate transaminase":
            jump Phosphoenolpyruvatetrans

        "Go with Pyruvate kinase":
            jump Pyruvatekin


label Phosphoenolpyruvatetrans:

    hide Pyruvate_kinase
    phpy  "Let's go with Phosphoenolpyruvate transaminase, he looks funny !"

    Phosphoenolpyruvate_transaminase "Exciting! You're on the right track. Let's begin by undergoing a transamination reaction with my help. This will transform you into a precursor molecule for Tyrosine."

    hide Phosphoenolpyruvate
    show 3-Phosphohydroxypyruvate at left:
        zoom 0.15
    "You now evolved into 3-Phosphohydroxypyruvate !"

    "A friend of Phosphoenolpyruvate transaminase appears !"
    show Tyrosine aminotransferase at center:
        zoom 0.15
    Tyrosine_aminotransferase "Hello, u did Great progress! Now that you're 3-Phosphohydroxypyruvate, I can help you become Tyrosine. I'll need to oxidatively decarboxylate you. You'll be Tyrosine in no time!"

    hide 3-Phosphoenolpyruvate
    show Tyrosine at left:
        zoom 0.15
    "... Felicitation you evolved into Tyrosine, you will now live an happy life, maybe you will join other amino acids to build an peptid or you will serve as precursor for severals neurotransmitters such as dopamine and adrenaline"
    "You reached the Tyrosine ending !"
    return

label Pyruvatekin :

    phpy "I want to become a super molecule, let's choose Pyruvate kinase !"

    hide phosphoenolpyruvate transaminase

    Pyruvate_kinase "Exciting! I can help you achieve your goal. Let's begin by undergoing a dephosphorylation reaction with the help of my enzyme. You'll be Pyruvate in no time!"

    hide 3-Phosphoenolpyruvate
    show pyruvate at left:
        zoom 0.15

    "In the blink of an eye, you transform into Pyruvate and you are ready to continue your journey."
    hide Pyruvate kinase
    #partie elfie

    "Now that it became a pyruvate, our former glucose was feeling that it was not so far from its goal. Continuing its journey, it kept going until it saw a warning message on a phospholipidic membrane. It said :"

    "“Pyruvates, beware, here starts the domain of the gluconeogenesis sect. Pay attention to the enzymes that will speak to you, some of them are the start of a chain of pyruvate trafficking that will take you back to the glucose stage.”"

    Pyruvate  "Wow, I didn’t know that such bad guys could exist, I’ll take good note of this warning message. Let’s be careful on the way."

    Pyruvate  "Nevertheless, what’s the next step now ? I can feel that I’m becoming stronger and stronger, I can’t wait to see what amino acid I’m going to transform into."

    "Hearing these words, an old lady started to approach our little pyruvate."
    show Alanine transaminase at right:
        zoom 0.15
    unk  "Dear Pyruvate, I just heard that you desire to transform into an amino acid. And I just know the way to help you doing so."

    "Pyruvate, initially on the defensive in front of this unknown enzyme coming out of nowhere, approached and asked:"

    Pyruvate  "And how can you help me doing so ? I know that some evil people transform pyruvates like me into glucose. I won’t be trapped so easily."

    unk "You don’t have to worry. My name is alanine transaminase, and as you can hear by my name, I’m a direct servant of the alanines, one of the amino acid clans ruling over this world."
    Alanine_transaminase "My purpose is to help pyruvates like you to access the rank of alanine. Like we say, the more the merrier ! Alanines are strongly lacking in the world right now, so it would be a big help if you’d consider becoming one. So, what will you do ?"

    "What could pyruvate do ? The threat of going back to the glucose stage was indeed a big one, but the opportunity to finally become an amino acid was too tempting, and the old lady had a warm and charming aura."

    menu:

        "Follow Alanine":
            jump Alanine

        "Don't follow Alanine":
            jump acetyl


label Alanine:

    Pyruvate "Okay, I’ll go with you"
    Alanine_transaminase  "Good choice, my young Pyruvate. Come with me, I’ll present you to my friend glutamic acid. He will help us in the process to become an alanine"

    "You follow the old lady, and finally meet glutamic acid. "
    show Glutamic acid at center:
        zoom 0.15
    Glutamic_acid  "Here, take my amine residue. Alanine transaminase will be able to make you absorb it to become a full-fledged alanine."

    "And as he spoke these words, alanine transaminase merged pyruvate and the amine residue together, finally transforming our former glucose into one of the so famous amino acids, an alanine."
    hide Pyruvate
    show Alanine at left:
        zoom 0.15
    "Now our alanine would finally be able to help the cell creating proteins, one of the most important creations in which a molecule could dream to take part in."
    "Alanine noticed after his transformation that a part of him had transformed into an alpha-ketoglutarate, which started going away, in quest of itself becoming an amino acid."
    "You reached the alanine ending !"
    return

label acetyl:
    Pyruvate "You look like a supporter of the gluconeogenesis sect. I won’t become a glucose again !"

    "And there you go, fleeing away from the old lady, giving her no time to say another word. Who knows, she could have really been here to make you access to the rank of alanine, but you can never be too careful."
    "You traveled for too long to start over from the beginning of your journey. "
    "But as soon as he started walking away from the old lady, he got kidnapped by another mysterious enzyme which blinded the pyruvate to take it to a mysterious place. "

    "Once arrived, the enzyme transformed pyruvate into an acetyl-CoA, leaving our pyruvate no choice.  "
    hide Pyruvate
    show acetyl-coA at left:
        zoom 0.15

    Acetyl_CoA  " What the heck are you doing !? Give me my old form back ! How dare you treat other molecules like that ?"

    "The mysterious enzyme answered, in a dry and cutting tone :"

    unk "Sometimes you can’t become what you want, that’s life. You wouldn’t have listened to me if I came talking to you in an orthodox way, seeing how you treated alanine transaminase."

    Acetyl_CoA "What did you do to me ? I swear that if you prevent me from achieving my goal, I will show no mercy. I’ll struggle until the end."

    unk "Calm down, I didn’t transform you into an Acetyl-CoA for nothing. It was to permit you to access to the Krebs Cycle, which can lead to multiple amino acids."
    unk "I brought you to a mitochondria to accomplish the first step of your transformation."
    unk "But if you sincerely want to succeed, you’ll have to listen to me really carefully, and also to become a citrate. By the way, my name is Pyruvate Dehydrogenase"

    "Hearing these words, Acetyl-CoA was really confused. He realized that he didn’t really had a choice, since it seemed too late to become a pyruvate again."
    "In top of that, he could see that he was in a place that looked like the inside of a mitochondria, which reinforced the words of the mysterious enzyme."

    Acetyl_CoA "You really don’t leave me the choice. So, how can I became your so-called citrate ?"

    Pyruvate_Dehydrogenase  "Here are my friends oxaloacetate and citrate synthase. I’m sure that you understand by their names what is going to happen."

    "And without wasting any more time, he tied us all three and locked us in a dark room. You come out a minute later, transformed into citrate."
    hide acetyl-coA
    show citrate at left:
        zoom 0.15
    "You have visibly merged with oxaloacetate, with the help of citrate synthase."

    Pyruvate_Dehydrogenase  "I will now leave you free. I advise you to be really careful on your journey, the Krebs Cycle is not a kind place."

    "Left to your own devices, you continue to move forward, traumatized by the turn events have just taken."
    "You encounter, within the Krebs cycle, a sign indicating two directions."

    menu:
        "Go to the left":
            jump left
        "Go to the right":
            jump right

label left:

    "You don’t really know how useful can a sign that indicates nothing except a direction be, but you decide to just go to your left."
    "And there, you hear a great ruckus coming from far away. You look away and seem to see a great massacre approaching... You?? "
    "You try to run away, but the tragedy is inextricably approaching : you can now see that ROS have invaded the cell, and that you're going to be torn apart in seconds."
    "You remember all your memories from your glucose form, and you shed a tear thinking of your comrades and your unfinished goal... "
    "You reached the ROS Clivage ending"
    return

label right:

    "You don’t really know how useful can a sign that indicates nothing except a direction be, but you decide to just go to your right. "
    "You start seeing another enzyme on your way. You can't take the enzymes anymore, so you go talking to him, in despair of your situation."
    "Better to face danger than to get kidnapped while avoiding it... "

    Citrate "Do you know the way I could become an amino acid please ? Anything can do, cut me in two if you want..."
    show aconitase at right:
        zoom 0.15
    unk "Yes, hello to you too ... Do I look like someone that could cut you in half ?"
    unk  "Such irrespect... However, I know the way to make you progress towards your goal, and for that you will have to merge with another citrate. My name is aconitase, by the way."

    "The perspective of merging with one of my siblings wasn’t the best one, but you don’t have any other option. Therefore, you accept."
    "The old man brings you to another citrate which according to aconitase ,had arrived here a bit earlier. He proceeds with the fusion, transforming you too in an isocitrate."
    hide citrate
    show isocitrate at left:
        zoom 0.15

    Isocitrate  "That’s a weird feeling...I feel like I lost a water molecule and won a hydroxyl group. Don’t tell me there’s more next ?"

    Aconitase  "I’ll present you to my collegue Isocitrate Dehydrogenase, he will catalyze the oxidative decarboxylation that will make you attein your next stage, the alpha-ketoglutarate."

    "You follow Aconitase to his collegue’s place, with a heavy heart. You have just absorbed the consciousness of one of your fellows."
    "Along the way, you wonder how many sacrifices and trials you will have to go through in order to reach your goal. "
    "There, Isocitrate Dehydrogenase performs the catalyzation, making you lose a CO2 molecule, and bringing you one step closer to the end of your journey."

    hide isocitrate
    show alpha-ketoglutarate at left:
        zoom 0.15
    "You now continue on your way, as an alpha-ketoglutarate."

    "If there's one thing you know, it's that you are closer to your goal than you have ever been."
    "You continue your journey through the mitochondria until you come across a suspicious looking man.  "

    show oxoglutarate_dehydrogenase at right:
        zoom 0.15
    Suspicious_man "Psst, stranger do you want this ?"

    "The man hands you Coenzyme A  "

    Suspicious_man "You should take it, it’s good for you."

    "You feel kind of reluctant. "

    Oxoglutarate_Dehydrogenase "Why would I lie to you, I’m the famous Oxoglutarate Dehydrogenase after all! "

    menu:

        "Take the CoA":
            jump coA

        "Let the CoA":
            jump let

label let:

    alpha_ketoglutarate  "Thank you old man but I refuse."

    alpha_ketoglutarate  "I think it would be better for me to leave the mitochondria and go back into the cytosol."
    hide Oxoglutarate_Dehydrogenase
    "You reach the cytosol and you see two people arguing at the end of a path. "

    "One of the two men is quite muscular, and he doesn't seem to be a native. He looks annoyed."
    show alanine at right:
        zoom 0.15

    show aminotransferase at right:
        zoom 0.15
    Alanine  "Please, I came all the way from Muscleland and I really need this oxygen for my family. I can even give you my amine... Please Aminotransferase..."

    Aminotransferase "Sorry Alanine. I really want to help you, but I can’t."

    "After finishing its sentence, Aminotransferase notices you."

    Aminotransferase "Hey you! Do you have any oxygen that you could trade for an amine?"

    menu:
        "Accept":
            jump accept
        "Refuse":
            jump refuse

label refuse:
    alpha_ketoglutarate  "Sorry. I don’t have any oxygen that I could trade."
    hide alanine
    hide aminotransferase

    "You continue your journey until you come across a job ad that looks like it pays well. You see in small print: 'Ketones only.'"

    alpha_ketoglutarate "I should apply or I will be starving"

    "You call the number that says you start work tomorrow."
    "When you arrive, you are asked to get ready and without your opinion, you are taken directly to the brain to be used as fuel."

    "You reached the ketone body ending"
    return

label accept:
    alpha_ketoglutarate "Yes of course! Here is my oxygen."
    hide alpha_ketoglutarate
    show glutamate at left:
        zoom 0.15
    "You receive your amine and you feel it, now you really are an amino acid; the Glutamate. The elite of the society."
    "However, something inside you told you that you could go further, that you had not reached your full potential. "

menu:
    "Try to go further":
        jump further
    "Stop here and live a peaceful life":
        jump stop

label stop:

    "Glutamate I think my journey ends here… Finally, an amino acid. I’ve dreamed of becoming one for so long. Maybe one day I will become a protein."
    "I’m so happy… Thank you mister Aminotransferase, thank you Alanine. Farewell."
    hide alanine
    hide aminotransferase
    "You decide to leave and look for a place to settle down."
    "Tears run down your cheeks, they are tears of joy."

    "You reached the Glutamate ending !"
    return
label further:
    Glutamate "Thank you but I have to go. I’ve got a lot of things to do. "
    hide alanine
    hide aminotransferase
    "You decide to continue your journey."

    Glutamate "I know it. I know that I could be better than my current state. I must."

    "While you’re walking, something catches your eye. You can read “Glutamine synthetase”."

    Glutamate "OH! I should go there. I shall get information about amino acid."

menu:
    "Enter the building":
        jump center
    "Don't enter":
        jump dont

label enter:

    "You enter the building, but you don’t see anybody. Actually, you can’t see at all."
    "Suddenly, you fall asleep. "
    "You wake up outside the building without remembering what happened. You really don't feel well but you are a Glutamine.In fact, you have lost a carboxylic acid to an amide."
    hide glutamate
    show glutamine at left:
        zoom 0.15
    Glutamine "I have transformed again but at what cost? Maybe I should stop and stick to glutamine. After all, if events of this type still occur, what's the point of climbing the social ladder?"

    "You decide to stop your journey right here. You are now a Glutamine, you’ll probably find your use in the society. You will eventually become a protein."

    "You reached the Glutamine ending !"
    return

label dont:
    Glutamate"No I shouldn't go in, this building seems very suspicious."

    "You pass by the building without entering it. "

    "You start thinking that you could start going to college. With your ATP savings you enroll in college."

    "Your first teacher is the Glutamate-5-kinase. Thanks to its lessons, you become a Glutamate-5-semialdehyde."
    "During the second semester, courses are given by Glutamate-5-semialdehyde dehydrogenase."
    "With a lot of work and NADH supplied, you eventually become a 1-Pyrroline-5-carboxylic acid."

    hide glutamate
    show 1-Pyrroline-5-carboxylic acid at left:
        zoom 0.15
    Pyrroline "It was a though year."
    "You are now entering your second year."
    "Courses are given by the Ornithine aminotransferase."
    "After a year even more difficult than the first one, you become Ornithine. At the end of the year, Ornithine aminotransferase has a speech to make. "
    hide 1-Pyrroline-5-carboxylic acid
    show Ornithine at left:
        zoom 0.15
    show Ornithine_aminotransferase at right:
        zoom 0.15
    Ornithine_aminotransferase "Dear students, next year will be your last as a student. You have the possibility to do it abroad if you wish. But think about it, it is not a choice to be taken lightly. It could affect your future."

    Ornithine "Oh it could be really cool. Perhaps I should apply."

    menu:
        "apply !":
            jump apply
        "don't apply":
            jump noapply

label apply:

    "When you get home, you complete the registration form and hand it in the next morning."
    "Three weeks later, you have an answer, you have been accepted to the urea cycle. "

    Ornithine "YES! It was my first choice."

    "Time passes and at the end of your exchange, you have become an Arginine. Thanks to this you will be able to do a job you like."
    hide Ornithine
    show Arginine at left:
        zoom 0.15
    "You reached the Arginine ending !"
    return

label noapply:

    Ornithine "I'm not really interested by that. I think I will stay here."

    "You decide to stay for your senior year and finally become a Proline."
    hide Ornithine
    show Proline at left:
        zoom 0.15
    Proline "Finally… I am finally an amino acid. It was a though journey, but a good one."

    "You reached the Proline ending !"
    return
    # TODO add color for mc
