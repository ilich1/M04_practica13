class book:
    def _init_(self, name, location, established_year, student_population, number_of_courses, ranking):
        self.name = name
        self.location = location
        self.established_year = established_year
        self.student_population = student_population
        self.number_of_courses = number_of_courses
        self.ranking = ranking

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_established_year(self):
        return self.established_year

    def set_established_year(self, established_year):
        self.established_year = established_year

    def get_student_population(self):
        return self.student_population

    def set_student_population(self, student_population):
        self.student_population = student_population

    def get_number_of_courses(self):
        return self.number_of_courses

    def set_number_of_courses(self, number_of_courses):
        self.number_of_courses = number_of_courses

    def get_ranking(self):
        return self.ranking

    def set_ranking(self, ranking):
        self.ranking = ranking

    def info(self):
        print("Name: ", self.name)
        print("Location: ", self.location)
        print("Established Year: ", self.established_year)
        print("Student Population: ", self.student_population)
        print("Number of Courses: ", self.number_of_courses)
        print("Ranking: ", self.ranking)