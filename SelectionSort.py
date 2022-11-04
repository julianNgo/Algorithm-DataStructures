import random

def san_sinh_mang_ngau_nhien(n):
    mang = []

    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)
    return mang

def sap_xep_chon(mang):
    n = len(mang)
    
    for i in range(n-1):
        vi_tri_min = i

        for j in range(i + 1, n):
            if mang[vi_tri_min] > mang[j]:
                vi_tri_min = j

        mang[i], mang[vi_tri_min] = mang[vi_tri_min], mang[i]
        print(i + 1, '-', mang)
    
    return mang

def main():
    mang = san_sinh_mang_ngau_nhien(10)
    print(mang)
    mang_da_sap_xep = sap_xep_chon(mang)
    return mang_da_sap_xep

if __name__ == "__main__":
    main()
    