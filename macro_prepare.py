import pya
from kqcircuit.defaults import default_layers

### This script has multiple sideeffects

def prep_empty_layout():

  # Create the layout
  global app, mw, layout_view
  app = pya.Application.instance()
  mw = app.main_window()
  layout_view = mw.current_view()
  
  # Do we have a view?
  global cell_view, layout
  if layout_view == None:
    # Create a new view
    cell_view = mw.create_layout(1)
    layout = cell_view.layout()
    layout_view = mw.current_view()
  else:
    # Use an active view
    cell_view = pya.CellView.active()
    layout = cell_view.layout()
  
  # Delete all cells 
  layout_view.clear_layers()
  
  ### Populate layers
  l = {}
  for name, layer in default_layers.items():
    #print(name,type(layer))
    l[name] = layout.layer(layer)    
    
  layout_view.add_missing_layers()
  
  return (layout, layout_view)