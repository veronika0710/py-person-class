class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    # Створюємо всіх Person
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    # Встановлюємо wife / husband
    for person in people:
        person_instance = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            person_instance.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            person_instance.husband = Person.people[person["husband"]]

    return person_list
