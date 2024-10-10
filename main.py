#Variables 
#Los parametros de las funciones van en el args y hay que importar el main

PI = 3.14
volume = 1

def run(radius: float) -> float:
    # TODO
    global volume
    
    volume = 4/3 * ((PI) * (radius ** 3))
    return volume

#Codigo principal


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print("El volumen del radio es: ", volume)