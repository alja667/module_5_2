class House:
    pass
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    #     self.go_to
    #
    # def go_to(self, new_floor):
    #     self.new_floor = int(new_floor)
    #     if 1 <= self.new_floor and  self.new_floor <= self.number_of_floors:
    #         for i in range(1,new_floor+1):
    #             print(i)

        # elif self.new_floor > self.number_of_floors:
        #     print(f"Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors
        print(self.number_of_floors)

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# h1.go_to(5)
# h2.go_to(10)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
