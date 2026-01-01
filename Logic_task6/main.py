def towerofhanoi(n, source, aux, dest):
    if n==1:
        print("Move disk 1 from source", source, " to ", dest)
        return
    towerofhanoi(n-1, source, dest, aux)
    print(f"Disk {n} moved from {source} to {dest}")
    towerofhanoi(n-1, aux, source, dest)
