# Multiplication Table Printer

def multiplication_table(table_of, upto_number):
    for i in range (1, upto_number+1):
        if i == 5:
            continue
        # 5 * 1 = 5
        yield f"{table_of} * {i} = {table_of*i}"


for i in multiplication_table(10, 7):
    print(i)