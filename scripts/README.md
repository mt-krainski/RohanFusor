### Getting FreeCAD scripts to work ###

To get the `automate.py` script working as standalone, you have to create a new virtual
environment. Due to FreeCAD's limitations (see [RD4]) it's best to create that
virtual environment with FreeCAD's python as the interpreter. I recommend using
`virtualenvwrapper` [RD5]. Makes life easier...

Assuming you have FreeCAD installed in `$FREECAD_DIR`:

``` bash
  mkvirtualenv freecad --python=$FREECAD_DIR/bin/python.exe

```

You have to also add FreeCAD's directories (bin and lib) to `PYTHONPATH`. It's
best done using Python's `.pth` files in the `site-packages` directory.

Simply put this into a new file (with a `.pth` extension) in your virtual
environment's `site-packages` directory:

```
$FREECAD_DIR\\bin\\Lib\\site-packages
$FREECAD_DIR\\bin
$FREECAD_DIR\\lib
```
(you might need to manually replace the `$FREECAD_DIR` tag).


[RD1]: http://edge.rit.edu/edge/P14651/public/Miscellaneous/Design%20rules%20for%20vacuum%20chambers.pdf
[RD2]: https://plastics.ulprospector.com/generics/3/c/t/acrylic-properties-processing
[RD3]: http://www.amesweb.info/Materials/Density_of_Aluminum.aspx
[RD4]: https://www.freecadweb.org/wiki/Embedding_FreeCAD
[RD5]: http://virtualenvwrapper.readthedocs.io/en/latest/index.html
