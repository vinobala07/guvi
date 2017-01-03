import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
assert(BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board must contain even number of boxes'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE +GAPSIZE))))
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * ( BOXSIZE + GAPSIZE))))

#COLOURS
GRAY = (100, 100, 100)
NAVY_BLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
ORANGE =    (255, 128, 0)

BGCOLOR = WHITE
LIGHTBGCOLOR = GRAY
BOXCOLOR = GRAY
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, CYAN, PURPLE, ORANGE)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the no of the shapes/ colour defined"

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Memory Game')

    main_board = get_randomized_board()
    revealed_boxes = generate_revealed_boxes(False)

    first_selection = None

    DISPLAYSURF.fill(BGCOLOR)
    start_game_animation(main_board)

    while True:
        mouse_clicked = False

        DISPLAYSURF.fill(BGCOLOR)
        draw_board(main_board, revealed_boxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouse_clicked = True

        boxx, boxy = get_box_at_pixel(mousex, mousey)
        if boxx != None and boxy != None:
            if not revealed_boxes[boxx][boxy]:
                draw_highlight_box(boxx, boxy)
            if not revealed_boxes[boxx][boxy] and mouse_clicked:
                reveal_boxes_animation(main_board, [(boxx, boxy)])
                revealed_boxes[boxx][boxy] = True
                if first_selection == None:
                    first_selection = [boxx, boxy]
                else:
                    icon1_shape, icon1_color = get_shape_and_color(main_board, first_selection[0], first_selection[1])
                    icon2_shape, icon2_color = get_shape_and_color(main_board, boxx, boxy)

                    if icon1_shape != icon2_shape or icon1_color != icon2_color:
                        pygame.time.wait(1000)
                        cover_boxes_animation(main_board, [(first_selection[0], first_selection[1]), (boxx, boxy)])
                        revealed_boxes[first_selection[0]][first_selection[1]] = False
                        revealed_boxes[boxx][boxy] = False
                    elif has_won(revealed_boxes):
                        game_won_animation(main_board)
                        pygame.time.wait(2000)
                        main_board = get_randomized_board()
                        revealed_boxes = generate_revealed_boxes(False)

                        draw_board(main_board, revealed_boxes)
                        pygame.display.update()
                        pygame.time.wait(500)

                        start_game_animation(main_board)
                    first_selection = None
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def has_won(revealed_boxes):
    for i in revealed_boxes:
        if False in i:
            return False
    return True

def game_won_animation(board):
    covered_boxes = generate_revealed_boxes(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR
    for i in range(13):
        color1, color2 = color2, color1
        DISPLAYSURF.fill(color1)
        draw_board(board, covered_boxes)
        pygame.display.update()
        pygame.time.wait(300)

def draw_highlight_box(boxx, boxy):
    left, top = left_top_coords(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)

def get_box_at_pixel(mousex, mousey):
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            left, top = left_top_coords(x,y)
            box_rect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if box_rect.collidepoint(mousex, mousey):
                return (x,y)
    return (None, None)

def start_game_animation(board):
    covered_boxes = generate_revealed_boxes(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x,y))

    random.shuffle(boxes)
    box_groups = split_into_groups_of(8, boxes)

    draw_board(board, covered_boxes)
    for box in box_groups:
        reveal_boxes_animation(board, box)
        cover_boxes_animation(board, box)

def draw_board(board, revealed):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = left_top_coords(boxx, boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                shape, color = get_shape_and_color(board, boxx, boxy)
                draw_icon(shape, color, boxx, boxy)

def draw_icon(shape, color, boxx, boxy):
    quarter = int (BOXSIZE * 0.25)
    half = int(BOXSIZE * 0.5)

    left, top = left_top_coords(boxx, boxy)
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top+half), half-5)
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top+half), quarter-5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left+quarter, top+quarter, BOXSIZE-half, BOXSIZE-half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half , top), (left + BOXSIZE - 1, top + half),
            (left + half, top + BOXSIZE -1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE -1), (left + BOXSIZE -1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))

def split_into_groups_of(size, box_list):
    result = []
    for i in range(0, len(box_list), size):
        result.append(box_list[i:i+size])
    return result

def cover_boxes_animation(board, box):
    for x in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
        draw_box_covers(board, box, x)

def reveal_boxes_animation(board, box):
    for x in range(BOXSIZE, (-REVEALSPEED) -1, -REVEALSPEED):
        draw_box_covers(board, box, x)

def draw_box_covers(board, boxes, x):
    for box in boxes:
        left, top = left_top_coords(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        shape, color = get_shape_and_color(board, box[0], box[1])
        draw_icon(shape, color, box[0], box[1])
        if x > 0:
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, x, BOXSIZE))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def left_top_coords(boxx, boxy):
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return left, top

def get_shape_and_color(board, boxx, boxy):
    return board[boxx][boxy][0], board[boxx][boxy][1]

def generate_revealed_boxes(val):
    revealed_boxes = []
    for i in range(BOARDWIDTH):
        revealed_boxes.append([val]*BOARDHEIGHT)
    return revealed_boxes

def get_randomized_board():
    icons = []
    for colours in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape, colours))

    random.shuffle(icons)
    no_icons_used = int (BOARDWIDTH * BOARDHEIGHT / 2)
    icons = icons[:no_icons_used] * 2
    random.shuffle(icons)

    board = []
    for x in range(BOARDWIDTH):
        col = []
        for y in range(BOARDHEIGHT):
            col.append(icons[0])
            del icons[0]
        board.append(col)
    return board

if __name__ == '__main__':
    main()
