class BirkbeckCourse:
    def __init__(self, department, code, title):
        self.department = department
        self.code = code
        self.title = title


class BirkbeckCSISCourse(BirkbeckCourse):
    def __init__(self, department, code, title, recorded=False):
        super().__init__(department, code, title)
        self.is_recorded = recorded


class CourseCatalog:
    def __init__(self, courses):
        pass
       
    def courses_by_department(self, department_name):
        pass
        
    def courses_by_search_term(self, search_snippet):
        pass

class Transportation:
    wheels = 0

    def __init__(self):
        self.wheels = -1

    def travel_one(self):
        print("Travelling on generic transportation")

    def travel(self, distance):
        for _ in range(distance):
            self.travel_one()

    def is_auto(self):
        return self.wheels == 4

class Bike(Transportation):

    def travel_one(self):
        print("Biking one mile")

class Car(Transportation):
    wheels = 4

    def travel_one(self):
        print("Driving one mile")

    def make_sound(self):
        print("VROOM")

class Ferrari(Car):
    pass

if __name__ == "__main__":
	t = Transportation()
	b = Bike()
	c = Car()
	f = Ferrari()
