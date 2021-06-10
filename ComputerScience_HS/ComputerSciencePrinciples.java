import java.util.Scanner;
public class ComputerSciencePrinciples
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inp = sc.nextLine();
        if (inp.length()!=18) {
            System.out.println("Your input is incorrect.");
            System.exit(0);
        }
        String x=shift2(inp);
        String y=shift(x);

        // inp=shift2(shift(inp));
        // if (inp.equals("inagzgkpm)Wl&Tg&io")) {
        //     System.out.println("Correct. Your input is the flag.");
        // }
        // else {
        //     System.out.println("Your input is incorrect.");
        // }
        System.out.println(inp);
    }
    public static String shift(String input) {
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)+i);
        }
        System.out.println(ret);
        return ret;
    }
    public static String shift2(String input) {
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)-Integer.toString((int)input.charAt(i)).length());
        }
        System.out.println(ret);
        return ret;
    }
}

// flag{intr0_t0_r3v}
