class School:
    def __init__(self, name, location, numStudents, numTeachers, numClasses, ranking):
        self.name = name
        self.location = location
        self.num_students = numStudents
        self.num_teachers = numTeachers
        self.num_classes = numClasses
        self.ranking = ranking

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def getNumStudents(self):
        return self.numStudents

    def setNumStudents(self, numStudents):
        self.numStudents = numStudents

    def getNumTeachers(self):
        return self.numTeachers

    def setNumTeachers(self, numTeachers):
        self.numTeachers = numTeachers

    def getNumClasses(self):
        return self.numClasses

    def setNumClasses(self, numClasses):
        self.numClasses = numClasses

    def getRanking(self):
        return self.ranking

    def set_ranking(self, ranking):
        self.ranking = ranking

    def info(self):
        print("Name:", self.name)
        print("Location:", self.location)
        print("Number of Students:", self.num_students)
        print("Number of Teachers:", self.num_teachers)
        print("Number of Classes:", self.num_classes)
        print("Ranking:", self.ranking)