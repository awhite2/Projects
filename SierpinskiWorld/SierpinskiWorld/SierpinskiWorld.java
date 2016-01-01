import java.awt.*;       // Import Abstract Window Toolkit
import java.applet.*;    // Import Applet stuff

// Drawing Sierpinski gaskets with turtles.

public class SierpinskiWorld extends TurtleWorld 
{
     String parameterNames [] = {"levels", "side"};
     String parameterFields [] = {"3", "400"};
     ParameterFrame params;
 
     //-----------------------------------------------------------------------
     // This main() method is needed to run the applet as an application
     public static void main (String[] args)
     {
          runAsApplication(new SierpinskiWorld(), "SierpinskiWorld"); 
     }
     //-----------------------------------------------------------------------

     public void setup()
     {
          params = new ParameterFrame("Sierpinski Parameters",
                                      TurtleWorld.frameSize, 0,
                                      180, 105,
                                      parameterNames, parameterFields);
     }
     public void run() 
     {
          SierpinskiMaker sierpa = new SierpinskiMaker();
          // Move to good initial position using simple geometry
          double radius = params.getIntParam("side") / Math.sqrt(3);
          sierpa.pu();
          sierpa.lt(90);
          sierpa.bd(radius/4.0);
          sierpa.rt(60);
          sierpa.bd(radius);
          sierpa.rt(30);
          sierpa.pd();
          sierpa.sierpinski(params.getIntParam("levels"), 
                            (double) params.getDoubleParam("side"));
          
     }
}

// Add your SierpinskiMaker class definition below.
class SierpinskiMaker extends Turtle{

public void sierpinski(int levels, double size){
  if(levels==0){
  }else
  {fd(size);
    lt(120);
    sierpinski(levels-1, size/2);
    fd(size);
    lt(120);
    sierpinski(levels-1, size/2);
    fd(size);
    lt(120);
    sierpinski(levels-1, size/2);
  }}}



  
