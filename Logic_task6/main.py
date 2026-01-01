def towerofhanoi(n, source, aux, dest):
    if n == 1:
        print(f"Disk 1 moved from {source} to {dest}")
        return
    towerofhanoi(n - 1, source, dest, aux)
    print(f"Disk {n} moved from {source} to {dest}")
    towerofhanoi(n - 1, aux, source, dest)

n = int(input("Enter no 1: "))
towerofhanoi(n, 'A', 'B', 'C')
n = int(input("Enter no 2: "))
towerofhanoi(n, 'A', 'B', 'C')