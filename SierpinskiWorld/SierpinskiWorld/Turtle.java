// Simple turtle graphics package
// Create by Lyn on 3/14/97
// Updated on 11/3/97
// Rewritten by Mark Sheldon as part 
// of the conversion to Swing. Spring 2006.

import java.awt.*;

public class Turtle
{
    private double x;          // x position of turtle
    private double y;          // y position of turtle
    private double heading;    // heading of turtle, in degrees
    private boolean pendown;   // is turtle in drawing mode?
    private Color color;       // Red is the default 

    public Turtle()
    {
        color = Color.red;
        home();
        TurtleWorld.addTurtle(this);
    }

    public void home() 
    {
        this.x = 0.0;
        this.y = 0.0;
        this.heading = 0.0;
        this.pendown = true;
    }

     // Forward

     public void fd(double dist) 
     {
          double rads = degreesToRadians(heading);
          this.moveTo(x + (dist * Math.cos(rads)), 
                      y + (dist * Math.sin(rads)));
     }

     public void fd (int dist) 
     {
          fd((double) dist);
     }

     // Backward

     public void bd(double dist) 
     {
          this.fd(-dist);
     }

     public void bd (int dist) 
     {
          bd((double) dist);
     }

     // Left 

     public void lt(double degrees) 
     {
          this.heading = heading + degrees;
     }

     public void lt (int degrees) 
     {
          lt((double) degrees);
     }

     // Right 

     public void rt(double angle) 
     {
          this.lt(-angle);
     }

     public void rt (int degrees) 
     {
          rt((double) degrees);
     }

     // Pen Up 
     public void pu() 
     {
          this.pendown = false;
     }

     // Pen Down 

     public void pd() 
     {
          this.pendown = true;
     }

     // Position
     public double getX() 
     {
          return x; 
     }

     public double getY() 
     {
          return y; 
     }

    public void setX(double newX)
     {
	 x = newX; 
     }

    public void setX(int newX)
     {
	 x = (double) newX; 
     }

    public void setY(double newY)
     {
	 y = newY; 
     }

    public void setY (int newY)
     {
	 y = (double) newY; 
     }

     public Location getPosition () 
     {
          return new Location ((int) x, (int) y);
     }

     public void setPosition (Location loc) 
     {
          x = (double) loc.x;
          y = (double) loc.y;
     }

     public void setPosition (int ix, int iy) 
     {
          x = (double) ix;
          y = (double) iy;
     }

     public void setPosition (double dx, double dy) 
     {
          x = dx;
          y = dy;
     }

     // Heading

     public double getHeading () 
     {
          return heading; 
     }

     public void setHeading (double degrees) 
     {
          heading = degrees;
     }

     public void setHeading (int degrees) 
     {
          heading = (double) degrees;
     }
     
     // Color
     public Color getColor () 
     {
          return color;
     }

     public void setColor (Color c) 
     {
          color = c;
     }

     // Other

     public void moveTo(double newx, double newy) 
     {
          // For testing purposes:
          /* System.err.println("Move: heading = " + heading 
                                  + "; x = " + x 
                                  + "; y = " + y 
                                  + "; newx = " + newx
                                  + "; newy = " + newy);
	  */
	            
          if (pendown) {
               Graphics g = TurtleWorld.getTurtleGraphics();
               g.setColor(color);
               g.drawLine(screenX(x), screenY(y), screenX(newx), screenY(newy));
          }
          x = newx;
          y = newy;
     }

     private int screenX(double xcoord) 
     {
         return (int) Math.round((TurtleWorld.getCanvasWidth() / 2) + xcoord);  // Assume origin (0,0)
     }

     private int screenY(double ycoord) 
     {
         return (int) Math.round((TurtleWorld.getCanvasHeight() / 2) - ycoord);
     }

     private static double degreesToRadians (double degrees) 
     {
          return 2 * Math.PI * (degrees / 360);
     }
}

class Location {
  
  // Immutable (really, write-once) instance variables
  public final int x; 
  public final int y; 
  
  // Constructor method
  public Location(int initx, int inity) {
    x = initx;
    y = inity;
  }

  // Instance methods
  
  public boolean equals (Object obj) {
    if (obj instanceof Location) {
      Location loc = (Location) obj;
      return (x == loc.x) && (y == loc.y);
    } else {
      return false;
    }
  }

  public Point toPoint () {
    return new Point(x,y); 
  }
  
  // Displaying as a string: 
  public String toString() {
    return "Location(x=" + x + ",y=" + y + ")";
  }

  // Returns a new location that sums the respective components of 
  // loc and this location. 
  public Location add (Location loc) {
    return new Location (this.x + loc.x, this.y + loc.y);
  }

  // Class methods

  public Location fromPoint (Point p) {
    return new Location(p.x, p.y); 
  }

  public Point toPoint (Location loc) {
    return new Point(loc.x, loc.y); 
  }
  
}
