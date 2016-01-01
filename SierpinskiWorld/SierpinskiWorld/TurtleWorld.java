/********************************************************************

Name: TurtleWorld.java

Description:
   Implementation of CS111 TurtleWorld classes.
   TurtleWorld is a Java microworld of drawing creatuers
   inspired by LOGO. 
   
History:

 ------------------------------------------------------------------
 [brian, 10/01/07] 
                 * Added "runAsApplication" method to allow 
                   TurtleWorld to be run as an application
                   as well as an applet. This is particularly
                   when the development environment is Dr. Java.
                   
                 * Added "main" method to allow TurtleWorld to
                   be run as an application.
                   
                 * Commented out "System.err.println" statements
                   to minimize unnecessary messages displayed in
                   console.
                   
                 * Added class variable "frameSize", which 
                   indicates the default frame size, i.e., 
                   a window with dimensions [frameSize x frameSize].
                   It is useful to know the frameSize so that 
                   ParameterFrames can be positioned appropriately.
 ------------------------------------------------------------------
 [mas, 03/01/06] Rewritten as part of the conversion to Swing.
 
   Issues and questions:
     o Why don't turtles become red when they go home?
     o Why do we keep a vector of turtles in TurtleWorld and send them
       home on Reset?  The only thing the use can do after Reset is Run
       again, which will create the turtles all over again.  This is a
       storage leak:  We should just let them be GC-ed.
     o Swing documentation cautions against overriding the paint()
       method. 
  ------------------------------------------------------------------
 [lyn, 03/14/97] TurtleWorld is born. Lyn created the simple
                 turtle graphics package.


********************************************************************/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;


public class TurtleWorld extends JApplet implements ActionListener
{
    private static final String runLabel = "Run";
    private static final String resetLabel = "Reset";

    public static final int frameSize = 500;  // Default frame size
    
    private static TurtleCanvas canvas;
    private static Vector turtles = new Vector();

    private boolean hasRun;

    //----------------------------------------------------------------------
    /*** [brian, 10/02/07] New code for running as an application ***/
  
    public static void main (String[] args) 
    {
        runAsApplication(new TurtleWorld(), "TurtleWorld"); 
    }
  
    public static void runAsApplication (final TurtleWorld applet, 
                                         final String name) 
    {
      // Schedule a job for the event-dispatching thread:
      // creating and showing this buggle world applet. 
      javax.swing.SwingUtilities.invokeLater(new Runnable() {
          public void run() // this is Java's thread run() method, 
          {                 // not TurtleWorld's!
              // enable window decorations. 
              JFrame.setDefaultLookAndFeelDecorated(true); 
              JFrame frame = new JFrame(name); // create and set up the window.

              frame.setSize(frameSize, frameSize); // Default frame size
   
              // Using EXIT_ON_CLOSE empirically exits all instances
              // of an application.
              // Use DISPOSE_ON_CLOSE to get rid of just one. 
              frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE); 
   
              // Need to add to frame and make visible *before* init 
              // so that attempts to reset dimensions will work. 
              frame.add(applet, BorderLayout.CENTER); // add applet to window
              frame.setVisible(true); // display the window.
              applet.init(); // initialize the applet
              // Need to make visible again *after* init in case
              //  something like setDimensions is not called in init. 
              frame.setVisible(true); // display the window.
          }
 });
    }
    //----------------------------------------------------------------------

    public void init()
    {
        //System.err.println("init()");

        Container content = getContentPane();
        content.setLayout(new BorderLayout());
 content.setBackground(Color.white);

        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new GridLayout(1, 2));
 controlPanel.setBackground(Color.white);

        JButton runButton = new JButton(runLabel);
 runButton.setBackground(Color.white);
        runButton.addActionListener(this);
        controlPanel.add(runButton);

        JButton resetButton = new JButton (resetLabel);
 resetButton.setBackground(Color.white);
        resetButton.addActionListener(this);
        controlPanel.add(resetButton);

        canvas = new TurtleCanvas();
        canvas.setBackground(Color.white);
        //System.err.println("Canvas size = " + canvas.getSize());
        //System.err.println("Canvas width = " + canvas.getWidth());
        //System.err.println("Canvas graphics = " + canvas.getGraphics());

        content.add(controlPanel, BorderLayout.SOUTH);
        content.add(canvas, BorderLayout.CENTER);
        //System.err.println("Canvas size = " + canvas.getSize());
        //System.err.println("Canvas graphics = " + canvas.getGraphics());

        this.setup();    // Hook for user-defined initializations

        hasRun = false;

    }

    public void paint (Graphics g)
    {
        //System.err.println("paint()");
        super.paint(g);
        if (hasRun)
            this.run();
    }

    /*
    public void paintComponent (Graphics g)
    {
        System.err.println("paintComponent()");
        super.paintComponent(g);
        this.run();
    }

    public void start()
    {
        System.err.println("start()");
    }

    public void stop()
    {
        System.err.println("stop()");
    }
*/
    public static void addTurtle(Turtle t) 
    {
        turtles.addElement(t);
    }

    public void setup()
    {
        // Users will override this method
    }

    public void run()
    {
        // Users will override this method
    }

    public static Graphics getTurtleGraphics()
    {
        return canvas.getGraphics();
    }

    public static int getCanvasWidth()
    {
        return canvas.getWidth();
    }

    public static int getCanvasHeight()
    {
        return canvas.getHeight();
    }

    public void actionPerformed(ActionEvent e)
    {
        String cmd = e.getActionCommand();
        if (cmd.equals(runLabel))
            runAction();
        else if (cmd.equals(resetLabel))
            resetAction();
        else
            System.err.println("Undefined button label: " + cmd);   // Should never happen
    }

    private void runAction()
    {
        //System.err.println("Run button hit");
        hasRun = true;
        this.run();
    }

    private void resetAction()
    {
        //System.err.println("Reset button hit");
        hasRun = false;

        Graphics g = getTurtleGraphics();
        g.drawString("Resetting...", 50, 50);
        g.setColor(canvas.getBackground());
        g.fillRect(0, 0, getCanvasWidth(), getCanvasHeight());
        for (int i = 0; i < turtles.size(); i++)     
            ((Turtle) turtles.elementAt(i)).home();   // why do we bother with this? -MAS
    }
}

class TurtleCanvas extends JPanel
{
    protected void paintComponent(Graphics g)
    {
        super.paintComponent(g);
    }
}
