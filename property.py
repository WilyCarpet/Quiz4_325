class College_Student:
    def __init__(self, name:str, id:int, work_ethic: str) -> None:
        self._name = name
        self._id = id
        self._work_ethic = work_ethic
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id

    @property
    def work_ethic(self):
        return self._work_ethic
    
    @work_ethic.setter
    def work_ethic(self, new_ethic):
        self._work_ethic = new_ethic
    
def main():
    student1 = College_Student('Austin',1,'no work ethic')

    print('Student',student1.id,'has', student1.work_ethic)

    student1.work_ethic = "Outstanding work ethic"

    print('Student',student1.id,'has', student1.work_ethic)

if __name__ == '__main__':
    main()