#!/usr/bin/env python

from math import tan, asin, sin, atan, exp,log, pi
import ConfigParser
import os

def get_detectorDiameter() :

    detectorDiameter = 0

    base_dir = os.path.dirname(os.path.abspath(__file__))
    config = ConfigParser.ConfigParser()
    config.read(base_dir + '/config.ini')

    beamline = config.get('DEFAULT','BEAMLINE')

    if beamline == "bl5c" : 
        detectorDiameter = config.get('BL5C','DETECTOR_DIAMETER')

    elif beamline == "bl11c" :
        detectorDiameter = config.get('BL11C','DETECTOR_DIAMETER')
    
    return detectorDiameter
    
def distanceCalc(energy, max_resolution):
    if energy == ""  or max_resolution == "" :
        distance = "NaN"
    else:
        wavelength = energyToWavelength(energy)
        distance = int(get_detectorDiameter()) / (2*tan (2* asin( float(wavelength)/(2*float(max_resolution)) )))

    return distance

def resolutionCalc(energy, distance):

    if energy == "" or distance == "" :
        max_resolution = "0"
    else:
        wavelength = energyToWavelength(energy)
        max_resolution = float(wavelength) / (sin (atan ((int(get_detectorDiameter())/2)/(float(distance)*1.0))/2)*2)

    return max_resolution

def wavelengthToEnergy(wavelength):
    if wavelength == "":
        energy = "infinity"
    else:
        energy = 6.626068e-34 * 299792458 / float(wavelength) / 1e-10 / 1.60217653e-16
 
    return energy

def energyToWavelength(energy):
    if energy == "":
        wavelength ="infinity"
    else:
        wavelength = (6.626068e-34 * 299792458 / (float(energy) * 1.60217653e-16)) / 1e-10

    return wavelength

def braggToEnergy(bragg):
    if bragg == "":
        energy = "infinity"
    else:
        energyA = 6.2695 * sin(float(bragg) * pi / 180)
        energy = (6.626068e-34 * 299792458) / (energyA * 1e-10 * 1.60217646e-16)

    return energy

def energyToBragg(energy):
    if energy == "":
        bragg = 0.0
    else:
        energyA = ((6.626068e-34 * 299792458) / (1.60217646e-16 * 1e-10)) / float(energy)
        bragg = 180.0 / pi * asin(energyA / 6.2695)

    return bragg

def xrayPhotonFluxCalc(s_energy, s_diodeCurrent, s_siThickness, s_alThickness, s_distance):

    if s_energy == "" or s_diodeCurrent == "" or s_siThickness == "" or s_alThickness == "" or s_distance == "" :
        return "NaN", "NaN", "NaN" 


    energy = float(s_energy)
    diodeCurrent = float(s_diodeCurrent)
    siThickness = float(s_siThickness)
    alThickness = float(s_alThickness)
    distance = float(s_distance)

    logEnergy = (log(energy) / log(10))
    logEnergyPow2 = pow(logEnergy, 2)
    logEnergyPow3 = pow(logEnergy, 3)

    flux = (((diodeCurrent * 3.62) * pow(10, 13) / (energy * 1.602)) * (1 / (1 - exp(-2.330 * siThickness * (pow(10, (4.158 - 2.238 * logEnergy - 0.477 * logEnergyPow2 + 0.0789 * logEnergyPow3))) / 10000))) * (1 / (exp(-2.699 * alThickness * (pow(10, (4.106 - 2.349 * logEnergy - 0.413 * logEnergyPow2 + 0.0638 * logEnergyPow3))) / 10000))) * (1 / (exp(-0.001205 * distance * (pow(10, (3.153 - 1.026 * logEnergy - 2.348 * logEnergyPow2 + 0.928 * logEnergyPow3))) / 10))) / 1000000000000)

    dose = 20000000 / ((((diodeCurrent * 3.62) * pow(10, 13) / (energy * 1.602))*( 1/ (1-exp(-2.330 * siThickness * (pow(10,(4.158 - 2.238 * (logEnergy) - 0.477 * logEnergyPow2 + 0.0789 * logEnergyPow3))) / 10000)))*( 1 / (exp(-2.699 * alThickness * (pow(10,(4.106 - 2.349 * (logEnergy) - 0.413 * logEnergyPow2 + 0.0638 * logEnergyPow3))) / 10000)))*( 1 / (exp(-0.001205 * distance * (pow(10,(3.153 - 1.026 * (logEnergy) - 2.348 * logEnergyPow2 + 0.928 * logEnergyPow3))) / 10))))*( 0.016 + 0.947056 * exp(-energy / 3.56)) / 1000000)

    henderson = ((((diodeCurrent*3.62) * pow(10, 13) / (energy * 1.602))*( 1 / (1-exp(-2.330 * siThickness * (pow(10,(4.158-2.238 * (logEnergy) - 0.477 * logEnergyPow2 + 0.0789 * logEnergyPow3))) / 10000)))*( 1 / (exp(-2.699 * alThickness * (pow(10,(4.106-2.349 * (logEnergy) - 0.413 * logEnergyPow2 + 0.0638 * logEnergyPow3))) / 10000)))*( 1 / (exp(-0.001205 * distance * (pow(10,(3.153-1.026 * (logEnergy) - 2.348 * logEnergyPow2 + 0.928 * logEnergyPow3))) / 10)))) * (0.016 + 0.947056 * exp(-energy / 3.56)) / 1000000)

    return flux, dose, henderson

