// A simple dictionary tree written in Java.
// See the Scheme version, which is simpler!

import java.util.Vector;
import java.io.*;

public class Dict {
    
  private boolean isFinal = false;
  private int numWords; 
  private Vector edges;

  public Dict () {
    this(false, 0, new Vector());
  }
     
  public Dict (boolean b, int n, Vector v) {
          this.isFinal = b;
          this.numWords = n;
          this.edges = v;
  }
     
  public Dict (String s) {
    if (s.equals("")) {
      this.isFinal = true;
      this.edges = null;
    } else {
      Vector v = new Vector();
      v.addElement(new DictEdge(s.charAt(0),new Dict(s.substring(1,s.length()))));
      this.isFinal = false;
      this.edges = v;
    }
  }
     
  public int size () {
    return numWords;
  }
    
  public boolean isWord (String s) {
    return find(s, 0); 
  }
     
  private boolean find(String s, int i) {
    if (i == s.length()) {
      return isFinal;
    } else if (edges == null) {
      return false;
    } else {
      Dict d = findSub(s.charAt(i));
      if (d == null) {
        return false;
      } else {
        return d.find(s,i+1);
      }
    } 
  }
  
  private Dict findSub(char c) {
    for (int i = 0; i < edges.size(); i++) {
      DictEdge edge = (DictEdge) (edges.elementAt(i));
      if (c < edge.letter) {
        return null;
      } else if (c == edge.letter) {
        return edge.dict;
      } else {
        // continue through loop
      }
    }
    return null; // Should never get here.
  }
  
  public boolean insert (String s) {
    // If the s is not already in this dict, inserts s and returns true.
    // Otherwise, leaves this dict unchanged and returns false. 
    if (s.equals("")) {
      if (isFinal) {
        return false;
      } else {
        isFinal = true;
        numWords = 1;
        return true;
      }
    } else {
      if (edges == null) {
        edges = new Vector();
      }
      char c = s.charAt(0);
      int len = edges.size();
      int i = 0; 
      DictEdge e = null;
      // If the s is not already in d, inserts s into d and returns true.
      // Otherwise, leaves d unchanged and returns false. 
      while ((i < len) && (c > (e = (DictEdge) (edges.elementAt(i))).letter)) {
        i++;
      }
      if (i == len) {
        edges.addElement(new DictEdge(c, fromWord(butFirst(s))));
        numWords++;
        return true;
      } else if (c == e.letter) {
        boolean b = e.dict.insert(LabOps.butFirst(s));
        if (b) numWords++;
        return b;
      } else { // c < e.letter
        edges.insertElementAt(new DictEdge(c, fromWord(butFirst(s))), i);
        numWords++;
        return true;
      }
    }
  }
  
  public static Dict fromWord (String s) {
    if (s.equals("")) {
      return new Dict(true,1,null);
    } else {
      Vector v = new Vector();
      v.addElement(new DictEdge(s.charAt(0),fromWord(butFirst(s))));
      return new Dict(false,1,v);
    }
  }
 
  // Return a dictionary from a file in which there is one word per line. 
  public static Dict fromWordFile (String filename) {
    Dict d = new Dict();
    d.insertLines(filename);
    return d;
  }
 
  // Return a dictionary from a file in which there is one word per line. 
  public void insertLines (String filename) {
    System.out.println("Creating dictionary from file " + filename);
    int n = 1;
    LineEnumeration le = new LineEnumeration(filename);
    while (le.hasMoreElements()) {
      if ((n % 1000) == 0) {
        System.out.println(n + " words processed.");
      }
      insert((String) (le.nextElement()));
      n++;
    }
    System.out.println("Done creating dictionary from file " + filename);
  }
 
  // Return a dictionary from a file in "tree format". 
  // This class does not write such files, but can read files
  // written by the Scheme version of this program
  public static Dict fromFile (String filename) {
    try{
 
         /*
          * Returns a String representing the path
          * to the location of the source/class files. 
          * Returns the empty String if its the current working directory.
          *
          * Why is this here?  DrJava sets the current directory to be the 
          * the location of the DrJava application by default.  On public
          * machines, you can't change this (it will be undone when the
          * machines are reset).  So we include this method to find out
          * where this .class file was loaded from.
          *
          * Problem:  getResource() returns a URL representation of the
          * path.  This means that spaces and other characters will be
          * turned into their URL standard versions (eg, %20 for space).
          * When interpreted as a path name, this will fail.
          */
         File temp = new File("Dict.class");
         String path = "";
         if (!temp.exists()) {  // Current path does NOT get to source/class files
              path = new File(Dict.class.getResource("Dict.class").getFile()).getParent() + File.pathSeparator;
              temp = new File(path + "Dict.class");
              if (!temp.exists()) {      // Machinations did not work. Try again.
                   path = Dict.class.getResource("Dict.class").toString();
                   int firstIndex = path.indexOf(":");  /* end of "file:" */
                   path = path.substring(firstIndex + 1);
                        
                   // For Macs, path (and Dict.class) should be accurate here
                   // For PCs, path (and Dict.class) begins with '/C:' and
                   // we want to remove leading slash and change all forward
                   // slashes to backward slashes (i.e., File.separator)
                   if (path.indexOf(":") != -1) {  
                        path = path.substring(1);
                   }
                   // Replace URL space notation with " "
                   path = path.replaceAll("%20", " "); 
              
                   path = path.replace('/', File.separatorChar);  // Does nothing on Macs
                   int lastIndex = path.lastIndexOf(File.separatorChar);
                   path = path.substring(0, lastIndex + 1);

                   temp = new File(path + "Dict.class");
                   if (!temp.exists()) {      // Machinations did not work. Give up.
                        // Ideally, should allow user to choose file
                        String dir1 = new File(".").getAbsolutePath();
                        String dir2 = path;
                        System.err.println("Error: unable to locate ");
                        System.err.println("file in:\t\t" + dir1);
                        System.err.println("\t\tor\t\t" + dir2);
                        throw new RuntimeException();
                   }
              }
         }
         filename = path + filename;
         
      // The following 5 lines were added to determine the "path" to the Dict.class
      // which should be the "prefix-path" to the "path" for "filename".
      // This is necessary with Dr. Java because the base path is determined as the
      // path to the Dr. Java application and NOT to the .class files being executed
      //String path = Dict.class.getClassLoader().getResource("Dict.class").toString();
      //int firstIndex = path.indexOf("/");
      //int lastIndex = path.lastIndexOf("/");
      //path = path.substring(firstIndex,lastIndex+1);
      //filename = path + filename;
   
      // InputStreamReader r = new InputStreamReader(new FileInputStream(filename),"US-ASCII");
      FileInputStream fis = new FileInputStream(filename);
      System.out.println("Constructing dictionary from file " + filename + ".");
      System.out.println("This may take a little while...");
      // System.out.println("New stack.");
      Vector stack = new Vector(); 
      Dict leaf = new Dict (true, 1, null);
      int c;
      while ((c = fis.read()) != -1) {
        // System.out.println("Read char " + (char)(c) + "(" + c + ")");
        if (c < 128) { // It's a character
          // System.out.println("Push char " + (char)(c));
          stack.addElement(new Character((char) c));
        } else if (c == 128) { // It's a leaf marker
          // System.out.println("Push leaf");
          stack.addElement(leaf);
        } else {
          int numEdges = c % 64;
          boolean isFinal = (c >= 192);
          int numWords = (isFinal) ? 1 : 0;
          Vector v = new Vector();
          for (int i = numEdges; i > 0; i--) {
            char ch = ((Character) (stack.lastElement())).charValue();
            // System.out.println("Popping char " + ch);
            stack.removeElementAt(stack.size()-1);
            Dict d = (Dict) (stack.lastElement());
            // System.out.println("Popping dict" + d);
            stack.removeElementAt(stack.size()-1);
            v.insertElementAt(new DictEdge(ch,d), 0);
            numWords = numWords + d.numWords;
          }
          Dict dict = new Dict(isFinal, numWords, v);
          // System.out.println("Pushing dict" + dict);
          stack.addElement(dict);
        }
      }
      if (stack.size() == 1) {
        Dict ans = (Dict) (stack.firstElement());
        System.out.println("Done! Dictionary constructed with " + ans.numWords + " words.");
        return ans;
      } else {
        throw new RuntimeException("Dict.fromFile -- unexpected stack configuration.");
      }
    } catch (FileNotFoundException e) {
      System.out.println("*** Dict.fromFile: File Not Found "
                           + filename
                           + " ***");
      throw new RuntimeException("Dict.fromFile: File Not Found: " +  filename);
    } catch (IOException e) {
      System.out.println("*** Dict.fromFile: IO Exception in file "
                           + filename
                           + "\n"
                           + e.getMessage()
                           + " ***");
      throw new RuntimeException("Dict.fromFile: IO Exception: " +  e.getMessage());
    }
  }
 
  public  StringList allWords () {
    if ((edges == null) || (edges.size() == 0)) {
      if (isFinal) {
        return StringListOps.prepend("", StringList.empty());
      } else {
        return StringList.empty();
      }
    } else {
      StringList L = StringList.empty();
      for (int i = edges.size() - 1; i>=0; i--) {
        DictEdge e = (DictEdge) (edges.elementAt(i));
        L = StringListOps.append(UnjumblerAnswers.mapConcat((new Character(e.letter)).toString(), 
                                                            e.dict.allWords()),
                                 L);
      }
      if (isFinal) {
        return StringListOps.prepend("", L);
      } else {
        return L;
      }
    }
  }
    
  public String toString () {
    return "<Dict with " + size() + " words: " + allWords() + ">";
  }
  
  public static void main (String [] args) {
    Dict d1 = new Dict();
    d1.insert("foo");
    d1.insert("bar");
    d1.insert("baz");
    System.out.println(d1);
    Dict d2 = fromFile("../m7.txt");
    System.out.println(d2.size());
    /*
            System.out.println("f? = " + d.isWord("f"));
            System.out.println("fo? = " + d.isWord("fo"));
            System.out.println("foo? = " + d.isWord("foo"));
            System.out.println("fool? = " + d.isWord("fool"));
            System.out.println("b? = " + d.isWord("b"));
            System.out.println("ba? = " + d.isWord("ba"));
            System.out.println("bar? = " + d.isWord("bar")); 
            System.out.println("bart? = " + d.isWord("bart"));
            System.out.println("baz? = " + d.isWord("baz")); 
          */
  }
 
  // Given a string s, returns the substring of s that contains
  // all characters except the first. 
  public static String butFirst (String s) {
    return s.substring(1,s.length());
  }
}

class DictEdge {
  
  public char letter;
  public Dict dict; 

  public DictEdge(char c, Dict d) {
    this.letter = c;
    this.dict = d;
  }
}
