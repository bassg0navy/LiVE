#def get_chunk(byte1=None, byte2=None):
        #full_path = "fam4330e84be1734f3b8f9bcc9df3bef1c8.mp4"
        #file_size = os.stat(obj).st_size
        #start = 0
    
        #if byte1 < file_size:
            #start = byte1
        #if byte2:
            #length = byte2 + 1 - byte1
        #else:
            #length = file_size - start

        #with open(obj, 'rb') as f:
            #f.seek(start)
            #chunk = f.read(length)
        #return chunk, start, length, file_size

    #range_header = request.headers.get('Range', None)
    #byte1, byte2 = 0, None
    #if range_header:
        #match = re.search(r'(\d+)-(\d*)', range_header)
        #groups = match.groups()

        #if groups[0]:
            #byte1 = int(groups[0])
        #if groups[1]:
            #byte2 = int(groups[1])
       
    #chunk, start, length, file_size = get_chunk(byte1, byte2)
    #resp = Response(chunk, 206, mimetype='video/mp4',
                      #content_type='video/mp4', direct_passthrough=True)
    #resp.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(start, start + length - 1, file_size))