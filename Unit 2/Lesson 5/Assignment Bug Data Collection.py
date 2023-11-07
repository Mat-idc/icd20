#1
def input_bug_counts(bug_type):
    num_bugs = int(input(f"How many {bug_type}'s are there?"))
    return num_bugs

#2
def calculate_percent(total,count):
    return (count/total)

#3
def input_bug_type_and_count():
    type_bug = input(f"Please enter the type of bug:") 
    count = input_bug_counts(type_bug)
    return type_bug,count

#4
def display_table(bug1, count1, bug2, count2, bug3, count3):
    total = count1+count2+count3
    print(f"{'Bug Type':<10} {'Count':>15} {'Percentage':>15} ")
    print("="*42)
    print(f"{bug1:<10} {count1:>15} {(calculate_percent(total, count1)):>15.2%}")
    print(f"{bug2:<10} {count2:>15} {(calculate_percent(total, count2)):>15.2%}") 
    print(f"{bug3:<10} {count3:>15} {(calculate_percent(total, count3)):>15.2%}") 
    print("="*42)
    print(f"{'Total':<10} {total:>15} {'100.00%':>15}")

#5
bug1,count1 = input_bug_type_and_count()
bug2,count2 = input_bug_type_and_count()
bug3,count3 = input_bug_type_and_count()


display_table(bug1,count1,bug2,count2,bug3,count3)



