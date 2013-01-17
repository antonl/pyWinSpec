from structs import Header, AxisCalibration, ROIinfo

if __name__ == '__main__':
    import inspect, re, io

    with io.FileIO('02_reference.SPE', mode='r') as f:
        A = Header()
        f.readinto(A)
        
        for i in [WinSpecHeader, AxisCalibration, ROIinfo]:
            fields = []

            print '{:20s}[{:4s}]\toffset'.format(str(i), 'size')
            
            for name,obj in inspect.getmembers(i):
                if inspect.isdatadescriptor(obj) and not inspect.ismemberdescriptor(obj) 
                    and not inspect.isgetsetdescriptor(obj):
                    
                    fields.append((name, obj))

            fields.sort(key=lambda x: re.search('(?<=ofs=)([0-9]+)', str(x[1])).group(0), 
                    cmp=lambda x,y: cmp(int(x),int(y))); fields

            for name, obj in fields:
                print '{:20s}[{:3d}]\toff={:4d}'.format(name, obj.size, obj.offset)

