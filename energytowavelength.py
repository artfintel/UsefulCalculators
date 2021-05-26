#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

import misc

class EnergyToWavelengthConverter:
    def __init__(self):
        print "Energy To Wavelength Converter Init"
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(400,120)
        self.window.set_resizable(False)
        self.window.set_title("Energy to Wavelength Converter")
        self.window.set_tooltip_text("Energy to Wavelength Converter\n by FISH")

        self.box = gtk.VBox()

        #energy
        self.energyBox = gtk.HBox()

        self.label_Energy = gtk.Label("Energy")
        self.label_Energy.set_size_request(100,25)
        self.entry_Energy = gtk.Entry()
        self.entry_Energy.set_text("12.659")
        self.entry_Energy.set_size_request(200,25)
        self.label_EnergyUnit = gtk.Label("KeV")
        self.label_EnergyUnit.set_size_request(100,25)

        self.energyBox.pack_start(self.label_Energy)
        self.energyBox.pack_start(self.entry_Energy)
        self.energyBox.pack_start(self.label_EnergyUnit)

        #button
        self.buttonBox = gtk.HBox()

        self.calcButton = gtk.Button("Calculate")
        self.calcButton.connect("clicked", self.energyToWavelengthConverter)
        self.calcButton.set_size_request(100,30)
        self.resetButton = gtk.Button("reset")
        self.resetButton.set_size_request(100,30)
        self.resetButton.connect("clicked", self.reset)
    
        self.fixed = gtk.Fixed()
        self.fixed.put(self.calcButton,100,10)
        self.fixed.put(self.resetButton,200,10)
 
        self.buttonBox.pack_start(self.fixed)

        #wavelength
        self.wavelengthBox = gtk.HBox()

        self.label_Wavelength = gtk.Label("Wavelength")
        self.label_Wavelength.set_size_request(100,25)
        self.entry_Wavelength = gtk.Entry()
        self.entry_Wavelength.set_size_request(200,25)
        self.label_WavelengthUnit = gtk.Label("A")
        self.label_WavelengthUnit.set_size_request(100,25)

        self.wavelengthBox.pack_start(self.label_Wavelength)
        self.wavelengthBox.pack_start(self.entry_Wavelength)
        self.wavelengthBox.pack_start(self.label_WavelengthUnit)

        self.entry_Energy.set_text("12.659")
        self.entry_Wavelength.set_text("")

        self.box.pack_start(self.energyBox)
        self.box.pack_start(self.buttonBox)
        self.box.pack_start(self.wavelengthBox)

        self.window.add(self.box)
       
        self.window.show_all()
        self.window.connect("destroy", self.destroy)

    def main(self):
        gtk.main()

    def destroy(self, widget, data=None):
        print "Energy To Wavelength Converter Exit"
        gtk.main_quit()

    def reset(self, widget):
        self.entry_Energy.set_text("12.659")
        self.entry_Wavelength.set_text("")
        print "reset data"

    def energyToWavelengthConverter(self,widget):
        wavelength = misc.energyToWavelength(self.entry_Energy.get_text())
        
        self.entry_Wavelength.set_text(str(wavelength))

if __name__ == "__main__" :
    etwc = EnergyToWavelengthConverter()
    etwc.main()
