import hashlib

class Hash:

    @staticmethod
    def create(file_path):
        """ 
            Create hash value with MD5 algorithm.
            @params file_path: absolute path of filename
            @return string md5 is a 128-bit encrypted hash
        """        
        md5 = hashlib.md5()
        # set mode = "rb" to read binary to handle different file types
        with open(file_path, "rb", 4098) as f:
            # chunks are buffer size of 4098
            for chunk in f:
                md5.update(chunk)
        
        return md5.hexdigest()