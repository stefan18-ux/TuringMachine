import pygame
import time

WIDTH, HEIGHT = 1200, 350
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TuringMachine")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


CELL_SIZE = 50
TAPE_OFFSET = 150  
NAME = ""
map = {}
tape = []
head_position = 10
accept = ''
curr_state = ''
steps = 0
right = 'right'
left = 'left'

Instruct = "./instructions.txt"
Tape = "./tape.txt"

tape_position = 10

def draw_program_name():
    global NAME
    font = pygame.font.SysFont('Arial', 40) 
    program_name_text = font.render(NAME, True, BLACK)
    WIN.blit(program_name_text, (50, 10))
    
def draw_tape():
    global tape, tape_position
    WIN.fill(WHITE)
    
    for i in range(-5,tape_position):
        rect = pygame.Rect(i * CELL_SIZE + 50, TAPE_OFFSET, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(WIN, BLUE, rect)
        pygame.draw.rect(WIN, BLACK, rect, 2)
        text = '' 
        font = pygame.font.SysFont('Arial', 30)
        WIN.blit(font.render(text, True, WHITE), (i * CELL_SIZE + 65, TAPE_OFFSET + 10))
    
    
    if tape_position - 10 < len(tape):
        for i in range(tape_position, 25):
            rect = pygame.Rect(i * CELL_SIZE + 50, TAPE_OFFSET, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(WIN, BLUE, rect)
            pygame.draw.rect(WIN, BLACK, rect, 2)
            text = ''
            font = pygame.font.SysFont('Arial', 30)
            WIN.blit(font.render(text, True, WHITE), (i * CELL_SIZE + 65, TAPE_OFFSET + 10))

    for i, symbol in enumerate(tape):
        rect = pygame.Rect((i + tape_position) * CELL_SIZE + 50, TAPE_OFFSET, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(WIN, BLUE, rect)
        pygame.draw.rect(WIN, BLACK, rect, 2)

        font = pygame.font.SysFont('Arial', 30)
        if symbol == '_':
            text = font.render('', True, WHITE) 
        else:
            text = font.render(symbol if symbol else '', True, WHITE) 
        WIN.blit(text, ((i + tape_position) * CELL_SIZE + 65, TAPE_OFFSET + 10))

    pygame.draw.polygon(WIN, BLACK, [
        (head_position * CELL_SIZE + 75, TAPE_OFFSET + CELL_SIZE),
        (head_position * CELL_SIZE + 60, TAPE_OFFSET + CELL_SIZE + 30),
        (head_position * CELL_SIZE + 90, TAPE_OFFSET + CELL_SIZE + 30)
    ])


def draw_final_message(final_message):
    font = pygame.font.SysFont('Arial', 40)
    if final_message:
        acceptance_text = font.render("Accepted", True, GREEN)
    else:
        acceptance_text = font.render("Rejected", True, RED)
    WIN.blit(acceptance_text, (WIDTH // 2 - 100, HEIGHT - 300))


def draw_info():
    global steps, curr_state
    font = pygame.font.SysFont('Arial', 30)
    steps_text = font.render(f"Steps: {steps}", True, BLACK)
    WIN.blit(steps_text, (50, 50))

    state_text = font.render(f"State: {curr_state}", True, BLACK)
    WIN.blit(state_text, (WIDTH - 200, 50))

def set_instructions():
    global NAME, map, tape, head_position, accept, curr_state
    with open(Instruct, 'r') as file:
        cnt = 0
        last = ['', '']
        for line in file:
            if line.startswith("//") or not line.strip():
                continue
            cnt += 1
            if cnt <= 3:
                key, value = line.split(': ', 1)
                if cnt == 1:
                    NAME = value.strip()
                elif cnt == 2:
                    curr_state = value.strip()
                else: accept = value.strip()
                continue
            instructions = line.split(',', 2)
            if len(instructions) > 2:
                map[(last[0], last[1].strip())] = [instructions[0], instructions[1], instructions[2].strip()]
            else: last = [instructions[0], instructions[1]]
    with open(Tape, 'r') as file:
        first_line = file.readline()
        tape = list(first_line.strip())
        
        
        
def run_step(direction):
    global tape_position
    if direction == 'right':
        tape_position += 1
    elif direction == 'left':
        tape_position -= 1

def run_simulation(arg):
    global NAME, map, tape, head_position, accept, curr_state, steps, tape_position
    final_message = False
    pygame.init()
    running = True
    idx = 0
    speed = (11 - int(arg)) * 0.1
    while running:
        draw_tape()
        draw_info()
        draw_program_name()
        pygame.display.update()
        time.sleep(speed)
        
        
        text = ''
        if idx >= 0 and idx < len(tape):
            text = tape[idx]
        else: text = '_' 
        
        if (curr_state, text) not in map:
            break
        
        value = map[curr_state, text]
        curr_state = value[0]
        
        if idx >= 0 and idx < len(tape):
            tape[idx] = value[1]
        
        elif idx == -1:
            tape.insert(0,value[1])
            tape_position -= 1
            idx = 0 
        elif idx == len(tape):
            tape.append(value[1])
            idx == len(tape) - 1
             
        if value[2] == '>':
            run_step(left)
            idx += 1
        elif value[2] == '<': 
            run_step(right)
            idx -= 1
        
        steps += 1
        if curr_state == accept:
            final_message = True
            break
        
    while True:
        draw_tape()
        draw_info()
        draw_program_name()
        draw_final_message(final_message)
        pygame.display.update()
        time.sleep(1000000)