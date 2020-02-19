c_num=input("Δώσε έναν αριθμό πιστωτκής κάρτας:")
met=len(card_number)
while(c_num==" ")or(met != 16):
  c_num= input("Δώσε έναν αριθμόπιστωτικής κάρτας:")
  met=len(c_num)
list1=[ ]
for i in range(met):
  j=c_num[i]
  list1.append(j)
  num=[int(c_num) for c_num in list1]
for i in range(14, -1, -2):
  k=int(list1[i])
  k += k
  list1[i]=k
  if (list1[i] > 9):
   list1[i] = k%10 + k//10
   num = [int(c_num) for c_num in list1]
 sum1=0
 for i in range(met):
   sum1 = (sum1 + num[i])
 t = sum1%10
 if (t != 0):
  print(" Η κάρτα δεν είναι ΕΓΚΥΡΗ!")
 else:
  print("Η κάρτα είναι ΕΓΚΥΡΗ!")
   
   

