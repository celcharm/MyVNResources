# script.rpy - Game script

# Characters
define q = Character("Quinn", who_color="#069CF7", window_background="gui/textbox.png")
define l = Character("Locus", color="#F7E406")


# Start game
label start:

    # Show corridor background
    scene bg corridor
    with fade

    # Show Quinn character
    show quinn default
    
    q "Hi, I'm Quinn. Nice to meet you. I will be your study buddy from now on!"
    
    q "What's your name?"
    
##### User enters his/her name
    
    
    # Show Locus character
    show locus default
    
    q "And this is Locus! He's my best friend. If you have any questions, you can ask him too."
    
    show locus protest
    
    l "Hey, that's not fair. I never asked to be part of this."
    
    q "Oh be nice, come on. Anyway, don't worry about him. He's always like this to newbies, but he'll warm up to you soon."
    
    l "Look, I gotta go. Bye, Quinn."
    
    show locus orly 
    with dissolve
    
    l "Oh, and you... maybe I'll see you around."

    # End game
    return
