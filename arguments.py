import argparse

def demo() -> None: 	
    parser=argparse.ArgumentParser()
    parser.add_argument("--string", dest="input_string", help='Enter a string', type =str)	
    parser.add_argument("--int",dest="input_int",help='Enter an integer',type=int)        	
    parser.add_argument("--float",dest="input_float",help='Enter a float',type=float)    
	
    args = parser.parse_args()  	

    input_string = args.input_string
    input_int=args.input_int 	
    input_float=args.input_float  	

    print("Your string is", input_string)
    print("Your integer is", input_int) 	
    print("Your float is",input_float)

if __name__=='__main__': 	
    demo()
