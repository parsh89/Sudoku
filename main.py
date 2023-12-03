import pygame
from constants import *
from sudoku_generator import SudokuGenerator
import sys

pygame.init()


# Set up the main screen
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Set up fonts
number_font = pygame.font.Font(None, 400)
game_over_font = pygame.font.Font(None, 40)
font = pygame.font.SysFont(None, 72)
font2 = pygame.font.SysFont(None, 45)
font3 = pygame.font.SysFont(None, 30)
text = font.render("Welcome to Sudoku!", True, (0, 128, 0))
text2 = font2.render("Select Game Mode:", True, (0, 128, 0))
text3 = font3.render("Easy", True, (0, 128, 0))
text4 = font3.render("Medium", True, (0, 128, 0))
text5 = font3.render("Hard", True, (0, 128, 0))

easy_rect = pygame.Rect((80, 463), (text3.get_width(), text3.get_height()))
medium_rect = pygame.Rect((250, 463), (text4.get_width(), text4.get_height()))
hard_rect = pygame.Rect((450, 463), (text5.get_width(), text5.get_height()))

screen.fill(BG_COLOR)

# Draw the title text
screen.blit(text, (WIDTH // 3 - text.get_width() // 3.3, HEIGHT // 3 - text.get_height() // 3))
screen.blit(text2, (WIDTH // 1.5 - text.get_width() // 2, HEIGHT // 1.5 - text.get_height() // 1.5))
screen.blit(text3, (80, 463))
screen.blit(text4, (250, 463))
screen.blit(text5, (450, 463))

# Update the main display
pygame.display.flip()




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

def check_num():
    if pygame.mouse.get_pressed()[0] == True:
        x, y = pygame.mouse.get_pos()
        print(x)
        print(y)
        x_counter = -1  # counter variable for x index
        y_counter = -1  # counter variable for y index
        for i in range(0, 540, 60):
            x_counter += 1
            if x <= i:
                for j in range(0, 540, 60):
                    y_counter += 1
                    if y <= j:
                        if event.type == pygame.KEYDOWN:
                            if pygame.K_1 <= event.key <= pygame.K_9:
                                user_num = int(pygame.key.name(event.key))
                                print(user_num)
                                if SudokuGenerator.is_valid(x_counter, y_counter, user_num):
                                    board_obj.board[x_counter, y_counter] = user_num
                                    return True



counter = 0

text6 = font3.render("RESET", True, (0, 128, 0))
text7 = font3.render("RESTART", True, (0, 128, 0))
text8 = font3.render("EXIT", True, (0, 128, 0))
restart_rect = pygame.Rect((225, 550), (text6.get_width(), text6.get_height()))


# Main game loop
while True:
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
                for i in range(9):
                    for j in range(9):
                        cell_value = board_obj.board[i][j]
                        if cell_value != 0:
                            cell_text = font.render(str(cell_value), True, (0, 128, 0))
                            cell_rect = pygame.Rect(j * 60, i * 60, 60, 60)
                            pygame.draw.rect(sudoku_screen, (255, 255, 255), cell_rect)
                            sudoku_screen.blit(cell_text, (j * 60 + 20, i * 60 + 10))
                draw_lines()
                text6 = font3.render("RESET", True, (0, 128, 0))
                text7 = font3.render("RESTART", True, (0, 128, 0))
                text8 = font3.render("EXIT", True, (0, 128, 0))
                screen.blit(text6, (55, 550))
                screen.blit(text7, (225, 550))
                screen.blit(text8, (425, 550))
                restart_rect = pygame.Rect((225, 550), (text6.get_width(), text6.get_height()))
                pygame.display.flip()
                pygame.time.Clock().tick(60)
                while True:
                    if check_num():
                        sudoku_screen.blit()

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
                for i in range(9):
                    for j in range(9):
                        cell_value = board_obj.board[i][j]
                        if cell_value != 0:
                            cell_text = font.render(str(cell_value), True, (0, 128, 0))
                            cell_rect = pygame.Rect(j * 60, i * 60, 60, 60)
                            pygame.draw.rect(sudoku_screen, (255, 255, 255), cell_rect)
                            sudoku_screen.blit(cell_text, (j * 60 + 20, i * 60 + 10))
                draw_lines()
                text6 = font3.render("RESET", True, (0, 128, 0))
                text7 = font3.render("RESTART", True, (0, 128, 0))
                text8 = font3.render("EXIT", True, (0, 128, 0))
                screen.blit(text6, (55, 550))
                screen.blit(text7, (225, 550))
                screen.blit(text8, (425, 550))
                pygame.display.flip()
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
                for i in range(9):
                    for j in range(9):
                        cell_value = board_obj.board[i][j]
                        if cell_value != 0:
                            cell_text = font.render(str(cell_value), True, (0, 128, 0))
                            cell_rect = pygame.Rect(j * 60, i * 60, 60, 60)
                            pygame.draw.rect(sudoku_screen, (255, 255, 255), cell_rect)
                            sudoku_screen.blit(cell_text, (j * 60 + 20, i * 60 + 10))
                draw_lines()
                text6 = font3.render("RESET", True, (0, 128, 0))
                text7 = font3.render("RESTART", True, (0, 128, 0))
                text8 = font3.render("EXIT", True, (0, 128, 0))
                screen.blit(text6, (55, 550))
                screen.blit(text7, (225, 550))
                screen.blit(text8, (425, 550))
                pygame.display.flip()
                pygame.time.Clock().tick(60)
            if pygame.mouse.get_pressed()[0] == True:
                if restart_rect.collidepoint(event.pos):
                    pass





