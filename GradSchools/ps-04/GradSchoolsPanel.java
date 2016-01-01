import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.lang.*;

/* The user can then click on the tab to Add Schools. She can enter the name of a school and select 
 * three numbers from pull-down menus 
 * 
 When the user clicks the "Add School" button, the information is entered and a message appears at the bottom panel announcing what the program read. 
 (Or, better, the latest school is added on top of the other schools that have already been entered before...) 
 If the user did not provide all the data needed to Add a School, 
 an appropriate message will advise the user.
 
 A few hints could be very useful here:
 
 * Important: You may not need to alter School.java or GradSchools.java in order to complete this task, 
 * though you need to include them in the same directory as your GUI program.
 */

public class GradSchoolsPanel extends JPanel {
  
  
  //instance variables
  private GradSchools grad;
  private JButton addSchool;
  private JTextField name;
  private JComboBox publications,academics,research;
  private Integer[] ranks;
  private JTextArea database;
  
  public GradSchoolsPanel(GradSchools g){
    setBackground(Color.orange);
    grad = g;
    ranks = new Integer[]{1,2,3,4,5};
    
    database = new JTextArea(grad.toString());
    database.setEditable(false);
    JScrollPane sp = new JScrollPane(database);
    
    
    JLabel b1 = new JLabel("Fill in the information for a new school and click 'Add School'");
    b1.setAlignmentX (Component.CENTER_ALIGNMENT);
    name = new JTextField(10);
    
    setLayout (new BoxLayout (this, BoxLayout.Y_AXIS));
    add(b1);
    add(addSchoolPanel());
    add(sp);
    
  }
  
  public JPanel addSchoolPanel(){
    JPanel school = new JPanel();
    school.setBackground(Color.orange);
    school.setLayout(new FlowLayout ());
    name.setPreferredSize(new Dimension(150,20));
    addSchoolButton().setPreferredSize(new Dimension(150,20));
    academics = new JComboBox(ranks);
    research = new JComboBox(ranks);
    publications = new JComboBox(ranks);
    
    
    
    school.add(name);
    school.add(academics);
    school.add(research);
    school.add(publications);
    school.add(addSchoolButton());
    return school;
  }
  
  public JButton addSchoolButton(){
    addSchool = new JButton("Add School");
    addSchool.addActionListener(new ButtonListener());
    return addSchool;
  }
  
  public class ButtonListener implements ActionListener{
    public void actionPerformed (ActionEvent event){
      if(event.getSource() == addSchool){
        grad.addSchool(name.getText(),ranks[academics.getSelectedIndex()], ranks[research.getSelectedIndex()],ranks[publications.getSelectedIndex()]);
        System.out.println(grad.toString());
        database.setText(grad.toString());
      }
    }
  }
  
}