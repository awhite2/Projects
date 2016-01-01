//********************************************************************  
// DuplicateIDException.java  
//  
// Represents an exceptional condition in which an object in a collection
// has the same id as another object
//********************************************************************  
public class DuplicateIDException extends Exception  
{  
 //-----------------------------------------------------------------  
 // Sets up the exception object with a particular message.  
 //-----------------------------------------------------------------  
 DuplicateIDException (String message)  
 {  
 super (message);  
 }
}