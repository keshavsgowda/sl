f2c_conversion_list=[] 
c2f_conversion_list=[] 
def f_to_c (fahr):
    return((fahr - 32) * 5.0/9.0)
def c_to_f (cel) :
    return(9.0/5.0 * cel + 32)
def main():
    i=True
    while(i):
        ch=input("Enter the choice :")
        if ch=="1": 
                input_fahr=float(input("Enter the fahrenhiet : "))
                conv_cel=f_to_c(input_fahr)
                f2c_conversion_list.append((input_fahr,conv_cel))
                print(conv_cel)
        elif ch=="2": 
                input_cel=float(input("Enter the celsius : "))
                conv_fahr=c_to_f(input_cel)
                c2f_conversion_list.append((input_cel,conv_fahr))
                print(conv_fahr)
        elif ch=="3": 
                print("Sorted list of F2C : " , sorted(f2c_conversion_list,key=lambda x:x[0]))
                print("Sorted list of C2F : " , sorted(c2f_conversion_list,key=lambda x:x[0]))
        elif ch=="4": 
                i=False
main()