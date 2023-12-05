import pygame
from constants import *
from sudoku_generator import SudokuGenerator
import sys
import copy

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

number_font = pygame.font.Font(None, 400)
game_over_font = pygame.font.Font(None, 40)
font = pygame.font.SysFont(None, 72)
font2 = pygame.font.SysFont(None, 45)
font3 = pygame.font.SysFont(None, 30)
font4 = pygame.font.SysFont(None, 75)
text = font.render("Welcome to Sudoku!", True, (0, 128, 0))
text2 = font2.render("Select Game Mode:", True, (0, 128, 0))
text3 = font2.render("Easy", True, (0, 128, 0))
text4 = font2.render("Medium", True, (0, 128, 0))
text5 = font2.render("Hard", True, (0, 128, 0))

easy_rect = pygame.Rect((80, 463), (text3.get_width(), text3.get_height()))
medium_rect = pygame.Rect((250, 463), (text4.get_width(), text4.get_height()))
hard_rect = pygame.Rect((450, 463), (text5.get_width(), text5.get_height()))
parameters = WIDTH // 3 - text.get_width() // 3.3, HEIGHT // 3 - text.get_height() // 3
game_start_font = pygame.Rect((parameters, (text.get_width(), text.get_height())))
pygame.draw.rect(screen, (0, 0, 0), game_start_font)

SOFTGRAY = 240, 248, 255
screen.fill(SOFTGRAY)

screen.blit(text, (WIDTH // 3 - text.get_width() // 3.3, HEIGHT // 3 - text.get_height() // 3))
screen.blit(text2, (WIDTH // 1.5 - text.get_width() // 2, HEIGHT // 1.5 - text.get_height() // 1.5))
screen.blit(text3, (60, 463))
screen.blit(text4, (230, 463))
screen.blit(text5, (434, 463))

pygame.display.update()

counter = 0
text6 = font3.render("RESET", True, (0, 128, 0))
text7 = font3.render("RESTART", True, (0, 128, 0))
text8 = font3.render("EXIT", True, (0, 128, 0))
restart_rect = pygame.Rect((225, 550), (text7.get_width(), text7.get_height()))
reset_rect = pygame.Rect((55,550), (text6.get_width(), text6.get_height()))
exit_rect = pygame.Rect((425,550), (text8.get_width(), text8.get_height()))
board_obj = None
old_board = None
x_counter, y_counter = None, None
x, y = None, None
x_val, y_val = None, None
game_continue = True
sudoku_screen = None


def game_win_screen():
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Winner!")
    SOFTGRAY = 240, 248, 255
    screen.fill(SOFTGRAY)
    win_text = font4.render("Game Won!", True, (0, 128, 0))
    screen.blit(win_text, (WIDTH // 2.5 - win_text.get_width() // 3.3, HEIGHT // 3 - win_text.get_height() // 3))
    text8 = font2.render("EXIT", True, (0, 128, 0))
    screen.blit(text8, (250, 350))
    exit_rect = pygame.Rect((250, 350), (text8.get_width(), text8.get_height()))
    reset_rect = None
    restart_rect = None
    pygame.display.update()


def game_over():
    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("LOSER!")
    SOFTGRAY = 240, 248, 255
    screen.fill(SOFTGRAY)
    win_text = font4.render("Game OVER!", True, (0, 128, 0))
    screen.blit(win_text, (WIDTH // 2.5 - win_text.get_width() // 3.3, HEIGHT // 3 - win_text.get_height() // 3))
    text8 = font2.render("RESTART", True, (0, 128, 0))
    screen.blit(text8, (200, 350))
    reset_rect = None
    restart_rect = None
    exit_rect = pygame.Rect((250, 350), (text8.get_width(), text8.get_height()))
    pygame.display.update()


def draw_lines():
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, 180),
                     (536, 180), LINE_WIDTH)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (60, 0),
                     (60, 536), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (120, 0),
                     (120, 536), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (240, 0),
                     (240, 536), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (300, 0),
                     (300, 536), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (360, 0),
                     (360, 536), LINE_WIDTH)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (420, 0),
                     (420, 536), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (480, 0),
                     (480, 536), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (180, 0),
                     (180, 536), LINE_WIDTH)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, 360),
                     (536, 360), LINE_WIDTH)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (360, 0),
                     (360, 536), LINE_WIDTH)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, 540),
                     (536, 540), LINE_WIDTH)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (540, 0),
                     (540, 541), LINE_WIDTH)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, 0),
                     (540, 0), LINE_WIDTH)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, 60),
                     (536, 60), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, 120),
                     (536, 120), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, 240),
                     (536, 240), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, 300),
                     (536, 300), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, 420),
                     (536, 420), SMALL_LINE)
    pygame.draw.line(sudoku_screen, BLACK_COLOR, (0, 480),
                     (536, 480), SMALL_LINE)


def draw_board():
    for i in range(9):
        for j in range(9):
            cell_value = board_obj.board[i][j]
            if cell_value != 0:
                cell_text = font.render(str(cell_value), True, (0, 128, 0))
                cell_rect = pygame.Rect(j * 60, i * 60, 60, 60)
                pygame.draw.rect(sudoku_screen, (255, 255, 255), cell_rect)
                sudoku_screen.blit(cell_text, (j * 60 + 20, i * 60 + 10))


def check_fill():
    num_counter = 0
    for i in range(9):
        for j in range(9):
            if board_obj.board[i][j] == 0:
                num_counter += 1

    game_winner = True
    if num_counter == 0:
        for row in board_obj.board:
            if sorted(row) != list(range(1, 10)):
                game_winner = False
                game_over()

            # Check each column
        for col in range(9):
            columns = [board_obj.board[row][col] for row in range(9)]
            if sorted(columns) != list(range(1, 10)):
                game_winner = False
                game_over()

            # Check each 3x3 subgrid
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                grid_values = [
                    board_obj.board[row][col]
                    for row in range(row_start, row_start + 3)
                    for col in range(col_start, col_start + 3)
                ]
                if sorted(grid_values) != list(range(1, 10)):
                    game_winner = False
                    game_over()

        if game_winner == True:
            game_win_screen()


while game_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if easy_rect.collidepoint(event.pos) and counter == 0:
                counter += 1
                print("Easy mode selected")
                sudoku_screen = pygame.display.set_mode((540, HEIGHT))
                pygame.display.set_caption("Sudoku Board Easy")
                sudoku_screen.fill(BG_COLOR)
                board_obj = SudokuGenerator(9, 30)
                board_obj.fill_diagonal()
                board_obj.fill_remaining(0, 0)
                board_obj.remove_cells()
                board_obj.print_board()
                old_board = copy.deepcopy(board_obj.board)
                draw_board()
                draw_lines()
                text6 = font3.render("RESET", True, (0, 128, 0))
                text7 = font3.render("RESTART", True, (0, 128, 0))
                text8 = font3.render("EXIT", True, (0, 128, 0))
                screen.blit(text6, (55, 550))
                screen.blit(text7, (225, 550))
                screen.blit(text8, (425, 550))
                pygame.display.update()
                pygame.time.Clock().tick(60)
            elif medium_rect.collidepoint(event.pos) and counter == 0:
                counter += 1
                print("Medium mode selected")
                sudoku_screen = pygame.display.set_mode((540, HEIGHT))
                pygame.display.set_caption("Sudoku Board Medium")
                sudoku_screen.fill(BG_COLOR)
                board_obj = SudokuGenerator(9, 40)
                board_obj.fill_diagonal()
                board_obj.fill_remaining(0, 0)
                board_obj.remove_cells()
                board_obj.print_board()
                old_board = copy.deepcopy(board_obj.board)
                draw_board()
                draw_lines()
                text6 = font3.render("RESET", True, (0, 128, 0))
                text7 = font3.render("RESTART", True, (0, 128, 0))
                text8 = font3.render("EXIT", True, (0, 128, 0))
                screen.blit(text6, (55, 550))
                screen.blit(text7, (225, 550))
                screen.blit(text8, (425, 550))
                pygame.display.update()
                pygame.time.Clock().tick(60)
            elif hard_rect.collidepoint(event.pos) and counter == 0:
                counter += 1
                print("Hard mode selected")
                sudoku_screen = pygame.display.set_mode((540, HEIGHT))
                pygame.display.set_caption("Sudoku Board Hard")
                sudoku_screen.fill(BG_COLOR)
                board_obj = SudokuGenerator(9, 50)
                board_obj.fill_diagonal()
                board_obj.fill_remaining(0, 0)
                board_obj.remove_cells()
                board_obj.print_board()
                old_board = copy.deepcopy(board_obj.board)
                draw_board()
                draw_lines()
                text6 = font3.render("RESET", True, (0, 128, 0))
                text7 = font3.render("RESTART", True, (0, 128, 0))
                text8 = font3.render("EXIT", True, (0, 128, 0))
                screen.blit(text6, (55, 550))
                screen.blit(text7, (225, 550))
                screen.blit(text8, (425, 550))
                pygame.display.update()
                pygame.time.Clock().tick(60)
            if pygame.mouse.get_pressed()[0] == True:
                if restart_rect.collidepoint(event.pos):
                    game_win_screen()
                elif reset_rect.collidepoint(event.pos):
                    print(old_board)
                    board_obj.board = old_board
                    old_board = copy.deepcopy(board_obj.board)
                    sudoku_screen.fill(BG_COLOR)
                    for i in range(9):
                        for j in range(9):
                            cell_value = old_board[i][j]
                            if cell_value != 0:
                                draw_board()
                                draw_lines()
                                cell_text = font.render(str(cell_value), True, (0, 128, 0))
                                cell_rect = pygame.Rect(j * 60, i * 60, 60, 60)
                                pygame.draw.rect(sudoku_screen, (255, 255, 255), cell_rect)
                                sudoku_screen.blit(cell_text, (j * 60 + 20, i * 60 + 10))
                                pygame.display.update()

                    draw_lines()
                    text6 = font3.render("RESET", True, (0, 128, 0))
                    text7 = font3.render("RESTART", True, (0, 128, 0))
                    text8 = font3.render("EXIT", True, (0, 128, 0))
                    screen.blit(text6, (55, 550))
                    screen.blit(text7, (225, 550))
                    screen.blit(text8, (425, 550))
                    pygame.display.update()
                    pygame.time.Clock().tick(60)
                elif exit_rect.collidepoint(event.pos):
                    game_continue = False
            if pygame.mouse.get_pressed()[0] == True:
                x, y = pygame.mouse.get_pos()
                print(x,y)
                x_counter = 8  # counter variable for x index
                y_counter = 8  # counter variable for y index
                for i in range(0, 510, 60):
                    if x <= i:
                        x_counter -= 1
                for j in range(0, 510, 60):
                    if y <= j:
                        y_counter -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if board_obj.board[y_counter][x_counter] != 0:
                    print(x_counter, y_counter)
                    board_obj.board[y_counter][x_counter] = 0
                    if x_counter == 0:
                        x_val = 30 - 10
                    if x_counter == 1:
                        x_val = 90 - 10
                    if x_counter == 2:
                        x_val = 150 - 10
                    if x_counter == 3:
                        x_val = 210 - 10
                    if x_counter == 4:
                        x_val = 270 - 10
                    if x_counter == 5:
                        x_val = 330 - 10
                    if x_counter == 6:
                        x_val = 390 - 10
                    if x_counter == 7:
                        x_val = 450 - 10
                    if x_counter == 8:
                        x_val = 510 - 10
                    if y_counter == 0:
                        y_val = 30 - 19
                    if y_counter == 1:
                        y_val = 90 - 19
                    if y_counter == 2:
                        y_val = 150 - 19
                    if y_counter == 3:
                        y_val = 210 - 19
                    if y_counter == 4:
                        y_val = 270 - 19
                    if y_counter == 5:
                        y_val = 330 - 19
                    if y_counter == 6:
                        y_val = 390 - 19
                    if y_counter == 7:
                        y_val = 450 - 19
                    if y_counter == 8:
                        y_val = 510 - 19
                    cell_rect = pygame.Rect(x_val - 18, y_val - 9, 56.5, 56.9)
                    pygame.draw.rect(sudoku_screen, (255, 255, 255), cell_rect)
                    pygame.display.update()
            if pygame.key.name(event.key).isdigit():
                user_num = pygame.key.name(event.key)
            if pygame.K_1 <= event.key <= pygame.K_9:
                user_num = int(pygame.key.name(event.key))
                if board_obj.board[y_counter][x_counter] == 0:
                    print(x_counter, y_counter)
                    board_obj.board[y_counter][x_counter] = user_num
                    user_num_gen = font.render(str(user_num), True, (0, 128, 0))
                    if x_counter == 0:
                        x_val = 30 - 10
                    if x_counter == 1:
                        x_val = 90 - 10
                    if x_counter == 2:
                        x_val = 150 - 10
                    if x_counter == 3:
                        x_val = 210 - 10
                    if x_counter == 4:
                        x_val = 270 - 10
                    if x_counter == 5:
                        x_val = 330 - 10
                    if x_counter == 6:
                        x_val = 390 - 10
                    if x_counter == 7:
                        x_val = 450 - 10
                    if x_counter == 8:
                        x_val = 510 - 10
                    if y_counter == 0:
                        y_val = 30 - 19
                    if y_counter == 1:
                        y_val = 90 - 19
                    if y_counter == 2:
                        y_val = 150 - 19
                    if y_counter == 3:
                        y_val = 210 - 19
                    if y_counter == 4:
                        y_val = 270 - 19
                    if y_counter == 5:
                        y_val = 330 - 19
                    if y_counter == 6:
                        y_val = 390 - 19
                    if y_counter == 7:
                        y_val = 450 - 19
                    if y_counter == 8:
                        y_val = 510 - 19
                    screen.blit(user_num_gen, (x_val, y_val))
                    pygame.display.update()
                    check_fill()









