import muDIC as dic

path = "video_frames"

image_stack = dic.image_stack_from_folder(path,file_type=".tif")

mesher = dic.Mesher()

mesh = mesher.mesh(image_stack)

inputs = dic.DICInput(mesh,image_stack)
