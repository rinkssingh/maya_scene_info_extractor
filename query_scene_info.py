import sys
import json
import maya.standalone
import maya.cmds as cmds

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    scene_file = sys.argv[1]
    txt_file = sys.argv[2]

    maya.standalone.initialize(name='python')
    #Opening Maya Scene File from python
    cmds.file(scene_file, o=True, force=True)

    references_list = []
    # finding references files from maya scene file
    references = cmds.file(q=True, r=True)
    for ref in references:
        references_list.append(ref)

    cameras_list = []
    camera_to_ignore = ["front" , "persp" , "side" , "top"]
    # Finding Cameras in scene
    cameras = cmds.ls(type='camera')
    # Get the transform nodes of the cameras
    for cam in cameras:
        transform_node = cmds.listRelatives(cam, parent=True)[0]
        if transform_node not in camera_to_ignore and transform_node not in cameras_list:
            cameras_list.append(transform_node)

    # Finding lights in scene, can search more lights like arnold using their transform nodes names these are default one.
    light_types = ['ambientLight', 'directionalLight', 'pointLight', 'spotLight', 'areaLight', 'volumeLight']
    lights_list = []
    for light_type in light_types:
        lights = cmds.ls(type=light_type)
        for light in lights:
            transform_node = cmds.listRelatives(light, parent=True)[0]
            if transform_node not in lights_list:
                lights_list.append(transform_node)

    # Making Dictionary
    result = {
        "References": references_list,
        "Cameras": cameras_list,
        "Lights": lights_list
    }

    # Writing dictionary to result.txt
    with open(txt_file, 'w') as f:
        json.dump(result, f, indent=4)

    print("Scene information has been written to result.txt")


if __name__ == "__main__":
    main()
