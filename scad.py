import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    oomp_mode = "project"
    #oomp_mode = "oobb"

    test = False
    #test = True

    if typ == "all":
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
        #default
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
        #default
        #filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        

        #one_piece
        one_pieces = []
        one_piece = {}
        one_piece["felt_pad_od"] = 40
        one_piece["felt_pad_border"] = 5
        one_piece["felt_pad_depth"] = 2
        one_piece["screw_spacing"] = 36
        one_piece["thickness"] = 12
        #one_piece["furniture_leg_od"] = 30
        one_pieces.append(one_piece)

        furniture_leg_ods = [25,26,27,28,29,30,31,32]


        for one_piece in one_pieces:
            for furniture_leg_od in furniture_leg_ods:
                one_piece["furniture_leg_od"] = furniture_leg_od
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["width"] = 0
                p3["height"] = 0
                p3.update(one_piece)
                #p3["thickness"] = 6
                p3["extra"] = f"{p3['felt_pad_od']}_mm_felt_pad_od"
                p3["extra"] += f"_{p3['furniture_leg_od']}_mm_furniture_leg_od"

                part["kwargs"] = p3
                nam = "one_piece"
                part["name"] = nam
                if oomp_mode == "oobb":
                    p3["oomp_size"] = nam
                if not test:
                    pass
                    parts.append(part)

        #bottom
        bottoms = []
        depth_bottom = 5
        bottom = {}
        #felt_pad_od 40 mm
        bottom["felt_pad_od"] = 40
        bottom["felt_pad_border"] = 5
        bottom["felt_pad_depth"] = 2
        bottom["screw_spacing"] = 36
        bottom["thickness"] = depth_bottom
        bottoms.append(bottom)

        for bot in bottoms:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3["width"] = 0
            p3["height"] = 0
            p3.update(bot)
            #p3["thickness"] = 6
            p3["extra"] = f"{p3['felt_pad_od']}_mm_felt_pad_od"

            part["kwargs"] = p3
            nam = "bottom"
            part["name"] = nam
            if oomp_mode == "oobb":
                p3["oomp_size"] = nam
            if not test:
                pass
                #parts.append(part)


        tops = []
        top = {}
        #furniture_leg_od
        top["furniture_leg_od"] = 30
        top["felt_pad_od"] = 40
        top["felt_pad_border"] = 5
        top["thickness"] = 6
        top["depth_bottom"] = depth_bottom
        top["screw_spacing"] = 36
        tops.append(top)

        for top in tops:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3["width"] = 0
            p3["height"] = 0
            p3.update(top)
            #p3["thickness"] = 6
        #felt pad first
            p3["extra"] = f"{p3['felt_pad_od']}_mm_felt_pad_od"
            p3["extra"] += f"_{p3['furniture_leg_od']}_mm_furniture_leg_od"

            part["kwargs"] = p3
            nam = "top"
            part["name"] = nam
            if oomp_mode == "oobb":
                p3["oomp_size"] = nam
            if not test:
                pass
                #parts.append(part)



    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        sort.append("felt_pad_od")
        sort.append("furniture_leg_od")
        sort.append("thickness")
        
        scad_help.generate_navigation(sort = sort)


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_bottom(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    felt_pad_od = kwargs.get("felt_pad_od", 40)
    felt_pad_border = kwargs.get("felt_pad_border", 5)
    felt_pad_depth = kwargs.get("felt_pad_depth", 2)
    screw_spacing = kwargs.get("screw_spacing", 36)
    furniture_leg_od = kwargs.get("furniture_leg_od", 27)

    outside_diameter = felt_pad_od + felt_pad_border

    #add main cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_cylinder"    
    p3["depth"] = depth
    p3["radius"] = outside_diameter / 2
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    
    #add pad cutout
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_cylinder"
    p3["depth"] = felt_pad_depth
    p3["radius"] = (felt_pad_od / 2 ) + 0.5
    
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += 0 + depth/2 - felt_pad_depth/2
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add oobb_screw_countersunk radius name m3 depth 6
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["depth"] = 10
    p3["radius_name"] = "m3"
    p3["nut"] = True
    poss = []
    pos1 = copy.deepcopy(pos)
    pos1[2] += 0 + depth/2 - felt_pad_depth/2
    pos11 = copy.deepcopy(pos1)
    pos11[0] += screw_spacing / 2
    poss.append(pos11)
    pos12 = copy.deepcopy(pos1)
    pos12[0] += -screw_spacing / 2
    poss.append(pos12)
    p3["pos"]  = poss
    rot1 = copy.deepcopy(rot)
    rot1[0] = 0
    p3["rot"] = rot1
    p3["m"] = "#"
    oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_one_piece(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    felt_pad_od = kwargs.get("felt_pad_od", 40)
    felt_pad_border = kwargs.get("felt_pad_border", 5)
    felt_pad_depth = kwargs.get("felt_pad_depth", 2)
    screw_spacing = kwargs.get("screw_spacing", 36)
    furniture_leg_od = kwargs.get("furniture_leg_od", 27)

    outside_diameter = felt_pad_od + felt_pad_border

    #add main cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_cylinder"    
    p3["depth"] = depth
    p3["radius"] = outside_diameter / 2
    
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add furniture leg cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_cylinder"
    p3["depth"] = depth
    p3["radius"] = (furniture_leg_od / 2 )
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += 0 
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)


    #add pad cutout
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_cylinder"
    p3["depth"] = felt_pad_depth
    p3["radius"] = (felt_pad_od / 2 ) + 0.5
    
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += 0 + depth/2 - felt_pad_depth/2
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_top(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    felt_pad_od = kwargs.get("felt_pad_od", 40)
    felt_pad_border = kwargs.get("felt_pad_border", 5)
    felt_pad_depth = kwargs.get("felt_pad_depth", 2)
    screw_spacing = kwargs.get("screw_spacing", 36)
    depth_bottom = kwargs.get("depth_bottom", 5)
    furniture_leg_od = kwargs.get("furniture_leg_od", 30)

    outside_diameter = felt_pad_od + felt_pad_border

    #add main cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_cylinder"    
    p3["depth"] = depth
    p3["radius"] = outside_diameter / 2
    
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[2] += -depth_bottom
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add firhiture leg cutout
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_cylinder"
    dep = depth - 3
    p3["depth"] = dep
    p3["radius"] = (furniture_leg_od / 2 ) + 0.5    
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += -depth_bottom - 3 + dep/2
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add oobb_screw_countersunk radius name m3 depth 6
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["depth"] = 10
    p3["radius_name"] = "m3"
    p3["nut"] = True
    poss = []
    pos1 = copy.deepcopy(pos)
    pos1[2] += 0 + depth/2 - felt_pad_depth/2
    pos11 = copy.deepcopy(pos1)
    pos11[0] += screw_spacing / 2
    poss.append(pos11)
    pos12 = copy.deepcopy(pos1)
    pos12[0] += -screw_spacing / 2
    poss.append(pos12)
    p3["pos"]  = poss
    rot1 = copy.deepcopy(rot)
    rot1[2] = 360/12
    p3["rot"] = rot1
    p3["m"] = "#"
    oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)