with open("schedule.txt", "r", encoding="utf-8") as file_obj:
    with open("tmp.txt", "w", encoding="utf-8") as new_obj:
        content = file_obj.readlines()
        print(content)
        for i in range(30000):
            for string in content:
                i = str(i)
                s = i + string
                new_obj.write(s)
