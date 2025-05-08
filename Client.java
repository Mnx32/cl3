import java.rmi.Naming;

public class Client {
    public static void main(String[] args) {
        try {
            ConcatService obj = (ConcatService) Naming.lookup("rmi://localhost/ConcatService");
            // String result = obj.concate("Hello ", "World");
            String result = obj.concate(args[0], args[1]);
            System.out.println("Result: "+result);     
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}
