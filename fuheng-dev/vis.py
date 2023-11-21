import json
from PIL import Image, ImageDraw
import hiq

import os

here = os.path.dirname(os.path.realpath(__file__))

# Path to the results file and the image directory
results_file_path = f'{here}/inference_results/system_results.txt'
image_directory = here  # Assuming the images are in the current directory

# Open and read the results file
lines = hiq.read_file(results_file_path)
for line in lines:  # Reading line by line
    # Splitting the line into filename and JSON part
    filename, json_part = line.split('\t')
    print(filename)
    
    # Load the JSON part as JSON
    results = json.loads(json_part.strip())
    
    # Create the full image path
    image_path = f'{image_directory}/{filename.strip()}'
    # Open the image file
    with Image.open(image_path) as im:
        # Create a drawing context
        draw = ImageDraw.Draw(im)
        
        # Loop through each result and draw a bounding box
        for result in results:
            # Extract the points from the result
            points = result['points']  # Adjust this to match the actual JSON key for points
            # Flatten the points
            flat_points = [coord for point in points for coord in point]
            # Draw a polygon (in this case a rectangle) by connecting all the points
            draw.polygon(flat_points, outline='red')  # red is the color of the bounding box
        
        # Save the image with bounding boxes
        output_path = f'{image_directory}/output_{filename.strip()}'
        im.save(output_path)
        # Show the image
        im.show()
