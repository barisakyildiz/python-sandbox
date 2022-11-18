def main():
    valid_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]

    """
    Getting and checking the values of squares

    """
    
    knight_hor = str(input("Please enter horizontal position of the knight: "))
    knight_hor = knight_hor.lower()
    if knight_hor.isalpha() == False or len(knight_hor) >= 2:
        print("Horizontal input for knight is not a letter")
        return
    if knight_hor not in valid_letters:
        print("Horizontal input for knight is not a proper letter")
        return
    
    knight_ver = str(input("Please enter vertical position of the knight: "))
    if knight_ver.isnumeric() == False:
        print("Vertical input for knight is not a number")
        return
    if knight_ver not in valid_numbers:
        print("Vertical input for knight is not a proper number")
        return
    
    bishop_hor = str(input("Please enter horizontal position of the bishop: "))
    bishop_hor = bishop_hor.lower()
    if bishop_hor.isalpha() == False or len(bishop_hor) >= 2:
        print("Horizontal input for bishop is not a letter")
        return
    if bishop_hor not in valid_letters:
        print("Horizontal input for bishop is not a proper letter")
        return
    
    
    bishop_ver = str(input("Please enter vertical position of the bishop: "))
    if bishop_ver.isnumeric() == False:
        print("Vertical input for bishop is not a number")
        return
    if bishop_ver not in valid_numbers:
        print("Vertical input for bishop is not a proper number")
        return
    
    if bishop_hor == knight_hor and bishop_ver == knight_ver:
        print("They can't be in the same square")
        return
    
    """
       Next 4 if blocks checks if bishop 
       can move to a valid position and 
       attack the knight

    """
    for i in range(1,8):
        if str(int(bishop_ver) + i) in valid_numbers and valid_letters.index(bishop_hor) + i <= len(valid_letters) - 1:
            hor = valid_letters[valid_letters.index(bishop_hor) + i]
            ver = str(int(bishop_ver) + i)
            if hor == knight_hor and ver == knight_ver:
                print("Bishop can attack knight")
                return

        if str(int(bishop_ver) - i) in valid_numbers and valid_letters.index(bishop_hor) + i <= len(valid_letters) - 1:
            hor = valid_letters[valid_letters.index(bishop_hor) + i]
            ver = str(int(bishop_ver) - i)
            if hor == knight_hor and ver == knight_ver:
                print("Bishop can attack knight")
                return
            

        if str(int(bishop_ver) + i) in valid_numbers and valid_letters.index(bishop_hor) - i >= 0:
            hor = valid_letters[valid_letters.index(bishop_hor) - i]
            ver = str(int(bishop_ver) + i)
            if hor == knight_hor and ver == knight_ver:
                print("Bishop can attack knight")
                return
            
        
        if str(int(bishop_ver) - i) in valid_numbers and valid_letters.index(bishop_hor) - i >= 0:
            hor = valid_letters[valid_letters.index(bishop_hor) - i]
            ver = str(int(bishop_ver) - i)
            if hor == knight_hor and ver == knight_ver:
                print("Bishop can attack knight")
                return

    """
       Next 8 if blocks checks if knight 
       can move to a valid position and 
       attack the bishop
       
    """

    if str(int(knight_ver) + 1) in valid_numbers and valid_letters.index(knight_hor) - 2 >= 0:
        hor = valid_letters[valid_letters.index(knight_hor) - 2]
        ver = str(int(knight_ver) + 1)
        if hor == bishop_hor and ver == bishop_ver:
            print("Knight can attack bishop")
            return

    if str(int(knight_ver) - 1) in valid_numbers and valid_letters.index(knight_hor) - 2 >= 0:
        hor = valid_letters[valid_letters.index(knight_hor) - 2]
        ver = str(int(knight_ver) - 1)
        if hor == bishop_hor and ver == bishop_ver:
            print("Knight can attack bishop")
            return

    if str(int(knight_ver) + 1) in valid_numbers and valid_letters.index(knight_hor) + 2 <= len(valid_letters) - 1:
        hor = valid_letters[valid_letters.index(knight_hor) + 2]
        ver = str(int(knight_ver) + 1)
        if hor == bishop_hor and ver == bishop_ver:
            print("Knight can attack bishop")
            return

    if str(int(knight_ver) - 1) in valid_numbers and valid_letters.index(knight_hor) + 2 <= len(valid_letters) - 1:
        hor = valid_letters[valid_letters.index(knight_hor) + 2]
        ver = str(int(knight_ver) - 1)
        if hor == bishop_hor and ver == bishop_ver:
            print("Knight can attack bishop")
            return
    
    if str(int(knight_ver) + 2) in valid_numbers and valid_letters.index(knight_hor) - 1 >= 0:
        hor = valid_letters[valid_letters.index(knight_hor) - 1]
        ver = str(int(knight_ver) + 2)
        if hor == bishop_hor and ver == bishop_ver:
            print("Knight can attack bishop")
            return

    if str(int(knight_ver) - 2) in valid_numbers and valid_letters.index(knight_hor) - 1 >= 0:
        hor = valid_letters[valid_letters.index(knight_hor) - 1]
        ver = str(int(knight_ver) - 2)
        if hor == bishop_hor and ver == bishop_ver:
            print("Knight can attack bishop")
            return

    if str(int(knight_ver) + 2) in valid_numbers and valid_letters.index(knight_hor) + 1 <= len(valid_letters) - 1:
        hor = valid_letters[valid_letters.index(knight_hor) + 1]
        ver = str(int(knight_ver) + 2)
        if hor == bishop_hor and ver == bishop_ver:
            print("Knight can attack bishop")
            return

    if str(int(knight_ver) - 2) in valid_numbers and valid_letters.index(knight_hor) + 1 <= len(valid_letters) - 1:
        hor = valid_letters[valid_letters.index(knight_hor) + 1]
        ver = str(int(knight_ver) - 2)
        if hor == bishop_hor and ver == bishop_ver:
            print("Knight can attack bishop")
            return
    
    print("Neither of them can attack each other")

if __name__ == '__main__':
    main()