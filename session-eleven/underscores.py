class Day(object):
    def __init__(self, visits, contacts):
        self.visits = visits
        self.contacts = contacts

    def __add__(self, other):
        total_visits = self.visits + other.visits
        total_contacts = self.contacts + other.contacts
        return Day(total_visits, total_contacts)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        return "Visits: %i, Contacts: %i" % (self.visits, self.contacts)

if __name__ == "__main__":
	day1 = Day(10, 1)
	day2 = Day(20, 2)
	print(day1)
	# Visits: 10, Contacts: 1

	print(day2)
	# Visits: 20, Contacts: 2

	day3 = day1 + day2
	
	print(day3)
	# Visits: 30, Contacts: 3

	day4 = sum([day1, day2, day3])

	print(day4)
	# Visits: 60, Contacts: 6