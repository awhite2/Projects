import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

/*The Evaluate tab.
When the user is done entering (some of) the schools, 
she can move on to the second tab to evaluate the schools in the overall category.
For example, when the user selects 3, 4, 5 for weights in the three categories, 
the GUI displays the top school in the label that now says "Use this slider..." 
(Or, better, prints a table-like listing of the top 3 schools, one per line.)
*/

public class EvalSchoolsPanel extends JPanel {
  private JSlider rSlider, pSlider, aSlider;
  private GradSchools grad;
  private JTextArea schools;
  private JLabel rLabel,aLabel,pLabel,ynLabel;
  
  public EvalSchoolsPanel(GradSchools g){
    setBackground(Color.orange);
    
    grad = g;
    schools = new JTextArea("");
    schools.setEditable(false);
    
    rSlider = new JSlider (JSlider.HORIZONTAL, 0, 5, 0);
    rSlider.setMajorTickSpacing (1);
    rSlider.setPaintTicks (true);
    rSlider.setPaintLabels (true);
    rSlider.setAlignmentX (Component.LEFT_ALIGNMENT);
    
    pSlider = new JSlider (JSlider.HORIZONTAL, 0, 5, 0);
    pSlider.setMajorTickSpacing (1);
    pSlider.setPaintTicks (true);
    pSlider.setPaintLabels (true);
    pSlider.setAlignmentX (Component.LEFT_ALIGNMENT);
    
    aSlider = new JSlider (JSlider.HORIZONTAL, 0, 5, 0);
    aSlider.setMajorTickSpacing (1);
    aSlider.setPaintTicks (true);
    aSlider.setPaintLabels (true);
    aSlider.setAlignmentX (Component.LEFT_ALIGNMENT);
    
    rLabel = new JLabel ("Research:");
    rLabel.setAlignmentX (Component.LEFT_ALIGNMENT);
    pLabel = new JLabel ("Publications:");
    pLabel.setAlignmentX (Component.LEFT_ALIGNMENT);
    aLabel = new JLabel ("Academics:");
    aLabel.setAlignmentX (Component.LEFT_ALIGNMENT);
    
    
//    
    SliderListener listener = new SliderListener();
    rSlider.addChangeListener(listener);
    pSlider.addChangeListener(listener);
    aSlider.addChangeListener(listener);
    
    

//    
    add(sliderPanel());
    add(schools);
    
  }
  public JPanel sliderPanel(){
    JPanel slider = new JPanel();
    BoxLayout layout = new BoxLayout (slider, BoxLayout.X_AXIS);
    add(rLabel);
    add(rSlider);
    add(pLabel);
    add(pSlider);
    add(aLabel);
    add(aSlider);
    return slider;
  }
  
  public class SliderListener implements ChangeListener{
    public void stateChanged (ChangeEvent event)
    {
      grad.computeRatings(aSlider.getValue(), rSlider.getValue(), pSlider.getValue());
      grad.rankSchools("Overall");
      schools.setText("Top School: "+ grad.getTop().toString());
      System.out.println("Top School: "+ grad.getTop().toString());
    }
  }

  
  
}