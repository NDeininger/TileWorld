import pygame

class Particle:
    def __init__(self, screen):
        self.particles = []
        self.screen = screen

    def create_particles(self, loc_x, loc_y, radius, direction_x, direction_y, shape, color):
        particle_object = [[loc_x, loc_y], radius, [direction_x, direction_y], shape, color]
        self.particles.append(particle_object)

    def animate_particles(self):
        #Check for particles with r < 0 before animating
        self.remove_particles()
        for particle in self.particles:
            #Move particle
            particle[0][0] += particle[2][0]
            particle[0][1] += particle[2][1]
            #Decay Particle
            particle[1] -= 0.25
            #Draw Particle
            if particle[3] == 1:
                pygame.draw.circle(self.screen, particle[4], particle[0], int(particle[1]))

    def remove_particles(self):
        cleaned_particles = [particle for particle in self.particles if particle[1] > 0]
        self.particles = cleaned_particles
