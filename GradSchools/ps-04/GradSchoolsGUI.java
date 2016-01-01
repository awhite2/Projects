
  /* Very Important: You will need to call the new GradSchools() constructor in a place 
  * that will be available and visible to the listeners of all tabbed panels. 
  * Hint: The easiest way would be to call it in the main() of the GUI file, 
  * before you define the JTabbedPane(). Then, to make it available to the two panels, 
  * you should pass it as a parameter to each panel. (Note: This hint is worth its bytes in gold ;-)
  * 
  * It is still desirable to use println statements to keep track of what is happening in the GUI 
  * (like figuring out what your program executed, or what a particular variable contains).
  */ 

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GradSchoolsGUI
{
   //-----------------------------------------------------------------
   //  Sets up a frame containing a tabbed pane. The panel on each
   //  tab demonstrates a different layout manager.
   //-----------------------------------------------------------------
   public static void main (String[] args)
   {
      JFrame frame = new JFrame ("GradSchools");
      
      GradSchools grad = new GradSchools();
      
      frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);

      JTabbedPane tp = new JTabbedPane();
      tp.addTab ("About", new AboutPanel());
      tp.addTab ("Grad Schools", new GradSchoolsPanel(grad));
      tp.addTab ("Evaluate Schools", new EvalSchoolsPanel(grad));
      
      
      frame.getContentPane().add(tp);

      frame.pack();
      frame.setVisible(true);
      
   }
}
