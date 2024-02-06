class College_Student:
    def __init__(self, name:str, id:int, work_ethic: str) -> None:
        self.name = name
        self.id = id
        self.work_ethic = work_ethic
    
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_work_ethic(self):
        return self.work_ethic
    
    def set_work_ethic(self, new_ethic):
        self.work_ethic = new_ethic

    
def main():
    student1 = College_Student('Austin',1,'no work ethic')

    print('Student',student1.get_id(),'has', student1.get_work_ethic())

    student1.set_work_ethic("He is dead....")

    print('Student',student1.get_id(),'has', student1.get_work_ethic())

if __name__ == '__main__':
    main()