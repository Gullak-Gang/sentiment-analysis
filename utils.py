import re
import json

# PARTIAL, NO NEED
def get_captions(data):
    """ 
    Get and preprocess captions from an array of input data.

    Parameters:
        data (list): Array of dictionaries containing captions.

    Returns:
        list: Array of cleaned captions.
    """
    
    captions = clean_captions(data)
    return captions


def clean_captions(data):
    """ 
    Clean and preprocess an array of captions, remove special characters like emojis, 
    and convert to UTF-8. Retain common punctuation.

    Parameters:
        data (list): Array of raw captions (strings).

    Returns:
        list: Array of cleaned captions.
    """
    cleaned_captions = []
    for caption in data:
        # Ensure caption is a string before processing
        if not isinstance(caption, str):
            print(f"Skipping non-string caption: {caption}")
            continue  # Skip non-string captions

        try:
            # Convert to UTF-8 (if not already in UTF-8, ensure proper encoding)
            caption_utf8 = caption.encode('utf-8', 'ignore').decode('utf-8')

            # Remove emojis and special characters except common punctuation (.,!?)
            clean_caption = re.sub(r'[^\w\s.,!?-]', '', caption_utf8)  # This removes emojis and special symbols

            # Optionally, remove multiple spaces or newlines
            clean_caption = re.sub(r'\s+', ' ', clean_caption)  # Replace multiple spaces or newlines with a single space

            # Strip leading/trailing whitespaces
            cleaned_captions.append(clean_caption.strip())

        except Exception as e:
            print(f"Error processing caption '{caption}': {e}")
            continue  # Skip problematic captions

    return cleaned_captions


def join_captions(captions):
    captions = "\n\n".join(caption for caption in captions)
    return captions


def get_json_response(response, analysis_results):
    response_json = response.json()  # Parse JSON from the response
    content = response_json.get('choices', [{}])[0].get('message', {}).get('content', None)
    match = re.search(r'\{.*?\}', content, re.DOTALL)
    if match:
        content = match.group(0)  # Extract the matched JSON-like string
        json_object = json.loads(content)  # Convert the string to a JSON object
        analysis_results.append(json_object)
    else:
        print(f"Error: No JSON object found in response for caption")


# if __name__=="__main__":
#     print(get_captions())