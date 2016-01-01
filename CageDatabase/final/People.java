/*For Jewett Cage Software
 *CS230 Nina Broocks and Abra White
 *This class provides the People object and methods associated with it. The people object
 *is used to store the name, email, type (department), class year, phone number, fines, id
 *restriction date, and checkouts.
 * 
 * @author Abra White
 */

import java.util.*;
import java.util.concurrent.*;


public class People implements Comparable<People>{
  
  //instance variables
  private String name, email, type, phone;
  private int classYear, id;
  private double fines;
  private Date restriction;
  private BlockingQueue<Checkout> checkouts;
  
  //constructors
  /*Constructor for People object
   * sets name, email, tyoe, classYear, phone, and restrictionDate using parameters
   * fines is 0
   * id is set later?
   * @param String nameString, String userName, String typeString, int classYearInt, String phoneNumber, Date restrictionDate
   * @author Abra White
   */
  People(String nameString, String userName, String typeString, int classYearInt, String phoneNumber, Date restrictionDate){
    name = nameString;
    setEmail(userName);
    type = typeString;
    classYear = classYearInt;
    phone = phoneNumber;
    restriction = restrictionDate;
    checkouts = new LinkedBlockingQueue<Checkout>();
    fines = 0.0;
  }
  
  //methods
  
  /*Checks if the person has anything checked out
   * @returns true if checkouts is not empty, false if it is
   * @author Abra White*/
  public boolean hasCheckouts(){
    return !checkouts.isEmpty();
  }
  /*Adds new value to fines variable
   * @param int plus
   * @author Abra White*/
  public void addFine(int plus){
    fines = fines + plus;
  }
  
  /*Sets fines variable to zero
   * @author Abra White
   */
  public void removeFine(){
    fines = 0.0;
  }
  
  /*Adds an equipment object to checkouts
   * @param Checkout c
   * @author Abra White
   */
  public void addCheckout(Checkout c){
    checkouts.add(c);
  }
  
  /*Removes an equipment object to checkouts
   * @param Checkout c
   * @author Abra White
   */
  public void removeCheckout(Checkout c){
    checkouts.remove(c);
  }
  
  
  //return
  public void returnEquip(Checkout c){
    removeCheckout(c);
  }
  
  public int compareTo(People p){
    if(id==p.getID()){
      return 0;
    }else if(id>p.getID()){
      return 1;}
    else{
      return -1;}
  }
  
  /*************************************Setters**********************************************/
  /*Sets id variable
   * @param int i
   * @author Abra White
   */
  public void setID(int i){
    id=i;
  }
  /*Sets name variable
   * @param String s
   * @author Abra White
   */
  public void setName(String s){
    name = s;
  }
  
  /*Sets phone variable
   * @param String s
   * @author Abra White
   */
  public void setPhone(String s){
    phone = s;
  }
  
  
  /*Sets email variable
   * takes username and adds the wellesley domain to the end
   * @param String userName
   * @author Abra White
   */ 
  public void setEmail(String userName){
    email = userName + "@wellesley.edu";
  }
  
  /*Sets type variable
   * @param String dept
   * @author Abra White
   */
  public void setType(String dept){
    type = dept;
  }
  
  /*Sets restriction variable
   * Aparameters Date date
   * @author Abra White
   */
  public void setRestrictionDate(Date date){
    restriction = date;
  }
  
  /*Sets restriction variable
   * @param Date date
   * @author Abra White
   */
  public void setRestriction(Date date){
    restriction = date;
  }
  
  public void setFine(double plus){
    fines = fines +plus;
  }
  /*************************************Getters**********************************************/
  /*Gets name variable
   * @returns String name
   * @author Abra White
   */
  public String getName(){
    return name;
  }
  
  /*Gets id variable
   * @returns int id
   * @author Abra White
   */
  public int getID(){
   return id;
  }
  
  /*Gets email variable
   * @returns String email
   * @author Abra White
   */
  public String getEmail(){
    return email;
  }
  
  /*Gets type variable
   * @returns String type
   * @author Abra White
   */
  public String getType(){
    return type;
  }
  
  /*Gets classYear variable
   * @returns int classYear
   * @author Abra White
   */
  public int getClassYear(){
    return classYear;
  }
  
  /*Gets phone variable
   * @returns String phone
   * @author Abra White
   */
  public String getPhone(){
    return phone;
  }
  
  /*Gets fines variable
   * @returns double fines
   * @author Abra White
   */
  public double getFines(){
    return fines;
  }
  
  /*Gets restriction variable
   * @returns Date restriction
   * @author Abra White
   */
  public Date getRestriction(){
    return restriction;
  }
  
  /*Gets checkouts variable
   * @returns Queue checkouts
   * @author Abra White
   */
  public BlockingQueue getCheckouts(){
    return checkouts;
  }

  //toString
  public String toString(){
    String s = " ";
    return name + s + id + s + fines + s + hasCheckouts();
  }
}