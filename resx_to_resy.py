import csv

def buildmap():
    coord_map = {(25,25) : {},
                 (25,50) : {},
                 (25,100) : {},
                 (50,50) : {},
                 (50,25) : {},
                 (50,100) : {},
                 (100,100) : {},
                 (100,25) : {},
                 (100,50) : {}
    }
    with open ("Z:/projects/macsur-scaling-cc-tuscany//unit_description/MACSUR_TUS_CC_cell_lookup.csv") as _:
        reader = csv.reader(_)
        reader.next()
        for row in reader:
            coord = {}
            coord[25] = (int(row[0]), int(row[1]))
            coord[50] = (int(row[2]), int(row[3]))
            coord[100] = (int(row[4]), int(row[5]))
            for res_x, coord_x in coord.iteritems():
                for res_y, coord_y in coord.iteritems():
                    if coord_x not in coord_map[(res_x, res_y)]:
                        coord_map[(res_x, res_y)][coord_x] = []
                    if coord_y not in coord_map[(res_x, res_y)][coord_x]:
                        coord_map[(res_x, res_y)][coord_x].append(coord_y)
        print("ok")
buildmap()
