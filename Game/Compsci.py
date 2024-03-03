#Danny Yang
#Educational Map Design
#05/29/2020

import pygame,random

#Initializes and opens the pygame window
pygame.init()
win = pygame.display.set_mode((1200,800))

#Colours used
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#Sets the location and the direction and speed the player moves
playerX = 500
playerY = 700
playeroutsideX = 0
playeroutsideY = 700
direction = "left"
speed = 25

#Changes the location of the map 
mapX = 0
mapY = 0

#Fonts used
font = pygame.font.SysFont('Calibri', 60)
font2 = pygame.font.SysFont('Arial', 50)
font3 = pygame.font.SysFont('Calibri', 30)
font4 = pygame.font.SysFont('Trebuchet_MS',40)
font5 = pygame.font.SysFont('Segoe_UI',30)

#Sets a FPS timer 
FPS = 30
FPS_Clock = pygame.time.Clock()

#Music and Sound used
pygame.mixer.music.load("music.ogg")
pygame.mixer.music.play(loops = -1)
highscore = pygame.mixer.Sound("highscore.wav")

#Images used
outside = pygame.image.load("outside.png")
tile = pygame.image.load("tiles.png")
player = pygame.image.load("player.png")
geogame = pygame.image.load("geogames.png")
mathgames = pygame.image.load("mathgames.png")
musicgames = pygame.image.load("musicgame.png")
shop = pygame.image.load("shop.png")
treble_clef = pygame.image.load("music.png")
note = pygame.image.load("note.png")
note_flipped = pygame.transform.rotate(note,180)
canada = pygame.image.load("canada.png")
playagain = pygame.image.load("play again.png")
skip_tutorial = pygame.image.load("skip tutorial.png")
gamer = pygame.image.load("gamer.png")
gamer2 = pygame.image.load("gamer2.png")
textbox = pygame.image.load("textbox.png")

#Objects in the Arcade
mathgames_rect = pygame.Rect(0,0,100,800)
geogames_rect = pygame.Rect(1100,0,100,800)
music_rect = pygame.Rect(400,400,400,200)
arcade_top = pygame.Rect(0,0,1200,0)
arcade_bottom = pygame.Rect(0,800,1200,0)
shop_rect = pygame.Rect(300,0,600,200)
gamer_rect = pygame.Rect(100,400,100,100)
gamer2_rect = pygame.Rect(1000,700,100,100)

#Objects outside
house_rect = pygame.Rect(0,0,1800,600)
arcade_rect = pygame.Rect(2100,0,1000,600)
grass_rect = pygame.Rect(0,900,3100,200)
border = pygame.Rect(0,0,3100,1100)
door_rect = pygame.Rect(2500,600,200,100)

#Rects to interact with the games
play_mathgames = pygame.Rect(0,0,125,800)
play_musicgames = pygame.Rect(400,375,400,250)
play_geogames = pygame.Rect(1075,0,150,800)

#Rects to interact with the people
gamer_talk_rect = pygame.Rect(75,375,150,150)
gamer2_talk_rect = pygame.Rect(975,675,150,150)
shop_talk_rect = pygame.Rect(800,0,125,200)

#Rect to interact with the sign
sign_rect = pygame.Rect(1800,0,300,25)

#List of the objects used
arcade_objects = [gamer_rect,gamer2_rect,geogames_rect,mathgames_rect,music_rect,arcade_top,arcade_bottom,shop_rect]
outside_objects = [house_rect,arcade_rect,grass_rect]

#Sets the current location or game
play = "Outside"

#Sets the tutorial to not trigger when playing the game again
mathtutorial = 1
geotutorial = 1
musictutorial = 1

#Sets the current status of the conversation to not talk again
gamertalk = 1
gamer2talk = 1
shoptalk = 1

#Current highscores of the games
math_highscore = 0
geo_highscore = 0
music_highscore = 0

#Starts the gameover screen
def gameover():
    win.fill(white)
    highscoreplayed = False
    if play == "mathgame":
        graphics = font2.render("GAME OVER  |  Points:" + str(points) +" Highscore:" + str(math_highscore),1, red)
    elif play == "musicgame":
        graphics = font2.render("GAME OVER  |  Points:" + str(points) +" Highscore:" + str(music_highscore),1, red)
    else:
        graphics = font2.render("GAME OVER  |  Points:" + str(points) +" Highscore:" + str(geo_highscore),1, red)
    win.blit(graphics, (200, 375))
    pygame.display.update()

#Main loop
while True:
    while play == "Outside": #Plays the outside scene
        #FPS Clock
        FPS_Clock.tick(FPS)

        #Takes the events to know what buttons were pressed
        pygame.event.clear()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_c]: #Uses the C key to interact 
            player_rect = pygame.Rect(playeroutsideX,playeroutsideY,100,100) #Player Rect to know if you interact with the sign or the door
            if player_rect.colliderect(sign_rect):#If you interact with the sign it starts the sign scene
                play = "sign"
            elif player_rect.colliderect(door_rect):#If you interact with the door you enter the arcade
                play = "Arcade"
                
                
        elif keys[pygame.K_LEFT]:#Makes you move left when you hit the left key and changes the player's direction
            direction = "left"
            player_rect = pygame.Rect(playeroutsideX - speed,playeroutsideY,100,100)

            #Moves the player if they will not hit the objects
            if player_rect.collidelist(outside_objects) == -1 and player_rect.colliderect(border):
                playeroutsideX -= speed
                
                
        elif keys[pygame.K_RIGHT]:#Makes you move right when you hit the right key and changes the player's direction
            direction = "right"
            player_rect = pygame.Rect(playeroutsideX + speed,playeroutsideY,100,100)
            
            if player_rect.collidelist(outside_objects) == -1 and player_rect.colliderect(border):
                playeroutsideX += speed
                

        elif keys[pygame.K_UP]:#Makes you move up when you hit the up key and changes the player's direction
            direction = "up"
            player_rect = pygame.Rect(playeroutsideX,playeroutsideY - speed,100,100)
            
            if player_rect.collidelist(outside_objects) == -1 and player_rect.colliderect(border):
                playeroutsideY -= speed

                
        elif keys[pygame.K_DOWN]:#Makes you move down when you hit the down key and changes the player's direction
            direction = "down"
            player_rect = pygame.Rect(playeroutsideX,playeroutsideY + speed,100,100)
            
            if player_rect.collidelist(outside_objects) == -1 and player_rect.colliderect(border):
                playeroutsideY += speed

        #Makes the map move according to player pos
        if 550 - playeroutsideX < 0:#If he is at away from the left edge of map
            
            if playeroutsideX + 650 > 3100:#If he is at the right edge of map
                screen_playerX = 1200 - (3100 - playeroutsideX)
                
            else:# In between left and right edges
                screen_playerX = 550
                mapX = 550 - playeroutsideX
                
        else:#If he is at the left edge
            screen_playerX = playeroutsideX
            mapX = 0

            
        if 350 - playeroutsideY < 0:#If he is away from the top edge
            if playeroutsideY + 450 > 1100:#If he is at the bottom edge
                screen_playerY = 800 - (1100 - playeroutsideY)
                mapY = -300
                
            else:#If he is between the top and the bottom
                screen_playerY = 350
                mapY = 350 - playeroutsideY
                
        else:#If he is at the top edge
            screen_playerY = playeroutsideY
            mapY = 0

        #Changes player direction
        if direction == "up":
            angle = 0
        elif direction == "left":
            angle = 90
        elif direction == "right":
            angle = 270
        else:
            angle = 180

        #Rotates the player
        player_face = pygame.transform.rotate(player,angle)

        #Draws and redraws the player and map then updates the window
        win.fill(white)
        win.blit(outside,(mapX,mapY))
        win.blit(player_face,(screen_playerX,screen_playerY))
        pygame.display.update()

        
    while play == "Arcade": #Inside the arcade
        
        FPS_Clock.tick(FPS)#FPS clock

        #Draws the arcade
        win.blit(tile, (100,0))
        win.blit(geogame, (1100,0))
        win.blit(mathgames, (0,0))
        win.blit(musicgames, (400,400))
        win.blit(shop, (300,0))
        win.blit(gamer,(100,400))
        win.blit(gamer2,(1000,700))

        #Changes player direction
        if direction == "up":
            angle = 0
        elif direction == "left":
            angle = 90
        elif direction == "right":
            angle = 270
        else:
            angle = 180

        #Rotates player
        player_face = pygame.transform.rotate(player,angle)

        #Draws the player 
        win.blit(player_face,(playerX,playerY))

        #Updates window
        pygame.display.update()

        #Finds the actions made and keys pressed
        pygame.event.clear()
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_c]:#Interact with games or people
            player_rect = pygame.Rect(playerX, playerY,100,100)
            if player_rect.colliderect(gamer_talk_rect):
                play = "gamer talk"
            elif player_rect.colliderect(gamer2_talk_rect):
                play = "gamer2 talk"
            elif player_rect.colliderect(shop_talk_rect):
                play = "shop talk"
            elif player_rect.colliderect(play_musicgames):
                play = "musicgame"
            elif player_rect.colliderect(play_mathgames):
                play = "mathgame"
            elif player_rect.colliderect(play_geogames):
                play = "geogame"

                
        elif keys[pygame.K_LEFT]:#Move left and change direction
            direction = "left"
            
            player_rect = pygame.Rect(playerX - speed,playerY,100,100)#Checks if you will hit an object
            if player_rect.collidelist(arcade_objects) == -1:
                playerX -= speed
                
        elif keys[pygame.K_RIGHT]:#Move right and change direction
            direction = "right"
            
            player_rect = pygame.Rect(playerX + speed,playerY,100,100)
            if player_rect.collidelist(arcade_objects) == -1:
                playerX += speed
                
        elif keys[pygame.K_UP]:#Move up and change direction
            direction = "up"
            player_rect = pygame.Rect(playerX,playerY - speed,100,100)
            
            if player_rect.collidelist(arcade_objects) == -1:
                playerY -= speed
                
        elif keys[pygame.K_DOWN]:#Move down and change direction
            direction = "down"
            player_rect = pygame.Rect(playerX,playerY + speed,100,100)
            
            if player_rect.collidelist(arcade_objects) == -1:
                playerY += speed

    #Starts the music game
    while play == "musicgame":
        #Dictionary for the key event to the key and from the random number to the note
        keydict = {97: "A", 98: "B", 99: "C", 100: "D" , 101: "E", 102: "F", 103: "G"}
        notedict = {0: "E", 1: "F", 2: "G", 3: "A", 4: "B", 5: "C", 6: "D" , 7: "E", 8: "F"}

        #Keeps track of your answers
        ans1 = 0
        ans2 = 0
        ans3 = 0

        #tracks points, wrong answers and the time
        points = 0
        wrong = 3
        time = 0
        highscoreplayed = False

        #Loop for the tutorial
        while musictutorial != 4:

            #Redraws the tutorial
            win.fill(white)
            win.blit(skip_tutorial,(0,0))

            #Keys pressed
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: #If you press C the tutorial continues
                    if event.key ==  99:
                        musictutorial += 1
                    elif event.key == 120:#If you press X the tutorial goes back
                        if musictutorial != 1:
                            musictutorial -= 1
                    elif event.key == 32:# If you press space the tutorial is skipped
                        musictutorial = 4
                        
            #Tutorial page 1
            if musictutorial == 1:
                graphics = font4.render("Use your keyboard to type the note that is displayed",1,black)
            #Tutorial page 2
            elif musictutorial == 2:
                graphics = font4.render("You will have 8s to correctly choose the three answers",1,black)
            #Tutorial page 3
            else:
                graphics = font4.render("If you get three wrong or do not complete in 8s you lose",1,black)

            #Writes the words and updates window
            win.blit(graphics, (150,380))
            pygame.display.update()

        #Main loop for the game
        while wrong > 0 and time != 240:#If you get three wrong or do not answer in time, you lose
            #Randomly generates the notes
            note1 = random.randint(0,8)
            note2 = random.randint(0,8)
            note3 = random.randint(0,8)
                
            Round = True
            
            while Round and time != 240:#Starts the game
                #FPS Clock
                FPS_Clock.tick(FPS)

                #Draws the background
                win.fill(white)
                win.blit(treble_clef,(0,0))

                #Draws the notes
                if note1 < 4:
                    win.blit(note,(400,240 - 40 * note1))
                else:
                    win.blit(note_flipped,(400,144 + 40 * (- note1 + 8)))
                if note2 < 4:
                    win.blit(note,(700,240 - 40 * note2))
                else:
                    win.blit(note_flipped,(700,144 + 40 * (- note2 + 8)))
                if note3 < 4:
                    win.blit(note,(1000,240 - 40 * note3))
                else:
                    win.blit(note_flipped,(1000,144 + 40 * (-note3 + 8)))

                #Adds time to the timer
                time += 1
                
                #Updates the window
                pygame.display.update()

                #Finds all the events and button presses
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if 97 <= event.key <= 103:

                            #Compares answers and gives points to correct answers and a wrong for every wrong
                            if ans1 == 0:
                                ans1 = keydict.get(event.key)
                            elif ans2 == 0:
                                ans2 = keydict.get(event.key)
                            elif ans3 == 0:
                                ans3 = keydict.get(event.key)
                                if ans1 == notedict.get(note1):
                                    points += 1
                                else:
                                    wrong -= 1
                                if ans2 == notedict.get(note2):
                                    points += 1
                                else:
                                    wrong -= 1
                                if ans3 == notedict.get(note3):
                                    points += 1
                                else:
                                    wrong -= 1

                                #Checks if they reach the highscore
                                if points > music_highscore:
                                    music_highscore = points
                                    if highscoreplayed == False:
                                        highscore.play(loops = 0)
                                        highscoreplayed = True
                                #Resets the game
                                time = 0
                                ans1 = 0
                                ans2 = 0
                                ans3 = 0
                                Round = False
               
        gameover()#Gameover Screen
        play_again = True
        playgame = False

        #Starts the play again scene
        while play_again:
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key ==  99:#Press C to play again
                            if playgame == False:
                                win.fill(white)
                                win.blit(playagain,(0,0))
                                pygame.display.update()
                                playgame = True
                            else:
                                play_again = False
                                
                        elif event.key == 32:#Press Space to go back to the arcade
                            play = "Arcade"
                            play_again = False

    #Starts the math game
    while play == "mathgame":
        #Sets the lane you are in
        lane = 2

        #Tracks points and wrong answers
        points = 0
        wrong = 3

        highscoreplayed = False

        #Answers for the questions
        lane1 = 0
        lane2 = 0
        lane3 = 0

        #The numbers for each question
        lane1_num1 = 0
        lane1_num2 = 0
        lane2_num1 = 0
        lane2_num2 = 0
        lane3_num1 = 0
        lane3_num2 = 0

        #Moves the question down
        lane1Y = 10
        lane2Y = 10
        lane3Y = 10

        #Sets the operation for the middle lane
        operation = 0
        #Tracks the amount of loops
        comp = 0

        #Dictionary for the keys pressed and the lane 
        key = {1073741912: 0, 1073741913: 1, 1073741914: 2, 1073741915: 3, 1073741916: 4, 1073741917: 5, 1073741918: 6, 1073741919: 7, 1073741920: 8, 1073741921: 9}
        laner  = {1: lane1, 2: lane2, 3: lane3}

        #Loop for tutorial
        while mathtutorial != 4:

            keys = pygame.key.get_pressed()#Finds the buttons pressed

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key ==  99:#Press C to continue tutorial
                        mathtutorial += 1
                    elif event.key == 120:#Press X to go back in the tutorial
                        if mathtutorial != 1:
                            mathtutorial -= 1
                    elif event.key == 32:#Press Space to skip
                        mathtutorial = 4
                
            if mathtutorial == 1:#Stage one of tutorial
                graphics = font4.render("Use the Z X C keys to switch rows and numpad to answer",1,black)
            elif mathtutorial == 2:#Stage two of tutorial
                graphics = font4.render("Answer incorrectly or don't answer in time gives you a loss",1,black)
            else:#Stage three of tutorial
                graphics = font4.render("Three losses and you lose the game",1,black)

            #Redraws the scene and updates the window
            win.fill(white)
            win.blit(skip_tutorial,(0,0))
            win.blit(graphics, (100,380))
            pygame.display.update()

        #Main loop for game
        while wrong > 0:
            win.fill(white)

            #If a lane does not have a equation it makes one
            if lane1 == 0 or lane2 ==0 or lane3 == 0 and comp % 100 == 0:
                
                pygame.time.delay(10)
                comp += 1

                #Makes two numbers
                num1 = random.randint (1,15)
                num2 = random.randint (1,15)
                #Makes a random operation
                op = random.randint (1,2)
                #If mid is 3 then the operation is in the middle
                mid = random.randint (1,3)

                #If operation is 1 then it is addition
                if op == 1:
                    if 10 > num1 + num2 > 0:
                        #The operation can go to either the first of mid lane
                        if mid == 3 and lane2 == 0:
                            lane2 = num1 + num2
                            lane2_num1 = num1
                            lane2_num2 = num2
                            operation = "+"
                        elif lane1 == 0:
                            lane1 = num1 + num2
                            lane1_num1 = num1
                            lane1_num2 = num2
                            
                #If the operation is 2 then it is subtraction
                else:
                    if 10 > num1 - num2 > 0:
                        #The operation can go to either the mid or last lane
                        if mid == 3 and lane2 == 0:
                            lane2 = num1 - num2
                            lane2_num1 = num1
                            lane2_num2 = num2
                            operation = "-"
                        elif lane3 == 0:
                            lane3 = num1 - num2
                            lane3_num1 = num1
                            lane3_num2 = num2

            #Takes the button down presses
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 122:#Press Z to go to the first lane
                        lane = 1
                    if event.key == 120:#Press X to go to the mid lane
                        lane = 2
                    if event.key == 99:#Press C to go to the last lane
                        lane = 3
                    print(event.key)
                    #If you press the numbers on the num pad then it becomes your answer
                    if event.key in key:
                        ans = event.key
                        print ("hello")

                        #Checks your answer and gives points for correct and a wrong for incorrect
                        if lane == 1:
                            if key.get(ans) == lane1:
                                points += 1
                            else:
                                wrong -= 1
                            lane1 = 0
                            lane1Y = 10
                        elif lane == 2:
                            if key.get(ans) == lane2:
                                points += 1
                                
                            else:
                                wrong -= 1
                            lane2 = 0
                            lane2Y = 10
                        else:
                            if key.get(ans) == lane3:
                                points += 1
                            else:
                                wrong -= 1
                            lane3 = 0
                            lane3Y = 10

                            #Checks if you beat the highscore and plays the sound
                            if points > math_highscore:
                                    math_highscore = points
                                    if highscoreplayed == False:
                                        highscore.play(loops = 0)
                                        highscoreplayed = True
                                        
            #Checks if you did not answer in time
            if lane1Y == 730:
                lane1 = 0
                lane1Y = 10
                wrong -= 1
            if lane2Y == 730:
                lane2 = 0
                lane2Y = 10
                wrong -= 1
            if lane3Y == 730:
                lane3 = 0
                lane3Y = 10
                wrong -= 1
            #Draws the three rectangles
            pygame.draw.rect(win,black,(10,10, 360, 760),2)
            pygame.draw.rect(win,black,(420,10, 360, 760),2)
            pygame.draw.rect(win,black,(820,10, 360, 760),2)

            #Writes the equations
            if lane1 != 0:
                graphics = font.render((str(lane1_num1) + "  +  " + str(lane1_num2)), 1, black)
                win.blit(graphics, (120, lane1Y))
                if comp % 75000:
                    lane1Y += 2
            if lane2 != 0:
                graphics = font.render((str(lane2_num1) +  "  " + str(operation) + "  " + str(lane2_num2)), 1, black)
                win.blit(graphics, (520, lane2Y))
                if comp % 75000:
                    lane2Y += 2
            if lane3 != 0:
                graphics = font.render((str(lane3_num1) + " - " + str(lane3_num2)), 1, black)
                win.blit(graphics, (920, lane3Y))
                if comp % 75000:
                    lane3Y += 2

            #If you are in the lane then the rectangle becomes red
            if lane == 1:
                pygame.draw.rect(win,red,(10,10, 360, 760),5)
            elif lane == 2:
                pygame.draw.rect(win,red,(420,10, 360, 760),5)
            else:
                pygame.draw.rect(win,red,(820,10, 360, 760),5)

            comp += 0.5

            pygame.time.delay(20)

            #Updates window
            pygame.display.update()

        #Gameover screen
        gameover()
        play_again = True
        playgame = False

        #Starts play agin screen
        while play_again:
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key ==  99: #Press C to play again
                            if playgame == False:
                                win.fill(white)
                                win.blit(playagain,(0,0))
                                pygame.display.update()
                                playgame = True
                            else:
                                play_again = False
                                
                        elif event.key == 32:#Press Space to go back to arcade
                            play = "Arcade"
                            play_again = False

    #Starts the Geo Game
    while play == "geogame":

        #Tracks the points
        point = 0

        highscoreplayed = False

        #Rectangles for the provinces and territories
        Yukon = pygame.Rect(259, 108,134, 159)
        NWTerr = pygame.Rect(338, 137,190, 193)
        Nunavut = pygame.Rect(426, 9,338, 313)
        BC = pygame.Rect(221, 215,174, 253)
        Alberta = pygame.Rect(362, 270,112, 190)
        Saskat = (396, 320,103, 169)
        Manitoba = pygame.Rect(470, 328,125, 170)
        Ontario = pygame.Rect(532, 379,220,215)
        Quebec = pygame.Rect(657, 293,180,237)
        Newfoundland = pygame.Rect(750, 300,193, 148)
        PEI = pygame.Rect(835, 470, 25, 16)
        NewBrunswick = pygame.Rect(783, 463, 55, 48)
        NovaScotia = pygame.Rect(832, 463, 51, 68)

        #Rectangle for the word of the province or territory
        word_rect = pygame.Rect(400,590,400,50)

        #List of the rectangles and the province and territories
        pro_terr_rect = [Yukon,NWTerr,Nunavut,BC,Saskat,Alberta,Manitoba,Ontario,Quebec,Newfoundland,PEI,NewBrunswick,NovaScotia]
        pro_terr_list = ["Yukon","North West Territories","Nunavut","British Columbia", "Saskatchewan","Alberta","Manitoba","Ontario","Quebec","Newfoundland and Labrador","Prince Edward Island","New Brunswick","Nova Scotia"]

        #Dictionary of the random number to the province rects
        pro_terrdict = {0: Yukon,1: NWTerr,2: Nunavut,3: BC,4: Saskat,5: Alberta,6: Manitoba,7: Ontario,8: Quebec,9: Newfoundland,10: PEI,11: NewBrunswick,12: NovaScotia}

        #Checks if you are holding the word
        holding_word = False

        #Get one wrong and you lose
        wrong = 1

        #Tracks the points and the time
        points = 0
        time = 0

        #Starts the game
        while geotutorial != 4:

            #Starts the tutorial
            win.fill(white)
            win.blit(skip_tutorial,(0,0))
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key ==  99:#Press C to continue
                        geotutorial += 1
                    elif event.key == 120:#Press X to go back
                        if geotutorial != 1:
                            geotutorial -= 1
                    elif event.key == 32:#Press Space to skip
                        geotutorial = 4

            #Tutorial lines
            if geotutorial == 1:
                graphics = font4.render("Click the word to grab it and move it around",1,black)
            elif geotutorial == 2:
                graphics = font4.render("Click again to the named province or territory",1,black)
            else:
                graphics = font4.render("If you get one wrong then you lose",1,black)

            #Writes the words and update the window
            win.blit(graphics, (150,380))
            pygame.display.update()

        #Starts the game
        while wrong != 0 and time != 240:
            #Random generated province/territory
            rng = random.randint(0,12)
            pro_terr = pro_terr_list[rng]

            #Writes the word
            wordX = 600 - len(pro_terr) * 10
            wordY = 600
            choose = True
            graphics = font3.render(str(pro_terr), 1,black)

            #Allows the user to play
            while choose and time != 240:
                FPS_Clock.tick(FPS)#FPS Clock

                #Redraws the window and draws the words and the map
                win.fill(white)
                win.blit(canada,(250,0))
                win.blit(graphics, (wordX,wordY))

                #Gets the mouse position and makes it a rect
                mouse = pygame.mouse.get_pos()
                mouse_rect = pygame.Rect(mouse[0],mouse[1],0,0)

                #If you the word you hold it
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 and mouse_rect.colliderect(word_rect) == 0:
                            print ("wow")
                            holding_word = True
                        if holding_word and mouse_rect.collidelist(pro_terr_rect) != -1:
                            holding_word = False
                            choose = False
                            if mouse_rect.colliderect(pro_terr_rect[rng]) == 0: #If you correctly choose the province/territory you get a point
                                points += 1
                                time = 0
                                #Checks for highscore
                                if points > geo_highscore:
                                    geo_highscore = points
                                    if highscoreplayed == False:
                                        highscore.play(loops = 0)
                                        highscoreplayed = True
                            else:
                                wrong -= 1
                        #Puts word back if you do not click on the map
                        else: 
                            wordX = 600 - len(pro_terr) * 10
                            wordY = 600
                if holding_word:
                    wordX = mouse[0] + 10
                    wordY = mouse[1] + 10

                time += 1
                #Updates the window
                pygame.display.update()

        #Gameover screen
        gameover()
        play_again = True
        playgame = True

        #Play again screen
        while play_again:
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key ==  99:
                            if playgame:
                                win.fill(white)
                                win.blit(playagain,(0,0))
                                pygame.display.update()
                                playgame = False
                            else:
                                play_again = False
                                
                        elif event.key == 32:
                            play = "Arcade"
                            play_again = False

    #Dialogue for talking to NPCs and the signs
    #Press C to continue conversation
    #Press Space to end
    while play == "gamer talk":
        win.blit(textbox,(0,600))
        if gamertalk == 1:
            graphics = font5.render("Hey I'm Timmy. Just got in the area to visit my grandmother",1,black)
        elif gamertalk == 2:
            graphics = font5.render("Can you believe how little people are here?",1,black)
        elif gamertalk == 3: 
            graphics = font5.render("I've tried all the games here, the music one seems the most fun.",1,black)
        else:
            play = "Arcade"
            break

        win.blit(graphics,(20,650))
        pygame.display.update()
        
        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key ==  99:
                                gamertalk += 1
                                
                        elif event.key == 32:
                            play = "Arcade"

    while play == "gamer2 talk":
        win.blit(textbox,(0,600))
        if gamer2talk == 1:
            graphics = font5.render("Yo, I'm Joe. I'm sorta a veteran here.",1,black)
        elif gamer2talk == 2:
            graphics = font5.render("Do not visit the shop, the only prize isn't even there, it's just the box",1,black)
        elif gamer2talk == 3: 
            graphics = font5.render("Today the games are free, great for learning and fun.",1,black)
        else:
            play = "Arcade"
            break

        win.blit(graphics,(20,650))
        pygame.display.update()
        
        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key ==  99:
                                gamer2talk += 1
                                
                        elif event.key == 32:
                            play = "Arcade"

    while play == "shop talk":
        win.blit(textbox,(0,600))
        if shoptalk == 1:
            graphics = font5.render("Hey there fella, I'm the shop keeper, you can call me Harold.",1,black)
        elif shoptalk == 2:
            graphics = font5.render("Today all the games here are free feel free to play.",1,black)
        elif shoptalk == 3: 
            graphics = font5.render("We also sell PlayStations. Only costs 500 tokens roughly 300 hours of playing.",1,black)
        else:
            play = "Arcade"
            break

        win.blit(graphics,(20,650))
        pygame.display.update()
        
        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key ==  99:
                                shoptalk += 1
                                
                        elif event.key == 32:
                            play = "Arcade"

    while play == "sign":
        win.blit(textbox,(0,600))
        graphics = font5.render("Closed For Construction.",1,black)
        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key ==  99:
                            play = "Outside"
                            pygame.time.delay(100)
        win.blit(graphics,(20,650))
        pygame.display.update()
