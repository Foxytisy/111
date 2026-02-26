class Stundent:
    student_id: str
    full_name: str
    is_enrolled: bool
    locker_number: int
    def __init__(self, id, name, enrolled, number):
        self.student_id = id
        self.full_name = name
        self.is_enrolled = enrolled
        self.locker_number = number
    def nomSkap(self, nr):
        self.locker_number = nr
    def __str__(self):
        return f"[{self.student_id}] {self.full_name}"
stud = Stundent("S-1001", "Berzins Berzins", True, 2)
print(stud.nomSkap)