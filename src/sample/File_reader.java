package sample;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

class File_reader {

    /**
     * C&W Networks
     * Juan Diego
     * Jorge Ortega
     */


    String File_out(String FILENAME){
        String Return_file = "";
        try {
            BufferedReader br = new BufferedReader(new FileReader(FILENAME));
            String sCurrentLine;
            while ((sCurrentLine = br.readLine()) != null) {
                Return_file = Return_file + sCurrentLine +"\n";
            }
            br.close();
            return Return_file;
        }catch (IOException e){
            //e.printStackTrace();
            return "";
        }
    }


    String Print_files(String Path){
        String files = "";
        File folder = new File(Path);
        File[] listOfFiles = folder.listFiles();

        if( listOfFiles != null ) {

            for (int i = 0; i < listOfFiles.length; i++) {
                if (listOfFiles[i].isFile()) {
                    String[] temp = listOfFiles[i].getName().replace(".", "-").split("-");
                    if (i == (listOfFiles.length - 1)) {

                        if (temp[temp.length - 1].equals("txt")) {
                            files = files + listOfFiles[i].getName();
                        }

                    } else {
                        files = files + listOfFiles[i].getName() + "/";
                    }
                }
            }

        }

        return files;
    }
}
