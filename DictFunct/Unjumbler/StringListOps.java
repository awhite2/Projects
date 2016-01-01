/* 
 * Operations built on top of the StringList class
 */

// [lyn, 03/13/11] Modified to contain suffixes, prefixes, toString

public class StringListOps {
  
  public static void main (String[] args) {
    System.out.println("first(\"computer\") = " + first("computer"));
    System.out.println("last(\"computer\") = " + last("computer"));
    System.out.println("butFirst(\"computer\") = " + butFirst("computer"));
    System.out.println("butLast(\"computer\") = " + butLast("computer"));
    System.out.println("suffixes(\"computer\") = " + suffixes("computer"));
    System.out.println("prefixes(\"computer\") = " + prefixes("computer"));
    System.out.println("prefixes2(\"computer\") = " + prefixes2("computer"));
  }
  
  // Operations built on top of the StringList class    
  public static int length (StringList L) {
    // Returns the number of elements in list L.
    if (isEmpty(L)) {
      return 0;
    } else {
      return 1 + length(tail(L));
    }
  }
  
  public static String min (String s1, String s2) {
    if (s1.compareTo(s2) < 0) {
      return s1;
    } else {
      return s2;
    }
  }
  
  public static String max (String s1, String s2) {
    if (s1.compareTo(s2) > 0) {
      return s1;
    } else {
      return s2;
    }
  }
  
  public static String least (StringList L) {
    // Returns the least string (by alphabetic ordering) number in L. 
    // (signals an exception if L is empty)
    if (isEmpty(L)) {
      throw new RuntimeException("StringList.min: emptyList");
    } else if (isEmpty(tail(L))) {
      return head(L);
    } else {
      return min(head(L), least(tail(L)));
    }
  }
  
  public static String greatest (StringList L) {
    // Returns the greatest string (by alphabetic ordering) in L,
    // or the empty string if L is empty. 
    if (isEmpty(L)) {
      return "";
    } else {
      return max(head(L), greatest(tail(L)));
    }
  }

  /************************************************************/
  /*              List combination operations                 */
  /************************************************************/

  // Returns a list whose elements are those of L1 followed by those of L2.
  public static StringList append(StringList L1, StringList L2) {
    // Returns a list whose elements are those of L1 followed by those of L2.
    if (isEmpty(L1)) {
      return L2;
    } else {
      return prepend (head(L1), append(tail(L1), L2));
    }
  }

  // Returns a list whose elements are those of L followed by s.
  public static StringList postpend(StringList L, String s) {
    // Returns a list whose elements are those of L followed by s.
    return append(L, prepend(s, empty()));
  }
  
  // Returns a list whose elements are the reverse of those in L. 
  public static StringList reverse(StringList L) {
    if (isEmpty(L)) {
      return L;
    } else {
      return postpend(reverse(tail(L)), head(L));
    }
  }
  
  // String ops
  // Assume string nonempty
  public static String first (String s) {
    return s.substring(0,1);
  }
  
  public static String last (String s) {
    return s.substring(s.length()-1,s.length());
  }
  
  public static String butFirst (String s) {
    return s.substring(1, s.length());
  }
  
  public static String butLast (String s) {
    return s.substring(0, s.length()-1);
  }
  
  public static StringList suffixes (String s) {
    if (s.equals("")) {
      return (prepend("", empty()));
    } else {
      return prepend(s, suffixes(butFirst(s))); 
    }
  }
  
  public static StringList prefixes (String s) {
    if (s.equals("")) {
      return (prepend("", empty()));
    } else {
      return prepend(s, prefixes(butLast(s))); 
    }
  }
  
  
  // Aleranative solution to prefixes that only uses butFirst
  public static StringList prefixes2 (String s) {
    if (s.equals("")) {
      return (prepend("", empty()));
    } else {
      return postpend(mapConcat(first(s), prefixes2(butFirst(s))),
                      "");
    }
  }
  
  // Don't show this in class because it's required on PS7
  public static StringList mapConcat (String s, StringList strs) {
    if (isEmpty(strs)) {
      return empty();
    } else {
      return prepend(s + head(strs), mapConcat(s, tail(strs)));
    }
  }
  
  // ----------------------------------------------------------
  // Local abbreviations
  
  public static StringList empty() {
    return StringList.empty();
  }
  
  public static boolean isEmpty(StringList L) {
    return StringList.isEmpty(L);
  }
  
  public static StringList prepend(String n, StringList L) {
    return StringList.prepend(n, L);
  }
  
  public static String head(StringList L) {
    return StringList.head(L);
  }
  
  public static StringList tail(StringList L) {
    return StringList.tail(L);
  }
  
  public static StringList fromString (String s) {
    return StringList.fromString(s);
  }
  
  public static String toString (StringList L) {
    return StringList.toString(L);
  }

  public static boolean equals (StringList L1, StringList L2) {
    return StringList.equals(L1, L2);
  }
    
}

