public class Pattern {
    static void main() {

        //Solid square Pattern

//        int n = 4;
//
//        for (int row = 1; row<=n; row++){
//            //for each row -> n columns
//            for (int col =1; col<=n; col++){
//                //Print Star
//                System.out.print("* ");
//            }
//            //move to next line or row
//            System.out.println();
//        }


        //Solid Rectangular Pattern

//        int n =3;
//        for (int row = 1; row<=n; row++){
//            //for each row -> 5 col
//            for(int col = 1; col<=5; col++){
//                //star
//                System.out.print("* ");
//            }
//            //move to next line or row
//            System.out.println();
//        }



        //right angle triangle

//        int n = 5;
//
//        for (int row = 1; row <=n ; row++){
//            //for each row -> Variable column
//            //formula--->> col-> (1->value of row)
//            for (int col=1; col<=row; col++){
//                System.out.print("* ");
//            }
//            //move to next line
//            System.out.println();
//        }


        //Solid Rombus Pattern


//        int n =5;
//
//        for (int row = 1; row<= n; row++){
//            //for each row--> spaces,stars
//
//            //spaces
//            for (int col=1; col<=n-row; col++){
//                System.out.print("  ");
//
//            }
//            //stars
//            for (int col = 1; col<=n; col++){
//                System.out.print("* ");
//            }
//            System.out.println();
//
//        }


        // Inverted right-angled Triangle

//        int n= 5;
//        for (int row = 1; row<=n;row++) {
//            // for each row--> variable column
//            for (int col = 1; col <= n - row + 1; col++) {
//                System.out.print("* ");
//            }
//            System.out.println();
//        }



        //Solid Pyramid Pattern

//        int n =5;
//
//        for (int row = 1; row <= n; row++){
//            for (int col=1; col<=n-row;col++){
//                System.out.print("  ");
//            }
//            for (int col  = 1; col<=2*row-1; col++){
//                System.out.print("* ");
//            }
//            System.out.println();
//        }


        // Inverted pyramid


//        int n = 4;
//
//        for (int row= 1; row <=n; row++){
//            //spaces
//            for (int col=1; col<=row-1; col++){
//                System.out.print("  ");
//            }
//            //stars
//            for (int col=1; col<=2*n-2*row+1;col++){
//                System.out.print("* ");
//            }
//            System.out.println();
//        }


        //Hollow rectangle


//        int n=4;
//
//        for(int row=1; row<=n; row++){
//            //for each row-->6colums
//            for (int col=1; col<=6; col++){
//                if (row==1 || row==n){
//                    System.out.print("* ");
//                }
//                else {
//                    if (col==1||col==6){
//                        System.out.print("* ");
//                    }
//                    else{
//                        System.out.print("  ");
//                    }
//                }
//            }
//            System.out.println();
//        }



        //Hollow right - angle Triangle

//        int n =50;
//
//        for(int row=1; row<=n; row++) {
//            // for each row --> variable columns
//            if (row==1||row==2||row==n){
//                for (int col=1; col<=row; col++){
//                    System.out.print("* ");
//                }
//            }
//            else{
//                //middle rows
//                ///1*
//                System.out.print("* ");
//                //(row-2) spaces
//                for (int col = 1; col<=row-2; col++){
//                    System.out.print("  ");
//                }
//                System.out.print("* ");
//
//            }
//            //move to next row
//            System.out.println();
//        }



        // Hollow Triangle

//        int n= 5;
//
//        for (int row= 1; row<=n; row++){
//                for (int col=1; col<=n-row; col++){
//                    System.out.print("  ");
//                }
//                //part 2
//                if(row==1||row==n){
//                    for (int col =1; col<=2*row-1; col++) {
//                        System.out.print("* ");
//                    }
//                }
//                else {
//                    //Middle rows
//                    //1*
//                    System.out.print("* ");
//                    //2r-3 space
//                    for (int col=1;col<=2*row-3;col++){
//                        System.out.print("  ");
//
//                    }
//                    //1*
//                    System.out.print("* ");
//                }
//            System.out.println();
//        }



        // Solid Diamond Pattern

        //Part:1
//        int n =4.;
//
//        for (int row = 1; row <= n; row++){
//            for (int col=1; col<=n-row;col++){
//                System.out.print("  ");
//            }
//            for (int col  = 1; col<=2*row-1; col++){
//                System.out.print("* ");
//            }
//            System.out.println();
//        }
//
//
//        //Part:2
//        for (int row= 1; row <=n; row++){
//            //spaces
//            for (int col=1; col<=row-1; col++){
//                System.out.print("  ");
//            }
//            if (row==1){
//                continue;
//            }
//            //stars
//            for (int col=1; col<=2*n-2*row+1;col++){
//                System.out.print("* ");
//            }
//            System.out.println();
//        }


        //Hollow Pyramid

//        int n= 4;
//
//        //Part 1
//
//        for (int row= 1; row<=n; row++){
//            for (int col=1; col<=n-row; col++){
//                System.out.print("  ");
//            }
//
//            //part 2
//            if(row==1){
//                for (int col =1; col<=2*row-1; col++) {
//                    System.out.print("* ");
//                }
//            }
//            else {
//                //Middle rows
//                //1*
//                System.out.print("* ");
//                //2r-3 space
//                for (int col=1;col<=2*row-3;col++){
//                    System.out.print("  ");
//
//                }
//                //1*
//                System.out.print("* ");
//            }
//            System.out.println();
//        }
//
//        //Part 2
//        for (int row=1; row<=(n-1); row++){
//            //for each row-> variable columns
//
//            //part1
//            for(int col=1; col<=row; col++){
//                System.out.print("  ");
//            }
//
//            //Part 2
//            if (row==(n-1)){
//                System.out.print("* ");
//            }
//            else{
//                //remaining rows
//                //1*
//                System.out.print("* ");
//                //20(n-r)-3 space
//                for (int col=1; col<=2*(n-row)-3; col++){
//                    System.out.print("  ");
//                }
//                //1*
//                System.out.print("* ");
//
//            }
//            System.out.println();
//        }


        //Symmetrical set

//        int n = 4;
//        for (int row =1; row<=n; row++){
//            //part1
//            for (int col=1; col<=row; col++){
//                System.out.print("* ");
//            }
//            //part2
//            for (int col=1; col<=2*(n-row); col++){
//                System.out.print("  ");
//            }
//            //part3
//            for (int col=1; col<=row; col++) {
//                System.out.print("* ");
//            }
//            System.out.println();
//        }
//
//        //inverted symmetrical half
//
//        for (int row=1; row<=n; row++){
//            //part4
//            for (int col=1; col<=n-row+1; col++){
//                System.out.print("* ");
//            }
//            //part5
//            for (int col=1; col<=(row-1)*2; col++){
//                System.out.print("  ");
//            }
//            //part6
//            for (int col=1; col<=n-row+1; col++) {
//                System.out.print("* ");
//            }
//
//            System.out.println();
//        }


        //Numerical values
        // right - angled triangle


//        int n =5;
//
//        for (int row=1; row<=n;  row++){
//            // for each row -> variable columns
//            for (int col=1;col<=row; col++){
//                System.out.print(col + "  ");
//            }
//            System.out.println();
//        }



        // using differ numbers

//        int n =5;
//        int count = 1;
//
//        for (int row=1; row<=n; row++){
//            //for each row-> variable col
//            for (int col=1; col<=row; col++){
//                System.out.print(count + "  ");
//                count ++;
//            }
//            System.out.println();
//        }


        // for A as a number

//        int n = 5;
//        for (int row = 1; row<=n; row++){
//            //for each row -> variable columns
//            for (int col=1; col<=row; col++){
//                int a = col;
//                int b = ('A'-1);
//                int ans = a+b;
//                char finalAns= (char)ans;
//                System.out.print(finalAns + "  ");
//            }
//            System.out.println();
//        }



        // same type

//        int n = 5;
//        for (int row = 1; row<=n; row++){
//            //for each row -> variable columns
//            for (int col=1; col<=row; col++){
//                int a = n-col;
//                int b = 'A';
//                int ans = a+b;
//                char finalAns= (char)ans;
//                System.out.print(finalAns + "  ");
//            }
//            System.out.println();
//        }








    }
}
