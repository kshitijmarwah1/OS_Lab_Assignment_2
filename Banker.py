import copy
 
# -------------------------------------------------------
# Task 1 - System Input and Data Representation
# -------------------------------------------------------
 
print("=" * 50)
print("   Banker's Algorithm - Deadlock Avoidance")
print("=" * 50)
 
n = int(input("\nEnter number of processes : "))
r = int(input("Enter number of resources : "))
 
# allocation matrix
print("\nEnter Allocation Matrix (row by row):")
allocation = []
for i in range(n):
    row = []
    print("  Process", i, ":")
    for j in range(r):
        val = int(input("    Resource " + str(j) + " : "))
        row.append(val)
    allocation.append(row)
 
# maximum matrix
print("\nEnter Maximum Matrix (row by row):")
maximum = []
for i in range(n):
    row = []
    print("  Process", i, ":")
    for j in range(r):
        val = int(input("    Resource " + str(j) + " : "))
        row.append(val)
    maximum.append(row)
 
# available resources
print("\nEnter Available Resources:")
available = []
for j in range(r):
    val = int(input("  Resource " + str(j) + " : "))
    available.append(val)
 
# display allocation matrix
print("\n------ Allocation Matrix ------")
print("Process  ", end="")
for j in range(r):
    print("R" + str(j) + "  ", end="")
print()
for i in range(n):
    print("  P" + str(i) + "      ", end="")
    for j in range(r):
        print(str(allocation[i][j]) + "   ", end="")
    print()
 
# display maximum matrix
print("\n------ Maximum Matrix ------")
print("Process  ", end="")
for j in range(r):
    print("R" + str(j) + "  ", end="")
print()
for i in range(n):
    print("  P" + str(i) + "      ", end="")
    for j in range(r):
        print(str(maximum[i][j]) + "   ", end="")
    print()
 
# display available
print("\n------ Available Resources ------")
for j in range(r):
    print("  R" + str(j) + " : " + str(available[j]))
 
# -------------------------------------------------------
# Task 2 - Need Matrix Calculation
# Need = Maximum - Allocation
# -------------------------------------------------------
 
need = []
for i in range(n):
    row = []
    for j in range(r):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)
 
print("\n------ Need Matrix (Max - Allocation) ------")
print("Process  ", end="")
for j in range(r):
    print("R" + str(j) + "  ", end="")
print()
for i in range(n):
    print("  P" + str(i) + "      ", end="")
    for j in range(r):
        print(str(need[i][j]) + "   ", end="")
    print()
 
# -------------------------------------------------------
# Task 3 - Banker's Safety Algorithm
# -------------------------------------------------------
 
work = available[:]
finish = [False] * n
safe_sequence = []
count = 0
 
while count < n:
    found = False
    for i in range(n):
        if finish[i] == False:
            can_run = True
            for j in range(r):
                if need[i][j] > work[j]:
                    can_run = False
                    break
            if can_run == True:
                for j in range(r):
                    work[j] = work[j] + allocation[i][j]
                finish[i] = True
                safe_sequence.append(i)
                found = True
                count = count + 1
    if found == False:
        break
 
all_done = True
for i in range(n):
    if finish[i] == False:
        all_done = False
 
print("\n------ Safety Algorithm Result ------")
if all_done == True:
    print("  System is in SAFE STATE")
else:
    print("  System is in UNSAFE STATE - Deadlock may occur")
 
# -------------------------------------------------------
# Task 4 - Safe Sequence Determination
# -------------------------------------------------------
 
print("\n------ Safe Sequence ------")
if len(safe_sequence) == n:
    print("  Safe Sequence is : ", end="")
    for i in range(len(safe_sequence)):
        print("P" + str(safe_sequence[i]), end="")
        if i != len(safe_sequence) - 1:
            print(" --> ", end="")
    print()
else:
    print("  No safe sequence found. System is UNSAFE.")
 
# -------------------------------------------------------
# Task 5 - Result Analysis
# -------------------------------------------------------
 
print("\n========================================")
print("         RESULT ANALYSIS")
print("========================================")
 
if all_done == True:
    print("\n  State      : SAFE STATE")
    print("\n  Safe Sequence : ", end="")
    for i in range(len(safe_sequence)):
        print("P" + str(safe_sequence[i]), end="")
        if i != len(safe_sequence) - 1:
            print(" --> ", end="")
    print()
    print("\n  Explanation :")
    print("  The system is in a safe state because")
    print("  all processes can finish without causing")
    print("  a deadlock. Each process gets the resources")
    print("  it needs one by one in the safe sequence.")
else:
    print("\n  State      : UNSAFE STATE")
    print("\n  Explanation :")
    print("  The system is in an unsafe state because")
    print("  no safe sequence of execution was found.")
    print("  Some processes are waiting for resources")
    print("  that cannot be fulfilled, leading to deadlock.")
 
print("\n========================================")