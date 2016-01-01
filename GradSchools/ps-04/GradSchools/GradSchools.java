/** Defines a class for maintaining an array of School objects
  * @author Takis Metaxas, based on previous solutions
  * KNOWN BUGS: 
  * 1. There is no limiting the weights in the [1..5] range. 
  * 2. It does not check if a School already exists in the collection
  * 3. No other bug. Likely I did not test hard enough.
  * FEATURE:-) It uses its own selection sorting method, and this can be slow 
  * for large collections of Schools. Better to have flexibility.
  */

public class GradSchools {
  
  // instance variables
  final private int SIZE = 1;
  private School[] schools;  // array of School objects
  private int numSchools;  // number of School objects stored in array
  
  /** constructors, one with SIZE number of Schools, the other with given number
    */ 
  public GradSchools () {
    schools = new School[SIZE];
    numSchools = 0;
  }
  
  public GradSchools (int size) {
    schools = new School[size];
    numSchools = 0;
  }
  
  /** instance method to add a new School object to the schools array
    * It does not check if School exists
    */
  public void addSchool (String name, int Academics, int Research, int pubs) {
    if (numSchools >= schools.length)
      doubleSize();
    
    schools[numSchools] = new School(name, Academics, Research, pubs);
    numSchools++;
    
  }
  
  /**  Increases the capacity of the school array by creating a
    *  larger array and copying the existing collection into it.
    --------------------------------------------------------------
    */
  private void doubleSize ()
  {
    
    School[] temp = new School[schools.length * 2];
    
    for (int s = 0; s < schools.length; s++)
      temp[s] = schools[s];
    
    schools = temp;
  }
  
  /** instance method that prints information about all of the School objects
    * in the schools array
    --------------------------------------------------------------
    */
  public String toString () {
    String s = "There are " + numSchools + " schools in the database:\n";
    for (int i = 0; i < numSchools; i++)
      s = s + schools[i];
    s  = s + "\n";
    return s;
  }
  
  
  
  /** instance method that computes overallRating for each School object
    --------------------------------------------------------------
    */ 
  public void computeRatings (int weightAcademics, int weightResearch, int weightPubs) {
    for (int i = 0; i < numSchools; i++) 
      schools[i].computeRating(weightAcademics, weightResearch, weightPubs);
  }
  
  
  /** instance method that rank orders the School objects in the schools
    * array, either by a single factor or the overallRating as specified
    * by an input String, and prints the names of the schools in order
    * from highest to lowest rank
    */
  public void rankSchools (String factor) {
    // The following loop stores the rating values for the desired factor
    // into the rankValue instance variable, and the sorting process then 
    // uses rankValue to sort the School objects in the schools array
    int i;
    for (i = 0; i < numSchools; i++) {
      if (factor.equals("Academics"))
        schools[i].setRankValue(schools[i].getRateAcademics());  
      else if (factor.equals("Research"))
        schools[i].setRankValue(schools[i].getRateResearch());  
      else if (factor.equals("Publications"))
        schools[i].setRankValue(schools[i].getRatePubs());  
      else if (factor.equals("Overall"))
        schools[i].setRankValue(schools[i].getOverallRating());
    }  
    sortSchools();     // You could also have used an external Sort program.
    // print resulting ranking of schools 
    displayRankResults(factor);
  }
  
  /* to display the rank results. Better have it separately than the rankSchools 
   so that rankSchools can be used independently.
   --------------------------------------------------------------
   */
  public void displayRankResults(String factor){
    //System.out.print("Ranking of schools from highest to lowest using ");
    System.out.println(factor);
    for (int i = numSchools-1; i >= 0; i--)
      System.out.println(schools[i].getName());
    System.out.println();
  }
  
  
  /** instance method that sorts the School objects in the schools array in 
    * order of increasing rankValue
    * Sorting strategy for original sortArray() method:
    * The sorting strategy used here is called "selection sort". Suppose 
    * arrayA contains n numbers to be sorted, in indices from 0 to n-1. 
    * First, the algorithm finds the largest number in the array and 
    * places it at index n-1. Then it locates the second largest number, 
    * in indices 0 to n-2, and places this number at index n-2. Then the 
    * third largest number is found in indices 0 to n-3, and placed at 
    * index n-3, and so on, until all n numbers are sorted. 
    --------------------------------------------------------------
    */
  private void sortSchools () {    
    int maxRating;     // maximum rating
    int maxIndex;      // index of School with maximum rating
    int i, j;
    for (j = numSchools - 1; j > 0; j--) {
      maxIndex = 0;
      maxRating = schools[0].getRankValue();
      for (i = 1; i <= j; i++) {
        if (schools[i].getRankValue() > maxRating) {
          maxRating = schools[i].getRankValue();
          maxIndex = i;
        } // end of if
      } // end of for
      swap(maxIndex, j);
    } // end of for
  }
  
  /** Helper method for sortSchools(); swaps the contents of schools[i] and schools[j]
    */
  private void swap (int i, int j) { 
    School temp = schools[i];
    schools[i] = schools[j];
    schools[j] = temp;
  }
  
  /** instance method to return the last School in the collection. When sorted, 
    * this should be the one with the maximum rank (the "top" school) in this category
    */
  public School getTop () {
    if (numSchools > 0) return schools[numSchools-1];
    else return new School("ERROR", 0, 0, 0);
  }
  
  
  /** Driver code for testing the methods defined in the
    * GradSchools class for maintaining an array of School objects
    --------------------------------------------------------------
    */
  public static void main (String[] args) {
    GradSchools myGradSchools = new GradSchools(1); // to test doubleSize()
    
    int weightAcademics = 0;
    int weightResearch = 0;
    int weightPubs = 0;
    
    if (args.length != 3) 
      if (args.length != 3) 
    {
      //System.out.println("Please provide 3 weights [1..5] for Academics, Research and Publications\n");
      //System.exit(0);
      // Alternatively, we could have gotten some default values
      weightAcademics = 1;
      weightResearch = 3;
      weightPubs = 5;
      System.out.println("Acad. "+weightAcademics+"\t Res. "+weightResearch+"\t Pubs. "+weightPubs);
    } else {
      weightAcademics = Integer.parseInt(args[0]);
      weightResearch = Integer.parseInt(args[1]);
      weightPubs = Integer.parseInt(args[2]);
    }
    
    // Disclaimer: Of course, the ratings here are arbitrary
    myGradSchools.addSchool("AcademicSch", 10, 5, 3);
    myGradSchools.addSchool("ResearchSch", 3, 10, 5);
    myGradSchools.addSchool("PubsFactory", 5, 3, 10);
    myGradSchools.addSchool("BalancedSch", 7, 7, 7);
    
    myGradSchools.computeRatings(weightAcademics, weightResearch, weightPubs);
    System.out.println(myGradSchools);
    
    myGradSchools.rankSchools("Academics");
    myGradSchools.rankSchools("Research");
    myGradSchools.rankSchools("Publications");
    myGradSchools.rankSchools("Overall");
  }
  
  
}