import java.awt.*;
import javax.swing.*;

/*When your program starts, a tab named "About" appears that contains information 
 * about the creator of the program and instructions on how to use it. Show overall rating.
 */

public class AboutPanel extends JPanel {

   //-----------------------------------------------------------------
   //  Sets up this panel with two labels.
   //-----------------------------------------------------------------
   public AboutPanel()
   {
      setBackground(Color.orange);

      JTextArea l4 = new JTextArea ("Grad Schools Application\nChoose the grad school for you!\n----------------------------------------------\nAdd grad schools in the grad school tab and rate the different categories. \nThen weight the importance of these categories in the 'Evaluate Schools' tab for a ranked list.\nCreated by: Abra White 2013");

      
      l4.setEditable(false);
      
      add (l4);
      setPreferredSize (new Dimension(500, 250));
      
   }

}