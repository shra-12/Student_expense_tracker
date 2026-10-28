def expense_list(n):

 x= input(f"enter expense {n} name:")
 y= input(f"enter category {n}:")
 z= int(input(f"enter amount {n}:"))
 print(n,"Expense:",x)
 print(n,"Category:",y)
 print(n,"Amount: Rs.",z)
 return z
count=int(input("enter number of entries :"))
t=0
for n in range(1,count+1):
 t=t+expense_list(n)

print("total expense: Rs. ",t )
