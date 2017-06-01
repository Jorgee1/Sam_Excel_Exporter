package sample;
/**
* V1.1
* */

import javafx.application.Application;

import javafx.scene.Scene;
import javafx.scene.Parent;

import javafx.stage.Stage;

import javafx.fxml.FXMLLoader;

public class Main extends Application {
    /**
     * C&W Networks
     * Juan Diego
     * Jorge Ortega
     */

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("sample.fxml"));
        primaryStage.setTitle("C&W Network - Export to Excel");
        primaryStage.setScene(new Scene(root, 600, 400));
        primaryStage.setResizable(false);
        primaryStage.show();
    }


}
