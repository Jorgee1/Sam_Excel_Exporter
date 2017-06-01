package sample;

import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;

import java.util.HashMap;
import java.util.Map;

public class Controller{
    /**
     * C&W Networks
     * Juan Diego
     * Jorge Ortega
     */
    private int Label_index  = 0;
    private String FILENAME = "";
    private File_reader file                 = new   File_reader();
    private Data_Exporter File_exporter      = new Data_Exporter();
    private Map<String,String[]> Files_Array = new     HashMap<>();
    private Map<String,Label>  New_file_name = new     HashMap<>();

    public Button Data_export, Add_File;
    public TextField File_location, Label_id;
    public VBox Elements;

    public void Export_action(){
        if(!Files_Array.isEmpty()) {
            System.out.println("Export");
            File_exporter.Wrapper(Files_Array,FILENAME);
            Elements.getChildren().clear();
            Files_Array.clear();
        }else{
            System.out.println("No file selected");
        }
    }

    public void Add_files(){
        FILENAME = File_location.getText();
        String[] Files = file.Print_files(FILENAME).split("/");
        for (String i:Files){
            Add_action(FILENAME + i);
            //System.out.println(FILENAME + i);
        }
    }

    private void Add_action(String FILE_PATH){
        String[] File_data = file.File_out(FILE_PATH).split("\n");  // Datos del archivo
        String[] name = FILE_PATH.split("/");
        if(( File_data.length > 1) && (name[name.length - 1].replace(".", "-").split("-")[name[name.length - 1].replace(".", "-").split("-").length-1].equals("txt"))){                                    // Si sube
            String ID = "File_"+String.valueOf(Label_index);
            Label label = new Label(name[name.length-1] + " - " + ID);
            Files_Array.put(ID,File_data);
            New_file_name.put(ID,label);
            Label_index++;
            Elements.getChildren().addAll(label);
            File_location.setText("");
        }else{
            System.out.println("Error uploading Files " + name[name.length-1] + " .-.");
        }
    }

    public void Remove_action(){
        String Labelname = Label_id.getText();

        Elements.getChildren().remove( New_file_name.get("File_" + String.valueOf(Labelname)) );
        Files_Array.remove("File_" + String.valueOf(Labelname));

        System.out.println("File_" + Integer.valueOf(Labelname) + " " + Files_Array.size());
        Label_id.setText("");
    }

}
