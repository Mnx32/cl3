import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ConcatService extends Remote {
    public String concate(String s1, String s2) throws RemoteException;
};
