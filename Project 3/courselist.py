'''The course list must be able to hold an unlimited number of Courses.
'''

class Node:
    'creates a node for linked lists'
    def __init__(self, data):
        self.data =data
        self.next =None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data =newdata

    def set_next(self, newnext):
        self.next =newnext

class CourseList:
    ' Your CourseList ADT must use a Linked List implementation. '
    def __init__(self):
        self.head =None

    def insert(self, courses):
        'insert the specified Course in Course Number ascending order'
        course_number = courses.number()
        course_node = Node(courses)
        if self.head is None:
            self.head = course_node

        else:
            head_node = self.head
            head_num = head_node.get_data()
            head_num = head_num.number()

            if course_number < head_num:
                course_node.set_next(self.head)
                self.head = course_node
            else:
                current = self.head
                while True:
                    if current.get_next() is None:
                        current.set_next(course_node)
                        break
                    next_node = current.get_next()
                    next_num = next_node.get_data()
                    next_num = next_num.number()
                    if course_number < next_num:
                        course_node.set_next(next_node)
                        current.set_next(course_node)
                        break
                    else:
                        current = next_node


    def remove(self, number):
        'remove the first occurrence of the specified Course'
        if self.head is None:
            raise Exception("Empty list")
        if self.head.get_data().number() == number:
            self.head = self.head.get_next()
            return

        one_before = self.head
        for node in self:
            if node.get_data().number() == number:
                one_before.set_next(node.get_next())
                return
            one_before = node

        raise Exception("Target node not found")

    def remove_all(self, number):
        'remove all occurances of item in list'
        while True:
            if self.head is None:
                raise Exception("Empty list")
            while self.head.get_data().number() == number:
                self.head = self.head.get_next()
                
            
            one_before = self.head
            for node in self:
                if node.get_data().number() == number:
                    one_before.set_next(node.get_next())
                    
                one_before = node
            break

    def find(self, number):
        'finds item in list'
        curr =self.head
        found = -1
        while curr is not None:
            if curr.get_data().number() == number:
                return curr.get_data()
            else:
                curr =curr.get_next()
        return -1

    def size(self):
        'returns size of list'
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def calculate_gpa(self):
        'return the GPA using all courses in the list'
        current = self.head
        total_grade = 0
        total_credits = 0
        while current:
            total_grade += (current.get_data().grade()* current.get_data().credit_hr())
            total_credits += current.get_data().credit_hr()
            current = current.get_next()
        if total_credits == 0:
            return 0
        return total_grade/total_credits


    def is_sorted(self):
        'return True if the list is sorted by Course Number, False otherwise'
        if self.head is None:
            return True
        current = self.head
        sorted = True
        while current.get_next() is None:
            next_node = current.get_next()
            next_num = next_node.get_data()
            next_num = next_num.number()
            current_num = current.get_data()
            current_num = current_num.number()
            if current_num>next_num:
                sorted = False
                break
            current = next_node
        return sorted

    def __str__(self):
        'make print the final thing'
        current = self.head
        string_return = ""
        while current is not None:
            string_return += (str(self.head.get_data()))
            current = current.get_next()
        return string_return
    
    def __iter__(self):
        'iterates through the list'
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __next__(self):
        'Gets next node'
        node = self.head
        node =node.next
        pass
