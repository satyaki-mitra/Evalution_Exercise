class Room(object):
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    
    def go(self, direction):
        return self.paths.get(direction, None)
        
    def add_paths(self, paths):
        self.paths.update(paths)       
        

game_description = Room("Game Description",
"""
THE DRAGON ARMY HAS INVADED YOUR CASTLE AND WANT TO TAKE AWAY ALL THE GOLDS & DIAMONDS KEPT IN DIFFERENT LOCKERS.
THEY HAVE ALREADY SHOOT ALL YOUR CREW MEMBERS AND YOU'RE THE LAST SURVIVING MEMBER OF THE CASTLE.
YOUR AIM IS TO SAVE THE GOLDS AND DIAMONDS ANYHOW AND ESCAPE FROM THE CASTLE BY THE SECRET DOOR.
YOU'RE RUNNING THROUGH THE MAIN CORRIDOR TOWARDS THE GOLD ROOM.

WOULD YOU LIKE TO PLAY THIS GAME(YES/NO) ??  
""")

      
main_corridor = Room("Main Corridor",
"""     
THREE DRAGONS JUMP OUT SUDDENLY IN FRONT OF YOU. ALL OF THEM ARE DAMN CRUEL AND ARMED TOO.
YOU FORGOT TO LOAD THE GUN AND ONLY 3 BULLET LEFT WITH YOU.
NOW YOU'RE IN A SITUATION TO TAKE A PROMPT ACTION. EITHER YOU CAN SHOOT OR YOU CAN DODGE THE DRAGONS.
BUT IN CASE YOU SHOOT, THE DRAGONS WILL DIE ONLY IF YOU SHOOT AT THEIR HEADS DIRECTLY.
""")


first_level_winner = Room("First Level Winner",
"""
AHHH.... NICE. ALL THE DRAGONS ARE DEAD NOW.
YOU'VE MANAGED SOMEHOW TO HIT ALL THE BULLETS PERFECTLY TO THE AIM.
WELL DONE. BUT FROM NEXT TIME NEVER FORGET TO LOAD YOUR GUN BEFORE GOING FOR A BATTLE.
NOW KEEP RUNNING TOWARDS THE GOLD ROOM.
TYPE 'NEXT' FOR THE NEXT LEVEL OR 'BACK' TO GO BACK AT PREVIOUS LEVEL.
""")
   
             

gold_room = Room("Gold Room",
"""
YOU DO A DIVE ROLL INTO THE ROOM AND SCAN THE ROOM FOR MORE DRAGONS THAT MIGHT BE HIDING.
BUT IT'S QUIET, DEAD QUIET.
SUDDENLY YOU FIND A BLINKING RED LIGHT IN THE FARTHEST CORNER OF THE ROOM.
YOU RUN TOWARDS THE RED LIGHT. WITH NO TIME YOU FOUND A NEUTRON BOMB THERE,WITH WHICH THE RED LIGHT IS ATTACHED.
THERE ARE TOO MANY WIRES ATTACHED WITH THE BOMB. THRE'S NOT ENOUGH LIGHT IN THE ROOM SO THAT YOU CAN SEE THE WIRES PROPERLY.
BUT YOU NEED TO DEFUSE THE BOMB IMMEDIATELY. OTHERWISE THE CASTLE WILL BE BLOWN UP AND YOU'LL BE DEAD WITH YOUR GOLDS & DIAMONDS.
AFTER WATCHING CLOSELY, YOU CAN SEE TWO WIRES: A GREEN AND A YELLOW ONE WHICH ARE DIRECTLY ATTACHED WITH THE BOMB.
YOU'RE NOT FROM BOMB SQUAD AND YOU HAVE TO GUESS WHICH WIRE TO CUT SO THE BOMB GO DEFUSED.
""")


second_level_winner = Room("Second Level Winner", 
"""
THE RED LIGHT STOP BLINKING.
YES... YOU'VE DONE IT MAN, YOU EXCLAIMED.
NOW YOU RUSH TOWARDS THE GOLD LOCKER.
TYPE 'NEXT' FOR THE NEXT LEVEL OR 'BACK' TO GO BACK AT PREVIOUS LEVEL.
""") 
 
            
gold_locker = Room("Gold Locker",
"""
NOW YOU REACHED IN FRONT OF THE GOLD LOCKER AND FIND A KEYPAD ATTACHED ON THE LOCKER DOOR.
YOU NEED THE CODE OF THE LOCKER TO GET ALL THE GOLDS IN LOCKER.
IF YOU GET THE CODE WRONG, THE LOCK CLOSES FOREVER AND YOU CAN'T GET THE DIAMONDS.
THE CODE IF 5 DIGITS.
""")


third_level_winner = Room("Third Level Winner",
"""
THE LOCKER DOOR CLICKS OPEN.
NOW YOU CAN COLLECT THE GOLDS.
YOU PUT THE GOLDS IN A BAG AND TIE IT TIGHTLY AROUND YOUR BACK AND RUN TOWARDS THE DIAMOND ROOM.
TYPE 'NEXT' FOR THE NEXT LEVEL OR 'BACK' TO GO BACK AT PREVIOUS LEVEL.
""")

diamond_room = Room("Diamond Room",
"""
YOU DO A DIVE ROLL INTO THE DIAMOND ROOM AND SCAN THE ROOM FOR MORE DRAGONS THAT MIGHT BE HIDING.
YOU FIND IT QUIET.
YOU RUN TOWARDS THE LOCKER AND FIND THAT THE LOCKER IS NOT BROKEN YET.. SIGH OF RELEIF.
THERE'S A KEYPAD ATTACHED WITH THE LOCKER DOOR AND YOU NEED THE CODE TO GET THE DIAMONDS OUT.
IF YOU GET THE CODE WRONG, THEN THE LOCK CLOSES FOREVER AND YOU CAN'T GET THE DIAMONDS.
THE CODE IS 4 DIGITS.
""")


fourth_level_winner = Room("Fourth Level Winner",
"""
FINLLY YOU HAVE ARE ALMOST THERE AND REACHED SAFELY IN THE GARAGE.
YOU ARE TIRED YET DETERMINED TO ESCAPE FROM THE CASTLE.
OTHERWISE DRAGON ARMY WILL SNATCH ALL THE GOLDS AND DIAMONDS.
TYPE 'NEXT' FOR THE NEXT LEVEL OR 'BACK' TO GO BACK AT PREVIOUS LEVEL
""")


garage = Room("Garage",
"""
SEVEN CARS NUMBERED 1-7 ARE THERE IN THE GARAGE.
SOME OF THEM ARE DAMAGED.
YOU HAVE TO CHOOSE RANDOMLY ONE OF THEM TO ESCAPE.
WHICH ONE WOULD YOU CHOOSE ??
""")



the_end_winner = Room("The End Winner", 
"""
YOU'VE SAVED ALL YOUR GOLDS AND DIAMONDS! 
GOOD JOB !!!!
YOU ARE THE TRUE SOLDIER. 
YOUR PARENTS SHOULD BE PROUD OF YOU.
""")

the_end_looser = Room("The End Looser",
"""
SUCH A CARELESS YOU ARE. 
IT WAS THE LAST STEP TO ESCAPE FROM THE DRAGON ARMY AND SAVING ALL YOUR BELONGINGS
AND YOU FAILED IN THIS LAST STEP !!
BEING A MEMBER OF THIS CASTLE YOU DON'T EVEN KNOW WHICH CAR IS IN WELL CONDITION.
""")

death = Room("Death",
"""
YOUR GAME IS OVER.
SUCH A LOOSER.
ALL YOUR GOLDS AND DIAMONDS ARE OWNED BY THE DRAGONS NOW.
""")


game_description.add_paths({
    'yes' : main_corridor,
    'no' : game_description
})


main_corridor.add_paths({
    'shoot' : first_level_winner,
    'SHOOT' : first_level_winner,
    'dodge' : death,
    'DODGE' : death,
    '*' : main_corridor
})


first_level_winner.add_paths({
    'next' : gold_room,
    'NEXT' : gold_room,
    'back' : main_corridor,
    'BACK' : main_corridor,
    '*' : first_level_winner
})


gold_room.add_paths({
    'green' : second_level_winner,
    'GREEN' : second_level_winner,
    'YELLOW' : death,
    'yellow' : death,
    '*' : gold_room
})


second_level_winner.add_paths({
    'next' : gold_locker,
    'NEXT' : gold_locker,
    '*' : second_level_winner
})


gold_locker.add_paths({
    '51993' : third_level_winner,
    '*' : death
})


third_level_winner.add_paths({
    'next' : diamond_room,
    'NEXT' : diamond_room,
    'back' : gold_locker,
    'BACK' : gold_locker,
    '*' : third_level_winner
})


diamond_room.add_paths({
    '1857' : fourth_level_winner,
    '*' : death
})


fourth_level_winner.add_paths({
    'next' : garage,
    'NEXT' : garage,
    'BACK' : diamond_room,
    'back' : diamond_room,
    '*' : fourth_level_winner
})


garage.add_paths({
    '2' : the_end_winner,
    '7' : the_end_winner,
    '1' : the_end_winner,
    '3' : the_end_looser,
    '4' : the_end_looser,
    '5' : the_end_looser,
    '6' : the_end_looser
})

START = game_description
