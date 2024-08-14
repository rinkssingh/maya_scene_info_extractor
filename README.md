# maya_scene_info_extractor
Python code to Extract data from scene such as References, camera and lights used in maya Scene.

How to use.

Here is script to run on windows Power Shell.
#Script
"C:\Program Files\Autodesk\Maya2022\bin\mayapy.exe" 'D:\task_sgt\query_scene_info.py' 'D:\task_sgt\UAT_2020.ma' 'D:\task_sgt\result.txt'

#Description
"""
"C:\Program Files\Autodesk\Maya2022\bin\mayapy.exe" - Path to your Maya installation folder with mayapy.exe

'D:\task_sgt\query_scene_info.py' - Path to your script which will run and passed to mayapy as first parameter.

'D:\task_sgt\UAT_2020.ma' - Path to you maya file which needs to checked and passed as first parameter to your python script.

'D:\task_sgt\result.txt' - Path to you txt file where data will be dumped from maya file and passed as Second parameter to your python script.
"""