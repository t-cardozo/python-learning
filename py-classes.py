class Planet:

    def __init__(self):
        self.name = 'Juan'
        self.radius = 30000
        self.gravity = 5.5
        self.system = 'Juan System'

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

juan_planet = Planet()

print(f'Name is {juan_planet.name}')
print(juan_planet.orbit())