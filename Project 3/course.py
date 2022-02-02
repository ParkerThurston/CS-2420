'You will implement a Course ADT which implements the following methods:'
class Course:
    'Creates an object for every course'
    def __init__(self, number= 0, name = '', credit_hr=0.0, grade=0.0):
        if (not isinstance(number, int))  or (number < 0):
            raise ValueError('course number needs to be positive')
        if not isinstance(name, str):
            raise ValueError('name needs to be a string')
        if(not(isinstance(credit_hr, float)) or (credit_hr < 0)):
            raise ValueError('credit_hr needs to be positive')
        if (not(isinstance(grade, float)) or (grade < 0)):
            raise ValueError('grade needs to be positive')
        self.number1 = number
        self.name1 = name
        self.credit_hr1 = credit_hr
        self.grade1 = grade
        self.next = None

    def number(self):
        'retrieve Course Number as an integer'
        return self.number1

    def name(self):
        'retrieve Course Name as a string'
        return self.name1

    def credit_hr(self):
        'retrieve Credits as a floating-point number'
        return self.credit_hr1

    def grade(self):
        'retrieve Grade as a numeric value in range 4.0 – 0.0'
        return self.grade1

    def __str__(self):
        'returns a string representing a single Course as shown in the Program Output section'
        string_return =( str(self.number1) + " " + str(self.name1) +
        " Grade: " + str(self.grade1) + " Credit Hours: "
        + str(self.credit_hr1))
        return string_return
    