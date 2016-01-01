import java.util.Enumeration;
import java.io.*;

public class LineEnumeration implements Enumeration 
{

    StreamTokenizer st;
    String buffer = null; // A one element buffer for storing most recent string
    boolean done = false; // Indicates whether we are done reading file

    public LineEnumeration (String filename)
    {
        try{
            st = new StreamTokenizer(new FileReader(filename));
            st.wordChars('\u0000', '\u00FF');
            st.whitespaceChars('\n', '\n'); // newline char; ((int) '\n') == 10 
            st.whitespaceChars('\r', '\r'); // carriage return char; ((int) '\r') == 13
        } catch (FileNotFoundException e) {
            System.out.println("*** LineEnumeration Error: File Not Found "
                               + filename
                               + " ***");
            throw new RuntimeException("File Not Found: " +  filename);
        } catch (IOException e) {
            System.out.println("*** LineEnumeration Error: IO Exception in file "
                               + filename
                               + "\n"
                               + e.getMessage()
                               + " ***");
            throw new RuntimeException("IO Exception: " +  e.getMessage());
        }
    }
        
    public boolean hasMoreElements ()
    {
        try {
            if (done) {
                return false;
            } else if (buffer != null) {
                return true;
            } else if (st.nextToken() == StreamTokenizer.TT_EOF) {
                done = true;
                return false;
            } else {
                buffer = st.sval;
                return true;
            }
        } catch (IOException e) {
            System.out.println("*** LineEnumeration Error: IO Exception "
                               + e.getMessage()
                               + " ***");
            throw new RuntimeException("IO Exception: " +  e.getMessage());
        }
    }
        
    public Object nextElement ()
    {
        try {
            if (buffer != null) {
                String s = buffer;
                buffer = null;
                return s;
            } else if (st.nextToken() != StreamTokenizer.TT_EOF) {
                return st.sval;
            } else {
                throw new RuntimeException ("LineEnumeration.nextElement called on empty enumeration");
            }
        } catch (IOException e) {
            System.out.println("*** LineEnumeration Error: IO Exception "
                               + e.getMessage()
                               + " ***");
            throw new RuntimeException("IO Exception: " +  e.getMessage());
        }
    }
}
