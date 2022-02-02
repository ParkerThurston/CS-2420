from course import Course
from courselist import CourseList

def main():
    with open('./data.txt') as f:
        lines = f.readlines()

    for line in lines:
        input = line.strip().split(",")
        amtOfCl = Course(int(input[0]), input[1], float(input[2]), float(input[3]))
        cl =CourseList()
        cl.insert(amtOfCl)
    
    print(cl.__str__())
    print("Cumulative GPA: " +str(cl.calculate_gpa()))

if __name__ =="__main__":
    main()