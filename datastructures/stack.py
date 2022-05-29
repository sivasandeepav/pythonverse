from abc import ABCMeta, abstractmethod


class AbstractStack(metaclass=ABCMeta):

  def __init__(self):
    self._top = -1

  def __len__(self):
    return self._top + 1

  def is_empty(self):
    return self._top == -1

  @abstractmethod
  def __iter__(self):
    pass

  @abstractmethod
  def push(self):
    pass

  @abstractmethod
  def pop(self):
    pass

  @abstractmethod
  def peek(self):
    pass

class ArrayStack(AbstractStack):
  
  def __init__(self, size):
    super().__init__()
    self._array = [None] * size
  
  def __len__(self):
    return super().__len__()

  def __iter__(self):
    probe = self._top
    while True:
        if probe == -1:
            return
        yield self._array[probe]
        probe -= 1

  def push(self, value):
    self._top += 1
    if self._top == len(self._array):
      self._expand()
    self._array[self._top] = value

  def pop(self):
    if self.is_empty():
      raise IndexError('Stack is empty.')
    value = self._array[self._top]
    self._top -= 1
    return value
  
  def peek(self):
    if self.is_empty():
      raise IndexError('Stack is empty.')
    return self._array[self._top]
  
  def _expand(self):
    self._array += [None] * len(self._array)