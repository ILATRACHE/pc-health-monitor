from monitor import monitoring
from exception import Negative_Null_number , Number_greater_than100

def main():
    while True :
        try :
            cpu_limit = float(input('please entre you cpu limit '))
            if cpu_limit <=0 :
                raise Negative_Null_number("the number should be more than zero ") 
            if cpu_limit >100 :
                raise Number_greater_than100("the number should be lower than 100 ")
            ram_limit = float(input('please entre you ram limit ')) 
            if ram_limit <=0 :
                raise Negative_Null_number("the number should be more than zero ")
            if ram_limit >100 :
                raise Number_greater_than100("the number should be lower than 100 ")
            disk_limit = float(input('please entre you disk limit '))
            if disk_limit <=0 :
                raise Negative_Null_number("the number should be more than zero ")
            if disk_limit >100 :
                raise Number_greater_than100("the number should be lower than 100 ")
            break
        except ValueError :
            print("Please enter a valid number.")
        except Negative_Null_number as e:
            print(f'message :{e} ')
        except Number_greater_than100 as e:
             print(f'message :{e} ')
    monitoring(cpu_limit,ram_limit,disk_limit)


if __name__ == "__main__":
    main()