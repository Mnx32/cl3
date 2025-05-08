import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ConcatServiceImplementation extends UnicastRemoteObject implements ConcatService {
    public ConcatServiceImplementation() throws RemoteException {
        super();
    }

    public String concate(String s1, String s2) throws RemoteException {
        return s1 + s2;
    }
}
