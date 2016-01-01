//********************************************************************  
// OutstandingRequirements.java  
//  
// Represents an exceptional condition in which an object in a collection
// has an outstanding requirement that will not let it be deleted.
//********************************************************************  
public class OutstandingRequirements extends Exception  
{  
 //-----------------------------------------------------------------  
 // Sets up the exception object with a particular message.  
 //-----------------------------------------------------------------  
 OutstandingRequirements (String message)  
 {  
 super (message);  
 }
}