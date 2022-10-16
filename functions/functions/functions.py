
import random;

def test(a, b):
	print(a + b);

def a(a, b, c):
	for i in range(10):
		v = random.choice([a, b, c])
		if i == 0:
			word = v[random.randint(len(v))];
		else:
			word += v[random.randint(len(v))];
		return word;
def b(a):
	r = a;
	for i in range(random.randint(1,3)):
		r += a;
	return r;
def c(a, b, c):
	ans = input(a(c, b, a));
	print(a(random.choice([a, b, c, ans]), random.choice([a, b, c, ans]), random.choice([a, b, c, ans])));