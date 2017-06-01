package sample;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

class Data_Exporter {
    /**
     * C&W Networks
     * Juan Diego
     * Jorge Ortega
     */
    private static final String Ref_name = "Target:", Ref_count = "show port description | match", Ref_search = " 10/100/G", SAP_CMD = "show service sap-using | match \"Number\"",Ref_SAP = "Number of SAPs : ", Ref_service = "Matching Services : ";
    private File_writer myFile          = new File_writer();
    private List<String> Data_Name      = new ArrayList<>();
    private List<String> Data_Sap       = new ArrayList<>();
    private List<String> Data_Services  = new ArrayList<>();
    private List<String> Data_Ports     = new ArrayList<>();

    void Wrapper(Map<String,String[]> myFiles,String URL ){
        String New_File= "";
        for(String key : myFiles.keySet()) {
            Exporter(myFiles.get(key));
            New_File = New_File + "Name,Services,Saps,Ports\n";
            System.out.println(Data_Name.size() + " " +Data_Services.size()+" "+Data_Sap.size()+" "+Data_Sap.size() + " " + Data_Ports.size());
            for(int j=0;j<Data_Name.size();j++){

                New_File = New_File + Data_Name.get(j) + "," + Data_Services.get(j) + ","+ Data_Sap.get(j) + "," + Data_Ports.get(j)+"\n";
            }
            New_File = New_File + "\n";
            Data_Name.clear();
            Data_Sap.clear();
            Data_Services.clear();
            Data_Ports.clear();
        }
        myFile.File_in(New_File,URL);
        System.out.println(New_File);
    }


    private void Exporter(String[] File_data)
    {
        int count = 0;
        for(int i=0;i<File_data.length;i++) {
            if(File_data[i].contains(Ref_name)) {
                String result = File_data[i].substring(File_data[i].indexOf(Ref_name) + Ref_name.length(), File_data[i].length());
                Data_Name.add(result);
            }

            if(File_data[i].contains(Ref_count+Ref_search)){

                int j=i+1;
                while(!File_data[j].contains("#")){
                    if(File_data[j].contains(Ref_search)){
                        count++;
                    }
                    if(j<(File_data.length-1)) {
                        j++;
                    }else{
                        break;
                    }
                }
                Data_Ports.add(String.valueOf(count));
                i=j;
                count=0;
            }

            if(File_data[i].contains(SAP_CMD)) {
                if (File_data[i+1].contains(Ref_SAP)) {
                    String result1 = File_data[i+1].substring(File_data[i+1].indexOf(Ref_SAP) + Ref_SAP.length(), File_data[i+1].length());
                    Data_Sap.add(result1);
                }
                else {
                    Data_Sap.add("0");
                }
            }

            if(File_data[i].contains(Ref_service)){
                String result1 = File_data[i].substring(File_data[i].indexOf(Ref_service) + Ref_service.length(), File_data[i].length());
                Data_Services.add(result1);
            }
        }




    }
}
