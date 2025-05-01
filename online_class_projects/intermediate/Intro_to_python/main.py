def main():
    planet_weights = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.360,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.140
}
    weight:float=float(input('Enter a weight on Earth: '))
    planet_name=input('Enter a planet: ')

    if planet_name in planet_weights:
        calculated_weight=round(weight*planet_weights[planet_name],2)
        print(f"The equivalent weight on {planet_name}: {calculated_weight}")
    else:
        print('Can\'t calculate weight..')        
    
    
if __name__=='__main__':
    main()