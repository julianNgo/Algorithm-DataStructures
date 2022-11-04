public class _demo_recursion {

    public static int GiaiThua (int n)
    {
        if (n == 0) {
            return 1;
        }
        int t = n*GiaiThua(n-1);
        return t;
    }

    public static int Fibo (int n) {
        if (n <=2) 
            return 1;
        int fn = Fibo(n-1) + Fibo(n-2);
        return fn;
    }

    public static void printElement(int[] arr, int index) {
        // bai toan co so
        if (index < 0 | index >= arr.length) 
            return;

        printElement(arr, index + 1);
        System.out.println(arr[index]);
    }
    
    // Toi uu de quy
    static int[] F = new int[1000];
    public static int Fibo2(int n) {
        if (F[n] != 0){
            return F[n];
        }
        System.out.println("can tinh: F["+n+"]");
        if (n <= 2) {
            F[1] = 1;
            F[2] = 1;
            return 1;
        }

        F[n] = Fibo2(n-1) + Fibo2(n-2);
        return F[n];
    }
    public static void main(String[] args) {
        System.out.println(Fibo2(10));
    }
}
