import java.net.*;
import java.util.Scanner;
import java.io.*;

public class Client {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter IP: ");
        String IP = scanner.nextLine();
        System.out.println("Enter Port: ");
        Integer port = scanner.nextInt();
        Socket socket = new Socket(IP, port);

        InputStreamReader inputReader = new InputStreamReader(socket.getInputStream());
        OutputStreamWriter outputWriter = new OutputStreamWriter(socket.getOutputStream());

        BufferedReader bufferedReader = new BufferedReader(inputReader);
        BufferedWriter bufferedWriter = new BufferedWriter(outputWriter);

        Boolean connected = true;
        while (connected) {
            System.out.print("(" + socket.getLocalAddress().getHostAddress() + ") > ");
            String msg = scanner.nextLine();

            bufferedWriter.write(msg);
            bufferedWriter.newLine();
            float timeStart = System.currentTimeMillis();
            bufferedWriter.flush();

            msg = bufferedReader.readLine();
            float timeEnd = System.currentTimeMillis();
            System.out.println(msg + " (" + (timeEnd - timeStart) + " ms)");

            if (msg.equalsIgnoreCase("DISCONNECT")) {
                break;
            }
        }
        socket.close();
        scanner.close();
    }
}
