public class Methods {
    //Declaration / Definition
    static void print2kaTable(){
        for(int i=1;i<=10;i++){
            int ans = 2*i;
            System.out.println("---->>>" + ans);
        }
    }

    // With Parameters

    static void printSum(int x ,int y){
        System.out.println("SUM: " + (x+y) );
    }

    //Non void or Return function

//    static int add(int p, int q){
//        int sum =  p+q;
//        return sum;
//    }

    //Method with same name [Method Overloading]

//    static int add(int p, int q){
//        int sum =  p+q;
//        return sum;
//    }
//
//    static int add(int p, int q, int r){
//        int sum =  p+q+r;
//        return sum;
//    }

    // Another Example of same overloading
    static int add(int p, int q){
        int sum =  p+q;
        return sum;
    }

    static float add(int p, float q){
        float ans =  p+q;
        return ans;
    }

    // Call by Value
    static void solve(int num) {
        System.out.println("inside solve : " + num);
        num*=10;
        System.out.println("inside solve : " + num);
    }



    static void main() {
//        System.out.println("Hii");
//        print2kaTable();
//        System.out.println("Saksham Singh");

//        printSum(5,10);

//        int result = add(5,50);
//        System.out.println("Result : " + result);

//        int ans1 = add(5,80);
//        int ans2 = add(5,10,55);
//        System.out.println("Ans1 : " + ans1);
//        System.out.println("Ans2 : " + ans2);

//        int ans1 = add(5,80);
//        float ans2 = add(5,8.0f);
//        System.out.println("Ans1 : " + ans1);
//        System.out.println("Ans2 : " + ans2);

        int num = 5;
        System.out.println("inside main : " + num);
        solve(num);
        System.out.println("inside main : " + num);
    }
}
