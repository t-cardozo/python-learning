from space.planet import Planet
from space.calc import planet_mass
from space.calc import planet_vol
       
x = Planet(name = 'Troy')

juan_mass = planet_mass(x.gravity, x.radius)
juan_vol = planet_vol(x.radius)

print(f'Name is {x.name} has a mass of {juan_mass} and a volume of {juan_vol}')
# print(juan_planet.orbit())
# print(juan_planet.shape)

# plantX = Planet()
# print(plantX.commons())
# print(plantX.spin(5000))