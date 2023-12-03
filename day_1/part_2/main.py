def main():
    num_in_txt_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    sorted_num_words = sorted(num_in_txt_dict.keys(), key=len, reverse=True)

    numbers = []
    with open("../puzzle_input.txt", encoding="UTF-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip().lower()
        tmp_number_list = []

        i = 0
        while i < len(line):
            if line[i].isdigit():
                tmp_number_list.append(line[i])
                i += 1
                continue

            matched = False
            for word in sorted_num_words:
                if line[i:].startswith(word):
                    tmp_number_list.append(str(num_in_txt_dict[word]))
                    i += len(word) - 1
                    matched = True
                    break

            if not matched:
                i += 1

        if not tmp_number_list:
            print("No numbers found in line: " + line)
            continue

        first_num = tmp_number_list[0]
        last_num = tmp_number_list[-1]
        final_num = int(first_num + last_num)
        numbers.append(final_num)
    print(sum(numbers))


if __name__ == "__main__":
    main()
