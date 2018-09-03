class Planet:

    shape = 'round'
    def __init__(self, name = 'Juan', radius = 30000, gravity = 5.5, system = 'Juan System'):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    @staticmethod
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins and spins at {speed}'

#-----------------------------------------
       
juan_planet = Planet(name = 'Troy')

print(f'Name is {juan_planet.name}')
print(juan_planet.orbit())
print(juan_planet.shape)

plantX = Planet()
print(plantX.commons())
print(plantX.spin(5000))