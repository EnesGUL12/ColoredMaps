# Project: Colored maps, task from Charles Wetherell book
#
# https://github.com/EnesGUL12/ColoredMaps.git
#
# dr.doberman, EnesGUL, Faf_Faf
#
"""
cm_disp creates graphic window to display colored maps model
"""

import pygame
import logging

import cmaps

NODE_SIZE = 40
NODE_SPACE = 30
S_OFFSET = (40, 40, 40, 40)
MIN_S_SIZE = (12 * NODE_SIZE + 11 * NODE_SPACE + S_OFFSET[1] + S_OFFSET[3],
              7 * NODE_SIZE + 6 * NODE_SPACE + S_OFFSET[0] + S_OFFSET[2])

C_BKGROUND  = ( 18,  81,   9)
C_GRAY_LINE = (128, 128, 128)

C_YELLOW  = (255, 255,   0)
C_CYAN    = (  0, 255, 255)
C_PINK    = (255,   0, 255)
C_ORANGE  = (255, 128,   0)
C_WHITE   = (255, 255, 255)
C_COLORS = [C_YELLOW, C_CYAN, C_PINK, C_ORANGE, C_WHITE]

def run():
    """
    Runs application

    Intializes graphics and runs event loop
    """
    pygame.init()

    screen = pygame.display.set_mode(MIN_S_SIZE, pygame.DOUBLEBUF, 16)
    pygame.display.set_caption("Colored Maps")    
    
    clock = pygame.time.Clock()

    # Инициализировать карту цветов
    cmap = cmaps.get_cmap()

    done = False
    ax, ay = -1, -1
    while not done:

        # --- Main event loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
                break

            if event.type == pygame.KEYDOWN:
                logging.debug("[EVT] Key pressed [%s]",
                              pygame.key.name(event.key))
                if event.key == pygame.K_ESCAPE:
                    done = True
                    break

            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                if (mx >= S_OFFSET[3] and mx <= MIN_S_SIZE[0] - S_OFFSET[1] and
                    my >= S_OFFSET[0] and my <= MIN_S_SIZE[1] - S_OFFSET[2]):
                    ax, ay = -1, -1
                    for x in range(12):
                        xx = S_OFFSET[3] + x * (NODE_SIZE + NODE_SPACE)
                        if mx >= xx and mx <= xx + NODE_SIZE:
                            ax = x
                            break
                    for y in range(7):
                        yy = S_OFFSET[0] + y * (NODE_SIZE + NODE_SPACE)
                        if my >= yy and my <= yy + NODE_SIZE:
                            ay = y
                            break
            
        # Логика приложения
                
        # Очистить экран
        screen.fill(C_BKGROUND)

        # Подготавливаем картинку
        # TODO: убрать двойную прорисовку линий
        anode = ""
        for nm in cmap:
            nd = cmap[nm]
            nline = C_GRAY_LINE
            if ax == nd.x and ay == nd.y:
                anode = nm
            for ndd in cmap[nm].peers:
                pygame.draw.line(screen, nline, 
                                 (S_OFFSET[3] + nd.x * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2),
                                  S_OFFSET[0] + nd.y * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2)), 
                                 (S_OFFSET[3] + ndd.x * (NODE_SIZE  + NODE_SPACE) + int(NODE_SIZE / 2),
                                  S_OFFSET[0] + ndd.y * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2)), 2)

        if anode != "":
            nd = cmap[anode]
            nline = C_COLORS[nd.color]
            for ndd in cmap[anode].peers:
                pygame.draw.line(screen, nline, 
                                 (S_OFFSET[3] + nd.x * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2),
                                  S_OFFSET[0] + nd.y * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2)), 
                                 (S_OFFSET[3] + ndd.x * (NODE_SIZE  + NODE_SPACE) + int(NODE_SIZE / 2),
                                  S_OFFSET[0] + ndd.y * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2)), 2)
            
        for nm in cmap:
            nd = cmap[nm]
            pygame.draw.circle(screen, C_BKGROUND,
                               (S_OFFSET[3] + nd.x * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2),
                                S_OFFSET[0] + nd.y * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2)),
                               int(NODE_SIZE / 2))
            pygame.draw.circle(screen, C_COLORS[nd.color],
                               (S_OFFSET[3] + nd.x * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2),
                                S_OFFSET[0] + nd.y * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2)),
                               int(NODE_SIZE / 2), 2)

            font = pygame.font.SysFont("Consolas", 16, bold = True)

            st_name = font.render(nm, True, C_COLORS[nd.color])
        
            screen.blit(st_name, (S_OFFSET[3] + nd.x * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2) - 10,
                                  S_OFFSET[0] + nd.y * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2) - 8))


        

        # Выводим подготовленную картинку на экран
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()



run()