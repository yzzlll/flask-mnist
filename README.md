# flask-mnist
Task: Use flask to provide a tensorflow-based mnist web service, and store the data in cassadra database

Description:

The user can upload a 28x28 pixel image of hand-written figure ranging from 0 to 9. The application will recognize the figure and return the actual number in the image. The database will assign every entry an id and store the figure of the image as well as the timestamp.

Install the required packages:

  $ pip install flask 
  
  $ pip install flask_cqlalchemy
  
  $ pip install tensorflow

