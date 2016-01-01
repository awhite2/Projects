/*For Jewett Cage Software
 *CS230 Nina Broocks and Abra White
 *This class provides the Checkout object and methods associated with it. The checkout object
 *is used to store the time taken out, due date, and time returned for a specific piece of 
 *equipment to a person.
 * 
 * @author Abra White
 */
import java.util.*;

public class Checkout implements Comparable<Checkout>{
  //instance variables
  private People person;
  private Equipment equip;
  private Date checkoutDate, dueDate, returnDate;
  //private int fine;
  
  
  //constructor method
  /*Constructor for Checkout object
   * sets person, equip, returnDate and dueDate using parameters
   * checkoutDate is the current date
   * returnDate is dueDate until changed
   * @param People name, Date due, Equipment e
   * @author Abra White
   */
  public Checkout(People name, Date due, Equipment e){
    person = name;
    equip = e;
    checkoutDate = new Date();
    dueDate = due;
    returnDate = due;
  }
  
  //methods
  /*Compares two Checkout objects
   * @param Checkout c
   * @returns 0 if equip, person, and checkoutDate are equal, 1 equip id is greater, person name comes after, or checkoutDate is after, else -1
   * @author Abra White
   */
  public int compareTo(Checkout c){
    int p = person.compareTo(c.getPerson());
    int e = equip.compareTo(c.getEquipment());
    if (p==0 && e==0 && checkoutDate.equals(c.getCheckoutDate())){
      return 0;}
    else if (p==1 || e==1 || checkoutDate.after(c.getCheckoutDate())){
      return 1;}
    else {
      return -1;
    }        
  }
  
  /* toString method
   * @returns String s which shows the name, equipmentid, checkout date, due date, and whether it's been returned or not
   * @author Abra White
   */
  public String toString(){
   String s = person.getName() + " " + equip.getID() + " " + checkoutDate + " " + dueDate;
   Date thisDate = new Date();
   if(!equip.getCheckedoutStatus()){
     s+=" " + returnDate;
   }else{
     s+= " Not Returned";
   }
   return s;
  }
  
  /*Gives a string to display on people pages for checkouts
   * @returns String s
   * @author Abra White
   */
  public String displayForPeople(){
    String s =  equip.getID() + " " + checkoutDate + " " + dueDate;
    Date thisDate = new Date();
    if(equip.getCheckedoutStatus()){
      s+=" " + returnDate;
    }else{
      s+= " Not Returned";
    }
    return s;
  }
  
  /*Gives a string to display on equipment page for checkouts
   * @returns String s
   * @author Abra White
   */
  public String displayForEquipment(){
    String s = person.getName() + " "  + checkoutDate + " " + dueDate;
    Date thisDate = new Date();
    if(equip.getCheckedoutStatus()){
      s+=" " + returnDate;
    }else{
      s+= " Not Returned";
    }
    return s;
  }
  
  /*"Returns" equipment by setting the return date
   * @author Abra White
   */
  public void returnEquip(){
    returnDate = new Date();
  }
  
  /*************************************Setters**********************************************/
  /*Sets person variable
   * @param People newPerson
   * @author Abra White
   */
  public void setPerson(People newPerson){
    person = newPerson;
  }
  
  /*Sets dueDate variable
   * @param Date due
   * @author Abra White
   */ 
  public void setDueDate(Date due){
    dueDate = due;
  }
  
  /*Sets returnDate variable
   * @param Date date
   * @author Abra White
   */
  public void setReturnDate(Date date){
    returnDate = date;
  }
  
  /*Sets returnDate variable
   * uses current date
   * @author Abra White
   */
  public void setReturnDate(){
    returnDate = new Date();
  }
  
  /*Sets equip variable
   * @param Equipment e
   * @author Abra White
   */
  public void setEquipment(Equipment e){
    equip = e;
  }
  
  /*************************************Getters**********************************************/
  /*Gets person variable
   * @returns person
   * @author Abra White
   */
  public People getPerson(){
    return person;
  }
  
  /*Gets checkoutDate variable
   * @returns checkoutDate
   * @author Abra White
   */
  public Date getCheckoutDate(){
   return checkoutDate;
  }
  
  /*Gets dueDate variable
   * @returns dueDate
   * @author Abra White
   */
  public Date getDueDate(){
   return dueDate;
  }
  
  /*Gets returnDate variable
   * @returns returnDate
   * @author Abra White
   */
  public Date getReturnDate(){
    return returnDate;
  }
  
  /*Gets equip variable
   * @returns equip
   * @author Abra White
   */
  public Equipment getEquipment(){
    return equip;
  }
}