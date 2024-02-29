def expression_and_variables():
    x:int = 20

    def to_str(x) -> str:
        return str(x)

    # print(f"{x} Converted:  "+type(to_str(x)))
    # print(f"{x} : "+type(x))
    # print("blabla = ", (x)) 
    # print("blabla = "+ (x)) these four are return an error 
    # print("blabla = ", str(x)) 

    word1 = "How"
    word2 = "do"
    word3 = "you"
    word4 = "like"
    word5 = "Python"
    word6 = "so"
    word7 = "far?"

    print(word1, word2, word3, word4, word5, word6, word7)

def functions():
    pass

def conditionals():
    
    return "aa" < "ab", "ba" < "bb", "aab" > "aabc"

print(conditionals())


def logical(number):
    if number > 11: 
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)

logical(10)

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size % filesize
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * (1+full_blocks)
    return block_size

print(calculate_storage(4092))
print(calculate_storage(6000))
print(calculate_storage(9000))