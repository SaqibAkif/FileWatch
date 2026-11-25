def masala_generator():
    yield"Biryani masala"
    yield"Tikka masala"
    yield"Nehari masala"

gen = masala_generator()
print(next(gen))
print(next(gen))
print(next(gen))