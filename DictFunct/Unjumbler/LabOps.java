/* FILE NAME: LabOps.java
 * AUTHOR: ???
 *
 * DATE: ???
 *
 * COMMENTS: Provides solutions to the lab excersises. (lab on StringList 's etc)
 * Notice that this class extends StringListOps, which extends StringList.
 * Therefore, all methods defined in these two classes are inherited here.
 * 
 * In particular:
 * The following methods are inherited from StringList:
 * public static StringList empty();
 * public static boolean isEmpty (StringList L);
 * public static StringList prepend (String s, StringList L);
 * public static String head (StringList L);
 * public static StringList tail (StringList L);
 * public static boolean equals (StringList L1, StringList L2);
 * public static String toString (StringList L);
 * public static String fromString (String s);
 * 
 * The following methods are inherited from StringList:
 * public static int length (StringList L);
 * public static StringList append (StringList L1, StringList L2);
 * public static StringList postpend (StringList L, String s);
 * public static StringList reverse (StringList L);
 * 
 * All the above methods can be used in this file without the explicit 
 * "StringList." or "StringListOps." prefixes.
 * For example, you can write "head(L)" rather than "StringList.head(L)",
 * and "length(L)" rather than "StringListOps.length(L)".
 * 
 * MODIFICATION HISTORY: stella edited on Oct 26 2007
*/   

public class LabOps extends StringListOps {
  
  public static StringList mapPluralize (StringList l) {
    if (isEmpty(l)) return empty();
    else {
      return prepend(head(l) + "s", mapPluralize(tail(l)));
    }
  } // mapPluralize()
  
  public static StringList mapUpperCase (StringList l) {
    if (isEmpty(l)) return empty();
    return prepend(head(l).toUpperCase(), mapUpperCase(tail(l)));
  } // mapUpperCase() 
  
  public static boolean isMember(String s, StringList l) {
    return !isEmpty(l) && (s.equals(head(l)) || isMember(s, tail(l)));
  } // isMember()
  
  public static StringList filterMatches (String s, StringList L) {
    if (isEmpty(L)) {
      return L;
    } else if (head(L).indexOf(s) != -1) {
      return prepend(head(L), filterMatches(s, tail(L)));
    } else {
      return filterMatches(s, tail(L));
    }
  } // filterMatches()
  
  public static StringList explode (String s) {
    if (s.equals("")) return empty();
    return prepend(first(s), explode(butFirst(s)));
  } // explode()
  
  public static String implode (StringList l) {
    if (isEmpty(l)) return "";
    return head(l)+implode(tail(l));
  } // implode() 
  
  // insert s into the correct position in an alphbetically sorted list
  public static StringList insert (String s, StringList L){
    if (isEmpty(L) || (s.compareTo(head(L)) <= 0)){
      return prepend(s,L);
    } else {
      return prepend(head(L), insert(s,tail(L)));
    }
  } // insert()
  
  public static StringList insertionSort (StringList L) {
    if (isEmpty(L)) {
      return L;
    } else {
      return insert(head(L), insertionSort(tail(L)));
    }
  } // insertionSort()
 
  public static void main (String [] args) {
    System.out.println("first(\"cs111\") => \"" + first("cs111") + "\"");
    System.out.println("butFirst(\"cs111\") => \"" + butFirst("cs111") + "\"");
    System.out.println("fromString(\"[I,do,not,like,green,eggs,and,ham]\") = "
                         + fromString("[I,do,not,like,green,eggs,and,ham]"));
    
    // Testing code here: 
    
    // Test mapPluralize()
    System.out.println("mapPluralize(fromString(\"[car,boat,apple,goose]\")) => " +
                       mapPluralize(fromString("[car,boat,apple,goose]")));
    System.out.println("mapPluralize(fromString(\"[dog,cat,mouse]\")) => "
                         + mapPluralize(fromString("[dog,cat,mouse]")));
    System.out.println("mapPluralize(fromString(\"[]\")) => "
                         + mapPluralize(fromString("[]")));
    
    // Test mapUpperCase()
    System.out.println("mapUpperCase(frfomString(\"[]\")) => " +
                       mapUpperCase(fromString("[]")));
    System.out.println("mapUpperCase(fromString(\"[I,do,not,like,green,eggs,and,ham]\")) => " +
                       mapUpperCase(fromString("[I,do,not,like,green,eggs,and,ham]")));
    
    // Test isMember()
    System.out.println("isMember(\"eggs\", empty()) => " + isMember("eggs", empty()));
    System.out.println("isMember(\"eggs\", fromString(\"[I,do,not,like,green,eggs,and,ham]\")) => " +
                       isMember("eggs", fromString("[I,do,not,like,green,eggs,and,ham]")));
    System.out.println("isMember(\"I\", fromString(\"[I,do,not,like,green,eggs,and,ham]\")) => " +
                       isMember("I", fromString("[I,do,not,like,green,eggs,and,ham]")));
    System.out.println("isMember(\"avocado\", fromString(\"[I,do,not,like,green,eggs,and,ham]\")) => " +
                       isMember("avocado", fromString("[I,do,not,like,green,eggs,and,ham]")));
    
    // Test filterMatches()
    System.out.println("filterMatches(\"com\", "
                         + "fromString(\"[computer,program,"
                         + "incomparable,intercom,Java]\")) = "
                         + filterMatches("com",
                                         fromString("[computer,program,"
                                                    +"incomparable,intercom,"
                                                    + "Java]")));
  
    // Test explode()
    System.out.println("explode(\"\") => " + explode(""));
    System.out.println("explode(\"CS111\") => " + explode("CS111"));
    
    // Test implode()      
    System.out.println("implode(empty()) => " + implode(empty()));
    System.out.println("implode(fromString(\"[I,do,not,like,green,eggs,and,ham]\")) => " +
                       implode(fromString("[I,do,not,like,green,eggs,and,ham]")));
    
    // strings that are equal by not ==
    System.out.println("implode(explode(\"a train\")).equals(\"a train\") => " +
                       implode(explode("a train")).equals("a train"));
    System.out.println("(implode(explode(\"a train\")) == \"a train\") => " +
                       (implode(explode("a train")) == "a train"));
       
    // Test insert()   
    System.out.println("insert(\"dog\", "
                         + "fromString(\"[ant,bat,cat,goat,lion]\"))) = "
                         + insert("dog",
                                  fromString("[ant,bat,cat,goat,lion]")));
    System.out.println("insert(\"aardvark\", "
                         + "fromString(\"[ant,bat,cat,goat,lion]\"))) = "
                         + insert("aardvark",
                                  fromString("[ant,bat,cat,goat,lion]")));
    System.out.println("insert(\"tiger\", "
                         + "fromString(\"[ant,bat,cat,goat,lion]\"))) = "
                         + insert("tiger",
                                  fromString("[ant,bat,cat,goat,lion]")));
    System.out.println("insert(\"cat\", "
                         + "fromString(\"[ant,bat,cat,goat,lion]\"))) = "
                         + insert("cat",
                                  fromString("[ant,bat,cat,goat,lion]")));
    
    // Test insertionSort()   
    System.out.println("insertionSort(fromString(\""
                         +  "[I,do,not,like,green,eggs,and,ham]"
                         + "\")) = "
                         + insertionSort(fromString("[I,do,not,like,green,eggs,and,ham]")));       
        
  } // main()
  
  //---------------------------------------------------------------
  // The following auxiliary methods are helpful for explode
  
  // Given a string s, returns a one-character string containing
  // the first character of s. 
  public static String first (String s) {
    return s.substring(0,1);
  }
  
  
  // Given a string s, returns the substring of s that contains
  // all characters except the first. 
  public static String butFirst (String s) {
    return s.substring(1,s.length());
  }
  
  
}

