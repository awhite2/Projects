import java.util.*;
import javafoundations.LinkedStack;

public class Equipment implements Comparable<Equipment>{
  //instance variables
  private String department, type, id;
  private boolean checkedoutStatus, goodCondition;
  private double fineRate;
  private LinkedStack<Checkout> checkouts;
  
  //constructor
  /*Constructor for Equipment object
   * sets department, type, and fineRate using parameters
   * id is set later?
   * goodCondition is set to true, checkedoutStatus is set to false, checkouts is initialized
   * @param String dept, String t, int fine
   * @author Abra White
   */
  public Equipment(String dept, String t, double fine){
    department = dept;
    type = t;
    checkedoutStatus = false;
    goodCondition = true;
    fineRate = fine;
    checkouts = new LinkedStack<Checkout>();
  }
  
  
  //methods
  //toString
  public String toString(){
    String s = " ";
    String n = id + s + checkedoutStatus;
    if(checkedoutStatus){
      n += s + checkouts.peek().getPerson().getName();
    }
    n += s + fineRate;
    return n;
  }
  
  /*Adds Checkout object to checkouts stack
   * @param Checkout c
   * @author Abra White
   */
  public void addCheckout(Checkout c){
    checkouts.push(c);
    //System.out.println("In equipment: " + checkouts);
    checkedoutStatus=true;
  }
  
  //return
  public void returnEquip(){
    Date now = new Date();
    checkedoutStatus = false;
    checkouts.peek().setReturnDate(now);
  }
  
  public int compareTo(Equipment e){
    return id.compareTo(e.getID());
  }
  
  /*************************************Setters**********************************************/
  /*Sets id variable
   * @author Abra White
   */
  public void setID(String s){
    id = s;
  }
  
  /*Sets department variable
   * @param String dept
   * @author Abra White
   */
  public void setDepartment(String dept){
    department = dept;
  }
 
  /*Sets type variable
   * @param String s
   * @author Abra White
   */
  public void setType(String s){
    type = s;
  }
  
  /*Sets checkedoutStatus variable
   * @param boolean b
   * @author Abra White
   */
  public void setCheckedoutStatus(boolean b){
    checkedoutStatus = b;
  }
  
  /*Sets goodCondition variable
   * true if in good condition, false if broken
   * cannot takeout if false
   * @param boolean b
   * @author Abra White
   */
  public void setCondition(boolean b){
    goodCondition = b;
  }
  
  /*Sets fineRate variable
   * @param double n
   * @author Abra White
   */
  public void setFineRate(double n){
    fineRate = n;
  }
  /*************************************Getters**********************************************/
  /*Gets department variable
   * @returns String department
   * @author Abra White
   */
  public String getDepartment(){
    return department;
  }
  
  /*Gets id variable
   * @returns String id
   * @author Abra White
   */
  public String getID(){
   return id;
  }
  
  /*Gets type variable
   * @returns String type
   * @author Abra White
   */
  public String getType(){
    return type;
  }
  
  /*Gets checkedoutStatus variable
   * @returns boolean checkedoutStatus
   * @author Abra White
   */
  public boolean getCheckedoutStatus(){
    return checkedoutStatus;
  }
  
  /*Gets goodCondition variable
   * @returns boolean goodCondition
   * @author Abra White
   */
  public boolean getGoodCondition(){
    return goodCondition;
  }
  
  /*Gets fineRate variable
   * @returns int fineRate
   * @author Abra White
   */
  public double getFineRate(){
    return fineRate;
  }
  
  /*Gets checkouts variable
   * @returns Queue checkouts
   * @author Abra White
   */
  public LinkedStack getCheckouts(){
    return checkouts;
  }
  
}