def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == "even":
            kwargs["even"] = [n for n in kwargs["even"] if n % 2 == 0] # kwargs[key] = [ n for n in value if n % 2 ==0]
        if key == "odd":
            kwargs["odd"] = [n for n in kwargs["odd"] if n % 2 != 0]
    return dict(sorted(kwargs.items(), key=lambda kvp: -len(kvp[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
