def Basic_operations(n1,n2):
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    operation = int(input("The operation: "))
    result = None
    if operation==1:
        result = n1+n2
    elif operation==2:
        result = n1-n2
    elif operation==3:
        result = n1*n2
    elif operation==4:
        if n2==0:
            print("undefined")
        else:
            result = n1/n2
    else:
        print("invalid operation")
    return{
        "n1": n1,
        "n2": n2,
        "result": result
    }
#operation_result = Basic_operations(3,9)
#print(operation_result)

def power_operation(base, exponent, **kwargs):
    if 'modulo' in kwargs :
        result = pow(base, exponent, kwargs['modulo'])
    else:
        result = pow(base,exponent)
    return {"result": result}
result = power_operation(2,3,modulo = 5)
print(result)
