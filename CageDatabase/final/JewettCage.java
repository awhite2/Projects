/*For Jewett Cage Software
 *CS230 Nina Broocks and Abra White
 *This class provides the Jewett Cage class which provides the main functionality for the software and combines the methods
 * from the other classes.
 * 
 * Uses hashtables to store equipment and people objects
 * 
 * Equipment is found by id number only because all ids are assumed to be on the equipment. All people should know their phone
 * number and thus ID.
 * 
 * @author Abra White
 */

import java.util.*;
import javafoundations.ArrayIterator;
import java.text.*;

public class JewettCage{
  //instance variables
  private Hashtable<String, Equipment> equipmentCollection;
  private Hashtable<Integer, People> peopleCollection;
  
  
  //constructor
  public JewettCage(){
    equipmentCollection = new Hashtable<String, Equipment>(400, (float)0.75);
    peopleCollection = new Hashtable<Integer, People>(400, (float)0.75);
  }
  
  //methods
  /* Adds an equipment object to the equipmentCollection
   * Uses the setID method to create the id
   * @param String dept, String t, double fine -- same as the equipment object
   * @author Abra White
   */
  public void newEquipment(String dept, String t, double fine){
    Equipment equip = new Equipment(dept, t, fine);
    String id = getEquipID(equip);
    equip.setID(id);
    equipmentCollection.put(equip.getID(), equip);
  }
  
  /* Generates and ID for an equipment based on the number of the same dept and type as it
   * @param Equipment e
   * @author Abra White
   */
  public String getEquipID(Equipment e){
    //department first letter
    String theID = String.valueOf(e.getDepartment().charAt(0));
    
    //first letter of each type word
    String s = e.getType();
    String [] types = s.split(" ");
    for(int i=0; i<types.length; i++){
      //System.out.println(types[i]);
      String a = String.valueOf(types[i].charAt(0));
      theID += a;
    }
    
    //gets the number of the same type and adds one
    Set keys = equipmentCollection.keySet();
    Iterator it = keys.iterator();
    int count = 0;
    while(it.hasNext()){
      String next = (String)it.next();
      //System.out.println(next);
      if(next.matches(theID+"\\d*")){
        count++;
      }
    }
    count += 1;
    theID = theID+count;
    return theID;
  }
  
  /* Sets the personID, sets id variable using setID and getPersonID
   * @param People p
   * @author Abra White
   */
  public void setPersonID(People p){
    p.setID(getPersonID(p));
  }
  
  /* gets an id number based on the last 4 digits of the phone number
   * @param People p
   * @returns id
   * @author Abra White
   */
  public int getPersonID(People p){
    int length = p.getPhone().length();
    int id =  Integer.parseInt(p.getPhone().substring(length-4, length));
    return id;
  }
  
  /* removes an equipment object from the equipmentCollection
   * @throws OutstandingRequirements if the equipment is checked out
   * @param Equipment e
   * @author Abra White
   */
  public void removeEquipment(Equipment e) throws OutstandingRequirements{
    if(e.getCheckedoutStatus()){
      OutstandingRequirements problem = new OutstandingRequirements("This item is currently checked out. Cannot delete.");
      throw problem;
    }else{
      equipmentCollection.remove(e.getID());
    }
  }
  
  /* Adds a people object to the peopleCollection
   * Uses the setPersonID method to set the id
   * @param String nameString, String userName, String typeString, int classYearInt, String phoneNumber, Date restrictionDate
   * @author Abra White
   */
  public void newPerson(String nameString, String userName, String typeString, int classYearInt, String phoneNumber, Date restrictionDate) {
    People p = new People(nameString, userName, typeString, classYearInt, phoneNumber, restrictionDate);
    setPersonID(p);
    peopleCollection.put(p.getID(),p);
    System.out.println(peopleCollection.get(p.getID()));
  }
  
  //!cage.getPeopleCollection().contains(getPersonID(p))
  
  /* adds a people object from the peopleCollection with a given id
   * @param String nameString, String userName, String typeString, int classYearInt, String phoneNumber, Date restrictionDate, int id
   * @author Abra White
   */
  public void newPersonWithID(String nameString, String userName, String typeString, int classYearInt, String phoneNumber, Date restrictionDate, int id){
    People p = new People(nameString, userName, typeString, classYearInt, phoneNumber, restrictionDate);
    p.setID(id);
    peopleCollection.put(p.getID(), p);
  }
  
  /* removes a people object from the peopleCollection
   * @throws OutstandingRequirements if there are checkouts or fines so the person cannot be deleted
   * @param People p
   * @author Abra White
   */
  public void removePerson(People p) throws OutstandingRequirements{
    if(p.getCheckouts().peek()==null){
      OutstandingRequirements problem = new OutstandingRequirements("This person has items currently checked out. Cannot delete.");
      throw problem;
    }else if (p.getFines()>0){
      OutstandingRequirements problem = new OutstandingRequirements("This person has outstanding fines. Cannot delete.");
      throw problem;
    }else{
      peopleCollection.remove(p.getID());
     
    }
  }
  
  /* "returns" equipment -- changes the people object and equipment object to reflect this. checks for overdue fines
   * @param Checkout c
   * @returns double fine -- returns the fine amount
   * @author Abra White
   */
  public double returnEquipment(Checkout c){
    Equipment e = c.getEquipment();
    People p = c.getPerson();
    Date now = new Date();
    e.returnEquip();
    p.returnEquip(c);
    double diffInDays = Math.round( (now.getTime() - c.getDueDate().getTime()) / (1000 * 60 * 60 * 24));
    double fine = diffInDays*e.getFineRate();
    p.setFine(fine);
    return fine;
  }
  
  /* checks out a piece of equipment to a person for a specific period of time
   * @param String People p, Date dueDate, Equipment e
   * @author Abra White
   */
  public void checkoutEquipment(People p, Date dueDate, Equipment e){
    if(!e.getCheckedoutStatus()&&e.getGoodCondition()){
    Checkout c = new Checkout(p, dueDate, e);
    p.addCheckout(c);
    e.addCheckout(c);
    }
  }
  
  /* searches the collection of people by id
   * @param int id
   * @author Abra White
   */
  public People peopleByID(int id){
    return (People)peopleCollection.get(id);
  }
  
  /* searches the collection of equipment by id
   * @param String id
   * @author Abra White
   */
  public Equipment equipByID(String id){
    return (Equipment)equipmentCollection.get(id);
  }
  
  /* toString
   * @returns String shows the number of equipment and number of people in the database
   * @author Abra White
   */
  public String toString(){
    return "Equipment: " + equipmentCollection.size() + " People: " + peopleCollection.size();
  }
  
   /* gets PeopleCollection hashtable
   * @returns Hashtable peopleCollection
   * @author Abra White
   */
  public Hashtable getPeopleCollection(){
    return peopleCollection;
  }
  /* gets equipmentCollection hashtable
   * @returns Hashtable equipmentCollection
   * @author Abra White
   */
  public Hashtable getEquipmentCollection(){
    return equipmentCollection;
  }
  
  public static void main(String [] args) throws ParseException{
    JewettCage test = new JewettCage();
    System.out.println("Adding two cameras of same type and dept...");
    test.newEquipment("Video","Video Camera", 5.0);
    test.newEquipment("Video","Video Camera", 5.0);
    System.out.println(test);
    String theDate = "03-06-2014";
    DateFormat format = new SimpleDateFormat("dd-MM-yyyy");
    Date date = format.parse(theDate);
    System.out.println("Adding new person...");
    test.newPerson("Abra", "awhite2", "Student", 2015, "7813611543", date);
    System.out.println(test);
    System.out.println(test.peopleByID(1543));
    System.out.println(test.getPeopleCollection().get(1543));
    System.out.println("Testing checkout equipment...");
    test.checkoutEquipment(test.peopleByID(1543), date, test.equipByID("VVC1"));
    System.out.println(test.peopleByID(1543));
    System.out.println(test.peopleByID(1543).getCheckouts());
    //System.out.println(test.equipByID("VVC1").getCheckouts().peek());
    System.out.println(test.equipByID("VVC1"));
    Checkout testCheck = (Checkout)test.equipByID("VVC1").getCheckouts().peek();
    System.out.println("Testing return equipment...");
    test.returnEquipment(testCheck);
    System.out.println(test.peopleByID(1543));
    System.out.println(test.peopleByID(1543).getCheckouts());
    System.out.println(test.equipByID("VVC1"));
  }
  
}