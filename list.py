## LIST IS MUTABLE--->>>IT MEANS WE CAN CHANGE ITS VALUES WHENEVER WE WANT
names = ["vansh","pandey","nitin"]
 
## APPEND AND INSERT NEW ITEM
names.append("Kapil")
names.insert(0,"Inder")

## PRINTING USING FOR LOOP
for name in names:
    print(name)

## CHECKING IF IT EXISTS IN LIST OR NOT
print("Vansh" in names)

## CHECKING THE LENGTH 
print(len(names))

## PRINTING USING WHILE LOOP
i=0
while i<len(names):
    print(names[i])
    i+=1
    
## TO EMPTY THE LIST
names.clear()
print(names)