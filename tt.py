if __name__ == '__main__':
    classlist = [['Tina', 37.2], ['Berry', 37.21], ['Harry', 37.21], ['Harsh', 39.0], ['Akriti', 41.0]]
    scorelist = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     scorelist.append(score)
    #     scorelist.sort()
    #     classlist.append([name, score])
    lst = sorted(sorted(classlist, key=lambda x: x[0]), key=lambda x: x[1], )
    lowestGrade = lst[0][1]
    nextlowestgradeStudent = []
    # print("lowest grade:", lowestGrade)
    # print(lst)
    for student in lst:
        # print(student[1], ">", lowestGrade, student[1] > lowestGrade)
        if student[1] > lowestGrade:
            # print(student[1], "is greater then ", lowestGrade)
            if (len(nextlowestgradeStudent) > 0):
                if (student[1] == nextlowestgradeStudent[0][1]):
                    nextlowestgradeStudent.append(student)
                    print(student[0])
            else:
                nextlowestgradeStudent.append(student)
                print(student[0])