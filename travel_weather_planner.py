distance_mi = 9
is_raining = True
has_bike = False
has_car = False
has_ride_share_app = True
if not distance_mi:
    print(False)
elif distance_mi <=1 :
    if is_raining == False :
        print(True)
    else:
        print(False)
elif distance_mi > 1 and distance_mi <= 6 :
    if has_bike == False and is_raining == True:
        print(False)
    elif has_bike == False and is_raining == False:
        print(False)
    elif has_bike == True and is_raining == False:
        print(True)
    else:
        print(False)
elif distance_mi > 6:
    if has_car == True or has_ride_share_app == True :
        print(True) 
    else :
        print(False) 
