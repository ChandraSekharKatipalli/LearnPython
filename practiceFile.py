ClassA_SubA = int(input())
ClassA_SubB = int(input())
ClassB_SubA = int(input())
ClassB_SubB = int(input())
Avg_ClassA = (ClassA_SubA + ClassA_SubB) / 2
Avg_ClassB = (ClassB_SubA + ClassB_SubB) / 2
print(Avg_ClassA)
print(Avg_ClassB)
if Avg_ClassA > Avg_ClassB:
    print(True)
else:
    print(False)