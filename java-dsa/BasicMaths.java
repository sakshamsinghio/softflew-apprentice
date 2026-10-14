public class BasicMaths {
//    Question ---->>> 1  Print Digits of a numbers

    static void printDigit(int num){
        //Agar mera num==0 ho to mai ruk jaunga
        // agar mera num!=0 hai to mai nhi rukunga

        while (num!=0){
            int digit = num % 10;
            System.out.println(digit);
            //Removing the last digit
            num = num /10;
        }
    }

    // Question --->>> 2 Count Digits of a numbers

    static int countDigit(int num){
        //Agar mera num==0 ho to mai ruk jaunga
        // agar mera num!=0 hai to mai nhi rukunga

        int count = 0;
        while (num!=0){
            int digit = num % 10;
            count++;
            //Removing the last digit
            num = num /10;
        }
        return count;
    }


    // Question --->>>3 Sum of digits of a number

    static int sumofDigit(int num){
        //Agar mera num==0 ho to mai ruk jaunga
        // agar mera num!=0 hai to mai nhi rukunga

        int sum = 0;
        while (num!=0){
            int digit = num % 10;
            sum = sum + digit ;
            //Removing the last digit
            num = num /10;
        }
        return sum;
    }





    static void main() {




        //Question ---->>>3
//        int num = 32168;
//        System.out.println(sumofDigit(num));



        //Questin --->.2
//        int num = 54321;
//        System.out.println(countDigit(num));


        //Question --->.1
//        int num = 531278952;
//        printDigit(num);
    }
}
