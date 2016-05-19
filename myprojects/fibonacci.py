if __name__=="__main__":
    list1=[1,1]
    i=0
    j=1
    flag=1
    while flag:
        list1.append(list1[i]+list1[j])
        i=i+1
        j=j+1
        length=len(list1)
        if length==20:
            break
    print list1