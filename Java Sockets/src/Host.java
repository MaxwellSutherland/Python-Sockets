import java.net.*;
import java.io.*;

public class Host extends Thread {
    public static void main(String[] args) throws IOException {
        int port = 1024;
        int backlog = 5;
        String bindaddr = "192.168.86.65";

        ServerSocket ss = new ServerSocket(port, backlog, InetAddress.getByName(bindaddr));
        Boolean running = true;
        while (running) {
            Socket socket = ss.accept();
            HandleClient obj = new HandleClient(socket);
            Thread thread = new Thread(obj);
            thread.start();
        }
        ss.close();
    }
}

class HandleClient implements Runnable {
    public HandleClient(Socket socket) throws IOException {
        InputStreamReader inputReader = new InputStreamReader(socket.getInputStream());
        OutputStreamWriter outputWriter = new OutputStreamWriter(socket.getOutputStream());

        BufferedReader bufferedReader = new BufferedReader(inputReader);
        BufferedWriter bufferedWriter = new BufferedWriter(outputWriter);
        String ip = socket.getLocalAddress().toString();

        Boolean connected = true;
        while (connected) {
            String msg = bufferedReader.readLine();

            System.out.println("(" + ip.substring(1) + "): " + msg);
            LogFile("(" + ip.substring(1) + "): " + msg);

            bufferedWriter.write(msg);
            bufferedWriter.newLine();
            bufferedWriter.flush();

            if (msg.equalsIgnoreCase("DISCONNECT")) {
                break;
            }
        }
    }

    public void run() {
        System.out.println("New Client Connection");
    }

    public void LogFile(String msg) throws IOException {
        File file = new File("log.txt");
        FileWriter fr = new FileWriter(file, true);
        fr.write(msg + "\n");
        fr.close();
    }
}