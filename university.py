class University:
    def __init__(self, name, location, founded, students, programs, ranking):
        self.__name = name
        self.__location = location
        self.__founded = founded
        self.__students = students
        self.__programs = programs
        self.__ranking = ranking

    # Getters
    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_founded(self):
        return self.__founded

    def get_students(self):
        return self.__students

    def get_programs(self):
        return self.__programs

    def get_ranking(self):
        return self.__ranking

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_location(self, location):
        self.__location = location

    def set_founded(self, founded):
        self.__founded = founded

    def set_students(self, students):
        self.__students = students

    def set_programs(self, programs):
        self.__programs = programs

    def set_ranking(self, ranking):
        self.__ranking = ranking

    def info(self):
        print("Name:", self.__name)
        print("Location:", self.__location)
        print("Founded:", self.__founded)
        print("Number of students:", self.__students)
        print("Programs offered:", self.__programs)
        print("Ranking:", self.__ranking)
