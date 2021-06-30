def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "so do you!"
gen = silly_generator()
print(next(gen))
print(next(gen))
print(next(gen))
gen = silly_generator()
for item in gen:
    print(item)
