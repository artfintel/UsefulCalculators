#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
from math import pi, asin

class EnergyToBraggConverter:
    def __init__(self):
        print "Energy To Bragg Converter Init"

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(400,120)
        self.window.set_resizable(False)
        self.window.set_title("Energy to Bragg Converter")
        self.window.set_tooltip_text("Energy to Bragg Converter\n by FISH")

        self.box = gtk.VBox()

        #energy
        self.energyBox = gtk.HBox()

        self.label_energy = gtk.Label("Energy")
        self.label_energy.set_size_request(100,25)
        self.entry_energy = gtk.Entry()
        self.entry_energy.set_size_request(200,25)
        self.label_kev = gtk.Label("KeV")
        self.label_kev.set_size_request(100,25)
        
        self.energyBox.pack_start(self.label_energy)
        self.energyBox.pack_start(self.entry_energy)
        self.energyBox.pack_start(self.label_kev)

        #button
        self.buttonBox = gtk.HBox()

        self.calcButton = gtk.Button("Calculate")
        self.calcButton.connect("clicked", self.energyToBraggConverter)
        self.calcButton.set_size_request(100,30)
        self.resetButton = gtk.Button("reset")
        self.resetButton.set_size_request(100,30)
        self.resetButton.connect("clicked", self.reset)
    
        self.fixed = gtk.Fixed()
        self.fixed.put(self.calcButton,100,10)
        self.fixed.put(self.resetButton,200,10)

        self.buttonBox.pack_start(self.fixed)

        #bragg
        self.braggBox = gtk.HBox()
        self.label_bragg = gtk.Label("Bragg")
        self.label_bragg.set_size_request(100,25)
        self.entry_bragg = gtk.Entry()
        self.entry_bragg.set_size_request(200,25)
        self.label_degrees = gtk.Label("degrees")
        self.label_degrees.set_size_request(100,25)

        self.braggBox.pack_start(self.label_bragg)
        self.braggBox.pack_start(self.entry_bragg)
        self.braggBox.pack_start(self.label_degrees)


        self.box.pack_start(self.energyBox)
        self.box.pack_start(self.buttonBox)
        self.box.pack_start(self.braggBox)

        self.window.add(self.box)
       
        self.window.show_all()
        self.window.connect("destroy", self.destroy)

    def main(self):
        gtk.main()

    def destroy(self, widget, data=None):
        print "Energy To Bragg Converter Exit"
        gtk.main_quit()

    def reset(self, widget):
        self.entry_energy.set_text("")
        self.entry_bragg.set_text("")
        print "reset data"

    def energyToBraggConverter(self,widget):
        if self.entry_energy.get_text() == "":
            bragg = 0.0
        else:
            energyA = ((6.626068e-34 * 299792458) / (1.60217646e-16 * 1e-10)) / float(self.entry_energy.get_text())
            bragg = 180.0 / pi * asin(energyA / 6.2695)

        self.entry_bragg.set_text(str(bragg))

if __name__ == "__main__" :
    etbc = EnergyToBraggConverter()
    etbc.main()
