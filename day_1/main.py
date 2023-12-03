def main():
    numbers = []
    with open("puzzle_input.txt", encoding="UTF-8") as f:
        lines = f.readlines()
    for line in lines:
        tmp_number_list = []
        tmp_number_string = ""
        for char in line:
            if int(char.isdigit()):
                tmp_number_list.append(char)
        if len(tmp_number_list) < 2:
            tmp_number_string = tmp_number_list[0] + tmp_number_list[0]
        else:
            tmp_number_string = tmp_number_list[0] + tmp_number_list[
                len(tmp_number_list) - 1]
        numbers.append(int(tmp_number_string))
    print(sum(numbers))


if __name__ == "__main__":
    main()
