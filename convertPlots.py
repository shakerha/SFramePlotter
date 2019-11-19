#!/usr/bin/env python
import glob,os,sys

OutDir="/afs/desy.de/user/s/shakerha/bachelor/Plots/DustPlots/"
if(len(sys.argv)<2):
	print("gib Plot Ordner an!")
	quit(0)

for epsFile in glob.glob(sys.argv[1]+'/*.eps'):
	plotName=epsFile.split("/")[-1].replace(".eps","")
	dirName=OutDir+plotName.split("_")[1].replace("#","")
	if("y_boost" in plotName):dirName=OutDir+"yboost"
	if(not os.path.exists(dirName)): os.makedirs(dirName)
	command="epstopdf "+ epsFile + " --outfile="+dirName+"/"+plotName+".pdf"
	print(command)
	os.system(command)
	
