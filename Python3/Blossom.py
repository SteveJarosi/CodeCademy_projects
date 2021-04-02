class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [None for x in range(size)]
  def hash(self, key):
    return sum(key.encode)
  def compress(self, hash_code):
    return hash_code % self.array.size
  def assign(self, key, value):
    pass