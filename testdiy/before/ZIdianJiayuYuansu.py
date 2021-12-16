def build_person(first_name,last_name,age=' ',sex=' '):
    ol={'first':first_name,'last':last_name}
    if age:
        ol['age']=age #在列表中新加入一个可选形参age,如果函数调用这个形参，其值就会存入到字典中
    # return ol  如果这里返回了后面的if语句就直接跳过了，导致后面的语句直接失效
    if sex:
        ol['sex']=sex #如果要重现加入多个形参，retrun语句要放在最后
    return ol
print(build_person('黄','泽民','20','man')) #以字典的形式输出


def user_huk(first,last,**usero):
    opo={}
    opo['first_name']=first
    opo['last_name']=last
    for key,value in usero.items():
        opo[key]=value
    return opo
lol=user_huk('黄','泽民',sexuality='man',age='20',speciality='土木')
print(lol)