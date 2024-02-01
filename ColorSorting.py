import time
from colorama import Fore,Style
import random
print("READY SET GO!!")
time.sleep(2)
def get_color_code(colored_text):
    # Iterate through Colorama's Fore constants to find the matching color
    for color_name in vars(Fore):
        color_code = getattr(Fore, color_name)
        # Check if the colored text contains the color code
        if color_code in colored_text:
            return color_code
    return None  # Return None if color code not found
count = 0
for i in range(5):
    l = ["RED","BLUE","GREEN","YELLOW"]
    index_list = []
    color_list = []
    # color_list = []
    while True:
        number = random.randint(0,3)
        if number not in index_list:
            index_list.append(number)
        if len(index_list) == 4:
            break
    colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
    while True:
        number = random.randint(0,3)
        if number not in color_list:
            color_list.append(number)
        if len(color_list) == 4:
            break
# Choose a random color and corresponding Colorama code
    color_index = random.randint(0, 3)
    chosen_color = colors[color_index]
    color_name = l[color_index]
    # print(index_list)
    # print(color_list)
# Use the chosen Colorama code for the color in the grid
    first = colors[color_list[0]] + l[index_list[0]]
    second = colors[color_list[1]] + l[index_list[1]]
    third = colors[color_list[2]] + l[index_list[2]]
    fourth = colors[color_list[3]] + l[index_list[3]]
    print(f'''

                  {Style.BRIGHT + first}
      
      
      {fourth}        {Fore.WHITE + color_name}         {second}
      
                
                   {third}

    ''')
    print(Style.RESET_ALL)
    print(Fore.RESET)
    start_time = time.time()
    choice = input("W/A/S/D Enter your answer: ")
    elapsed_time = time.time() - start_time
    
    if elapsed_time < 3:
        if choice.capitalize() == "W":
            color_code = get_color_code(first)
            if color_code == chosen_color:
                print("CORRECT")
                Fore.RESET
                count += 1
                continue
            else:
                print("INCORRECT")
                continue
        elif choice.capitalize() == "D":
            color_code = get_color_code(second)
            if color_code == chosen_color:
                print("CORRECT")
                Fore.RESET
                count += 1
                continue
            else:
                print("INCORRECT")
                continue
        elif choice.capitalize() == "S":
            color_code = get_color_code(third)
            if color_code == chosen_color:
                print("CORRECT")
                Fore.RESET
                count += 1 
                continue
            else:
                print("INCORRECT")
                continue
        elif choice.capitalize() == "A":
            color_code = get_color_code(fourth)
            if color_code == chosen_color:
                print("CORRECT")
                Fore.RESET
                count += 1
                continue
            else:
                print("INCORRECT")
                continue
        else:
            print("INVALID INPUT")
            i -= 1
    else:
        print("TIME'S UP")
        continue

print(f"SCORE: , {count}/5")