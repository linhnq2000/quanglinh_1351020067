def tongn(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;

n = int(input("Nhap so nguyen duong n = "));
print("Tong cac so cua", n , "la",tongn(n));