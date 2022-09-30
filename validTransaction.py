def insert_data(input, dict1): 
    for line in input:
	# Considering that each line of input is a json string
        trx_id = json.loads(line)['trx_id'] #loads() is used to convert the JSON String document into the Python dictionary.
        if trx_id not in dict1.keys():
            print("Unique")
            dict1[trx_id] = line
        else:
            print("Duplicate")
	return dict1 # This contains trx_id as key and line as value (Value is our trx data which is a json string containing time and trx id
#store the Trxs
   
def purge(data):
	for key, value in data.keys:
		trx_time = json.loads(value)['trx_time']
		# need to check if this time is within 1 hour range
		curr_time = time.time() - trx_time # Assumimg trx time is the number of seconds passed since epoch
		if curr_time >= 60 * 60: # Surely the difference should be less than or equal to 3600 secs
			del data[key] # deleting the trx key which is trx_id

if __name__ = "__main__":
	data_records = {} # This will be maintained as our data base
	
	while True:
		start = time.time()
		input_strm = input("This is bunch of lines each line have trx id and trx time") 
		uni_data = insert_data(input_strm, data_records) # only unique data records will be inserted 
		end = time.time()
		diff = end - start # Assuming that insertion this data won't take more than a min 
		# Purging older records at every min
		time.sleep(60 - diff)
		purge(uni_data)
		
