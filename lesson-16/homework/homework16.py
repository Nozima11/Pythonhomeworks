import numpy as np

# 51
position_color = np.array([(1, 2, 255, 0, 0), (3, 4, 0, 255, 0), (5, 6, 0, 0, 255)],
                          dtype=[('position', '2int32'), ('color', '3int32')])

# 52
coords = np.random.random((100, 2))
distances = np.linalg.norm(coords[1:] - coords[:-1], axis=1)

# 53
float_array = np.random.rand(10).astype(np.float32)
int_array = float_array.astype(np.int32)

# 54
# 1, 2, 3, 4, 5
# 6,  ,  , 7, 8
#  ,  , 9,10,11
from io import StringIO

data = """1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11"""
file = StringIO(data)
arr = np.genfromtxt(file, delimiter=',', filling_values=np.nan)

# 55
arr = np.array([10, 20, 30])
for idx, value in np.ndenumerate(arr):
    print(idx, value)

# 56
x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2))

# 57
array_2d = np.zeros((5, 5), dtype=int)
p = 5
indices = np.random.choice(array_2d.size, p, replace=False)
np.put(array_2d, indices, 1)

# 58
matrix = np.random.rand(4, 4)
matrix_mean_subtracted = matrix - matrix.mean(axis=1)[:, np.newaxis]

# 59
matrix = np.random.rand(4, 4)
sorted_matrix = matrix[matrix[:, 1].argsort()]

# 60
array = np.array([[1, 2, np.nan], [3, 4, 5], [6, 7, 8]])
null_columns = np.any(np.isnan(array), axis=0)

# 61
array = np.array([1, 3, 7, 10])
value = 5
nearest_value = array[np.abs(array - value).argmin()]

# 62
arr1 = np.array([[1, 2, 3]])
arr2 = np.array([4], [5], [6]])
sum_result = np.add(arr1, arr2)

# 63
class NamedArray(np.ndarray):
    def __new__(cls, shape, dtype, name):
        obj = super(NamedArray, cls).__new__(cls, shape, dtype)
        obj.name = name
        return obj

named_array = NamedArray((3, 3), dtype=int, name="MyArray")

# 64
vector = np.array([1, 2, 3, 4, 5])
indices = np.array([1, 3, 3])
vector[indices] += 1

# 65
X = np.array([1, 2, 3, 4, 5])
I = np.array([0, 2, 2, 4])
F = np.zeros(5)
np.add.at(F, I, X)

# 66
image = np.random.randint(0, 256, size=(10, 10, 3), dtype=np.uint8)
unique_colors = np.unique(image.reshape(-1, 3), axis=0)

# 67
array = np.random.rand(3, 3, 3, 3)
sum_over_last_two = array.sum(axis=(-1, -2))

# 68
D = np.array([1, 2, 3, 4, 5])
S = np.array([0, 0, 1, 1, 1])
means = [D[S == i].mean() for i in np.unique(S)]

# 69
A = np.random.rand(4, 3)
B = np.random.rand(3, 4)
dot_product = np.dot(A, B)
diagonal = np.diagonal(dot_product)

# 70
vector = np.array([1, 2, 3, 4, 5])
new_vector = np.zeros(len(vector) * 4 - 3, dtype=int)
new_vector[::4] = vector

# 71
array = np.random.rand(5, 5, 3)
array2 = np.random.rand(5, 5)
result = array * array2[:, :, np.newaxis]

# 72
array = np.random.rand(5, 5)
array[[0, 1]] = array[[1, 0]]

# 73
triplets = np.array([[1, 2, 3], [3, 4, 5], [1, 3, 5], [4, 2, 6], [1, 4, 2], [3, 5, 6], [1, 6, 3], [4, 2, 1], [2, 6, 5], [5, 1, 6]])
edges = np.unique(np.sort(np.concatenate([triplets[:, [0, 1]], triplets[:, [0, 2]], triplets[:, [1, 2]]], axis=0), axis=1), axis=0)


