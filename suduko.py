from typing import ValuesView


rows=[]
original_rows=[]
columns=[]
changes=0
test_data=r"non-program bulcrapo/test_data.txt"
with open(test_data, 'r') as file:
    test_data=file.readlines()
for i in test_data:
    i = i.split("\n")[0]
    original_rows.append(i.split())
    rows.append(i.split())
# for i in range(9):
    # rows.append(input("Type out the row with spaces in between the numbers and with a ? to represent blank spaces: ").split())
for x in range(9):
    colum=[]
    for i in rows:
        colum.append(i[x])
    columns.append(colum)
blocks=[]
for x in [0, 3, 6]:
    block=[]
    for i in rows[x:x+3]:
        block.extend(i[:3])
    blocks.append(block)
    block=[]
    for i in rows[x:x+3]:
        block.extend(i[3:6])
    blocks.append(block)
    block=[]
    for i in rows[x:x+3]:
        block.extend(i[6:9])
    blocks.append(block)
    block=[]
block_rows={"0": rows[:3], "1": rows[3:6], "2": rows[6:9]}
block_columns={"0": columns[:3], "1": columns[3:6], "2": columns[6:9]}
numbers="123456789"
indexes="012345678"
int_indexes=[int(i) for i in "012345678"]
def update_rows():
    global columns, rows
    rows=[]
    for i in range(9):
        row=[]
        for c in columns:
            row.append(c[i])
        rows.append(row)
def update_blocks():
    update_rows()
    global rows, blocks
    blocks=[]
    for x in [0, 3, 6]:
        block=[]
        for i in rows[x:x+3]:
            block.extend(i[:3])
        blocks.append(block)
        block=[]
        for i in rows[x:x+3]:
            block.extend(i[3:6])
        blocks.append(block)
        block=[]
        for i in rows[x:x+3]:
            block.extend(i[6:9])
        blocks.append(block)
        block=[]
def find_missing(array, numberslist):
    numbers=[i for i in numberslist]
    missing=[]
    for i in numbers:
        if array.count(i) == 0:
            missing.append(i)
    return missing
def row_solve(number):
    global rows, columns
    number=str(number)
    for r in rows:
        if r.count(number) == 0:
#find_missing(r, numbers).count(number) != 0
            not_number=[]
            for b in range(len(r)):
                if r[b] !="?":
                    not_number.append(r.index(r[b]))
                elif r[b] == "?":
                    if columns[r.index(r[b])].count(number) != 0:
                        not_number.append(r.index(r[b]))
            for z in not_number:
                if not_number.count(z) > 1:
                    for i in range(not_number.count(z)-1):
                        not_number.remove(z)
            if len(not_number) == 8:
                rows[b][(find_missing(not_number, int_indexes)[0])] = number
                columns[(find_missing(not_number, int_indexes)[0])][b] = number
def colum_solve(number):
    global rows, columns, changes, block_columns, block_rows
    number=str(number)
    for colum in columns:
        colum_index=columns.index(colum)
        if not number in colum:
            not_number=[]
            for a in range(len(colum)):
                if colum[a] != "?":
                    not_number.append(a)
                elif colum[a] == "?":
                    if rows[a].count(number) != 0:
                        not_number.append(a)
            for z in not_number:
                if not_number.count(z) > 1:
                    for i in range(not_number.count(z)-1):
                        not_number.remove(z)
            if len(not_number) == 8:
                    if len(find_missing(not_number, int_indexes)) == 1:
                        columns[colum_index][find_missing(not_number, int_indexes)[0]] = number
                        rows[(find_missing(not_number, int_indexes)[0])][colum_index] = number
                        block_rows={"0": rows[:3], "1": rows[3:6], "2": rows[6:9]}
                        block_columns={"0": columns[:3], "1": columns[3:6], "2": columns[6:9]}
                        # changes += 1
def block_logic(blocknumber, number):
    update_blocks()
    global blocks, block_rows, block_columns, rows, columns, changes
    number=str(number)
    selected_rows=block_rows[str(blocknumber//3)]
    selected_columns=block_columns[str(blocknumber%3)]
    for block in blocks:
        if not number in block:
            not_number=[]
            empty_space=[]
            for i in range(len(block)):
                if block[i] != "?":
                    not_number.append(i)
                elif block[i] == "?":
                    empty_space.append(i)
            for space in empty_space:
                space_row=selected_rows[space//3]
                space_column=selected_columns[space%3]
                if number in space_row:
                    not_number.append(space)
                    if space in empty_space:
                        empty_space.remove(space)
                if number in space_column:
                    not_number.append(space)
                    if space in empty_space:
                        empty_space.remove(space)
            if len(not_number) == 8:
                if len(empty_space) == 1:
                    print("it's called.")
                    c_index=columns.index(selected_columns[int(empty_space[0])%3])
                    r_index=rows.index(selected_rows[int(empty_space[0])//3])
                    #God I fucking hope this works.......
                    blocks[blocknumber][find_missing(not_number, int_indexes)[0]] = number
                    rows[r_index][c_index] = number
                    columns[c_index][r_index] = number
                    block_rows={"0": rows[:3], "1": rows[3:6], "2": rows[6:9]}
                    block_columns={"0": columns[:3], "1": columns[3:6], "2": columns[6:9]}
                    changes += 1


print("\n"*20)
for z in range(9):
    # for i in numbers:
    #     row_solve(i)
    for i in numbers:
        colum_solve(i)
    update_blocks()
    for i in numbers:
        block_logic(z, i)
for i in rows:
    print_row=""
    for n in i:
        print_row += n
        print_row += " "
    print(print_row)
original_score=0
for i in range(len(original_rows)):
    if original_rows[i] == rows[i]:
        original_score += 1
if original_score == 9:
    print("Aw fuck they're the same")
    print(f"# of Changes: {changes}")
else:
    print(f"originality socre is: {original_score}.")
    print(f"# of Changes: {changes}")

#I want to see if this bottom bit changes.........