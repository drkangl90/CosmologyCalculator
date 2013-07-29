#!/usr/local/bin/jython
# -*- coding: utf-8 -*-

# SWING imports
from java.awt       import *
from java.awt.event import *

from javax.swing    import *

# Calculator imports
from cosmo import *

class Calculator_GUI(JFrame, ActionListener):

    def __init__(self):
        super(Calculator_GUI, self).__init__()

        self.init_components()
        self.init_UI()

    def init_components(self):
        self.openUniverse_btn = JButton("Open")
        self.openUniverse_btn.addActionListener(self)
        self.flatUniverse_btn = JButton("Flat")
        self.flatUniverse_btn.addActionListener(self)
        self.generalUniverse_btn = JButton("General")
        self.generalUniverse_btn.addActionListener(self)

        self.labels = {}
        self.fields = {}

        self.labels[0] = JLabel("H_0: ", JLabel.RIGHT)
        self.fields[0] = JTextField()
        self.fields[0].setText("0.71")

        self.labels[1] = JLabel("Omega_M: ", JLabel.RIGHT)
        self.fields[1] = JTextField()
        self.fields[1].setText("0.27")

        self.labels[2] = JLabel("RedShift: ", JLabel.RIGHT)
        self.fields[2] = JTextField()
        self.fields[2].setText("3.00")

        self.labels[3] = JLabel("Mnu(e): ", JLabel.RIGHT)
        self.fields[3] = JTextField()
        self.fields[3].setText("0.001")

        self.labels[4] = JLabel("Mnu(mu): ", JLabel.RIGHT)
        self.fields[4] = JTextField()
        self.fields[4].setText("0.009")

        self.labels[5] = JLabel("Mnu(tau): ", JLabel.RIGHT)
        self.fields[5] = JTextField()
        self.fields[5].setText("0.049")

        self.labels[6] = JLabel("w: ", JLabel.RIGHT)
        self.fields[6] = JTextField()
        self.fields[6].setText("-1")

        self.labels[7] = JLabel("w': ", JLabel.RIGHT)
        self.fields[7] = JTextField()
        self.fields[7].setText("0")

        self.labels[8] = JLabel("T_0: ", JLabel.RIGHT)
        self.fields[8] = JTextField()
        self.fields[8].setText("2.72528")

        self.labels[9] = JLabel("Omega_DE: ", JLabel.RIGHT)
        self.fields[9] = JTextField()
        self.fields[9].setText("0.73")

    def init_UI(self):
        input_panel = JPanel()
        input_panel.setLayout(GridLayout(12, 1))

        for i in range(10):
            panel = JPanel()
            panel.setLayout(GridLayout(1, 2))
            panel.add(self.labels[i])
            panel.add(self.fields[i])

            input_panel.add(panel)

        panel = JPanel()
        panel.setLayout(GridLayout(1, 2))
        panel.add(self.openUniverse_btn)
        panel.add(self.flatUniverse_btn)
        input_panel.add(panel)
        input_panel.add(self.generalUniverse_btn)

        self.setLayout(GridLayout(1, 2))
        self.add(input_panel)
        self.add(JLabel("< RESULTS >", JLabel.CENTER))

    def launch_UI(self):
        # Master Assembly
        self.setTitle("Cosmology Calculator")
        self.setSize(300, 500)
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setLocationRelativeTo(None)
        self.setVisible(True)

    def actionPerformed(self, event):
        h = float(self.fields[0].getText())
        o_m = float(self.fields[0].getText())
        z = float(self.fields[0].getText())
        mnu_e = float(self.fields[0].getText())
        mnu_mu = float(self.fields[0].getText())
        mnu_tau = float(self.fields[0].getText())
        w = float(self.fields[0].getText())
        dw = float(self.fields[0].getText())
        t = float(self.fields[0].getText())
        o_de = float(self.fields[0].getText())

        calculatronamaton(h, o_m, z, mnu_e, mnu_mu, mnu_tau, w, dw, t, o_de, "general")

# LAUNCH
if __name__ == '__main__':
    Calculator_GUI().launch_UI()