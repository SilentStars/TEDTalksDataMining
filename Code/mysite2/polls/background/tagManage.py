#people_tag:string
#tag:list

def add(people_tag,tag):
    la = people_tag.split(",")
    for i in  range(0,len(tag)):
        flag = 0
        for j in range(0,len(la)):
            if tag[i] == la[j]:
                flag = 1
        if flag == 0:
            l = [tag[i]]
            la.extend(l)

    ans = ",".join(la)
    return ans


def delete(people_tag, tag):
    la = people_tag.split(",")
    for i in tag:
        flag = 0
        for j in la:
            if i ==j:
                flag = 1
        if flag == 1:
            la.remove(i)



    ans = ",".join(la)
    return ans

