# Defining an image
image pic_start = "start.jpg"
image pic_1 = "game jam pic1.jpg"
image pic_2 = "pic 2.jpg"
image pic_3 = "pic 3.jpg"
image pic_4 = "pic 4.jpg"
image pic_5 = "pic 5.jpg"
image pic_6 = "pic 6.jpeg"
image pic_7 = "img 7.jpg"
image pic_8 = "img 8.jpg"
image pic_9 = "pic 9.jpg"
image pic_10 = "img 10.jpg"
image pic_11 = "img 11.jpg"
image pic_12 = "img 12.jpg"
image pic_13 = "img 13.jpg"
image pic_14 = "img 14.jpg"
image pic_15 = "img 15.jpg"
image pic_16 = "img 16.jpg"
image pic_17 = "img 17.jpg"
image pic_18 = "img 18.jpg"
image pic_19 = "img 19.jpg"



scene pic_start at truecenter

label start:

    # Ask the player for their name

    $ player_name = renpy.input("What is your name?")

    # Ensure the name isn't empty
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Steve"  # Default name if no input is given

    # Use the player's name in dialogue

    scene pic_1 at truecenter

    "[player_name] wakes up in your bed and this is the first day in your uni life. The alarm is ringing."

label chose1:

    scene pic_2 at truecenter

    "You haven't fallen in love for the past 18 years of your life so you decide not to waste your time in uoft. "

    menu:
        "Going to uni":
            jump going_uni  # Jumps to the open_box label

        "Not going to uni (Are you serious!? You can’t drop out of the university.) ":
            jump drop_uni  # Jumps to the leave_box label

label going_uni:

    scene pic_3 at truecenter

    "You finally arrive at your first class which is Game Design."

    "Your teacher is Steve. He is a handsome guy and the inevitable thrill comes to your heart. This handsome man exudes wisdom and he is obviously your dream lover."
    
    "You are thinking about the chance to express your love to Steve. "

    scene pic_4 at truecenter

    "Finally, the chance comes; Steve is teaching the class about coding. To let your computer output some words, you need to try this code: print('hello world')"

label chose2:

    scene pic_5 at truecenter

    "You are so happy to find out about this chance. Now you decide to enter..."

    menu:
        "I love you, Steve!": 
            jump love_steve 

        "Hello, World":
            jump not_love_steve

label love_steve:

    scene pic_6 at truecenter

    "Every classmate’s output sentence has appeared on the whiteboard screen. Your confession of love is extraordinarily conspicuous."

    "You find that Steve’s face turns red. Is it a sign of acceptance? Is it because he is shy? Oh… here must be your chance… "

label steve_answer:

    scene pic_7 at truecenter

    "Steve: How dare you!"

    "You are shocked. It seems that you do not attract Steve. He breaks your imagination of love in person. Oh… love… Oh… LOVE… How poor you are!"

    "Your classmates burst into laughter. You know they don’t have malicious, but you still get ashamed. However, one of your classmates, Jamie, doesn’t laugh at you!"

    scene pic_8 at truecenter

    "You are touched. What a lovely person! Jamie must be your Mr. Right. You should find some time to confess your love… "

    "The class ends. Jamie leaves the classroom alone. You follow him quietly and suddenly pat him on his shoulder. He is surprised."

    "Jamie: Oh, [player_name]! It’s nice to see you. What’s up?"

    "[player_name]: Jamie, thank you so much for not laughing at me."

    "Jamie: (shamed) I just feel like I should not do so… I guess you typed the sentence by mistake…"

    menu:
        "To be honest, I love you, Jamie, you are the only person who really knows me!":
            jump love_jamie
        
        "Jamie, you are such an idiot! It was not a mistake. I expressed my true feelings.":
            jump not_love_jamie

label love_jamie:

    scene pic_10 at truecenter

    "Jamie: How dare you!"

    "I don’t really know much about you. It is not suitable to fall in love with you."

    jump jamie_left

label not_love_jamie:

    scene pic_10 at truecenter

    "Jamie: How dare you!"

    "It is not going to be an equal relationship even if you succeed!"

    jump jamie_left  

label jamie_left:

    scene pic_11 at truecenter

    "Jamie has left."

    scene pic_12 at truecenter

    "You return to your residence with a sigh."

    "It is so difficult to find a lover, even if you enter the university!"

    "You decide to surf the Internet for a bit of comfort."

    "An advertisement draws your attention."

    scene pic_13 at truecenter

    "Looking for love? Here we are! Love agency, your satisfaction is guaranteed! Visit us at 666 Fools Street."

    menu:
        "Go!":

            jump go

        "Don’t go":

            jump dont_go

label dont_go:

    "You feel quite bored and fall asleep gradually. You missed the chance to find out what is love."  #bad ending with picture of it

label go:

    scene pic_14 at truecenter

    "You arrive at the address in the ad, but no one is there but a dilapidated building."

    "While you are wondering, a sudden attack hit your head. You faint…"

    scene pic_15 at truecenter

    "When you open your eyes again, you find that you are tied to a chair and cannot move at all."

    "A kidnapper shows up and he asks you to call your family. Give me a million dollars or death!"

    "At this moment, two familiar figures appeared."

    "They were Steve and Jamie"

    scene pic_17 at truecenter

    "They quietly appeared behind the kidnapper, holding a large frying pan."

    "With a clang sound, the kidnapper fell to the ground, and the sirens sounded."

    "Steve&Jamie: Go back"

    "[player_name]: I don’t know how to express my gratitude now, but how did you figure out I was cheated and kidnapped?"

    "Jamie: I am guilty about shouting at you… so I followed you when you went home and wanted to apologize to you."

    "Jamie: I saw you left home and headed to a strange place, I was worried you were facing danger as you entered the building for a long while, so I called Steve to assist me…"

    "Steve: Yes, that’s how we find out you are kidnapped!"

    scene pic_19 at truecenter
    
    "You talk about your experience of being cheated. Steve and Jamie laugh and pat you on your shoulder."

    "Steve: If you want to find your love, it should be an equal relationship, based on sufficient understanding of each other. You are not able to seek true love from random feelings! And next time, don’t get cheated by these ads online!" 
    #good ending

    jump good_end

label not_love_steve:
    "You don’t know why, your finger can’t help shaking, which makes it “I LOVE YOU, STEVE!” instead."

    jump chose2


label drop_uni:
    "Are you serious!? You can’t drop out of the university."
    
    jump chose1

label good_end:

    "Ends"
    #happy ending picture

    return

return