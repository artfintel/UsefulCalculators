#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk


import distanceCalc,resolutionCalc,wavelengthtoenergy,energytowavelength,braggtoenergy,energytobragg,xrayPhotonFlux

class UsefulCalculators:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        #self.window.set_position(gtk.WIN_POS_MOUSE)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(400,400)
        self.window.set_resizable(False)
        self.window.set_title("Useful Calculators v1.1")
        self.window.set_tooltip_text("Useful Calculators\n by FISH")

        self.box = gtk.VBox()

        #button
        self.distanceButton = gtk.Button("Distance Calculator")
        self.distanceButton.connect("clicked", self.distanceCalc)

        self.resolutionButton = gtk.Button("Resolution Calculator")
        self.resolutionButton.connect("clicked", self.resolutionCalc)

        self.wavelengthToEnergyButton = gtk.Button("Wavelength to Energy Converter")
        self.wavelengthToEnergyButton.connect("clicked", self.wavelengthToEnergyConverter)

        self.energyToWavelengthButton = gtk.Button("Energy to Wavelength Converter")
        self.energyToWavelengthButton.connect("clicked", self.energyToWavelengthConverter)

        self.braggToEnergyButton = gtk.Button("Bragg to Energy Converter")
        self.braggToEnergyButton.connect("clicked", self.braggToEnergyConverter)

        self.energyToBraggButton = gtk.Button("Energy to Bragg Converter")
        self.energyToBraggButton.connect("clicked", self.energyToBraggConverter)

        self.xrayPhotonFluxButton = gtk.Button("X-ray Photon Flux Calculator")
        self.xrayPhotonFluxButton.connect("clicked", self.xrayPhotonFluxCalc)

        self.exitButton = gtk.Button("Exit")
        self.exitButton.connect("clicked", self.destroy)

        self.box.pack_start(self.distanceButton)    
        self.box.pack_start(self.resolutionButton)    
        self.box.pack_start(self.wavelengthToEnergyButton)    
        self.box.pack_start(self.energyToWavelengthButton)    
        self.box.pack_start(self.braggToEnergyButton)    
        self.box.pack_start(self.energyToBraggButton)    
        self.box.pack_start(self.xrayPhotonFluxButton) 
        self.box.pack_start(self.exitButton)   

        self.window.add(self.box)
       
        self.window.show_all()
        self.window.connect("destroy", self.destroy)

    def main(self):
        gtk.main()

    def destroy(self, widget, data=None):
        print "Useful Calculator Exit"
        gtk.main_quit()
 
    def distanceCalc(self,widget):
        dist = distanceCalc.DistanceCalculator()
        dist.main()

    def resolutionCalc(self,widget):
        resol = resolutionCalc.ResolutionCalculator()
        resol.main()

    def wavelengthToEnergyConverter(self,widget):
        wtec = wavelengthtoenergy.WavelengthToEnergyConverter()
        wtec.main()

    def energyToWavelengthConverter(self,widget):
        etwc = energytowavelength.EnergyToWavelengthConverter()
        etwc.main()

    def braggToEnergyConverter(self,widget):
        btec = braggtoenergy.BraggToEnergyConverter()
        btec.main()

    def energyToBraggConverter(self,widget):
        etbc = energytobragg.EnergyToBraggConverter()
        etbc.main()

    def xrayPhotonFluxCalc(self,widget):
        xpfc = xrayPhotonFlux.XrayPhotonFlux()
        xpfc.main()

if __name__ == "__main__" :
    uc  = UsefulCalculators()
    uc.main()
