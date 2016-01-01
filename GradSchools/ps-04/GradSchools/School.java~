/** Defines a class of School objects that store information about individual grad schools
  * @author Takis Metaxas
  * KNOWN BUGS: 
  * 1. Enforces ratings in the range [1..10] by limiting larger/smaller values
  * but only for academics, research, pubs. 
  * 2. Having the overallRating and rankValue included in this class is not the best approach,
  * because it reveals knowledge on how Schools will be used in a particular application.
  * Better create class RankedSchool extending School, and have them in there.
  * 3. Does not check whether the weights given are in the range [1..5]. That should also
  * be done in the RankedSchool class.
  */
public class School {  
  
  // instance variables 
  
  // ratings are assumed to be an integer from 1 to 10
  final int MIN = 1;
  final int MAX = 10;
  
  private String name;         // name of school
  private int rateAcademics;   // rating of Academics  
  private int rateResearch;    // rating in educating research scholars 
  private int ratePubs;        // rating of impact of faculty publications
  private int overallRating;   // overall rating that uses all factors
  private int rankValue;       // value used to rank schools, based on one
  // factor or all factors combined
  
  /** constructor forces values within MIN and MAX
    */
  public School (String name, int academics, int research, int pubs) {
    this.name = name; 
    // ratings are assumed to be an integer from MIN to MAX
    rateAcademics = (academics > MAX)? MAX : academics; 
    rateAcademics = (academics < MIN)? MIN : rateAcademics; // do you see why?
    rateResearch = (research > MAX)? MAX : research; 
    rateResearch = (research < MIN)? MIN : rateResearch; 
    ratePubs = (pubs > MAX)? MAX : pubs;
    ratePubs = (pubs < MIN)? MIN : ratePubs;
   
    
  }
  
  // Getters and setters for each instance variable (when appropriate)
  // All trivially defined except setOverallRanking()
  
  public String getName () {
    return name;
  }
  
  public void setName (String newName) {
    name = newName;
  }
  
  public int getRateAcademics () {
    return rateAcademics;
  }
  
  public void setRateAcademics (int newRate) {
    rateAcademics = newRate;
  }
  
  public int getRateResearch () {
    return rateResearch;
  }
  
  public void setRateResearch (int newRate) {
    rateResearch = newRate;
  }
  
  public int getRatePubs () {
    return ratePubs;
  }
  
  public void setRatePubs (int newRate) {
    ratePubs = newRate;
  }
  
  public int getRankValue () {
    return rankValue;
  }
  
  public void setRankValue (int newValue) {
    rankValue = newValue;
  }
  
  public int getOverallRating () {
    return overallRating;
  }
  
  /** setter method that computes overallRating for a School that considers 
    * all factors, given input weights for the individual factors
    */
  public void setOverallRating (int weightAcademics, int weightResearch, int weightPubs) {
    overallRating = (weightAcademics * rateAcademics) +  
      (weightResearch * rateResearch) + (weightPubs * ratePubs);
  }
  
  
  /** Since the assignment wants a synonym for the OverallRating setter, we just call it
    */
  public void computeRating (int weightAcademics, int weightResearch, int weightPubs) {
    setOverallRating ( weightAcademics,  weightResearch,  weightPubs);
  }
  
  
  /** instance method that returns a String containing the information
    * stored in a single School object. Used for printing.
    */
  public String toString () {
    String S = "SCHOOL: " + name;
    S = S + "\t Academics: " + rateAcademics;
    S = S + "\t Research: " + rateResearch;
    S = S + "\t Publications: " + ratePubs;
    S = S + "\n Overall: " + overallRating;
    S = S + "\t Current rank: " + rankValue;
    S = S + "\n";
    return S;
  }
  
  /** Driver method to test this class
    */
  public static void main (String[] args) {
    int weightAcademics = 0;
    int weightResearch = 0;
    int weightPubs = 0;
    
    if (args.length != 3) 
    {
      //System.out.println("Please provide 3 weights [1..5] for Academics, Research and Publications\n");
      //System.exit(0);
      // Alternatively, we could have gotten some default values
      weightAcademics = 3;
      weightResearch = 4;
      weightPubs = 5;
      
    } else {
      weightAcademics = Integer.parseInt(args[0]);
      weightResearch = Integer.parseInt(args[1]);
      weightPubs = Integer.parseInt(args[2]);
    }
    
    School wellesley = new School("Wellesley", 15, 8, -5);
    
    wellesley.computeRating(weightAcademics, weightResearch, weightPubs);
    System.out.println(wellesley);
    
    wellesley.setName("LTC-Wellesley!");
    wellesley.setRateResearch(10);
    wellesley.setOverallRating(weightAcademics, weightResearch, weightPubs);
    wellesley.setRankValue(1);
    System.out.println(wellesley);
  }
  
}

