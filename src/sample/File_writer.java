package sample;

import java.io.IOException;
import java.io.PrintWriter;

class File_writer {
    /**
     * C&W Networks
     * Juan Diego
     * Jorge Ortega
     */
    void File_in(String text,String URL){
        try {
            PrintWriter out = new PrintWriter(URL+"Out_Spreadaheet.csv","UTF-8");
            System.out.println(text);
            out.println(text);
            out.close();
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
