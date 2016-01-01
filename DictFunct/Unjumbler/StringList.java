// Immutable linked lists of strings

// [lyn, 03/13/11]
// * Can't understand why constructors were public, so made them private. 
// * Incorporate toString from PowerSet problem that shows empty string
//   with pair of double quotes (else can't "see' it). 
// * Incorporate fromString from PowerSet problem that allows reading 
//   any string delimited by double quotes. 

// [lyn, 10/26/07] Made a few modifications:
// * Made constructor methods public to match change agreed to by Brian and me. 
// * Replaced ListException by RuntimeException
// * Removed silly empty instance variable, instead representing empty list with null tail. 
// * Define a distinguished static IntList object that is the empty list. 


public class StringList {
  
  // Instance variables
  
  private String head;
  private StringList tail;
  
  // Have a distinguished empty list node. 
  private static StringList theEmptyList = new StringList();
  
  // Constructor method:
  
  private StringList () {
  }
  
  private StringList (String head, StringList tail) {
    this.head = head;
    this.tail = tail;
  }
  
  // Instance methods: 
  
  private boolean isEmpty() {
    return this == theEmptyList; 
  }
  
  private StringList prepend(String s) {
    return new StringList (s, this);
  }
  
  private String head () {
    if (isEmpty()) {
      throw new RuntimeException("Attempt to get the head of an empty String list");
    } else {
      return head;
    }
  }
  
  private StringList tail() {
    if (isEmpty()) {
      throw new RuntimeException("Attempt to get the tail of an empty String list");
    } else {
      return tail;
    }
  }
  
  public String toString () {
    if (isEmpty()) {
      return "[]";
    } else {
      StringBuffer sb = new StringBuffer();
      sb.append("[");
      sb.append(toStringException(head));
      StringList toDo = tail;
      while (! toDo.isEmpty()) {
        sb.append(",");
        sb.append(toStringException(toDo.head));
        toDo = toDo.tail;
      }
      sb.append("]");
      return sb.toString();
    }
  }
  
  // Handle specially the empty string (else cannot "see" it)
  // and strings beginning/ending with whitespace.
  public static String toStringException(String s) {
    if (s.equals(""))
      return ("\"\"");
    else if (isWhitespace(s.charAt(0)) || isWhitespace(s.charAt(s.length()-1)))
      return "\"" + s + "\"";
    else 
      return s;
  }
  
  // Handle specially strings delimited by double quotes. 
  public static String fromStringException(String s) {
    if ((s.length() >= 2) 
          && (s.charAt(0) == '\"') 
          && (s.charAt(s.length()-1) == '\"') )
      return s.substring(1,s.length()-1);
    else 
      return s; 
  }
  
  // Class Methods: 
  
  public static StringList empty() {
    return theEmptyList; // return unique empty list 
  }
  
  public static boolean isEmpty(StringList L) {
    return L.isEmpty();
  }
  
  public static StringList prepend(String n, StringList L) {
    return new StringList(n, L);
  }
  
  public static String head(StringList L) {
    return L.head();
  }
  
  public static StringList tail(StringList L) {
    return L.tail();
  }
  
  public static StringList arrayToStringList(String [ ] a) {
    StringList result = empty();
    for (int i = a.length - 1; i >=0; i--) {
      result = prepend(a[i], result);
    }
    return result;
  }
  
  public static String toString (StringList L) {
    return L.toString();
  }
  
  public static boolean equals (StringList L1, StringList L2) {
    if (isEmpty(L1) && isEmpty(L2)) {
      return true;
    } else if (isEmpty(L1) || isEmpty(L2)) {
      return false;
    } else {
      return ((head(L1).equals(head(L2))) && (equals(tail(L1),tail(L2))));
    }
  }
  
  public static StringList fromString (String s) {
    if (s.charAt(0) != '[') {
      throw new RuntimeException("StringList.fromString: string does not begin with '[': "
                                   + "\"" + s + "\"");
    } else if ((s.charAt(s.length() - 1)) != ']') {
      throw new RuntimeException("StringList.fromString: string does not end with ']': "
                                   + "\"" + s + "\"");
    } else {
      return fromStringHelp (s, 1);
    }
  }
  
  // Warning: this does not handle quoted commas appropriately!
  private static StringList fromStringHelp (String s, int lo) {
    int commaIndex = s.indexOf(',', lo);
    if (commaIndex == -1) { // last element or empty list
      int hi = s.length()-1; // index of ']';
      if (lo >= hi) {
        return empty();
      } else {
        return prepend(s.substring(lo,hi), empty());
      }
    } else {
      return prepend(fromStringException(s.substring(lo,commaIndex)), fromStringHelp(s, commaIndex+1));
    }
  }
  
  public static boolean isWhitespace (char c) {
    return " \n\t\r".indexOf(c) != -1; 
  }
  
  private static void testFromString (String s) {
    System.out.println("fromString(\"" + s + "\") = " + fromString(s)); 
  }
  
  public static StringList SL;
  
  public static void main (String [] args) {
    System.out.println(SL.prepend("u", SL.prepend("vw", SL.prepend("xyz", SL.empty()))));
    testFromString("[a,b,c]");
    testFromString("[a,bc,def,ghij,klmno]");
    testFromString("[ a ,  bc  ,  def  ,    ghij    ,     klmno     ]");
    testFromString("[regular,,leading space,trailing space , leading and trailing ]");
    testFromString("[]");
    testFromString("[ ]");
    testFromString("[  ]");
    testFromString("[a string with spaces,another one]"); 
    testFromString("[\"yet another string with spaces\",\"\",foo]"); 
  }
    
}



