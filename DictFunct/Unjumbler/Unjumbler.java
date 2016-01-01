/*Abra White
 * problem set 7
 * cs 111
 * Oct 29, 2012
 */

public class Unjumbler extends LabOps {

  public static void main (String [] args) {
    
    //method 1
    System.out.println(remove("voldemort", fromString("[harry,voldemort,ginny,ron,dumbledore,voldemort]")));
    //method 2
    System.out.println(removeDuplicates(fromString("[one,ring,to,rule,them,all,one,ring,to,find,them,one,ring,to,bring,them,all,and,in,the,darkness,bind,them]")));
    //method 3
    System.out.println(mapConcat("time", fromString("[ and relative dimension in space,lord,y wimey stuff]")));
    //method 4
    System.out.println(insertions(":", ")"));
    //method 5
    System.out.println(insertionsList("*", fromString("[expecto,patronum]")));
    //method 6
    System.out.println(permutations("bcd"));
    //method 7
    System.out.println(filterWords(fromString("[yes,no,ki,asdf,why]")));
    //method 8
    System.out.println(unjumble("argle"));
  }
 
  /************************************************************
   Returns a new list in which all occurrences of s in L have
   been removed. The other strings in the list should have the
   same relative order in the resulting list as in the given list.
   ***********************************************************/
  public static StringList remove (String s, StringList L) {
    //stop at end of list 
    if (isEmpty(L)) {
      return L;
    } 
    //if the head is "s" remove it and continue to the rest of the list 
    else if (head(L).equals(s)) {
      return (remove(s, tail(L)));
    } 
    //if not, keep the head and continue on
    else {
      return prepend(head(L), remove(s, tail(L)));
    }  
  }
  
  /***********************************************************  
   Returns a list containing each string in L exactly once. 
   The order of the elements in the returned list should be the
   relative order of the *first* occurrence of each element in L.
   **********************************************************/
  public static StringList removeDuplicates (StringList L) {
    
    //Method 2 is prewritten
    return UnjumblerAnswers.removeDuplicates(L);

  }

  /***********************************************************  
   Given a list L with n strings, returns a new list with n
   strings in which the ith string of the resulting list is
   the result of concatenating s to the ith element of L.
   **********************************************************/
  public static StringList mapConcat (String s, StringList L) {
    //if list is empty
    if(isEmpty(L)){
      return L;
    }
    //adds s to the beginning of each string in the string list
    else{
      return prepend(s + head(L), mapConcat(s, tail(L)));}
    
  }
  
  /***********************************************************  
   Returns a list of all strings in L that are English
   words. The resulting strings should be in the same relative
   order as in L.
  ***********************************************************/
  public static StringList filterWords (StringList L)
  {
     if (isEmpty(L)) {
      return L;
    } else if (isWord(head(L))) {
      //if it is a word leave in the list and move on
      return prepend(head(L), filterWords(tail(L)));
    } else {
      //if not a word remove and move on
      return filterWords(tail(L));
    }
  }
 
  
  /***********************************************************  
   Given two strings s1 and s2, where s2 has n characters,
   returns a list of n + 1 strings that result from inserting
   s1 at all possible positions within s2, from left to right.
   ***********************************************************/
  public static StringList insertions (String s1, String s2) {
    
    //insertions is written for us
    return UnjumblerAnswers.insertions(s1,s2);
    
  }
  
  /***********************************************************  
   Returns a list that contains all the strings that result
   from inserting s at all possible positions in all the
   strings of L.
   ***********************************************************/
  public static StringList insertionsList (String s, StringList L) {
    if(isEmpty(L)){
      return L;
    }else{
      //run insertion through the head and recurse through the rest of the list
      return append(insertions(s, head(L)), insertionsList(s, tail(L)));}
    
  }
  
  /***********************************************************  
   Returns a list of all permutations of the string s. 
   A permutation of a string s is any string that is formed by
   reordering the letters in the string s (without duplicating
   or deleting any letters). For a string with n distinct
   characters, there are exactly n! (i.e., "n factorial")
   permutations. If some characters in s are repeated, there
   are still n! permutations, but the permutations contain
   duplicates. The elements in the list returned by
   permutations may be in any order.
   ***********************************************************/
  public static StringList permutations (String s)
  {
    
    if(s.equals("")){
      return prepend(s, empty());
  }else{
    //takes the first character and inserts it through the permutations of the other chracters
    //insert first + (permutations of the others)
    return insertionsList(first(s), permutations(butFirst(s)));
  }
  }
  
  /***********************************************************  
   Returns a list of all the permutations of s that are
   English words (as determined by the default
   dictionary). The order of elements in the resulting list
   does not matter, but each word in the resulting list should
   be listed only once.
   ***********************************************************/
  public static StringList unjumble (String s)
  {
    if(s.equals("")){
      return empty();
    }else{
   //create list
      StringList list = permutations(s);
   //use only words
      StringList filteredList = filterWords(list);
   //take out doubles
      StringList noDoubles = removeDuplicates(filteredList);
   //return final list
      return noDoubles;}}
  
  // ------------------------------------------------------------
  // DICTIONARIES
  
  // You are provided with a method
  //
  //    private static boolean isWord (String s);
  //
  // that determines whether the string s is an English word. 
  // You do not need to understand any of the details how this is
  // done, except to know that it is performed by testing if s
  // appears in a certain word list file.  So the test is only as
  // good as the word list file it uses. 
  
  // The name of the file in which the dictionary resides is a
  // class variable.  By default, it is "dicts/dict8.bin", but you
  // can change it to be one of the other choices below.  All of
  // the following dictionaries are derived from  the freely
  // available Linux word list. Files with more words take longer
  // to load. Note that the Linux word list is missing some English
  // words. 
  
  private static String dir = "dicts" + java.io.File.separatorChar;  // directory
  // private static String dictFile = "dict-small.bin";  // "foo", "bar", "baz" 
  // private static String dictFile = "dict5.bin"; // Words up to 5 letters (5525 words)
  // private static String dictFile = "dict6.bin"; // Words up to 6 letters (10488 words)
  // private static String dictFile = "dict7.bin"; // Words up to 7 letters (16618 words)
  private static String dictFile = "dict8.bin"; // Words up to 8 letters (22641 words)
  // private static String dictFile = "dict.bin"; // Whole linux word list (45425 words)
  
  // For efficiency's sake, the dictionary itself is stored in a
  // class variable.  This variable initially contains no
  // dictionary.  It is intialized the first time that isWord() is
  // called. 
  private static Dict dict = null;
  
  // You should not need to add any other class variables!  The
  // ones above suffice.   
  private static boolean isWord (String s) {
    if (dict == null) {         // If no dictionary yet
      dict = Dict.fromFile(dir + dictFile);
    }
    return dict.isWord(s);
  }
}
