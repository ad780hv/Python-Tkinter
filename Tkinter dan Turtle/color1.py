from tkinter.commondialog import Dialog

# color chooser class

class Chooser(Dialog):
    "Ask for a color"

    command = "tk_chooseColor"

    def _fixoptions(self):
        try:
            # make sure initialcolor is a tk color string
            color = self.options["initialcolor"]
            if isintance(color, tuple):
                # assume an RGB triplet
                self.options["initialcolor"] = "#%02x%02x%02x"  % color
        except KeyError:
            pass

        def _fixresult(self, widget, result):
            # result can be somethings: an empety tuple, an empty string or
            # a Tcl_Obj, so this somewhat weird check handles that
            if not result or not str(result):
                return None, None # canceled

            # to simplify application code, the color chooser returns
            # an RGB tuple together with the Tk color string
            r, g, b = widget.winfo_rgb(result)
            return (r/256, g/256, b/256), str(result)

#
# convenience stuff

def askcolor(color = None, **options):
    "Ask for a color"

    if color:
        options = options.copy()
        option["initialcolor"] = color

    return Chooser(**options).show()

# ----------------------------------------------------
# test stuff

if __name__ == "__main__":
    print("color", askcolor())
