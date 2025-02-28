import pygame
pygame.init()

#color variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

#game variables
X_turn = True
X_score = 0
O_score = 0
X_win = False
O_win = False
X_places = []
O_places = []
pressed = False
position = 0
location = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
top = False
middle = False
bottom = False
left = False
column = False
right = False
TL_BR_diagonal = False
TR_BL_diagonal = False

#position variables for X and O
forX_x_1 = 30
forX_y_1 = 150
forX_x_2 = 117.5
forX_y_2 = 247.5
forX_x_3 = 132.5
forX_y_3 = 252.5
forX_x_4 = 217.5
forX_y_4 = 347.5
forX_x_5 = 232.5
forX_y_5 = 352.5
forX_x_6 = 320
forX_y_6 = 450
forO_x_1 = 75
forO_y_1 = 200
forO_x_2 = 175
forO_y_2 = 300
forO_x_3 = 275
forO_y_3 = 400

#screen settings
screen = pygame.display.set_mode((350, 475))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill((white))

def draw_gameboard():

    #tic-tac-toe board
    pygame.draw.line(screen, black, (125, 150), (125, 450), 5)
    pygame.draw.line(screen, black, (225, 150), (225, 450), 5)
    pygame.draw.line(screen, black, (25, 250), (325, 250), 5)
    pygame.draw.line(screen, black, (25, 350), (325, 350), 5)

    #X score shape
    pygame.draw.line(screen, red, (10, 57.5), (61.875, 120), 5)
    pygame.draw.line(screen, red, (61.875, 57.5), (10, 120), 5)

    #O score shape
    pygame.draw.circle(screen, blue, (202, 90), 26, 5)

    #game board borders
    pygame.draw.line(screen, black, (0, 0), (0, 475), 20)
    pygame.draw.line(screen, black, (350, 0), (350, 475), 20)
    pygame.draw.line(screen, black, (0, 0), (350, 0), 20)
    pygame.draw.line(screen, black, (0, 125), (350, 125), 10)

    #top-section game board boarders
    pygame.draw.line(screen, black, (230, 0), (230, 125), 5)
    pygame.draw.line(screen, black, (0, 55), (350, 55), 5)
    pygame.draw.line(screen, black, (64.375, 55), (64.375, 125), 5)
    pygame.draw.line(screen, black, (118.75, 55), (118.75, 125), 5)
    pygame.draw.line(screen, black, (173.125, 55), (173.125, 125), 5)

    #score title 
    text_font = pygame.font.SysFont("microsofthimalaya", 80)
    img = text_font.render("Score", True, black)
    screen.blit(img, (55, 2.5))

    #X score number
    text_font = pygame.font.SysFont("microsofthimalaya", 110)
    img = text_font.render(str(X_score), True, black)
    screen.blit(img, (72.375, 47.4))

    #O score number
    text_font = pygame.font.SysFont("microsofthimalaya", 110)
    img = text_font.render(str(O_score), True, black)
    screen.blit(img, (126.75, 47.4))

    #turn title 
    text_font = pygame.font.SysFont("microsofthimalaya", 80)
    img = text_font.render("Turn", True, black)
    screen.blit(img, (235, 2.5))

    #turn title shape
    if X_turn:
        pygame.draw.polygon(screen, white, [(232.5, 57.5), (340, 57.5), (340, 120), (232.5, 120)])
        pygame.draw.line(screen, red, (256.5, 60), (316.5, 118), 5)
        pygame.draw.line(screen, red, (316.5, 60), (256.5, 118), 5)
    if not X_turn:
        pygame.draw.polygon(screen, white, [(232.5, 57.5), (340, 57.5), (340, 120), (232.5, 120)])
        pygame.draw.circle(screen, blue, (286.5, 90), 30, 5)

def draw_X(position, location, X_turn):

    #draw X based on position variable
    if position == 1 and 1 in location:
        pygame.draw.line(screen, red, (forX_x_1, forX_y_1), (forX_x_2, forX_y_2), 10)
        pygame.draw.line(screen, red, (forX_x_2, forX_y_1), (forX_x_1, forX_y_2), 10)
        X_places.append(1)
    if position == 2 and 2 in location:
        pygame.draw.line(screen, red, (forX_x_3, forX_y_1), (forX_x_4, forX_y_2), 10)
        pygame.draw.line(screen, red, (forX_x_4, forX_y_1), (forX_x_3, forX_y_2), 10)
        X_places.append(2)
    if position == 3 and 3 in location:
        pygame.draw.line(screen, red, (forX_x_5, forX_y_1), (forX_x_6, forX_y_2), 10)
        pygame.draw.line(screen, red, (forX_x_6, forX_y_1), (forX_x_5, forX_y_2), 10)
        X_places.append(3)
    if position == 4 and 4 in location:
        pygame.draw.line(screen, red, (forX_x_1, forX_y_3), (forX_x_2, forX_y_4), 10)
        pygame.draw.line(screen, red, (forX_x_2, forX_y_3), (forX_x_1, forX_y_4), 10)
        X_places.append(4)
    if position == 5 and 5 in location:
        pygame.draw.line(screen, red, (forX_x_3, forX_y_3), (forX_x_4, forX_y_4), 10)
        pygame.draw.line(screen, red, (forX_x_4, forX_y_3), (forX_x_3, forX_y_4), 10)
        X_places.append(5)
    if position == 6 and 6 in location:
        pygame.draw.line(screen, red, (forX_x_5, forX_y_3), (forX_x_6, forX_y_4), 10)
        pygame.draw.line(screen, red, (forX_x_6, forX_y_3), (forX_x_5, forX_y_4), 10)
        X_places.append(6)
    if position == 7 and 7 in location:
        pygame.draw.line(screen, red, (forX_x_1, forX_y_5), (forX_x_2, forX_y_6), 10)
        pygame.draw.line(screen, red, (forX_x_2, forX_y_5), (forX_x_1, forX_y_6), 10)
        X_places.append(7)
    if position == 8 and 8 in location:
        pygame.draw.line(screen, red, (forX_x_3, forX_y_5), (forX_x_4, forX_y_6), 10)
        pygame.draw.line(screen, red, (forX_x_4, forX_y_5), (forX_x_3, forX_y_6), 10)
        X_places.append(8)
    if position == 9 and 9 in location:
        pygame.draw.line(screen, red, (forX_x_5, forX_y_5), (forX_x_6, forX_y_6), 10)
        pygame.draw.line(screen, red, (forX_x_6, forX_y_5), (forX_x_5, forX_y_6), 10)
        X_places.append(9)
    if position in location:
        location.remove(position)
        X_turn = False
    return X_turn
    
def draw_O(position, location, X_turn):

    #draw O based on position variable
    if position == 1 and 1 in location:
        pygame.draw.circle(screen, blue, (forO_x_1, forO_y_1), 50, 10)
        O_places.append(1)
    if position == 2 and 2 in location:
        pygame.draw.circle(screen, blue, (forO_x_2, forO_y_1), 50, 10)
        O_places.append(2)
    if position == 3 and 3 in location:
        pygame.draw.circle(screen, blue, (forO_x_3, forO_y_1), 50, 10)
        O_places.append(3)
    if position == 4 and 4 in location:
        pygame.draw.circle(screen, blue, (forO_x_1, forO_y_2), 50, 10)
        O_places.append(4)
    if position == 5 and 5 in location:
        pygame.draw.circle(screen, blue, (forO_x_2, forO_y_2), 50, 10)
        O_places.append(5)
    if position == 6 and 6 in location:
        pygame.draw.circle(screen, blue, (forO_x_3, forO_y_2), 50, 10)
        O_places.append(6)
    if position == 7 and 7 in location:
        pygame.draw.circle(screen, blue, (forO_x_1, forO_y_3), 50, 10)
        O_places.append(7)
    if position == 8 and 8 in location:
        pygame.draw.circle(screen, blue, (forO_x_2, forO_y_3), 50, 10)
        O_places.append(8)
    if position == 9 and 9 in location:
        pygame.draw.circle(screen, blue, (forO_x_3, forO_y_3), 50, 10)
        O_places.append(9)
    if position in location:
        location.remove(position)
        X_turn = True 
    return X_turn

running = True
while running: 
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = True
            if pygame.mouse.get_pos()[0] < 125 and pygame.mouse.get_pos()[1] < 250 and 1 in location:
                position = 1
            elif pygame.mouse.get_pos()[0] < 225 and pygame.mouse.get_pos()[0] > 125 and pygame.mouse.get_pos()[1] < 250 and 2 in location:
                position = 2
            elif pygame.mouse.get_pos()[0] < 325 and pygame.mouse.get_pos()[0] > 225 and pygame.mouse.get_pos()[1] < 250 and 3 in location:
                position = 3
            elif pygame.mouse.get_pos()[0] < 125 and pygame.mouse.get_pos()[1] < 350 and pygame.mouse.get_pos()[1] > 250 and 4 in location:
                position = 4
            elif pygame.mouse.get_pos()[0] < 225 and pygame.mouse.get_pos()[0] > 125 and pygame.mouse.get_pos()[1] < 350 and pygame.mouse.get_pos()[1] > 250 and 5 in location:
                position = 5
            elif pygame.mouse.get_pos()[0] < 325 and pygame.mouse.get_pos()[0] > 225 and pygame.mouse.get_pos()[1] < 350 and pygame.mouse.get_pos()[1] > 250 and 6 in location:
                position = 6
            elif pygame.mouse.get_pos()[0] < 125 and pygame.mouse.get_pos()[1] < 450 and pygame.mouse.get_pos()[1] > 350 and 7 in location:
                position = 7
            elif pygame.mouse.get_pos()[0] < 225 and pygame.mouse.get_pos()[0] > 125 and pygame.mouse.get_pos()[1] < 450 and pygame.mouse.get_pos()[1] > 350 and 8 in location:
                position = 8
            elif pygame.mouse.get_pos()[0] < 325 and pygame.mouse.get_pos()[0] > 225 and pygame.mouse.get_pos()[1] < 450 and pygame.mouse.get_pos()[1] > 350 and 9 in location:
                position = 9

    if X_turn == True and pressed == True:
        pressed = False
        X_turn = draw_X(position, location, X_turn)

    if X_turn == False and pressed == True:
        pressed = False
        X_turn = draw_O(position, location, X_turn)

    #check if X wins
    for i in X_places:
        #check for win rows
        if i == 1 or i == 4 or i == 7:
            if i + 1 in X_places and i + 2 in X_places:
                X_win = True
                if i == 1:
                    top = True
                elif i == 4:
                    middle = True
                else:
                    bottom = True

        #check for win columns
        if i == 1 or i == 2 or i == 3:
            if i + 3 in X_places and i + 6 in X_places:
                X_win = True
                if i == 1:
                    left = True
                elif i == 2:
                    column = True
                else:
                    right = True

        #check for win diagonals
        if i == 1:
            if i + 4 in X_places and i + 8 in X_places:
                X_win = True
                TL_BR_diagonal = True
        if i == 3:
            if i + 2 in X_places and i + 4 in X_places:
                X_win = True
                TR_BL_diagonal = True
    
    #check if O wins
    for i in O_places:
        #check for win rows
        if i == 1 or i == 4 or i == 7:
            if i + 1 in O_places and i + 2 in O_places:
                O_win = True
                if i == 1:
                    top = True
                elif i == 4:
                    middle = True
                else:
                    bottom = True

        #check for win columns
        if i == 1 or i == 2 or i == 3:
            if i + 3 in O_places and i + 6 in O_places:
                O_win = True
                if i == 1:
                    left = True
                elif i == 2:
                    column = True
                else:
                    right = True

        #check for win diagonals
        if i == 1:
            if i + 4 in O_places and i + 8 in O_places:
                O_win = True
                TL_BR_diagonal = True
        if i == 3:
            if i + 2 in O_places and i + 4 in O_places:
                O_win = True
                TR_BL_diagonal = True
        
        #green line for winning
        if X_win or O_win:
            if top:
                pygame.draw.line(screen, green, (forO_x_1, forO_y_1), (forO_x_3, forO_y_1), 10)
                top = False
            if middle:
                pygame.draw.line(screen, green, (forO_x_1, forO_y_2), (forO_x_3, forO_y_2), 10)
                middle = False
            if bottom:
                pygame.draw.line(screen, green, (forO_x_1, forO_y_3), (forO_x_3, forO_y_3), 10)
                bottom = False
            if left:
                pygame.draw.line(screen, green, (forO_x_1, forO_y_1), (forO_x_1, forO_y_3), 10)
                left = False
            if column:
                pygame.draw.line(screen, green, (forO_x_2, forO_y_1), (forO_x_2, forO_y_3), 10)
                column = False
            if right:
                pygame.draw.line(screen, green, (forO_x_3, forO_y_1), (forO_x_3, forO_y_3), 10)
                right = False
            if TL_BR_diagonal:
                pygame.draw.line(screen, green, (forO_x_1, forO_y_1), (forO_x_3, forO_y_3), 10)
                TL_BR_diagonal = False
            if TR_BL_diagonal:
                pygame.draw.line(screen, green, (forO_x_3, forO_y_1), (forO_x_1, forO_y_3), 10)
                TR_BL_diagonal = False
            pygame.display.flip()
            pygame.time.wait(2000)
        
        #X wins 1 time
        if X_win:
            X_score += 1
            X_win = False
            X_places = []
            O_places = []
            screen.fill((white))
            position = 0
            location = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
            X_turn = False
            
        #O wins 1 time
        if O_win:
            O_score += 1
            O_win = False
            O_places = []
            X_places = []
            screen.fill((white))
            position = 0
            location = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
            X_turn = True

        #draw condition
        if location == [] and (X_win == False or O_win == False):
            O_places = []
            X_places = []
            screen.fill((white))
            position = 0
            location = [1, 2, 3, 4, 5, 6, 7, 8 , 9]

        #if a player wins 9 times program quits
        if X_score == 9:
            print("X wins !")
            running = False
        
        if O_score == 9:
            print("O wins !")
            running = False

    draw_gameboard()
    pygame.display.flip() 

pygame.quit()
