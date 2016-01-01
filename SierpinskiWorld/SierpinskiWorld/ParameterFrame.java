/********************************************************************

Name: ParameterFrame.java

Description:
   Enables Parameter windows to appear along with the TutleWorld
   window. Parameter windows allow users to interactively
   adjust parameters for TurtleWorld programs.
   
History:

 ------------------------------------------------------------------
 [brian, 10/01/07] 
                 * Modified to include parameter fields. These
                   are useful so that default parameter values can
                   be included in parameter frames. If no default
                   parameter values are included in the parameter
                   frames and a user clicks the TurtleWorld "run"
                   button, then a runtime exception will occur.
                   
                 * ParameterFrame constructors were expanded to include 
                   parameter fields as well as (x,y) coordinates indicating
                   where the ParameterFrame window should be placed
                   on the screen. Specification of where the window
                   is placed is important so that the Parameter
                   window is not placed underneath the TurtleWindow
                   window, but rather alongsize it.

                 * Updated ParameterPanel constructors to 
                   appropriately handle parameter fields.
 ------------------------------------------------------------------
 [mas, 07/01/07] 
               * Use Swing classes

               * Expand constructors so width and height may be
                 omitted (in which case the pack() method uses
                 the layout manager to pick the size)
 ------------------------------------------------------------------
 [lyn, 11/13/06] Modified to handle colors.
 ------------------------------------------------------------------
 [lyn, 03/10/03] Modified to include result names.


********************************************************************/

import java.awt.*;
import javax.swing.*;

public class ParameterFrame extends JFrame 
{
    private static Color backgroundColor = Color.green;
    private ParameterPanel params;
    private static String [] emptyNames = {}; 

    public ParameterFrame (String title, String [] paramNames,
                           String [] resultNames, String [] paramFields) 
    {
        setTitle(title);
        setBackground(backgroundColor);
        Container content = getContentPane();
        content.setLayout(new FlowLayout());
        params = new ParameterPanel(paramNames, resultNames, paramFields);
        content.add(params);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        pack();
        setVisible(true);
    }

    public ParameterFrame (String title, String [] paramNames,
                           String [] resultNames)
    {
        this(title, paramNames, resultNames, new String[paramNames.length]);
    }
    
    public ParameterFrame (String title, int x, int y, int width, int height,
                           String [] paramNames, String [] paramFields) 
    {
        this(title, paramNames, emptyNames, paramFields);
        setBounds(x,y,width,height);
    }
    
    public ParameterFrame (String title, int x, int y, int width, int height,
                           String [] paramNames, String [] resultNames, 
                           String [] paramFields) 
    {
        this(title, paramNames, resultNames, paramFields);
        setBounds(x,y,width,height);
    }
    
    public ParameterFrame (String title, int width, int height,
                           String [] paramNames, String [] resultNames) 
    {
        this(title, 0, 0, width, height, paramNames,
             resultNames, new String[paramNames.length]);
    }
    
    public ParameterFrame (String title, int width, int height,
                           String [] paramNames) 
    {
        this(title, width, height, paramNames, emptyNames);
    }

    public ParameterFrame (String title, int x, int y,
                           int width, int height,
                           String [] paramNames) 
    {
        this(title, x, y, width, height, paramNames, emptyNames);
    }
    
    public ParameterFrame (String title, String [] paramNames) 
    {
        this(title, paramNames, emptyNames);
    }
  
    public int getIntParam (String name)
    {
        return params.getIntParam(name);
    }
 
    public double getDoubleParam (String name)
    {
        return params.getDoubleParam(name);
    }
 
    public boolean getBooleanParam (String name)
    {
        return params.getBooleanParam(name);
    }
 
    public String getStringParam (String name)
    {
        return params.getStringParam(name);
    }
 
    public Color getColorParam (String name)
    {
        return params.getColorParam(name);
    }
 
    public void setIntParam (String name, int value)
    {
        params.setIntParam(name, value);
    }
 
    public void setBooleanParam (String name, boolean value)
    {
        params.setBooleanParam(name, value);
    }
 
    public void setDoubleParam (String name, double value)
    {
        params.setDoubleParam(name, value);
    }

    public void setStringParam (String name, String value)
    {
        params.setStringParam(name, value);
    }
 
    public void setColorParam (String name, Color c)
    {
        params.setColorParam(name, c);
    }
 
    public int getIntResult (String name)
    {
        return params.getIntResult(name);
    }
 
    public double getDoubleResult (String name)
    {
        return params.getDoubleResult(name);
    }
 
    public boolean getBooleanResult (String name)
    {
        return params.getBooleanResult(name);
    }
 
    public String getStringResult (String name)
    {
        return params.getStringResult(name);
    }
 
    public Color getColorResult (String name)
    {
        return params.getColorResult(name);
    }
 
    public void setIntResult (String name, int value)
    {
        params.setIntResult(name, value);
    }
 
    public void setBooleanResult (String name, boolean value)
    {
        params.setBooleanResult(name, value);
    }
 
    public void setDoubleResult (String name, double value)
    {
        params.setDoubleResult(name, value);
    }

    public void setStringResult (String name, String value)
    {
        params.setStringResult(name, value);
    }
 
    public void setColorResult (String name, Color c)
    {
        params.setColorResult(name, c);
    }

    // [MAS] Former version of this method was handleEvent(Event) which 
    // returned a boolean.  However, the super.handleEvent() is deprecated
    // with a recommendation that one use processEvent(AWTEvent) instead.
    // However, processEvent() is void.  Renaming the method will help me
    // find any dependencies (since the method was public).
    public void processEvent(AWTEvent evt) 
    { 
        // [MAS] Make parameter window go away when click upper left button
        // Now handled by setting the default action in the constructor.
/*         if (evt.id == AWTEvent.WINDOW_DESTROY) {
 *             setVisible(false);
 *             dispose();
 *         }
 */
        super.processEvent(evt);  
        return;
    }
}

class ParameterPanel extends JPanel
{
    private static Color paramLabelColor = Color.white;
    private static Color paramFieldColor = Color.yellow;
    private static Color resultLabelColor = Color.magenta;
    private static Color resultFieldColor = Color.cyan;
    private static Font font = new Font("Serif", Font.PLAIN,20);

    private static int fieldWidth = 4; // Default field width
    private String [] paramNames;
    private JTextField [] paramFields;
    private String [] resultNames;
    private JTextField [] resultFields;

 
    public ParameterPanel (String [] pnames, String [] rnames,
                           String [] pfields)
    {
        this.paramNames   = pnames; 
        this.resultNames  = rnames; 
        this.paramFields  = new JTextField [pnames.length];
        this.resultFields = new JTextField [rnames.length];
        int rows = pnames.length + rnames.length;
        this.setLayout (new GridLayout(rows, 2));
        try {
            for (int i = 0; i < pnames.length; i++) {
                JLabel label = new JLabel(pnames[i]);
                label.setBackground(paramLabelColor);
                label.setFont(font);
                this.add(label);
                JTextField field = new JTextField(fieldWidth);
                field.setBackground(paramFieldColor);
                field.setFont(font);
                field.setText(pfields[i]);
                this.add(field);
                paramFields[i] = field;
            }
            for (int i = 0; i < rnames.length; i++) {
                JLabel label = new JLabel(rnames[i]);
                label.setBackground(resultLabelColor);
                label.setFont(font);
                this.add(label);
                JTextField field = new JTextField(fieldWidth);
                field.setBackground(resultFieldColor);
                field.setEditable(false); 
                field.setFont(font);
                this.add(field);
                resultFields[i] = field;
            }
        } catch (ParameterException e) {
            System.out.println("Error initializing parameter window fields:\n"
                               + e.getMessage());
        }
    }

    
    public ParameterPanel (String [] pnames, String [] rnames)
    {
        this(pnames, rnames, new String[pnames.length]);
    }
    
    public int getIntParam (String name)
    {
        return Integer.parseInt(paramFields[paramIndex(name)].getText());
    }
 
    public double getDoubleParam (String name)
    {
        int i = paramIndex(name);
        
        return (Double.valueOf(paramFields[i].getText())).doubleValue();
    }
 
    public boolean getBooleanParam (String name)
    {
        return ((paramFields[paramIndex(name)].getText()).equals("true"));
    }
 
    public String getStringParam (String name)
    {
        return paramFields[paramIndex(name)].getText();
    }
 
    public Color getColorParam (String name)
    {
        return stringToColor(paramFields[paramIndex(name)].getText());
    }
 
    public void setIntParam (String name, int value)
    {
        paramFields[paramIndex(name)].setText(Integer.toString(value));
    }
 
    public void setBooleanParam (String name, boolean value)
    {
        paramFields[paramIndex(name)].setText(value ? "true" : "false");
    }
 
    public void setDoubleParam (String name, double value)
    {
        paramFields[paramIndex(name)].setText(Double.toString(value));
    }

    public void setStringParam (String name, String value)
    {
        paramFields[paramIndex(name)].setText(value);
    }
 
    public void setColorParam (String name, Color c)
    {
        paramFields[paramIndex(name)].setText(colorToString(c));
    }
 
    public int getIntResult (String name)
    {
        return Integer.parseInt(resultFields[resultIndex(name)].getText());
    }
 
    public double getDoubleResult (String name)
    {
        int i = resultIndex(name);
        return (Double.valueOf(resultFields[i].getText())).doubleValue();
    }
 
    public boolean getBooleanResult (String name)
    {
        return ((resultFields[resultIndex(name)].getText()).equals("true"));
    }
 
    public String getStringResult (String name)
    {
        return resultFields[resultIndex(name)].getText();
    }
 
    public Color getColorResult (String name)
    {
        return stringToColor(resultFields[resultIndex(name)].getText());
    }
 
    public void setIntResult (String name, int value)
    {
        resultFields[resultIndex(name)].setText(Integer.toString(value));
    }
 
    public void setBooleanResult (String name, boolean value)
    {
        resultFields[resultIndex(name)].setText(value ? "true" : "false");
    }
 
    public void setDoubleResult (String name, double value)
    {
        resultFields[resultIndex(name)].setText(Double.toString(value));
    }

    public void setStringResult (String name, String value)
    {
        resultFields[resultIndex(name)].setText(value);
    }
 
    public void setColorResult (String name, Color c)
    {
        resultFields[resultIndex(name)].setText(colorToString(c));
    }
 
    protected int paramIndex(String name)
    {
        for (int i = 0; i < paramNames.length; i++)
            if (name.equals(paramNames[i]))
                return i;

        throw new ParameterException("Parameter name \""
                                     + name + "\" not found!");
    }
 
    protected int resultIndex(String name)
    {
        for (int i = 0; i < resultNames.length; i++)
            if (name.equals(resultNames[i]))
                return i;

        throw new ParameterException("Parameter name \""
                                     + name + "\" not found!");
    }
 
    public static ColorEntry[] colorTable =
    {
        new ColorEntry("black", Color.black),
        new ColorEntry("blue", Color.blue),
        new ColorEntry("cyan", Color.cyan), 
        new ColorEntry("darkGray", Color.darkGray),
        new ColorEntry("gray", Color.gray),   
        new ColorEntry("green", Color.green), 
        new ColorEntry("lightGray", Color.lightGray),
        new ColorEntry("magenta", Color.magenta),   
        new ColorEntry("orange", Color.orange),    
        new ColorEntry("pink", Color.pink),
        new ColorEntry("red", Color.red),   
        new ColorEntry("white", Color.white),    
        new ColorEntry("yellow", Color.yellow)
    };
   
    public static Color stringToColor (String s)
    {
        for (int i = 0; i < colorTable.length; i++) {
            if (colorTable[i].name.equals(s)) 
                return colorTable[i].color;
        }
        throw new RuntimeException("Unknown color name: "  + s);
    }
 
    public static String colorToString (Color c)
    {
        for (int i = 0; i < colorTable.length; i++) {
            if (colorTable[i].color.equals(c)) 
                return colorTable[i].name;
        }
        throw new RuntimeException("Unknown color: "  + c);
    }
}

class ColorEntry
{
    public String name;
    public Color color;
  
    public ColorEntry (String s, Color c)
    {
        name = s;
        color = c;
    }
}

class ParameterException extends RuntimeException
{
    public ParameterException (String msg)
    {
        super(msg);
    }
}
