# Creted and edit with DataFrame in Pandas
# import pandas as pd

# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'Los Angeles', 'Chicago']}
# df = pd.DataFrame(data)

# Calculate average age
# average_age = df['Age'].mean()

# Filter data in Pandas
# filter_df = df[df['Age'] > 30]

# print(filter_df)

# Using Numpy for numerical operations
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# mean = np.mean(arr)
# print(arr, mean)

# Add new column to use Numpy
# df['Age Squared'] = np.square(df['Age'])
# print(df)

# Using Matplotlib for plotting
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]

# plt.plot(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Sample Plot')
# plt.show()

# Using Matplotlib for bar chart
# categories = ['A', 'B', 'C', 'D']
# values = [10, 20, 30, 40]

# plt.bar(categories, values)
# plt.xlabel('Categories')
# plt.show()

# Using Matplotlib for scatter plot
# x = [1, 2, 3, 4, 5]
# y = [5, 4, 3, 2, 1]

# plt.scatter(x, y)
# plt.title('Sample Scatter Plot')
# plt.show()

# import seaborn as sns 

# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# sns.histplot(data, kde=True)
# plt.title('Box Plot Example')
# plt.show()

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Hàm thêm padding (DES yêu cầu block 8 byte)
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Tạo key 8 byte ngẫu nhiên
key = get_random_bytes(8)
print("🔑 Key (hex):", key.hex())

# Tạo đối tượng DES ở chế độ ECB
cipher = DES.new(key, DES.MODE_ECB)

# Văn bản cần mã hóa
plaintext = "Hello GPT-5"
padded_text = pad(plaintext)
print("📜 Plaintext:", padded_text)

# Mã hóa
encrypted = cipher.encrypt(padded_text.encode())
print("🔒 Encrypted (hex):", encrypted.hex())

# Giải mã
decrypted = cipher.decrypt(encrypted).decode().strip()
print("🔓 Decrypted:", decrypted)