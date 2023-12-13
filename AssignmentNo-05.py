# Function for Bubble Sort of elements

def Bubble_Sort(marks):
    n = len(marks)
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Marks of students after performing Bubble Sort on the list :")
    for i in range(len(marks)):
        print(marks[i])

# Function for displaying top five marks

def top_five_marks(marks):
    print("Top",len(marks),"Marks are : ")
    print(*marks[::-1], sep="\n")

# Main

marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students (Press ENTER after every students marks): ")
for i in range(0, n):
    ele = int(input())
    marks.append(ele)  # adding the element

print("The marks of",n,"students are : ")
print(marks)

flag=1;
while flag==1:
    print("\n---------------MENU---------------")
    print("1. Bubble Sort of the marks")
    print("2. Exit")
    ch=int(input("\n\nEnter your choice (from 1 and 2) : "))

    if ch==1:
        Bubble_Sort(marks)
        a = input("\nDo you want to display top five marks from the list (yes/no) : ")
        if a == 'yes':
            top_five_marks(marks)
        else:
            print("\nThanks for using this program!")
            flag = 0

    elif ch==2:
        print("\nThanks for using this program!!")
        flag=0

    else:
        print("\nEnter a valid choice!!")
        print("\nThanks for using this program!!")
        flag=0
