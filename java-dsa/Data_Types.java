public class Data_Types {
    static void main(){


        byte num1=127;
        System.out.println(num1);


        short num2=5000;
        System.out.println(num2);

        int num3=50000;
        System.out.println(num3);

        long num4=3598412;
        System.out.println(num4);


        float num5=3.14f;
        System.out.println(num5);


        double num6=3.146545165421;
        System.out.println(num6);


        boolean eligibletovote=true;
        System.out.println(eligibletovote);


        char firstCharacter='a';
        System.out.println("My First Character is : "+(char)(firstCharacter+3));


        // implicit conversion

        byte num7=127;
        long newnum=num7;
        System.out.println("New Num :" + newnum);



        //explicit conversion

        long value1=1234567899;
        int value2=(int)value1;
        System.out.println(value2);

    }
}
