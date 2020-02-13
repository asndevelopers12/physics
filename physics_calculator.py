class classical:
    
    def __init__(self):
        self.pi = 3.141592653589793238

    def belt_length(large_pulley,small_pulley,distance):
        
        large_pulley = float(large_pulley)
        small_pulley = float(small_pulley)
        distance = float(distance)
        try:
            if(large_pulley>0 and small_pulley>0 and distance>0 ):
                if(large_pulley>small_pulley):
                    length=((large_pulley+small_pulley)*(3.14/2)) + (2*distance) + ((large_pulley-small_pulley)**2/(4*distance))
                    return length
                else:
                    print("The values given are either lesser than radii or distance is lesser than sum of radii")
                
            else:
                print("Neither large pulley nor small pulley or distance values are not greater than zero")
                
                
        except(ZeroDivisionError, ValueError):
            print("ZeroDivisionError or ValueError")
