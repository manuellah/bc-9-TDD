def super_sum(*args):
    if not args:
        return "empty tuple"
    
    aggr_sum=0
    for item in args:
        if isinstance(item,(str,bool)):
            raise ValueError
        elif isinstance(item,(int,float)):
            aggr_sum+=item
        elif isinstance(item,(list,tuple)):
            for value in item:
                if isinstance(value,(str,bool)):
                    raise ValueError
                elif isinstance(value,(int,float)):
                    aggr_sum+=value
                    
    return aggr_sum
       
print(super_sum(2,3,4))
print(super_sum(5,[3,4]))
print(super_sum(4,5,2))
