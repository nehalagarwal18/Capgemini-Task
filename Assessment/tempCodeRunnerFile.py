class Student:
    s_name="ABC"
    def __init__(self,roll, sec):
        self.roll=roll
        self.sec=sec

s1=Student(21,'A')
print(s1.s_name)
Student.s_name='JECRC'
print(s1.s_name)
s2=Student(22,'B')
print(s2.s_name)