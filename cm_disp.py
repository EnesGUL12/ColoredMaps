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


def run():
    """
    Runs application

    Intializes graphics and runs event loop
    """
    pygame.init()
    screen = pygame.display.set_mode(MIN_S_SIZE, pygame.DOUBLEBUF, 16)
    pygame.display.set_caption("Colored Maps")    
    
    done = False

    while not done:

        # --- Main event loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
                continue

            if event.type == pygame.KEYDOWN:
                logging.debug("[EVT] Key pressed [%s]",
                              pygame.key.name(event.key))
                if event.type == pygame.K_ESCAPE:
                    done = True
                    continue





run()