if __name__ == '__main__':
    
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #we need to store the names and scores in the nested list
        students.append([name,score])
        
    unique= sorted(set([grade for name, grade in students]))
        
    second_lowest = [name for name, grade in students if grade==unique[1]]
    for name in sorted(second_lowest):
        print(name)
    
