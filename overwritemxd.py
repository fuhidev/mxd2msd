import arcpy, os, sys

def read_mxd_in_folder(path):
  print '-----------------------------------------'
  print 'dang doc du lieu tu folder'
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
      for file in f:
          if '.mxd' in file:
              files.append(os.path.join(r, file))
  print '-------------------//----------------------'
  return files

def set_datasource(mxd_path,database):
  try:
    print '-----------------------------------------'
    print 'set data source ' + mxd_path
    mxd = arcpy.mapping.MapDocument(mxd_path)
    resource_layers = arcpy.mapping.ListLayers(mxd)

    for layer in resource_layers:
      if layer.supports("DATASOURCE"):
        layer.replaceDataSource(database,'SDE_WORKSPACE')
    mxd.save()
    del mxd
    return True
  except Exception as e:
    print 'khong the set datasource '+mxd_path
    print e
  print '-------------------//----------------------'
  return False
  
def mxd_to_msd(mxd_path):
  try:
    print '-----------------------------------------'
    print 'mxd to msd ' + mxd_path
    mxd = arcpy.mapping.MapDocument(mxd_path)
    msd_path = os.path.splitext(mxd_path)[0]
    arcpy.mapping.ConvertToMSD(mxd,msd_path)
    del mxd
  except Exception as e:
    print 'khong the chuyen mxd sang msd '+mxd_path
    print e
  print '-------------------//----------------------'

if __name__ == "__main__":
  folder = os.getcwd()
  if os.path.exists(folder) is False:
    raise Exception(folder + ' khong ton tai')
  files = read_mxd_in_folder(folder)
  for file in files:
    mxd_to_msd(file)

