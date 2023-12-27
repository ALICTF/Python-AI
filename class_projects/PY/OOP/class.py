class Foursquare :
    def __init__(self, first_edge , second_edge , third_edge , fourth_edge ):
        self.first_edge = first_edge
        self.second_edge = second_edge
        self.third_edge = third_edge
        self.fourth_edge = fourth_edge

class square(Foursquare):
    def __init__(self, first_edge, second_edge, third_edge, fourth_edge):
        super().__init__(first_edge, second_edge, third_edge, fourth_edge)
        
    def area(self):
        x = pow(self.first_edge,2)
        print(f"area is {x} cm")
    def perimeter (self) :
        y = self.first_edge * 4
        print(f"perimeter is {y} cm")


class cube(square):
    def __init__(self, first_edge, second_edge, third_edge, fourth_edge):
        super().__init__(first_edge, second_edge, third_edge, fourth_edge)
    
    def cube_area(self):
        c = (self.first_edge * self.first_edge) * 6
        print(f"cube_area is {c} cm")
    def cube_volume(self):
        c = pow(self.first_edge,3)
        print(f"cube_volume is {c} cm3")


y = square(2,2,2,2)
y.area()
y.perimeter()

z = cube(2,2,2,2)
z.cube_area()
z.cube_volume()

