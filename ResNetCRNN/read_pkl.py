import pickle

f = open("ResNetCRNN_varylength/UCF8actions.pkl", "rb")
data = pickle.load(f)
print(data)