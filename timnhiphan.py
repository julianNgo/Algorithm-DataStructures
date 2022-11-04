import random



def san_sinh_mang_tang_dan(n):
    mang = []
    mang.append(random.randint(-100, 100))

    for i in range(1,n):
        tang = random.randint(1,100)
        so = mang[i-1] + tang
        mang.append(so)
    return mang


def tim_nhi_phan(mang, x):
    trai = 0
    phai = len(mang) - 1

    while trai <= phai:
        giua = (trai + phai) // 2

        if mang[giua] == x:
            return giua
        if x < mang[giua]:
            phai = giua - 1
        else:
            trai = giua + 1
    return -1

def main():
    mang = san_sinh_mang_tang_dan(20)
    print(mang)

    x = int(input("Nhap vao gia tri so nguyen can tim: "))

    vitri = tim_nhi_phan(mang, x)
    if vitri != -1:
        print(f"Gia tri {x} duoc tim thay tai vi tri {vitri}")
    else:
        print(f"Khong tim thay vi tri gia tri {x}")
    
if __name__ == "__main__":
    main()