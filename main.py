print("●STUDENT EXPENSE TRACKER●")
expenses=[]
def expense_list(n):

 x= input(f"enter expense {n} name:")
 y= input(f"enter category {n}:")
 z= int(input(f"enter amount {n}:"))
 exp= { "name": x ,"category": y ,"amount": z }
 return exp 
 
count=int(input("▪︎Enter number of entries :"))

total=0
for n in range(1,count+1):
 exp=expense_list(n)
 total=total+exp["amount"]
 expenses.append(exp)
category_total={}
for n,exp in enumerate(expenses,start=1):
 print("■EXPENSE",n ) 
 print("☆Name:",exp["name"] )
 print("~☆Category:",exp["category"])
 print("~~☆Amount:Rs.",exp["amount"])
 category=exp["category"]
 amount=exp["amount"]
 if category in category_total:
  category_total[category]+=amount
 else:
  category_total[category]=amount
print("■Category-wise total:")
for category,amount in category_total.items():
 print(category,"|Rs.",amount)

print("■Highest spend category:",max(category_total,key=category_total.get))
print("■Total expense:Rs.",total)
mbgt=int(input("Enter monthly budget:Rs."))
remaining=mbgt-total
if remaining>0:
 print("you are within your budget with remaining Rs.",remaining)
elif remaining==0:
 print("budget fully used.")
else:
 print("Overspent Rs.",abs(remaining))
