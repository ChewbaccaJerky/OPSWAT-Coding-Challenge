import requests
API_KEY = "<API_KEY>"
test_hash = "E71A6D8760B37E45FA09D3E1E67E2CD3"

class OpswatService:
    """ OPSWAT SERVICE connects to OPSWAT API and does following methods """
    
    @staticmethod
    def hash_lookup(hash):
        """ 
            Checks OPSWAT store to see if file has already been scanned 
            @params hash => hashed value of file
            @return Response result either success or failure
        """
        headers = {'apikey': API_KEY}
        url = "https://api.metadefender.com/v2/hash/" + hash
        result = requests.get(url, headers=headers)
        return result


    @staticmethod
    def upload_file(path, filename):
        """ 
            Upload file to scan into OPSWAT API
            @params path => String absolute path
                    filename => String filename
            @return Response object with data_id
        """
        byteFile = ""

        with open(path, "rb", 4098) as f:
            for chunk in f:
                byteFile += chunk

        headers = {'apikey': API_KEY}
        files = {'file': byteFile}
        
        url = "https://api.metadefender.com/v2/file"

        result = requests.post(url, headers=headers, files=files)
        
        return result.json()["data_id"]

    @staticmethod
    def get_results_by_data_id(data_id):
        """
            After retrieving data_id you can get results from OPSWAT API
            @params data_id => String to access scan details
            @return Response object of scan details
        """
        headers = {'apikey': API_KEY}
        url = "https://api.metadefender.com/v2/file/" + data_id
        result = requests.get(url, headers=headers)
        return result

    @staticmethod
    def print_result(res, filename):
        """
            Print results by specific format
            @params res => Response result 
                    filename => String filename
            
        """
        result = res.json()["scan_results"]
        details = result["scan_details"]

        print "\nfilename: " + filename
        print "overall status: " + result["scan_all_result_a"] + "\n"

        for key in details:
            print "engine: " + key

            if details[key]["threat_found"]:
                print "threat_found: " + details[key]["threat_found"] 
            else:
                print "threat_found: Clean"
            print "scan_result: " + str(details[key]["scan_result_i"])
            print "def_time: " + details[key]["def_time"]

            print "\n"
