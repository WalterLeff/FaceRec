# import os, uuid
# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# try:
#     print("Azure Blob storage ")
#     # Quick start code goes here
#     connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

#     # Create the BlobServiceClient object which will be used to create a container client
#     blob_service_client = BlobServiceClient.from_connection_string(connect_str)

#     # Create a unique name for the container
#     container_name = "test" + str(uuid.uuid4())

#     # Create the container
#     container_client = blob_service_client.create_container(container_name)

#     # Create a file in local Documents directory to upload and download
#     local_path = "./data"
#     local_file_name = "first_upload" + str(uuid.uuid4()) + ".txt"
#     upload_file_path = os.path.join(local_path, local_file_name)

#     # Write text to the file
#     file = open(upload_file_path, 'w')
#     file.write("Hello, World!")
#     file.close()

#     # Create a blob client using the local file name as the name for the blob
#     blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

#     print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

#     # Upload the created file
#     with open(upload_file_path, "rb") as data:
#         blob_client.upload_blob(data)

#     print("\nListing blobs...")

#     # List the blobs in the container
#     blob_list = container_client.list_blobs()
#     for blob in blob_list:
#         print("\t" + blob.name)

#     # Download the blob to a local file
#     # Add 'DOWNLOAD' before the .txt extension so you can see both files in Documents
#     download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
#     print("\nDownloading blob to \n\t" + download_file_path)

#     with open(download_file_path, "wb") as download_file:
#         download_file.write(blob_client.download_blob().readall())

# except Exception as ex:
#     print('Exception:')
#     print(ex)


# import os, uuid
# from azure.storage.blob import BlockBlobService
# from werkzeug import secure_filename

# account  = 'facerecblob'  # Azure account name
# key = 'ro3K4T0Jhcd1cx7X3rrFCzRztDk8IEdCkrH3'    # Azure Storage account access key  
# container = 'TestContainer' # Container name

# blob_service = BlockBlobService(account_name=account, account_key=key)

# @app.route('/blobStorage', methods=['GET', 'POST'])
# def uploadToBlob():
# 	if request.method == 'POST':
# 		file = request.files['file']
# 		filename = secure_filename(file.filename)
# 		fileextension = filename.rsplit('.',1)[1]
# 		Randomfilename = id_generator()
# 		filename = Randomfilename + '.' + fileextension
# 		try:
# 			container_client = blob_service_client.create_container(container)
# 			print('print out containers')
# 			blob_list = container_client.list_blobs()
# 			for blob in blob_list:
# 				print("\t" + blob.name)

# 			blob_service.create_blob_from_stream(container, filename, file)
# 		except Exception:
# 			print(Exception)
# 			pass
# 		ref =  'http://'+ account + '.blob.core.windows.net/' + container + '/' + filename
# 		return '''
# 		<!doctype html>
# 		<title>File Link</title>
# 		<h1>Uploaded File Link</h1>
# 		<p>''' + ref + '''</p>
# 		<img src="'''+ ref +'''">
# 		'''
# 	return '''
# 	<!doctype html>
# 	<title>Upload new File</title>
# 	<h1>Upload new File</h1>
# 	<form action="" method=post enctype=multipart/form-data>
# 	  <p><input type=file name=file>
# 		 <input type=submit value=Upload>
# 	</form>
# '''
# import string, random, requests
# def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
# 	return ''.join(random.choice(chars) for _ in range(size))


#     #create container
# 	azure_storage.block_blob_service.create_container('test_container')

# 	from azure.storage.blob import ContentSettings
# 	azure_storage.block_blob_service.create_blob_from_path(container_name='test_container',
# 														 blob_name='wouter_lefebvre', 
# 														 file_path='/FaceRec/Data_upload2Blob/WIN_20191227_11_56_51_Pro.jpg', 
# 														 content_settings=ContentSettings(content_type='image'))
# 	azure_storage.block_blob_service.exists('test_container', 'wouter_lefebvre')
# 	return ('dit is blob upload')
