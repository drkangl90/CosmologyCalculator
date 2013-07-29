#!/usr/local/bin/jython
# -*- coding: utf-8 -*-

# SWING imports
from java.awt       import *
from java.awt.event import *

from javax.swing     import *

# Calculator imports
from cosmo import *

class Calculator_GUI(JFrame, ActionListener):

    def __init__(self):
        super(Calculator_GUI, self).__init__()

        self.init_UI()

    def init_UI(self):
        # Build Components
        a_label = JLabel("A:", JLabel.CENTER)
        b_label = JLabel("B:", JLabel.CENTER)
        c_label = JLabel("C:", JLabel.CENTER)
        self.a_field = TextField()
        self.b_field = TextField()
        self.c_field = TextField()
        self.c_field.setEditable(False)

        enter_btn = JButton("Calculate")
        enter_btn.addActionListener(self)

        a_panel = JPanel()
        a_panel.setLayout(GridLayout(1, 2))
        a_panel.add(a_label)
        a_panel.add(self.a_field)

        b_panel = JPanel()
        b_panel.setLayout(GridLayout(1, 2))
        b_panel.add(b_label)
        b_panel.add(self.b_field)

        c_panel = JPanel()
        c_panel.setLayout(GridLayout(1, 2))
        c_panel.add(c_label)
        c_panel.add(self.c_field)

        self.setLayout(GridLayout(4, 1))
        self.add(a_panel)    
        self.add(b_panel)
        self.add(c_panel)
        self.add(enter_btn)    

    def launch_UI(self):
        # Master Assembly
        self.setTitle("Cosmology Calculator")
        self.setSize(750, 500)
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setLocationRelativeTo(None)
        self.setVisible(True)

    def actionPerformed(self, event):
        a = int(self.a_field.getText())
        b = int(self.b_field.getText())
        self.c_field.setText(str(dirks_example_calc(a, b)))


Calculator_GUI().launch_UI()