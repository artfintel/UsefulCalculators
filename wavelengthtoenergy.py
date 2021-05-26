#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

import misc

class WavelengthToEnergyConverter:
    def __init__(self):
        print "Wavelength to Energy Converteri Init"
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        #self.window.set_position(gtk.WIN_POS_MOUSE)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(400,120)
        self.window.set_resizable(False)
        self.window.set_title("Wavelength To Energy Converter")
        self.window.set_tooltip_text("Wavelength To Energy Converter\n by FISH")

        self.box = gtk.VBox()

        #wavelength
        self.wavelengthBox = gtk.HBox()

        self.label_Wavelength = gtk.Label("Wavelength")
        self.label_Wavelength.set_size_request(100,25)
        self.entry_Wavelength = gtk.Entry()
        self.entry_Wavelength.set_text("0.97941516906")
        self.entry_Wavelength.set_size_request(200,25)
        self.label_WavelengthUnit = gtk.Label("A")
        self.label_WavelengthUnit.set_size_request(100,25)

        self.wavelengthBox.pack_start(self.label_Wavelength)
        self.wavelengthBox.pack_start(self.entry_Wavelength)
        self.wavelengthBox.pack_start(self.label_WavelengthUnit)

        #button
        self.buttonBox = gtk.HBox()

        self.calcButton = gtk.Button("Calculate")
        self.calcButton.connect("clicked", self.wavelengthToEnergyConverter)
        self.calcButton.set_size_request(100,30)
        self.resetButton = gtk.Button("reset")
        self.resetButton.set_size_request(100,30)
        #self.resetButton.set_alignment(10,10)
        self.resetButton.connect("clicked", self.reset)
    
        self.fixed = gtk.Fixed()
        self.fixed.put(self.calcButton,50,10)
        self.fixed.put(self.resetButton,150,10)

        self.buttonBox.pack_start(self.fixed)

        #Energy
        self.energyBox = gtk.HBox()

        self.label_Energy = gtk.Label("Energy")
        self.label_Energy.set_size_request(100,25)
        self.entry_Energy = gtk.Entry()
        self.entry_Energy.set_size_request(200,25)
        self.label_EnergyUnit = gtk.Label("KeV")
        self.label_EnergyUnit.set_size_request(100,25)

        self.energyBox.pack_start(self.label_Energy)
        self.energyBox.pack_start(self.entry_Energy)
        self.energyBox.pack_start(self.label_EnergyUnit)

        self.entry_Wavelength.set_text("0.97941516906")
        self.entry_Energy.set_text("")

        self.box.pack_start(self.wavelengthBox)
        self.box.pack_start(self.buttonBox)
        self.box.pack_start(self.energyBox)

        self.window.add(self.box)
       
        self.window.show_all()
        self.window.connect("destroy", self.destroy)

    def main(self):
        gtk.main()

    def destroy(self, widget, data=None):
        print "Wavelength To Energy Converter Exit"
        gtk.main_quit()

    def reset(self, widget):
        self.entry_Wavelength.set_text("0.97941516906")
        self.entry_Energy.set_text("")
        print "reset data"

    def wavelengthToEnergyConverter(self,widget):
        energy =  misc.wavelengthToEnergy(self.entry_Wavelength.get_text())

        self.entry_Energy.set_text(str(energy))

if __name__ == "__main__" :
    wtec = WavelengthToEnergyConverter()
    wtec.main()
