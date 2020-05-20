import os
import sys
import numpy as np



def calculate_collisions(table,n):
    
    collision = False
    under_md_pos = []
    above_md_pos = []

    under_sd_pos = []
    above_sd_pos = []
    
    for i in range(n-1,-1,-1):
        
        count_quenns_mdiag = 0
        
        for k in range(i,n):
            if table[k][k-i] == 1:
                count_quenns_mdiag +=1
                under_md_pos.append((k,k-i))
        if count_quenns_mdiag > 1:
            collision = True
        elif count_quenns_mdiag == 1:
            under_md_pos = under_md_pos[:-1]
        
        count_quenns_mdiag = 0
        
        for k in range(i,n):
            if i == 0:
                break
            if table[k-i][k] ==1:
                count_quenns_mdiag+=1
                above_md_pos.append((k-i,k))
        if count_quenns_mdiag > 1:
            collision = True
        elif count_quenns_mdiag == 1:
            above_md_pos = above_md_pos[:-1]
        
        colls_mdiag = under_md_pos + above_md_pos
        
        count_quenns_mdiag = 0

        for k in range(i,n):
            if table[k][n-1-k+i] == 1:
                count_quenns_mdiag +=1
                under_sd_pos.append((k,n-1-k+i))

        if count_quenns_mdiag > 1:
            collision = True
        elif count_quenns_mdiag == 1:
            under_sd_pos = under_sd_pos[:-1]   

        count_quenns_mdiag = 0

        for k in range(i-1,-1,-1):
            if table[k][i-k-1] == 1:
                count_quenns_mdiag+=1
                above_sd_pos.append((k,i-k-1))
        
        if count_quenns_mdiag > 1:
            collision = True
        elif count_quenns_mdiag == 1:
            above_sd_pos = above_sd_pos[:-1]

        colls_sdiag = under_sd_pos + above_sd_pos

        bad_queens = len(colls_mdiag) + len(colls_sdiag)

    if collision:
        return(bad_queens,colls_mdiag,colls_sdiag)
    else:
        return(0,0,0)


if __name__ == "__main__":

    SIZE = input("Queen nums (must be > 3) = ")
    n = int(SIZE)
        

    nm = list(range(0,n))

    queens = np.random.permutation(nm)
    print(queens)
    print("\n")

    table = np.zeros((n, n), dtype=int)

    for i in range (n):
        table[queens[i]][i] = 1


    print(table)
    print("\n")


    collnums,mdiag,sdiag = calculate_collisions(table,n)

    #print(mdiag)
    #print(sdiag)

    while collnums > 0:
        copy_queens = queens
        for i in range (n):
            for j in range(i+1,n):
                copy_table = np.zeros((n, n), dtype=int)
                aux = copy_queens[i]
                copy_queens[i] = copy_queens[j]
                copy_queens[j] = aux
                for k in range(n):
                    copy_table[copy_queens[k]][k] = 1

                numc,maindiag,secdiag = calculate_collisions(copy_table,n)

                if numc < collnums:
                    collnums = numc
                    print(copy_table)
                    print("\n")
                else:
                    aux = copy_queens[i]
                    copy_queens[i] = copy_queens[j]
                    copy_queens[j] = aux

        if collnums > 0:
            queens = np.random.permutation(nm)
            print("New permutation", end='')
            print(queens)
            print("\n")


                    
                
            
        





        






        

