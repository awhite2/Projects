/*Abra White
 * CS 111
 * Problem set 9
 * Dec. 2, 2012
 */
import java.awt.*;
import java.util.*;
import java.io.*;

public class Pic{
  
  //instance variables
  
  private int[][] picture; //2D int array for the picture
  
  private int height;//height of picture
  
  private int width;//width of picture
  
  //constructor method
  
  public Pic (String textFileName) throws FileNotFoundException{
    picture = readInTextFile(textFileName);
    height = picture.length;
    width = picture[0].length;
  }
  
  //instance methods
  
  //gets the height, or number of rows, in an picture
  //yes
  public int getHeight(){
    return height;
  }
  
  //gets the height, or number of columns, in the picture
  //yes
  public int getWidth(){
    return width;
  }
  
  //returns an integer corresponding to that pixel in the image
  //yes
  public int getPixel(int row, int col){
    return picture[row][col];
  }
  
  //changes specifid pixel to the corresponding value as specifd by the int value
  //yes
  public void setPixel (int row, int col, int value){
    picture[row][col]=value;
  }
  
  //make new 2d array corresponding to this one
  public int[][] getPixArray(){
    return picture;
  }
  
  //flips the image horizontally
  public void mirror(){
   
    int var = 0;//create a variable to store the value so it can be switched
    int wIndex=width-1;//create a variable for one less than the width or the greatest index
    for(int row = 0; row<height; row++){
      for(int col=0; col<width/2; col++){
        var = picture[row][col];//store value of the first
        picture[row][col] = picture[row][wIndex-col];//give the first the last value
        picture[row][wIndex-col]=var;//give the last the first value

      }
    }//no need to redefine picture object, modified above
  }
  
  //shrinks the image by 1/4
  //method is shrinking but it is not redefininging the new values in the array correctly. Probably an error in which row and col in the shrink image to use
  public void shrink(){
    int [][] shrink = new int [height/2][width/2];//create new array
    for (int row = 0; row<height/2; row++){
      for(int col = 0; col<width/2; col++){
        if(row%2==0){//if the row or the column is even
          int r = 0;//create a variable for shrink row 
          if(col%2==0){
           int c = 0;//create a variable for shrink col
           shrink[r][c]=picture[row][col];//insert this row into the new array
           c++;//add a column
          }r++;//add a row
        }
      }
    }
    picture = shrink;//redefine picture object with shrink
    height = height/2;
    width=width/2;
  }

  
  //rotates the image 90 degrees
  public void rotate90(){
    int[][] right = new int [width][height]; //creates new array where the height is the width of the previous and the width is the height of the previous
    int hIndex = height - 1;//create a variable for one less than the height or the greatest index
    for (int row = 0; row<height; row++){
      for(int col = 0; col<width; col++){
        right[col][hIndex-row]=picture[row][col];//makes the row and column of the old picture opposite
      }
    }
    int var = 0;
    picture = right;//redefine picture object with rotation
    width=var;//set variable to store the width
    width=height;//switch height and width
    height=var;//switch height and width
  }


  //reads in a text file representation of an image and converts it to a 2d array
  public static int[][] readInTextFile (String textFileName) throws FileNotFoundException{
    Scanner scan = new Scanner(new File(textFileName));//open new scanner
    //count to get numbers for array size
    int row = scan.nextInt();
    int col = scan.nextInt();
    //create new array
    int[][] newImage = new int[row][col];
    //close the scanner
    scan.close();
    
    //open a new scanner
    Scanner scan2 = new Scanner(new File(textFileName));

    for (int i=0; i<row; i++){//for each row
      for(int j=0; j<col; j++){//and for each column
        if(scan2.hasNextInt()){//see if there is another int
        newImage[i][j]= scan2.nextInt();//make the nextInt the value at this index
        }
      }
    }
    
    scan2.close();//close scanner
    return newImage;//return the picture
  }
  
  //outputs a 2d array to a text file with the given name
  public static void outputTextFile (String textFileName, int[][] pix) throws IOException{
    PrintWriter newFile = new PrintWriter(new File(textFileName));//new PrintWriter object
    newFile.print(pix);//print int array into a new file
  }
    
 
    public static void usage () {
    System.out.println(
        "java Pic <command> <arg1>...\n"
        + "where <command> <arg1>... is:\n"
        + "  display <fileName>\n"
        + "  getHeight <fileName>.txt\n"
        + "  getPixArray <fileName>.txt\n"
        + "  getPixel <row> <col> <fileName>.txt\n"
        + "  getWidth <fileName>.txt\n"
        + "  mirror <inFileName>.txt <outFileName>.txt\n"
        + "  readInTextFile <fileName>.txt\n"
        + "  rotate90 <inFileName>.txt <outFileName>.txt\n"
        + "  setPixel <row> <col> <value> <fileName>.txt\n"
        + "  shrink <inFileName>.txt <outFileName>.txt\n"
        + "  textFileToJPEG <fileName>.txt\n"
        + "  toTextFile <fileName.jpg>\n"
    ); 
}
 
public static void main (String[] args) throws IOException {

    if (args.length < 2) {
        usage();

    } else if (args[0].equals("display")) {
        String fileName = PicOps.getFolder() + args[1];
        PicOps.display(fileName);

    } else if (args[0].equals("getHeight")) {
        String fileName = PicOps.getFolder() + args[1];
        Pic p = new Pic(fileName);
        System.out.println(p.getHeight());

    } else if (args[0].equals("getPixArray")) {
         String fileName = PicOps.getFolder() + args[1];
         Pic p = new Pic(fileName);
         PicOps.display(p.getPixArray());

    // Write the clause for getPixel here!
    }else if(args[0].equals("getPixel")) {
      if(args.length<3){
        usage();
      }else{
         int row = Integer.parseInt(args[1]);//sets the second statement as the rows
         int col = Integer.parseInt(args[2]);//sets the third statement as the columns
         String fileName = PicOps.getFolder()+ args[3];
         Pic p = new Pic(fileName);
         System.out.println(p.getPixel(row, col));//finds the pixel with these rows and columns
      }


    // Write the clause for getWidth here!
    } else if (args[0].equals("getWidth")){
      String fileName = PicOps.getFolder()+ args[1];//get the file
      Pic p = new Pic(fileName);//new pic object
      System.out.println(p.getWidth());//return the width
  
    } else if (args[0].equals("mirror")) {
        if (args.length < 3) {
            usage();
        } else {
            String inFileName = PicOps.getFolder()+ args[1];
            String outFileName = PicOps.getFolder()+ args[2];
            Pic p = new Pic(inFileName);
            p.mirror();
            PicOps.display(p.getPixArray());
            outputTextFile(outFileName, p.getPixArray());
        }

    } else if (args[0].equals("readInTextFile")) {
        String fileName = PicOps.getFolder() + args[1];
        PicOps.display(readInTextFile(fileName));

    // Write the clause for rotate90 here!
    }else if(args[0].equals("rotate90")){
        if (args.length<3){//if the number of arguements isn't correct show menu
          usage();
        }else {
          String inFileName = PicOps.getFolder()+ args[1];//get file 1
          String outFileName = PicOps.getFolder()+ args[2];//creat file 2
          Pic p = new Pic(inFileName);//new pic object
          p.rotate90();//potatte pic
          PicOps.display(p.getPixArray());//show new pic
          outputTextFile(outFileName, p.getPixArray());//save to second file
        }

    } else if (args[0].equals("setPixel")) {
        if (args.length < 5) {
            usage();
        } else {
            int row = Integer.parseInt(args[1]);
            int col = Integer.parseInt(args[2]);
            int value = Integer.parseInt(args[3]);
            String fileName = PicOps.getFolder() + args[4];
            Pic p = new Pic(fileName);
            p.setPixel(row, col, value);
            PicOps.display(p.getPixArray());
         }

    // Write the clause for shrink here!
    }else if (args[0].equals("shrink")){
      if(args.length<3){
        usage();
      }else{
        String inFileName = PicOps.getFolder()+ args[1];
        String outFileName = PicOps.getFolder()+ args[2];
        Pic p = new Pic(inFileName);
        p.shrink();
        PicOps.display(p.getPixArray());
        outputTextFile(outFileName, p.getPixArray());
      }

    } else if (args[0].equals("textFileToJPEG")) {
        String fileName = PicOps.getFolder() + args[1];
        System.out.println("Create JPEG file for " + fileName);
        PicOps.textFileToJPEG(fileName);

    } else if (args[0].equals("toTextFile")) {
        String fileName = PicOps.getFolder() + args[1];
        System.out.println("Create text file for " + fileName);
        PicOps.toTextFile(fileName);

    } else {
        usage();
    }
}  // end of main method 

}