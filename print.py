import tempfile
import win32api
import win32print

if __name__ == '__main__':

    filename = tempfile.mktemp(".txt")
    open(filename, "w").write("This is a test")
    win32api.ShellExecute(
        0,
        "print",
        filename,
        #
        # If this is None, the default printer will
        # be used anyway.
        #
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
