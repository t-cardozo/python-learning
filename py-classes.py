class Planet:

    def __init__(self, name = 'Juan', radius = 30000, gravity = 5.5, system = 'Juan System'):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

juan_planet = Planet(name = 'Troy')

print(f'Name is {juan_planet.name}')
print(juan_planet.orbit())

plantX = Planet()