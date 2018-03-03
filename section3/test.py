my_name = 'James'
#print(my_name)

my_dict = {'name':'Jose', 'age':90, 'grades':[13,45,66,90]}
another_dict = {1:15,2:75,3:150}

lottery_player = {
    'name':'ROLF',
    'numbers':(13,45,66,23,22)
}

#print(sum(lottery_player['numbers']))

#print(lottery_player['name'])

universities = [
    {
        'name':'Oxford',
        'location':'UK'
    },
    {
        'name':'MIT',
        'location':'US'
    }
]

class LotterPlayer:
    def __init__(self, name):
        self.name = name,
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

player = LotterPlayer("Rolf")
#print(player.name)
#print(player.total())

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to school.")
        #print("I'm a {}".format())
        #print("I'm going to {}".format(self.school))

anna = Student("Anna","MIT")
rolf = Student("Rolf","Oxford")

anna.marks.append(56)
anna.marks.append(71)
#print(anna.marks)
#print(anna.average())
anna.go_to_school()
Student.go_to_school()

my_list = [13,22,77,484]
print(list(filter(lambda x: x!=13, my_list)))
print([x for x in my_list if x!= 13])