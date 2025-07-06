print("TIC TAC TOE")
print()
print("INSTRUCTIONS:")
print()
print("The game requires 2 players. Player 1 ----> O ; Player 2 ----> X")
print("Players must enter either 0,1 or 2 in the Row and Column space. Make sure to not repeat your entries.")
print()
print("Let the game begin")
p1=input("Player 1:")
p2=input("Player 2:")
N=[0,1,2]
import numpy as n
a=n.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
print(a)
print()
num=0
while(num<10):
    if(num%2==0):
        print(p1,"'s turn (O)")
        r=int(input("Row:"))
        c=int(input("Column:"))
        if(r in N and c in N):
            if(a[r][c]==' '):
                a[r][c]="O"
                print(a)
                print()
                if(a[r][0]==a[r][1]==a[r][2]!=' '):
                    print("THE WINNER IS",p1.upper())
                    break
                elif(a[0][c]==a[1][c]==a[2][c]!=' '):
                    print("THE WINNER IS ",p1.upper())
                    break
                elif(a[0][0]==a[1][1]==a[2][2]!=' '):
                    print("THE WINNER IS ",p1.upper())
                    break
            else:
                print("Invalid")
                print()
                continue
        else:
            print("Invaild")
            print()
            continue
    else:
         print(p2,"'s turn (X)")
         r=int(input("Row:"))
         c=int(input("Column:"))
         if(r in N and c in N):
            if(a[r][c]==' '):
                a[r][c]="X"
                print(a)
                print()
                if(a[r][0]==a[r][1]==a[r][2]!=' '):
                    print("THE WINNER IS ",p2.upper())
                    break
                elif(a[0][c]==a[1][c]==a[2][c]!=' '):
                    print("THE WINNER IS ",p2.upper())
                    break
                elif(a[0][0]==a[1][1]==a[2][2]!=' '):
                    print("THE WINNER IS ",p2.upper())
                    break
            else:
                print("Invaild")
                print()
                continue
         else:
            print("Invaild")
            print()
            continue
    num=num+1
