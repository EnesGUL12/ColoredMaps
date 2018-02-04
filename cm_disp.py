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
    cmap = cmaps.map_create()

    done = False
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

        # Логика приложения

        # Очистить экран
        screen.fill(C_BKGROUND)

        # Подготавливаем картинку
        # TODO: убрать двойную прорисовку линий
        for nm in cmap:
            nd = cmap[nm]
            for ndd in cmap[nm].peers:
                pygame.draw.line(screen, C_GRAY_LINE, 
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
            pygame.draw.circle(screen, C_GRAY_LINE,
                               (S_OFFSET[3] + nd.x * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2),
                                S_OFFSET[0] + nd.y * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2)),
                               int(NODE_SIZE / 2), 2)

            font = pygame.font.SysFont("Consolas", 16, bold = True)

            st_name = font.render(nm, True, C_GRAY_LINE)
        
            screen.blit(st_name, (S_OFFSET[3] + nd.x * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2) - 10,
                                  S_OFFSET[0] + nd.y * (NODE_SIZE + NODE_SPACE) + int(NODE_SIZE / 2) - 8))


        

        # Выводим подготовленную картинку на экран
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()



run()