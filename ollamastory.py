import ollama

res = ollama.chat(
	model="llava",
	messages=[
		{
			'role': 'user',
			'content': 'Decris moi cette image en francais:',
			'images': ['./static/images/image1.jpg']
		}
	]
)

print(res['message']['content'])