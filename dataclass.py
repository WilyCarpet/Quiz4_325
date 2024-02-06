from dataclasses import dataclass

@dataclass
class Barbie:
    model: str
    quality: str
    clean: bool

def main():
    myBarbie = Barbie("Nurse Barbie", "Poor quality", False)

    print(myBarbie.model)

    if(myBarbie.clean == True):
        print("ready to sell")
    else:
        print('ew yucky')



if __name__ == '__main__':
    main()