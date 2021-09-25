def tongcachuso(n):
    k = 0;
    while (n > 0):
        k = k + n % 10;
        n = int(n / 10);
    return k;


n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n, "là", tongcachuso(n));
