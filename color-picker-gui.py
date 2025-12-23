import sys

wx = None
Gtk = None

try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
except ImportError:
    try:
        import gtk as Gtk
        try:
            Gdk = Gtk.gdk
        except AttributeError:
            from gi.repository import Gdk
    except ImportError:
        Gtk = None
    raise ImportError("No GTK bindings found")

def open_color_picker_via_gtk():
    color_sel = Gtk.ColorSelectionDialog("Sublime Color Picker")

    if len(sys.argv) > 1:
        current_color = Gdk.color_parse(sys.argv[1])
        if current_color:
            try:
                color_sel.colorsel.set_current_color(current_color)
            except AttributeError:  # newer version of GTK
                color_sel.get_color_selection().set_current_color(current_color)

    if color_sel.run() == getattr(Gtk, 'RESPONSE_OK', Gtk.ResponseType.OK):
        color = color_sel.get_color_selection().get_current_color()
        #Convert to 8bit channels
        red = int(color.red / 256)
        green = int(color.green / 256)
        blue = int(color.blue / 256)
        #Format
        RGB_values = (red, green, blue)


    color_sel.destroy()
    return [red, green, blue]


open_color_picker_via_gtk()
