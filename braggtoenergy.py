#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

import misc

class BraggToEnergyConverter:
    def __init__(self):
        print "Bragg To Energy Converter Init"

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        #self.window.set_position(gtk.WIN_POS_MOUSE)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(400,120)
        self.window.set_resizable(False)
        self.window.set_title("Bragg To Energy Converter")
        self.window.set_tooltip_text("Bragg To Energy Converter\n by FISH")

        self.box = gtk.VBox()

        #bragg
        self.braggBox = gtk.HBox()

        self.label_bragg = gtk.Label("Bragg")
        self.label_bragg.set_size_request(100,25)
        self.entry_bragg = gtk.Entry()
        self.entry_bragg.set_size_request(200,25)
        self.label_braggUnit = gtk.Label("degrees")
        self.label_braggUnit.set_size_request(100,25)
        
        self.braggBox.pack_start(self.label_bragg)
        self.braggBox.pack_start(self.entry_bragg)
        self.braggBox.pack_start(self.label_braggUnit)
  
        #button
        self.buttonBox = gtk.HBox()
        
        self.calcButton = gtk.Button("Calculate")
        self.calcButton.connect("clicked", self.braggToEnergyConverter)
        self.calcButton.set_size_request(100,30)
        self.resetButton = gtk.Button("reset")
        self.resetButton.set_size_request(100,30)
        self.resetButton.connect("clicked", self.reset)
    
        self.fixed = gtk.Fixed()
        self.fixed.put(self.calcButton,100,10)
        self.fixed.put(self.resetButton,200,10)

        self.buttonBox.pack_start(self.fixed)

        self.energyBox = gtk.HBox()
        self.label_energy = gtk.Label("Energy")
        self.label_energy.set_size_request(100,25)
        self.entry_energy = gtk.Entry()
        self.entry_energy.set_size_request(200,25)
        self.label_energyUnit = gtk.Label("KeV")
        self.label_energyUnit.set_size_request(100,25)

        self.energyBox.pack_start(self.label_energy)
        self.energyBox.pack_start(self.entry_energy)
        self.energyBox.pack_start(self.label_energyUnit)

        self.entry_bragg.set_text("8.98750286391")
        self.entry_energy.set_text("")

        self.box.pack_start(self.braggBox)
        self.box.pack_start(self.buttonBox)
        self.box.pack_start(self.energyBox)

        self.window.add(self.box)
       
        self.window.show_all()
        self.window.connect("destroy", self.destroy)

    def main(self):
        gtk.main()

    def destroy(self, widget, data=None):
        print "Bragg To Enery Converter Exit"
        gtk.main_quit()

    def reset(self, widget):
        self.entry_bragg.set_text("8.98750286391")
        self.entry_energy.set_text("")
        print "reset data"

    def braggToEnergyConverter(self,widget):
        energy = misc.braggToEnergy(self.entry_bragg.get_text())

        self.entry_energy.set_text(str(energy))

if __name__ == "__main__" :
    btec = BraggToEnergyConverter()
    btec.main()
