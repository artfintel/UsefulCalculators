#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

import misc

class DistanceCalculator:
    def __init__(self):
        print "Distance Calculator Init"

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        #self.window.set_position(gtk.WIN_POS_MOUSE)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(450,120)
        self.window.set_resizable(False)
        self.window.set_title("Distance Calculator")
        self.window.set_tooltip_text("Distance Calculator\n by FISH")

        self.box = gtk.VBox()
        
        #parameter
        self.parameterBox = gtk.VBox()

        #energyBox
        self.energyBox = gtk.HBox()
        self.label_energy = gtk.Label("Energy")
        self.label_energy.set_size_request(200,25)
        self.entry_energy = gtk.Entry()
        self.entry_energy.set_size_request(200,25)
        self.label_energyUnit = gtk.Label("KeV")
        self.label_energyUnit.set_size_request(50,25)

        self.energyBox.pack_start(self.label_energy)
        self.energyBox.pack_start(self.entry_energy)
        self.energyBox.pack_start(self.label_energyUnit)

        #Max Resolution
        self.resolutionBox = gtk.HBox()
        self.label_MaxResolution = gtk.Label("Max Resolution")
        self.label_MaxResolution.set_size_request(200,25)
        self.entry_MaxResolution = gtk.Entry()
        self.entry_MaxResolution.set_size_request(200,25)
        self.label_MaxResolutionUnit = gtk.Label("A")
        self.label_MaxResolutionUnit.set_size_request(50,25)

        self.resolutionBox.pack_start(self.label_MaxResolution)
        self.resolutionBox.pack_start(self.entry_MaxResolution)
        self.resolutionBox.pack_start(self.label_MaxResolutionUnit)

        self.parameterBox.pack_start(self.energyBox)
        self.parameterBox.pack_start(self.resolutionBox)

    
        #button
        self.buttonBox = gtk.HBox()
        self.buttonBox.set_size_request(450,30)
        self.calcButton = gtk.Button("Calculate")
        self.calcButton.connect("clicked", self.distanceCalculator)
        self.calcButton.set_size_request(100,25)
        self.resetButton = gtk.Button("reset")
        self.resetButton.set_size_request(100,25)
        #self.resetButton.set_alignment(10,10)
        self.resetButton.connect("clicked", self.reset)

        self.fixed = gtk.Fixed()
        self.fixed.put(self.calcButton,200,10)
        self.fixed.put(self.resetButton,300,10)
   
        self.buttonBox.pack_start(self.fixed)

        #Result
        self.resultBox = gtk.HBox()
        self.resultBox.set_size_request(450,30)
        self.label_Distance = gtk.Label("Distance")
        self.label_Distance.set_size_request(200,25)
        self.entry_Distance = gtk.Entry()
        self.entry_Distance.set_size_request(200,25)
        self.label_DistanceUnit = gtk.Label("mm")
        self.label_DistanceUnit.set_size_request(50,25)

        self.resultBox.pack_start(self.label_Distance)
        self.resultBox.pack_start(self.entry_Distance)
        self.resultBox.pack_start(self.label_DistanceUnit)


        self.box.pack_start(self.parameterBox)
        self.box.pack_start(self.buttonBox)
        self.box.pack_start(self.resultBox)

        self.entry_energy.set_text("12.659")
        self.entry_MaxResolution.set_text("")

        self.window.add(self.box)
       
        self.window.show_all()
        self.window.connect("destroy", self.destroy)

    def main(self):
        gtk.main()

    def destroy(self, widget, data=None):
        print "Distance Calculator Exit"
        gtk.main_quit()

    def reset(self, widget):
        self.entry_energy.set_text("12.659")
        self.entry_MaxResolution.set_text("")
        self.entry_Distance.set_text("")
        print "reset data"

    def distanceCalculator(self,widget):
        distance = misc.distanceCalc(self.entry_energy.get_text(), self.entry_MaxResolution.get_text())

        self.entry_Distance.set_text(str(distance))

if __name__ == "__main__" :
    dc = DistanceCalculator()
    dc.main()
