student_list=[]

def add():
    name=input("姓名：")
    if name  in student_list:

        print("已录入该学生，无法重复")
        return
    try:
        id=int(input("学号："))
        math=float(input("数学成绩:"))
        chinese=float(input("语文成绩:"))
        english=float(input("数学成绩:"))
    except ValueError:
        print("学号成绩需要输入数字，失败了")
        return
    student={"姓名":name,"学号":id,"成绩":[math,chinese,english]}
    student_list.append(student)
    print(f"{name}信息录入成功")

def search():
    search_id=input("输入查询学号")
    for id1 in student_list:
        if id1["id"]==search_id:
            print(id1)
    print("未查到该学生")

def tongji():
    total_list=[]
    for id1 in student_list:
        sum_score=sum(id1["成绩"])
        total_list.append(sum_score)
        print(f"{id1['姓名']}总分:{sum_score}")
        max_total=max(total_list)
        min_total=min(total_list)
        avg_score=sum(total_list)/len(total_list)
    print(f"全班总分最高分{max_total},最低分{min_total},平均分{avg_score}")

while True:
    print(f"可输入一下操作1、add,2、search,3、tongji,4、exit")
    a=input("输入序号内单词")
    if a=="add":
        add()
    elif a=="search":
        search()
    elif a=="tongji":
        tongji()
    elif a=="exit":
        break
    else:
        print("为输入正确指令")
