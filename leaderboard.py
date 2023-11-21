def read_leaderboard():
    file_name = 'leaderboard.txt'
    msg = ""
    count = 1
    with open(file_name) as file_object:
        for line in file_object:
            msg += f"{count}: {line}\n"
            count +=1
    print(msg)

read_leaderboard()