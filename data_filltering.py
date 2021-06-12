import csv


def file_open(data_list, open_csv_path):
    with open(open_csv_path, 'r', encoding='utf-8-sig') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for i in csv_file:
            data_list.append(i)
    return data_list


def make_new_sub(data, csv_save_path):
    with open(csv_save_path, 'a', encoding='utf-8-sig') as new:
        new_sub = csv.writer(new)
        new_sub.writerow(data)
    new.close()


def add_file(file1, file2, data_list1, data_list2, new_sub_list, file_path):
    file_open(data_list1, file1)
    file_open(data_list2, file2)
    print(len(data_list1))
    print(len(data_list2))
    for i in data_list2:
        #print(type(i))
        new_sub_list.append(i)
        for j in data_list1:
            #print(j[1:])
            if j[1][0] == "h":
                if i[0][:-1] == j[1]:
                    if int(i[1]) == 1 and int(j[4]) == 1:
                        data = [i[0][:-1], 1, j[4], i[1], j[2], j[3], j[5], j[6]] #new_sub_list.append(j[1:])
                        print(data)
                        make_new_sub(data, file_path)
                    elif int(i[1]) == 1 and int(j[4]) == 0:
                        data = [i[0][:-1], 1, j[4], i[1], j[2], j[3], j[5], j[6]] #new_sub_list.append(j[1:])
                        print(data)
                        make_new_sub(data, file_path)
                    elif int(i[1]) == 0 and int(j[4]) == 1:
                        data = [i[0][:-1], 1, j[4], i[1], j[2], j[3], j[5], j[6]] #new_sub_list.append(j[1:])
                        print(data)
                        make_new_sub(data, file_path)
                    elif int(i[1]) == 0 and int(j[4]) == 0:
                        data = [i[0][:-1], 0, j[4], i[1], j[2], j[3], j[5], j[6]] #new_sub_list.append(j[1:])
                        print(data)
                        make_new_sub(data, file_path)
            elif j[0][0] == "h":
                print(j)
                if i[0][:-1] == j[0]:
                    if int(i[1]) == 1 and int(j[3]) == 1:
                        data = [i[0][:-1], 1, j[3], i[1], j[1], j[2], j[4], j[5]]  # new_sub_list.append(j[1:])
                        print(data)
                        make_new_sub(data, file_path)
                    elif int(i[1]) == 1 and int(j[3]) == 0:
                        data = [i[0][:-1], 1, j[3], i[1], j[1], j[2], j[4], j[5]]  # new_sub_list.append(j[1:])
                        print(data)
                        make_new_sub(data, file_path)
                    elif int(i[1]) == 0 and int(j[3]) == 1:
                        data = [i[0][:-1], 1, j[3], i[1], j[1], j[2], j[4], j[5]]  # new_sub_list.append(j[1:])
                        print(data)
                        make_new_sub(data, file_path)
                    elif int(i[1]) == 0 and int(j[3]) == 0:
                        data = [i[0][:-1], 0, j[3], i[1], j[1], j[2], j[4], j[5]]  # new_sub_list.append(j[1:])
                        print(data)
                        make_new_sub(data, file_path)
