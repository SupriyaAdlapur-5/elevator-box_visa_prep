    vignesh, charan = input().split()
    if(vignesh == 'R' and charan == 'S') or (vignesh == 'P' and charan == 'R') or (vignesh == 's' and charan == 'P'):
        print("vignesh")
    elif (charan == 'R' and  vignesh == 'S') or (charan == 'P' and vignesh == 'R') or (charan == 'S' and vignesh == 'P'):
        print("charan")
    else:
        print("NULL")
    
