name_list = [] 
score_list = []
students = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name,score)) 
        

# for name in name_list:
#     new_dict = {"name": name}
#     print(new_dict)  
    
# new_dict{"name": name_list}
# newer = name_list+score_list


for s in sorted([s for s,g in students if g==sorted(set([x[1] for x in students]))[1]]): print(s)
