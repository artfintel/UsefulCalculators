#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

import misc

class XrayPhotonFlux:
    def __init__(self):
        print "X-Ray Photon Flux Calculator Init"
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(620,350)
        self.window.set_resizable(False)
        self.window.set_title("Xray Photon Flux Calculator")
        self.window.set_tooltip_text("Xray Photon Flux\n by FISH")

        self.box = gtk.VBox()
        
        #parameter box
        self.paraBox = gtk.VBox()

        #optional parameters label
        self.paraLabelBox = gtk.HBox()
        self.label_option = gtk.Label("Parameters")
        
        self.paraLabelBox.pack_start(self.label_option)

        #parameter :  Si Thickness
        self.siBox = gtk.HBox()

        self.label_SiThickness = gtk.Label("Thickness of Si diode")
        self.label_SiThickness.set_size_request(200,25)
        self.entry_SiThickness = gtk.Entry()
        self.entry_SiThickness.set_size_request(200,25)
        self.label_SiThicknessUnit = gtk.Label("microns")
        self.label_SiThicknessUnit.set_size_request(220,25)

        self.siBox.pack_start(self.label_SiThickness)
        self.siBox.pack_start(self.entry_SiThickness)
        self.siBox.pack_start(self.label_SiThicknessUnit)

        #parameter : Energy
        self.energyBox = gtk.HBox()

        self.label_Energy  = gtk.Label("Energy")
        self.label_Energy.set_size_request(200,25)
        self.entry_Energy =  gtk.Entry()
        self.entry_Energy.set_size_request(200,25)
        self.label_EnergyUnit = gtk.Label("KeV")
        self.label_EnergyUnit.set_size_request(220,25)

        self.energyBox.pack_start(self.label_Energy)
        self.energyBox.pack_start(self.entry_Energy)
        self.energyBox.pack_start(self.label_EnergyUnit)

        #parameter : Diode Current
        self.diodeBox = gtk.HBox()

        self.label_DiodeCurrent = gtk.Label("Diode Current")
        self.label_DiodeCurrent.set_size_request(200,25)
        self.entry_DiodeCurrent = gtk.Entry()
        self.entry_DiodeCurrent.set_size_request(200,25)
        self.label_DiodeCurrentUnit = gtk.Label("mA")
        self.label_DiodeCurrentUnit.set_size_request(220,25)

        self.diodeBox.pack_start(self.label_DiodeCurrent)
        self.diodeBox.pack_start(self.entry_DiodeCurrent)
        self.diodeBox.pack_start(self.label_DiodeCurrentUnit)

        #parameter : blank
        self.paraBlankBox = gtk.HBox()

        self.paraBox.pack_start(self.paraLabelBox)
        self.paraBox.pack_start(self.siBox)
        self.paraBox.pack_start(self.energyBox)
        self.paraBox.pack_start(self.diodeBox)
        self.paraBox.pack_start(self.paraBlankBox)


        #optional parameters
        self.optionBox = gtk.VBox()

        #optional parameters label
        self.optionLabelBox = gtk.HBox()
        self.label_option = gtk.Label("Optional parameters")
        
        self.optionLabelBox.pack_start(self.label_option)

        #optional parameters : Thickness of Al filter
        self.alBox = gtk.HBox()
        self.label_AlThickness = gtk.Label("Thickness of Al filter")
        self.label_AlThickness.set_size_request(200,25)
        self.entry_AlThickness = gtk.Entry()
        self.entry_AlThickness.set_size_request(200,25)
        self.label_AlThicknessUnit = gtk.Label("microns")
        self.label_AlThicknessUnit.set_size_request(220,25)

        self.alBox.pack_start(self.label_AlThickness)     
        self.alBox.pack_start(self.entry_AlThickness)     
        self.alBox.pack_start(self.label_AlThicknessUnit)     

        #optional parameters : Distance travelled in air
        self.distanceBox = gtk.HBox()
        self.label_Distance = gtk.Label("Distance travelled in air")
        self.label_Distance.set_size_request(200,25)
        self.entry_Distance = gtk.Entry()
        self.entry_Distance.set_size_request(200,25)
        self.label_DistanceUnit = gtk.Label("mm")
        self.label_DistanceUnit.set_size_request(220,25)

        self.distanceBox.pack_start(self.label_Distance)
        self.distanceBox.pack_start(self.entry_Distance)
        self.distanceBox.pack_start(self.label_DistanceUnit)

        #optional parameters : Blank
        self.optionBlankBox = gtk.HBox()

        self.optionBox.pack_start(self.optionLabelBox)
        self.optionBox.pack_start(self.alBox)
        self.optionBox.pack_start(self.distanceBox)
        self.optionBox.pack_start(self.optionBlankBox)

        #calc buttons
        self.buttonBox = gtk.VBox()
        self.buttonBox.set_size_request(600,25)

        self.calcButton = gtk.Button("Calculate")
        self.calcButton.connect("clicked", self.xrayPhotonFluxCalculation)
        self.calcButton.set_size_request(100,25)
        self.resetButton = gtk.Button("Reset")
        self.resetButton.set_size_request(100,25)
        #self.resetButton.set_alignment(10,10)
        self.resetButton.connect("clicked", self.reset)
    
        self.fixed = gtk.Fixed()
        self.fixed.put(self.calcButton,200,10)
        self.fixed.put(self.resetButton,300,10)

        self.buttonBox.pack_start(self.fixed)


        #result
        self.resultBox = gtk.VBox()        

        #result Label
        self.resultLabelBox = gtk.HBox()

        self.resultLabel = gtk.Label("Result")
        self.resultLabelBox.pack_start(self.resultLabel)

        #result : Calculated Photon Flux
        self.fluxBox = gtk.HBox()
        
        self.label_Flux = gtk.Label("Calculated Photon Flux")
        self.label_Flux.set_size_request(200,25)
        self.entry_Flux = gtk.Entry()
        self.entry_Flux.set_size_request(200,25)
        self.label_FluxUnit = gtk.Label("x10^12 Photons per second")
        self.label_FluxUnit.set_size_request(220,25)

        self.fluxBox.pack_start(self.label_Flux)
        self.fluxBox.pack_start(self.entry_Flux)
        self.fluxBox.pack_start(self.label_FluxUnit)

        #result : Absorbed Dose
        self.doseBox = gtk.HBox()

        self.label_AbsorbedDose = gtk.Label("Absorbed Dose")
        self.label_AbsorbedDose.set_size_request(200,25)
        self.entry_AbsorbedDose = gtk.Entry()
        self.entry_AbsorbedDose.set_size_request(200,25)
        self.label_AbsorbedDoseUnit = gtk.Label("Gray per second")
        self.label_AbsorbedDoseUnit.set_size_request(220,25)

        self.doseBox.pack_start(self.label_AbsorbedDose)
        self.doseBox.pack_start(self.entry_AbsorbedDose)
        self.doseBox.pack_start(self.label_AbsorbedDoseUnit)
 
        #result : Time to Henderson Limit
        self.hendersonBox = gtk.HBox()

        self.label_Henderson = gtk.Label("Time to Henderson Limit")
        self.label_Henderson.set_size_request(200,25)
        self.entry_Henderson = gtk.Entry()
        self.entry_Henderson.set_size_request(200,25)
        self.label_HendersonUnit = gtk.Label("seconds")
        self.label_HendersonUnit.set_size_request(220,25)

        self.hendersonBox.pack_start(self.label_Henderson)
        self.hendersonBox.pack_start(self.entry_Henderson)
        self.hendersonBox.pack_start(self.label_HendersonUnit)


        self.resultBox.pack_start(self.resultLabelBox)
        self.resultBox.pack_start(self.fluxBox)
        self.resultBox.pack_start(self.doseBox)
        self.resultBox.pack_start(self.hendersonBox)


        self.box.pack_start(self.paraBox)
        self.box.pack_start(self.optionBox)
        self.box.pack_start(self.buttonBox)
        self.box.pack_start(self.resultBox)


        self.window.add(self.box)
        
        self.entry_SiThickness.set_text("300")
        self.entry_Energy.set_text("12.659")
        self.entry_DiodeCurrent.set_text("1.0")
        self.entry_AlThickness.set_text("0.0")
        self.entry_Distance.set_text("0.0")
        self.entry_Flux.set_text("")
        self.entry_AbsorbedDose.set_text("")
        self.entry_Henderson.set_text("")
 
        self.window.show_all()
        self.window.connect("destroy", self.destroy)

    def main(self):
        gtk.main()

    def destroy(self, widget, data=None):
        print "X-Ray Photon Flux Calculator Exit"
        gtk.main_quit()

    def reset(self, widget):
        self.entry_SiThickness.set_text("300")
        self.entry_Energy.set_text("12.659")
        self.entry_DiodeCurrent.set_text("1.0")
        self.entry_AlThickness.set_text("0.0")
        self.entry_Distance.set_text("0.0")
        self.entry_Flux.set_text("")
        self.entry_AbsorbedDose.set_text("")
        self.entry_Henderson.set_text("")
        print "reset data"

    def xrayPhotonFluxCalculation(self,widget):

        flux, dose, henderson = misc.xrayPhotonFluxCalc(self.entry_Energy.get_text(), self.entry_DiodeCurrent.get_text(), self.entry_SiThickness.get_text(), self.entry_AlThickness.get_text(), self.entry_Distance.get_text() )
   
        self.entry_Flux.set_text(str(flux))
        self.entry_AbsorbedDose.set_text(str(dose))
        self.entry_Henderson.set_text(str(henderson))
 

if __name__ == "__main__" :
    xpf = XrayPhotonFlux()
    xpf.main()
