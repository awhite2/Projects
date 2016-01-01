/*CS 230
 * Abra White
 * HW 5
 * Last updated: October 17, 2013
 */

/*create linked list in constructor
 *for each line add a new item
 * if the line is a file name read the file and close
 * if the line is a url read the url 
 * use scanner for the keyboard and a buffered reader for the file
 * as it reads sort the urls based on the url length
 */

import java.io.*;  // Java I/O package
import java.net.*; // Java web package
import java.util.*;


public class Cyberspace {
  
  private LinkedList<Webpage> urls;
  
  /* Read in the contents of a file line by line,
   * and print out each line after it is read in.
   * Stop when the end of the file is reached.
   */
  public Cyberspace(String inFileName) {
    try {
      BufferedReader reader = new BufferedReader(new FileReader(inFileName));
      urls = new LinkedList<Webpage>();
      String line = reader.readLine();  // Read the first line of the file.
      while (line != null) {  // Line becomes null at end of file
        URL r = new URL(line);
        Webpage in = new Webpage(r);
        in.lineCounter();
        urls.add(in);
        //sort(in,urls.size());
        line = reader.readLine();  // Read the next line of the file
      }
      reader.close();
    } catch (IOException ex) {
      System.out.println(ex);
    }
  }
  
  public Cyberspace () {
      Scanner scan = new Scanner(System.in);
      urls = new LinkedList<Webpage>();
    try{ do{String line = "";
      line = scan.nextLine();  // Read the next line of keyboard input
      URL r = new URL(line);
      Webpage in = new Webpage(r);
      in.lineCounter();
      //sort method
      urls.add(in);
      sorter(urls);
      }while (scan.hasNext());}
    catch (Exception ex) {
      if(ex instanceof IOException||ex instanceof MalformedURLException){
        System.out.println(ex);
      }
    }
  }
  
  //sorting using comparable
  //for int i compare the current to i
  //if current is greater than i i++
  //if not add the current to that indeax
  public static void sorter(LinkedList<Webpage> data){
    int min = 0;
    if(data.size()==1||data.size()==0){
    }else{
    for(int i = 0;i<data.size()-1;i++){
      for(int j=i+1;j<data.size();j++){
        if(data.get(j).compareTo(data.get(min))<0){
          min = j;
        }
      }
      swap(data, min, i);
    }
    }
  }
  
  public static void swap(LinkedList<Webpage> data, int i, int j){
    Webpage temp = data.get(i);
    data.set(i,data.get(j));
    data.set(j,temp);
  }

  
  public String toString(){
    String s = "";
    for(int i=0; i<urls.size(); i++){
      s += urls.get(i).toString() + "\n";
    }return s;
  }
  
  // MAIN method
  // no throws clause because exceptions are caught!
  public static void main (String[] args) { 
  if (args.length > 0) {
      Cyberspace test1 = new Cyberspace(args[0]);
      System.out.println(test1.toString());
    } else {
      Cyberspace test1 = new Cyberspace();
      System.out.println(test1.toString());
    }
    
  }  // End of "main"
  
}  