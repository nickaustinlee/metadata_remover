# No Fuss Metadata Remover
A lot of social media websites flag photographs as AI-generated even though the use of AI tools does not fundamentally change the spirit of the photo. For example, Photoshop tags images with an AI metadata tag even if you use the generative fill to remove dust specks or blemishes on the photo, and then Instagram detects the metadata tag and flags it as AI generated. This over-eager AI tagging undermines photographers who aren't actually using these tools to produce artificial content. 

By using this tool, you can easily remove all metadata on a JPG before uploading to social media, and opt-in to the AI-generated tag rather than allowing social media to flag everything as AI-generated.

## Instructions to use

1. Create a virtual environment
```
python -m venv my_virtual_environment
```
2. Activate the virtual environment

Windows
```
my_virtual_environment\Scripts\activate
```
  macOS/Linux
```
source my_virtual_environment/bin/activate
```
3. Install one dependency
```
pip install pillow
```
5. Run the program
```
python remove_metadata.py <your_image_file.jpg>
```
6. Deactivate the virtual environment when done
```
deactivate
```
