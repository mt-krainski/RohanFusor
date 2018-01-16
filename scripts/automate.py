#!python

"""
This file contains a few handy FreeCAD functions to automate boring stuff.
Add the path to this file to Python's path and enjoy! At some point I'll
make this a package - but not now :-)

SCRIPTS_PATH = './scripts'

import sys
sys.path.append(SCRIPTS_PATH)
import automate

"""

import FreeCAD
import Document
import FreeCADGui
import Mesh
import sys, os

"""
These should be adopted to your project structure!
"""
CAD_DIR = "cad"
STL_DIR = "stl"
PATH_CHANGE_KEYWORD = CAD_DIR
PATH_CHANGE_KEYWORD_LOCATION = "./"

try:
    mw = FreeCADGui.showMainWindow()
    mw = FreeCADGui.getMainWindow()
    mw.hide()
except:
    pass


def change_paths_to_relative():
    features = Document.FreeCAD.ActiveDocument.findObjects("Part::FeaturePython")
    for ob in features:
        if not "muxedAssembly" in ob.Name:
            if PATH_CHANGE_KEYWORD in ob.sourceFile:
                print("Changed path for: " + ob.Name)
                print("From: " + ob.sourceFile)
                ob.sourceFile = PATH_CHANGE_KEYWORD_LOCATION +\
                            ob.sourceFile.split(PATH_CHANGE_KEYWORD)[-1]
                print("To: " + ob.sourceFile + "\n")
            else:
                print("Warning - keyword not found in object name!")
                print("Name: " + ob.Name)
                print("sourceFile: " + ob.sourceFile + "\n")


def get_radius_of_current_selected():
    return FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0].Curve.Radius


def export_document_as_stl(doc):
    file_name = doc.FileName
    if not CAD_DIR in file_name:
        file_name = os.getcwd() + "/" + file_name

    project_dir = file_name.split(CAD_DIR)[0]
    working_dir = file_name.split(CAD_DIR)[1]
    working_dir = STL_DIR + "/" + working_dir.split(".FCStd")[0] + ".stl"

    objects = []
    for ob in Document.FreeCAD.ActiveDocument.findObjects():

        if "Part" in ob.TypeId and ob.ViewObject.isVisible():
            objects.append(ob)

    if len(objects)>0:
        Mesh.export(objects, project_dir + working_dir)
    else:
        #raise ValueError("No visible objects found in document!")
        print("\tNo visible objects found in document! " + doc.FileName)


def export_active_as_stl():
     export_document_as_stl(Document.FreeCAD.ActiveDocument)


def export_all_as_stl():

    cwd = os.getcwd()
    if CAD_DIR in cwd:
        cwd = cwd.split(CAD_DIR)[0]

    cwd += "/" + CAD_DIR
    os.chdir(cwd)
    dirs = os.listdir(".")

    cad_files = [os.path.join(dp, f) \
        for dp, dn, filenames in os.walk(".") \
        for f in filenames if os.path.splitext(f)[1] == '.FCStd']

    for cad_file in cad_files:
        print "Processing " + cad_file
        stl_file = '..\\' + STL_DIR + "\\" + cad_file
        stl_file = stl_file.split('.FCStd')[0] + '.stl'
        try:
            if os.path.getmtime(cad_file) < os.path.getmtime(stl_file):
                print "\tUp to date..."
                continue
        except OSError:
            print "\tstl file not found!"

        print "\tExporting stl..."
        doc = FreeCAD.open(cad_file)
        export_document_as_stl(doc)
        FreeCAD.closeDocument(doc.Name)


if __name__ == "__main__":
    export_all_as_stl()
