/*CS 230
 * Abra White
 * HW 5
 * Last updated: October 17, 2013
 */
import java.util.*;
import javax.swing.*;

public class Vigenere implements Encryptable{
  //instance variables
  private String message;
  private boolean encrypted;
  private String password;
  
  //constructor set the message and password. make them lowercase. set encrypted to false
  public Vigenere(String msg, String pswrd){
    message = msg.toLowerCase();//message to lowercase
    message = message.replaceAll("\\s","");//remove spaces
    password = pswrd.toLowerCase();//password to lowercase
    encrypted = false;//to start it is not encrypted
  }
  
  //encrypt the message with the password.If not already encrypted 
  public void encrypt (){
    if(!encrypted)
    {
      //set a temporary message variable, a variable to store the encrypted result, and a variable to store the substring
      String str = message;//temp message string
      String after = "";//encrypted message
      String sub= "";//substring
      
      //if the message string is shorter than the password make the substring that length
      //to avoid out of bounds exceptions
      if(str.length()<password.length()){
        sub=str;
      }else{
        //otherwise the substring should be the length of the password
        sub = str.substring(0,password.length());
      }
      
      //take a section of the whole message that is the length of the password
      //or, if it is shorter than the password the whole length
      //and shift each character with the corresponding password letter
      //and if it shifts past z it goes back to the beginning of alphabet
      //moves to the next section of the message
      //at the end sets encrypted to true and sets the message as the encrypted message
      
      //go through for as many password lengths are in the message
      for(int i =0; i<=message.length()/password.length();i++){
        //if the substring is less than the length of the password use the length of the substring to avoid exception 
        if(sub.length()<password.length()){
          for(int j=0; j<sub.length(); j++){
            Character index = sub.charAt(j); //set index to current character
            int passwordNum = (Character.getNumericValue(password.codePointAt(j))-10); //get the number associated with the current password character
            int code = sub.charAt(j)+passwordNum;//add the shift key to the current character
            
            //for returning back to the beginning
            //if code is greater than the number of z 
            char z = 'z';
            char a = 'a';
            if(code>z){
              index = (char)(((passwordNum-(z-sub.charAt(j)))+a)-1);//subtract the current from z and then subtract that from the numeric value and add the numeric value to a
            }
            else{
              index=(char)(code);//set the index
            }
            // }
            after+=index;//add the index to the encrypted message
          }
        }else{
          //for a substring the length of the password
          for(int j=0; j<password.length(); j++){ //go through each of the password letters 
            Character index = sub.charAt(j);//set the index character
            int passwordNum = (Character.getNumericValue(password.codePointAt(j))-10); //the shift integer
            int code = sub.charAt(j)+passwordNum; //
            
            //if code is greater than the codepoint of z 
            char z = 'z';
            char a = 'a';
            if(code>z){
              index = (char)(((passwordNum-(z-sub.charAt(j)))+a)-1);
            }
            //subtract the current from z and then subtract that from the numeric value and add the numeric value to a
            else{
              index=(char)(code);
              
            }after+=index;//add the index to the new string
          }
          sub=str.substring(password.length()*(i+1));//go through as many times as passwords fit in the message
        }
      }
      encrypted=true;
      message=after.toUpperCase();//set message to new string
    }
  }
  
  
  public String decrypt(){
    if(encrypted){
      message=message.toLowerCase();
      //set a temporary message variable, a variable to store the encrypted result, and a variable to store the substring
      String str = message;//temp message string
      String after = "";//encrypted message
      String sub= "";//substring
      
      //if the message string is shorter than the password make the substring that length
      //to avoid out of bounds exceptions
      if(str.length()<password.length()){
        sub=str;
      }else{
        //otherwise the substring should be the length of the password
        sub = str.substring(0,password.length());
      }
      
      //go through for as many password lengths are in the message
      for(int i =0; i<=message.length()/password.length();i++){
        //if the substring is less than the length of the password use the length of the substring to avoid exception 
        if(sub.length()<password.length()){
          for(int j=0; j<sub.length(); j++){
            Character index = sub.charAt(j); //set index to current character
            int passwordNum = (Character.getNumericValue(password.codePointAt(j))-10); //get the number associated with the current password character
            int code = sub.charAt(j)-passwordNum;//add the shift key to the current character
            
            //for returning back to the beginning
            //if code is greater than the number of z 
            char z = 'z';
            char a = 'a';
            if(code<a){
              index = (char)((z-(passwordNum-(sub.charAt(j)-a)))+1);
            }
            else{
              index=(char)(code);//set the index
            }
            // }
            after+=index;//add the index to the encrypted message
          }
        }else{
          //for a substring the length of the password
          for(int j=0; j<password.length(); j++){ //go through each of the password letters 
            Character index = sub.charAt(j);//set the index character
            int passwordNum = (Character.getNumericValue(password.codePointAt(j))-10); //the shift integer
            int code = sub.charAt(j)-passwordNum; //
            
            //if code is greater than the codepoint of z 
            char z = 'z';
            char a = 'a';
            if(code<a){
              index = (char)((z-(passwordNum-(sub.charAt(j)-a)))+1);
            }else{
              index=(char)(code);
            }after+=index;
          }
          sub=str.substring(password.length()*(i+1));
        }
      }
      encrypted=true;
      message=after.toUpperCase();}
      return message;
  }
  
  
  //checks if it is encrypted
  public boolean isEncrypted(){
    return encrypted;
  }
  
  //to string method
  public String toString(){
    return message;
  }
  
  public static void main(String [] args){
    Scanner scan = new Scanner(System.in);
    String msg = JOptionPane.showInputDialog ("Enter a message");
    String pswd = JOptionPane.showInputDialog ("Enter a password");
    Vigenere test1 = new Vigenere(msg, pswd);
    test1.encrypt();
    JOptionPane.showMessageDialog (null, test1.toString());
    System.out.println(test1.toString());
    int again = JOptionPane.showConfirmDialog (null, "Decrypt?");
    if(again == JOptionPane.YES_OPTION){
      test1.decrypt();
      JOptionPane.showMessageDialog (null, test1.toString());
      System.out.println(test1.toString());
    }
    
  }
  
  
  
}