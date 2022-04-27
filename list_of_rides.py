import os


RidesPath = "/datadrive/rides/"

sensors = ["EyeTracking/LeftEye", 
            "EyeTracking/RightEye",
            "HeadTracking",
            "ZED/depth_images",
            "ZED/rgb_images"]

labels = ["E.Tr./L", 
          "E.Tr./R",
          "H.Tr.",
          "Z./dpth",
          "Z./rgb",
          "~len (s)"]

rides = {}


for dirpath, dirnames, filenames in os.walk(RidesPath):
    if "run" in dirpath:
        r = dirpath.replace(RidesPath, "").split("/") 
        ride = r[0] 
        sensor = "/".join(r[1:])
        if not(ride in rides):
            rides[ride]={}
            for s in sensors:
                rides[ride][s] = 0
        if sensor in sensors:
                rides[ride][sensor]=len(filenames)
        
len_name = 50
len_others = 10
len_id = 7

id_counter = 1
tot_len = len_name+len_others*len(labels) + len_id
print("-"*(tot_len))
print("AVAILABLE RIDES".center(tot_len))
print("-"*(tot_len))
print("Ride id".rjust(len_id)+"Ride name".rjust(len_name)+"".join([labels[i].rjust(len_others) for i in range(len(labels))] ))
print("-"*(tot_len))
for ride in sorted(rides.keys()):
    desirialized = os.path.isfile(os.path.join(*[RidesPath, ride, "deserialized"]))
    if desirialized:
        video_length = str(rides[ride]["ZED/rgb_images"]//26).rjust(len_others)
        print(str(id_counter).rjust(len_id) + ride.rjust(len_name) + "".join([str(rides[ride][sensors[i]]).rjust(len_others) for i in range(len(sensors))]) + video_length)       
        id_counter+=1