# RohanFusor


### Development environment ###
This project is fully designed using [FreeCAD](https://www.freecadweb.org/) and additional modules:
* [assembly2](https://github.com/hamish2014/FreeCAD_assembly2)

### Current state of the project ###
* first draft model complete
* starting to finalize bom
* finalizing required physical properties
* performed calculations seem to confirm that selected shapes and sized are acceptable.


### todo ###
* add proper description with a picture
* add a proper physical introduction to the topic of fusors
* Convert calculations.py to an jupyter notebook, add plots showing trends a provide a small report
* write a script to automatically generate/update all necessary files (e.g. stls and images so they can be displayed in GitHub)
* agree on required pressure (so far it's 1 mbar)
* agree on required voltage (so far we have a range of 3-10 kV)
* agree on the shape of inner cages
* finish bom (i.e. find all of required parts and get the final cost estimate)
* order parts
* manufacture required parts
* assemble
* test
* hopefully not explode...


### Other important notes ###
* The length of a possible spark, when dealing with HV is approximately  1 cm per 30 kV. Verify (and modify if needed) existing isolations to prevent sparking.

### References ###
* [RD1] - Design rules for vacuum chambers
* [RD2] - Acrylic Typical Properties Generic Acrylic (PMMA)
* [RD3] - Density of aluminum


[RD1]: http://edge.rit.edu/edge/P14651/public/Miscellaneous/Design%20rules%20for%20vacuum%20chambers.pdf
[RD2]: https://plastics.ulprospector.com/generics/3/c/t/acrylic-properties-processing
[RD3]: http://www.amesweb.info/Materials/Density_of_Aluminum.aspx
