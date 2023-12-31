from modules import Stack

def my_stack_function(arr):
    p = Stack()
    p2 = Stack()
    
    for i in arr:
        p.push(i)
    
    while p.isEmpty() == False:
        act = p.pop()
        if p2.isEmpty() == False:
            c = -1
            while c != p2.size():
                if p2.isEmpty() == True:
                    p2.push(act)
                    c = p2.size()
                elif p2.top() < act:
                    s = p2.pop()
                    p.push(s)
                else:
                    p2.push(act)
                    c = p2.size()
        else:
            p2.push(act)
    
    return p2.items

result = my_stack_function([2, 6 , 7, 5, 1, 7, 6, -1, 3])
print(result)