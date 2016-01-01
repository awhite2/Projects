/*CS 230
 * Abra White
 * HW 5
 * Last updated: October 17, 2013
 */

import java.net.*;
import java.util.*;
import java.io.*;

public class Webpage implements Comparable<Webpage> {
  private URL u;
  private Object textContent;
  private int lineCount;

  public Webpage(URL url) throws IOException{
    u = url;
    textContent = u.getContent();
    lineCount =0;
  }
  
  public void lineCounter(){
    try {
      BufferedReader reader = new BufferedReader(new InputStreamReader(u.openStream()));
      String line = reader.readLine();  // Read the first line of the web page 
      while (line != null) {  // Line becomes null at end of web page 
        lineCount++;
        line = reader.readLine();  // Read the next line of the web page
      }
      reader.close();
    } catch (IOException ex) {
      System.out.println(ex);
    }
  }
  
  public int getLineCount(){
    return lineCount;
  }
  
  public int compareTo(Webpage w2){
    String webpage2 = String.valueOf(w2.getLineCount());
    String webpage1 = String.valueOf(this.getLineCount());
    return webpage1.compareTo(webpage2);
  }
  
  public String toString(){
    String str = u.toString() + ": " + lineCount;
    return str;
  }
 }
  
  
