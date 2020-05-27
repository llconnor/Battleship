class Fleet:    
    def __init__(self):
        ship_list = []
		ship_list.append(Ship.Ship(2))
		ship_list.append(Ship.Ship(3))
		ship_list.append(Ship.Ship(3))
		ship_list.append(Ship.Ship(4))
		ship_list.append(Ship.Ship(5))

	def placeShip(num_ship:int, x:int, y:int, horizontal:true):
		# *** TODO Figure out if there are overlaps between ships
		ship_list[num_ship].placeShip(x,y,horizontal)
	
