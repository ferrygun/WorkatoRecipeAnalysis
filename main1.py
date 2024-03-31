from raptor import RetrievalAugmentation

# Initialize with default configuration. For advanced configurations, check the documentation. [WIP]
RA = RetrievalAugmentation()
SAVE_PATH = "demo/workato_recipe_3424670"

with open('code.json', 'r') as file:
    text = file.read()
RA.add_documents(text)
RA.save(SAVE_PATH)
